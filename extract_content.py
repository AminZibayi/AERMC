"""
Document Content Extraction Script
Uses Docling for parsing (tables, images, layout) + EasyOCR for OCR with GPU acceleration.
Implements memory-efficient page-level chunking for large PDFs + token-level chunking for RAG.
"""

import gc
import json
import logging
import sys
from pathlib import Path
from typing import Optional

import cv2
import easyocr
import numpy as np

# Docling imports
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, smolvlm_picture_description
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling_core.types.doc.base import Size
from docling_core.types.doc.document import ImageRef

# Chunking imports
from docling_core.transforms.chunker.hybrid_chunker import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION — edit these variables directly
# ═══════════════════════════════════════════════════════════════════════════════

# Hardware / Processing
USE_GPU                = True             # Enables GPU for both Docling and EasyOCR
DOCLING_THREADS        = 4                # Number of CPU threads for Docling
PAGES_PER_CHUNK        = 10               # Memory management: process PDF N pages at a time

# EasyOCR (for extracting text from pictures)
USE_EASYOCR            = True
OCR_LANGS              = ["en", "fa"]
OCR_BATCH_SIZE         = 16               # Batch size for EasyOCR inference

# Vision Extraction
IMAGE_RESOLUTION_SCALE = 2.0              # 2.0 = High res image extraction
EXPORT_PAGE_IMAGES     = True             # Save full page images
EXPORT_PICTURES        = True             # Save extracted figures/pictures
EXPORT_TABLE_IMAGES    = False            # Save extracted tables as images
ENRICH_PICTURES        = True             # Enrich pictures using VLM
CHART_EXTRACTION       = False             # Enable chart extraction

# Token Chunking (LLM / RAG prep)
CHUNK_SIZE_TOKENS      = 512              # Max tokens per chunk
CHUNK_OVERLAP_TOKENS   = 50               # Overlap between adjacent chunks
TOKENIZER_MODEL        = "sentence-transformers/all-MiniLM-L6-v2"

# File / System
GC_INTERVAL            = 5                # Run garbage collection every N files (dir mode)
OUTPUT_DIR             = "output"         # Master output directory
SUPPORTED_EXTENSIONS   = (
    ".pdf", ".docx", ".doc", ".pptx", ".xlsx",
    ".png", ".jpg", ".jpeg", ".tiff", ".bmp",
)


# ═══════════════════════════════════════════════════════════════════════════════
#  internals — no need to touch below
# ═══════════════════════════════════════════════════════════════════════════════

_ocr_reader: Optional[easyocr.Reader] = None


def get_pdf_page_count(pdf_path: Path) -> Optional[int]:
    """Try to detect total pages using pypdf to allow batching."""
    try:
        from pypdf import PdfReader
        return len(PdfReader(str(pdf_path)).pages)
    except ImportError:
        log.warning("pypdf not installed. Cannot batch PDF processing by pages. (pip install pypdf)")
        return None
    except Exception as e:
        log.warning("Failed to detect PDF page count: %s", e)
        return None


def _get_ocr_reader() -> easyocr.Reader:
    global _ocr_reader
    if _ocr_reader is None:
        log.info("Initializing EasyOCR (langs=%s, gpu=%s)", OCR_LANGS, USE_GPU)
        _ocr_reader = easyocr.Reader(
            lang_list=OCR_LANGS,
            gpu=USE_GPU,
            quantize=True,
            cudnn_benchmark=True,
            verbose=False,
        )
    return _ocr_reader


def _ocr_images_batch(images: list[np.ndarray], batch_size: int) -> list[list[dict]]:
    if not images or not USE_EASYOCR:
        return []
    reader = _get_ocr_reader()
    all_results: list[list[dict]] = []
    for i in range(0, len(images), batch_size):
        batch = images[i : i + batch_size]
        target_h = max(img.shape[0] for img in batch)
        target_w = max(img.shape[1] for img in batch)
        resized = [
            cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_AREA)
            if img.shape[:2] != (target_h, target_w) else img
            for img in batch
        ]
        raw = reader.readtext_batched(resized, batch_size=batch_size, detail=1, output_format="standard")
        for page_results in raw:
            all_results.append([{"text": t, "bbox": b, "confidence": c} for b, t, c in page_results])
        del resized
        gc.collect()
    return all_results


def _build_converter() -> DocumentConverter:
    device = "cuda" if USE_GPU else "cpu"
    
    # Configure specific PDF Pipeline options
    pipeline_options = PdfPipelineOptions()
    pipeline_options.accelerator_options = AcceleratorOptions(device=device, num_threads=DOCLING_THREADS)
    
    # Enable robust table and image extraction
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
    pipeline_options.generate_page_images = EXPORT_PAGE_IMAGES
    pipeline_options.generate_picture_images = EXPORT_PICTURES

    # Enable chart extraction
    pipeline_options.do_chart_extraction = CHART_EXTRACTION

    if ENRICH_PICTURES:
        pipeline_options.do_picture_description = True
        pipeline_options.picture_description_options = smolvlm_picture_description

    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def _build_chunker() -> HybridChunker:
    tok = HuggingFaceTokenizer(tokenizer=AutoTokenizer.from_pretrained(TOKENIZER_MODEL))
    return HybridChunker(tokenizer=tok, max_tokens=CHUNK_SIZE_TOKENS)


def extract_document(source: str | Path) -> dict:
    source = Path(source).expanduser().resolve()
    base_name = source.stem
    
    # Prepare directories
    out_dir = Path(OUTPUT_DIR) / f"{base_name}_extracted"
    pics_dir = out_dir / "pictures"
    tables_dir = out_dir / "tables"
    pages_dir = out_dir / "pages"
    chunks_dir = out_dir / "chunks"

    for d in (out_dir, pics_dir, tables_dir, pages_dir, chunks_dir):
        d.mkdir(parents=True, exist_ok=True)

    log.info("Processing: %s", source)
    
    # Determine page ranges (only for PDFs)
    page_ranges = []
    total_pages = get_pdf_page_count(source) if source.suffix.lower() == ".pdf" else None

    if total_pages:
        for start in range(1, total_pages + 1, PAGES_PER_CHUNK):
            end = min(start + PAGES_PER_CHUNK - 1, total_pages)
            page_ranges.append((start, end))
    else:
        page_ranges.append(None) # Process entire document at once

    converter = _build_converter()
    chunker = _build_chunker()

    merged_md_path = out_dir / f"{base_name}.merged.md"
    merged_md_file = merged_md_path.open("w", encoding="utf-8")

    global_pic_counter = 0
    global_table_counter = 0
    failed_ranges = []
    
    all_hybrid_chunks = []
    all_ocr_results = []

    for rng in page_ranges:
        if rng:
            log.info("Processing pages %d-%d ...", rng[0], rng[1])
        
        try:
            kwargs = {"page_range": rng} if rng else {}
            result = converter.convert(str(source), raises_on_error=False, **kwargs)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            err_msg = f"Pages {rng}: {e}" if rng else f"Failed to convert: {e}"
            failed_ranges.append(err_msg)
            log.error(err_msg)
            continue

        doc = getattr(result, "document", None)
        if not doc:
            err_msg = f"Pages {rng}: No document returned" if rng else "No document returned"
            failed_ranges.append(err_msg)
            log.error(err_msg)
            continue

        # 1. Save Page Images
        if EXPORT_PAGE_IMAGES and hasattr(doc, "pages"):
            for page_no, page in doc.pages.items():
                if hasattr(page, "image") and page.image and hasattr(page.image, "pil_image"):
                    page_img_path = pages_dir / f"{base_name}-p{page_no:05d}.png"
                    with page_img_path.open("wb") as fp:
                        page.image.pil_image.save(fp, format="PNG")

        # 2. Extract Figures and Tables, and set image URIs for Markdown references
        pic_images = []
        for element, _level in doc.iterate_items():
            if isinstance(element, TableItem):
                global_table_counter += 1
                pil_img = element.get_image(doc)
                if pil_img:
                    tbl_filename = f"{base_name}-table-{global_table_counter:05d}.png"
                    tbl_img_path = tables_dir / tbl_filename
                    with tbl_img_path.open("wb") as fp:
                        pil_img.save(fp, "PNG")
                    # Set image URI relative to the output directory for Markdown references
                    if element.image is None:
                        element.image = ImageRef(
                            mimetype="image/png",
                            uri=Path(f"tables/{tbl_filename}"),
                            dpi=72,
                            size=Size(width=pil_img.width, height=pil_img.height)
                        )
                    else:
                        element.image.uri = Path(f"tables/{tbl_filename}")

            elif isinstance(element, PictureItem):
                global_pic_counter += 1
                pil_img = element.get_image(doc)
                if pil_img:
                    pic_filename = f"{base_name}-picture-{global_pic_counter:05d}.png"
                    pic_img_path = pics_dir / pic_filename
                    with pic_img_path.open("wb") as fp:
                        pil_img.save(fp, "PNG")
                    # Set image URI relative to the output directory for Markdown references
                    if element.image is None:
                        element.image = ImageRef(
                            mimetype="image/png",
                            uri=Path(f"pictures/{pic_filename}"),
                            dpi=72,
                            size=Size(width=pil_img.width, height=pil_img.height)
                        )
                    else:
                        element.image.uri = Path(f"pictures/{pic_filename}")
                    # Queue for EasyOCR
                    img_cv2 = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                    pic_images.append((global_pic_counter, img_cv2))

        # 3. EasyOCR on extracted pictures
        if pic_images and USE_EASYOCR:
            log.info("Running EasyOCR on %d picture(s) in this chunk", len(pic_images))
            raw_cv2_imgs = [img for _, img in pic_images]
            ocr_res = _ocr_images_batch(raw_cv2_imgs, OCR_BATCH_SIZE)
            for (pic_id, _), page_ocr in zip(pic_images, ocr_res):
                all_ocr_results.append({
                    "picture_id": pic_id,
                    "text": " ".join(r["text"] for r in page_ocr)
                })
        
        # 4. Hybrid Token Chunking (for RAG)
        doc_chunks = list(chunker.chunk(doc))
        chunk_data = [
            {
                "text": c.text,
                "metadata": {
                    "headings": getattr(c.meta, "headings", []) if hasattr(c, "meta") else [],
                    "origin": str(c.origin) if hasattr(c, "origin") else None,
                },
            }
            for c in doc_chunks
        ]
        all_hybrid_chunks.extend(chunk_data)

        # 5. Export Markdown & JSON for this chunk
        rng_suffix = f".p{rng[0]:05d}-p{rng[1]:05d}" if rng else ""
        
        chunk_md = doc.export_to_markdown(image_mode=ImageRefMode.REFERENCED)
        chunk_md_path = chunks_dir / f"{base_name}{rng_suffix}.md"
        chunk_md_path.write_text(chunk_md, encoding="utf-8")
        
        chunk_json_path = chunks_dir / f"{base_name}{rng_suffix}.json"
        chunk_json_path.write_text(json.dumps(doc.export_to_dict(), indent=2), encoding="utf-8")

        # Append to merged Markdown
        if rng:
            merged_md_file.write(f"\n\n<!-- pages {rng[0]}-{rng[1]} -->\n\n")
        merged_md_file.write(chunk_md)
        
        gc.collect()

    merged_md_file.close()

    # Log failures
    if failed_ranges:
        failures_path = out_dir / "failures.log"
        with failures_path.open("w", encoding="utf-8") as f:
            for err in failed_ranges:
                f.write(f"{err}\n")
        log.warning("Some chunks failed. See: %s", failures_path)

    # Save master hybrid chunks & OCR text
    master_json = out_dir / f"{base_name}.hybrid_chunks.json"
    master_data = {
        "hybrid_chunks": all_hybrid_chunks,
        "ocr_results": all_ocr_results,
        "total_pictures": global_pic_counter,
        "total_tables": global_table_counter
    }
    master_json.write_text(json.dumps(master_data, indent=2, ensure_ascii=False), encoding="utf-8")

    log.info("Merged Markdown: %s", merged_md_path)
    log.info("Total Pictures: %d | Total Tables: %d | Total Chunks: %d", 
             global_pic_counter, global_table_counter, len(all_hybrid_chunks))

    return master_data


def extract_directory(dir_path: str | Path) -> list[dict]:
    dir_path = Path(dir_path)
    files = sorted(f for f in dir_path.rglob("*") if f.suffix.lower() in SUPPORTED_EXTENSIONS)
    log.info("Found %d file(s) in %s", len(files), dir_path)
    results = []
    for i, fpath in enumerate(files, 1):
        log.info("\n=== [%d/%d] %s ===", i, len(files), fpath.name)
        try:
            extract_document(fpath)
            results.append({"file": str(fpath), "status": "ok"})
        except Exception as e:
            log.error("Failed to process %s: %s", fpath, e)
            results.append({"file": str(fpath), "status": "error", "error": str(e)})
        if i % GC_INTERVAL == 0:
            gc.collect()
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <file_or_directory>")
        sys.exit(1)

    src = Path(sys.argv[1])
    if src.is_dir():
        extract_directory(src)
    else:
        extract_document(src)
