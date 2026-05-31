#!/usr/bin/env python3
"""
Risk Research Data Fetcher — Enterprise Risk Analysis
=====================================================
Fetches raw SEC EDGAR and market data required for the Risk Research Protocol.
This script extracts raw text and tables to avoid excessive LLM MCP calls.
The LLM is responsible for parsing, analyzing, and generating the final report.

Usage:
    python risk_research.py JPM
"""

import argparse
import json
import os
import sys
from datetime import datetime

def setup_identity():
    from edgar import set_identity
    from edgar.storage import use_local_storage
    identity = os.environ.get("EDGAR_IDENTITY", "RiskResearchBot research@example.com")
    set_identity(identity)
    os.makedirs("./edgar_cache", exist_ok=True)
    use_local_storage("./edgar_cache")

def safe_import_yfinance():
    try:
        import yfinance as yf
        return yf
    except ImportError:
        return None

def fetch_raw_data(ticker: str, output_dir: str):
    setup_identity()
    os.makedirs(output_dir, exist_ok=True)
    print(f"Fetching raw risk data for {ticker} into {output_dir}/ ...")

    from edgar import Company
    company = Company(ticker)
    
    # 1. Company Metadata
    metadata = {
        "ticker": ticker,
        "name": str(company).split("[")[0].strip(),
        "cik": str(company.cik) if hasattr(company, "cik") else "",
        "extraction_date": datetime.now().isoformat()
    }

    # 2. Market Data (yfinance)
    yf = safe_import_yfinance()
    if yf:
        stock = yf.Ticker(ticker)
        try:
            info = stock.info
            metadata["market_cap"] = info.get("marketCap")
            metadata["current_price"] = info.get("currentPrice")
            metadata["employees"] = info.get("fullTimeEmployees")
            
            holders = stock.institutional_holders
            if holders is not None and not holders.empty:
                with open(os.path.join(output_dir, "institutional_holders.json"), "w") as f:
                    json.dump(holders.head(5).to_dict("records"), f, indent=2, default=str)
                print(" [OK] Institutional holders saved")
            
            print(" [OK] Market data saved")
        except Exception as e:
            print(f" [WARN] yfinance error: {e}")

    # 3. 10-K Retrieval
    tenk_filings = company.get_filings(form="10-K").head(1)
    if not tenk_filings:
        print(f" [ERROR] No 10-K found for {ticker}")
        return
        
    filing = tenk_filings[0]
    metadata["10k_accession"] = filing.accession_number if hasattr(filing, 'accession_number') else ""
    tenk = filing.obj()
    metadata["10k_period"] = tenk.period_of_report if hasattr(tenk, 'period_of_report') else ""
    metadata["auditor"] = str(tenk.auditor.name) if tenk and hasattr(tenk, 'auditor') and tenk.auditor else "Not found"
    
    with open(os.path.join(output_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)
    print(" [OK] Metadata saved")

    # 4. Extract 10-K Core Items (Raw Text)
    items_to_extract = {
        "Item 1": "item_1_business.txt",
        "Item 1A": "item_1A_risk_factors.txt",
        "Item 3": "item_3_legal.txt",
        "Item 9A": "item_9A_controls.txt"
    }

    for item_key, filename in items_to_extract.items():
        try:
            content = tenk[item_key]
            text = str(content) if content else "Not found"
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(text)
            print(f" [OK] {item_key} saved")
        except Exception as e:
            print(f" [WARN] Failed to extract {item_key}: {e}")

    # 5. Extract Financial Statements
    try:
        financials = company.get_financials()
        if financials:
            with open(os.path.join(output_dir, "financial_statements.txt"), "w", encoding="utf-8") as f:
                f.write("=== INCOME STATEMENT ===\n")
                f.write(str(financials.income_statement()))
                f.write("\n\n=== BALANCE SHEET ===\n")
                f.write(str(financials.balance_sheet()))
            print(" [OK] Financial statements saved")
    except Exception as e:
        print(f" [WARN] Failed to extract financials: {e}")

    # 6. Search and Extract Key Notes (Credit, Cyber, Litigation)
    try:
        notes = tenk.notes
        if notes:
            target_notes = ["credit risk", "litigation", "cybersecurity", "contingencies"]
            with open(os.path.join(output_dir, "relevant_notes.txt"), "w", encoding="utf-8") as f:
                for target in target_notes:
                    results = notes.search(target)
                    f.write(f"\n{'='*50}\n--- Search Results for '{target}' ---\n{'='*50}\n")
                    if results:
                        best_match = results[0]
                        f.write(f"Note Title: {best_match.title}\n\n")
                        f.write(str(best_match.text)[:15000]) # Cap length to avoid massive files
                    else:
                        f.write("No matching note found.\n")
            print(" [OK] Relevant notes saved")
    except Exception as e:
        print(f" [WARN] Failed to extract notes: {e}")

    # 7. Extract Proxy Governance (DEF 14A)
    try:
        proxies = company.get_filings(form="DEF 14A").head(1)
        if proxies:
            proxy = proxies[0].obj()
            text = str(proxy)
            import re
            gov_chunks = re.findall(r'.{0,500}risk committee.{0,3000}', text, re.IGNORECASE | re.DOTALL)
            with open(os.path.join(output_dir, "proxy_governance.txt"), "w", encoding="utf-8") as f:
                if gov_chunks:
                    f.write("--- Extracted 'Risk Committee' Snippets ---\n")
                    for i, chunk in enumerate(gov_chunks[:5]):
                        f.write(f"\n--- Snippet {i+1} ---\n{chunk.strip()}\n")
                else:
                    f.write("Risk committee not found in Proxy. LLM should look into the text below for possible alternatives (e.g., Audit and Compliance Committee).\n\n")
                    f.write("--- FULL PROXY TEXT (First 150k chars) ---\n")
                    f.write(text[:150000])
            print(" [OK] Proxy governance saved")
    except Exception as e:
        print(f" [WARN] Failed to extract proxy: {e}")

    print(f"\n[DONE] All raw data ready for LLM analysis in {output_dir}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("--output-dir", "-o", default=None)
    args = parser.parse_args()
    
    out_dir = args.output_dir or f"./dist/{args.ticker}/raw"
    fetch_raw_data(args.ticker, out_dir)
