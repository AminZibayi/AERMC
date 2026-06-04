# Phase 17 — Final Report Assembly & Output

## Prerequisites

**You MUST have completed Phase 16 (Final Gate) and documented the validation checklist BEFORE reading this phase.**

## Report Writing Instructions

Write the final `ERM_Report.md` to `./dist/<TICKER>/ERM_Report.md`. Use the professional report structure template in `references/report-structure.md` as your section-level guide.

### Report Structure (from `references/report-structure.md`)

Follow the `report-structure.md` template EXACTLY for section headings.

### Critical Output Rules

1. **Dense Citations**: Every factual claim, dollar figure, and risk quote MUST be immediately followed by `[^n]`. Do not save citations for sentence endings.

2. **CSV Tables**: Embed in ` ```csv ` fenced blocks. Citation goes in the markdown header line immediately before the CSV, NOT as a CSV column. Remove redundant columns (Item, Risk_ID).

3. **Mermaid Diagrams**: Add a one-sentence caption in plain English below each diagram explaining what it shows. Cite the source data in the caption.

4. **No Redundancy**: Never repeat the same table in both "Section X" and "Appendix Y"

5. **Reference List**: Use academic format: _Company Name (Year). Form X-K, Item Y / Note Z..._ All `[^n]` numbers used in the body MUST appear in the reference list.

6. **No Meta-Commentary**: Never mention scripts, MCP tools, LLM reasoning, or extraction mechanics. The report must read as if you personally read the filings.

7. **Verbatim Quotes**: All Item 1A risk factor quotes must be in quotation marks with a citation immediately after: `"...exact phrase..." [^5]`

8. **Derived Metrics**: Label with "(derived)" and show the formula if non-obvious. Example: "ROE (derived): $57,048M ÷ $362,438M = 15.73%"

### Output Locations

| Output       | Path                            |
| ------------ | ------------------------------- |
| Final report | `./dist/<TICKER>/ERM_Report.md` |
| Raw data     | `./dist/<TICKER>/raw/`          |
