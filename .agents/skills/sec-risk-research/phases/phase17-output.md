# Phase 17 — Final Report Assembly & Output

## Prerequisites

**You MUST have completed Phase 16 (Final Gate) and completed terminal logging of validation checks BEFORE reading this phase.**

## Report Writing Instructions

Write the final `ERM_Report.md` to `./dist/<TICKER>/ERM_Report.md`. Use the professional report structure template in `references/report-structure.md` as your section-level guide.

### Report Structure (from `references/report-structure.md`)

Follow the `report-structure.md` template EXACTLY for section headings.

### Artifact References (NOT Embeddings)

All structured data (CSV tables, Mermaid diagrams) is written to separate artifact files in `./dist/<TICKER>/artifacts/`. In the report, reference these artifacts by file path in the markdown header/caption. Do NOT embed raw CSV rows or Mermaid code blocks in `ERM_Report.md`.

| Artifact Type         | File Path                                               | Report Usage                                                |
| --------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| Risk Factor Register  | `./dist/<TICKER>/artifacts/risk_register.csv`           | Header citation + "See artifact: risk_register.csv"         |
| Financial Indicators  | `./dist/<TICKER>/artifacts/financial_indicators.csv`    | Header citation + "See artifact: financial_indicators.csv"  |
| Credit Concentrations | `./dist/<TICKER>/artifacts/credit_concentrations.csv`   | Header citation + "See artifact: credit_concentrations.csv" |
| Risk Cascade Diagram | Embedded inline in `ERM_Report.md` | `graph TD` / `graph LR` with ` ```mermaid ` block |
| Governance Risk Map | Embedded inline in `ERM_Report.md` | `flowchart LR` or `graph TD` with ` ```mermaid ` block |
| Financial Trend Chart | Embedded inline in `ERM_Report.md` | `xychart-beta` with ` ```mermaid ` block |
| Credit Pie Chart | Embedded inline in `ERM_Report.md` | `pie` with ` ```mermaid ` block |

### Critical Output Rules

1. **Dense Citations**: Every factual claim, dollar figure, and risk quote MUST be immediately followed by `[^n]`. Do not save citations for sentence endings.

2. **CSV Tables (Artifact Files)**: Write all CSV content to `./dist/<TICKER>/artifacts/` as separate `.csv` files. In the report, place the citation `[^n]` in the markdown header line before a one-line reference (e.g., `### Financial Risk Indicators [^3]` followed by `> Full data: ./dist/<TICKER>/artifacts/financial_indicators.csv`).

3. **Mermaid Diagrams (Embedded Inline)**: Embed all Mermaid diagrams directly inline in `ERM_Report.md` using ` ```mermaid ` fenced code blocks. Each diagram must be followed by a one-sentence plain text caption. Do NOT write `.mermaid` artifact files.

4. **No Redundancy**: Never repeat the same table in both "Section X" and "Appendix Y".

5. **Reference List**: Use academic format: _Company Name (Year). Form X-K, Item Y / Note Z..._ All `[^n]` numbers used in the body MUST appear in the reference list.

6. **No Meta-Commentary**: Never mention scripts, MCP tools, LLM reasoning, or extraction mechanics. The report must read as if you personally read the filings.

7. **Verbatim Quotes**: All Item 1A risk factor quotes must be in quotation marks with a citation immediately after: `"...exact phrase..." [^5]`.

8. **Derived Metrics**: Label with "(derived)" and show the formula if non-obvious. Example: "ROE (derived): $57,048M ÷ $362,438M = 15.73%".

9. **Clean Report**: The report must contain NO validation tables, NO terminal logs, NO pass/fail checklists. It must be a polished, professional document only.

### Output Locations

| Output             | Path                            |
| ------------------ | ------------------------------- |
| Final report       | `./dist/<TICKER>/ERM_Report.md` |
| Artifact directory | `./dist/<TICKER>/artifacts/`    |
| Raw data           | `./dist/<TICKER>/raw/`          |
