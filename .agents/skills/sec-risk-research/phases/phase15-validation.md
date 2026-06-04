# Phase 15 — Data Accuracy Validation Gate (Mandatory Pre-Flight Check)

## Purpose

This mandatory validation phase must be completed BEFORE writing the final report output. Catches the most common accuracy errors: mismatched financials, unverified proxy data, missing citations, and arithmetic inconsistencies.

**CRITICAL:** ALL validation results MUST be logged to terminal output only. Do NOT embed the validation checklist, validation tables, or any validation pass/fail details in the final `ERM_Report.md`. The report must be clean and polished — validation mechanics stay in the terminal session.

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
- [ ] Every institutional holder statistic

Target: >95% of factual claims have an inline citation.

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

Record any recalculated figures in this format (terminal output only):

```
RECALC: ROE FY2025 → $57,048M / $362,438M = 15.73% [source: financial_statements.txt, 10-K Item 8]
```

## Terminal Output Format

After completing all checks, output a concise summary to the terminal:

```
=== PHASE 15: VALIDATION GATE ===
Financial Arithmetic:    PASS | RECALCULATED
Citation Completeness:   PASS | FLAGGED
Proxy Governance:        PASS | FLAGGED
Cyber Data:              PASS | FLAGGED
Data Gaps Logged:        YES | NO
Arithmetic Logs:         YES | NO
GATE STATUS:             CLEARED | BLOCKED
=== END PHASE 15 ===
```

Do NOT write this table into the report body.
