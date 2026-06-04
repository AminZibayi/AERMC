# Phase 4 — ERM Framework Detection

## Steps

1. Read `./dist/<TICKER>/raw/item_9A_controls.txt` (if generated) and `./dist/<TICKER>/raw/item_1_business.txt`.
2. Search for framework keywords: COSO, ISO 31000, Basel III, NIST, RCSA, SOX, ICERC, CRO.
3. Note explicit framework references; if absent, infer from risk categorization structure. **CRITICAL: You MUST use direct quotes (verbatim) when extracting the exact ERM system or framework mentioned (e.g., "The Company uses the COSO 2017 framework...").**
4. Check `./dist/<TICKER>/raw/proxy_governance.txt` for Risk Committee language.
5. Determine which framework the company most closely follows.
6. Write "ERM Framework Assessment" table to report.

## Required Outputs

| Output                      | Source                                     |
| --------------------------- | ------------------------------------------ |
| Detected Framework(s)       | Derived from keyword search                |
| Framework Adoption Evidence | Verbatim quotes with exact phrase citation |
| Risk Governance Model       | Proxy + 10-K combined                      |
| Gaps / Inferences Flagged   | If framework not explicitly stated         |
