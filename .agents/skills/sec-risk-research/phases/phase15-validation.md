# Phase 15 — Data Accuracy Validation Gate (Mandatory Pre-Flight Check)

## Purpose

This mandatory validation phase must be completed BEFORE writing the final report output (Phase 14). Catches the most common accuracy errors found in prior outputs: mismatched financials, unverified proxy data, missing citations, and arithmetic inconsistencies.

## Required Validation Checks

### Financial Arithmetic Check

For EVERY derived metric in the report, recalculate from raw data:

| Metric            | Formula                           | Tolerance | Action if Wrong                          |
| ----------------- | --------------------------------- | --------- | ---------------------------------------- |
| ROE               | Net Income ÷ Stockholders' Equity | ±0.5 pp   | Re-extract from financial_statements.txt |
| PCL Growth %      | (FY2025 - FY2024) ÷ FY2024 × 100  | ±0.5 pp   | Recalculate                              |
| Net Margin        | Net Income ÷ Total Revenue        | ±0.1 pp   | Recalculate                              |
| Credit Exposure % | Sector Exposure ÷ Total Exposure  | ±1%       | Recalculate from Note 4                  |
| YoY Asset Change  | (FY2025 - FY2024) ÷ FY2024 × 100  | ±0.5 pp   | Recalculate                              |

### Citation Completeness Check

Scan the draft report for these patterns — every instance MUST have a `[^n]` immediately preceding it or within the same sentence:

- [ ] Every dollar amount or percentage value
- [ ] Every verbatim quote from a filing
- [ ] Every mention of a framework name (COSO, Basel III, NIST)
- [ ] Every governance structure (Board Risk Committee, CRO name)
- [ ] Every risk factor category heading
- [ ] Every reference to a specific note (Note 4, Note 37, etc.)
- [ ] Every peer comparison number
- [ ] Every institutional holder statistic

### Proxy Governance Check

- [ ] `proxy_governance.txt` does NOT contain "Risk committee not found"
- [ ] If it does, `edgartools_edgar_filing` (DEF 14A) was retried
- [ ] CRO named or explicitly stated as "not disclosed in filing"
- [ ] Risk Committee meeting count present or explicitly stated as "not disclosed"
- [ ] Three Lines of Defense model evidence extracted or flagged

### Litigation Check

- [ ] `item_3_legal.txt` is not empty or "Not found"
- [ ] Material proceedings are listed with names, courts, and status
- [ ] ASC 450 classification (Probable / Reasonably Possible) applied

### Cyber / IT Risk Check

- [ ] Note 37 content extracted or state "Note 37 not retrievable"
- [ ] 8-K cyber incidents checked via `edgartools_edgar_text_search`
- [ ] NIST CSF adoption explicitly stated or "not disclosed"

### Data Gap Log

For every data item that could NOT be retrieved:

- [ ] Write it to the "Data Gaps & Limitations" section
- [ ] Specify the exact retrieval command needed
- [ ] Do NOT fabricate — use "Not disclosed in filing"

### Arithmetic Verification Log

Record any recalculated figures in this format:

```
RECALC: ROE FY2025 → $57,048M / $362,438M = 15.73% [source: financial_statements.txt, 10-K Item 8]
```

## Required Outputs

| Check                                             | Status              |
| ------------------------------------------------- | ------------------- |
| Financials verified (all derived metrics)         | PASS / RECALCULATED |
| Citation completeness (>95% factual claims cited) | PASS / FLAGGED      |
| Proxy governance complete                         | PASS / FLAGGED      |
| Litigation data complete                          | PASS / FLAGGED      |
| Cyber data complete                               | PASS / FLAGGED      |
| Data Gaps section written                         | YES / NO            |
| Arithmetic Verification Log present               | YES / NO            |
