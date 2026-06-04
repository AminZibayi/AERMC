# Phase 5 — Corporate Governance & Risk Committee

## Steps
1. Read `./dist/<TICKER>/raw/proxy_governance.txt`.
2. Search for "risk committee", "audit committee", "CRO", "Chief Risk Officer", "Three Lines".
3. Identify explicit Board Risk Committee or equivalent. **CRITICAL: You MUST use direct quotes (verbatim) when extracting important data like the three lines of defense, risk committee details, or CRO roles.**
4. Note board oversight structure, risk reporting lines.
5. Cross-reference with `./dist/<TICKER>/raw/item_1A_risk_factors.txt` for governance-related risk disclosures.
6. If the proxy file says "Risk committee not found", optionally use `edgartools_edgar_read` on the DEF 14A for dynamic drill-down.
7. Write "Governance & Risk Oversight Summary" section to report.

## Required Outputs
| Output | Source |
|--------|--------|
| Risk Committee Name (exact) | proxy_governance.txt |
| Committee Chair / Member Summary | proxy_governance.txt |
| CRO Name and Title (if disclosed) | proxy_governance.txt |
| Three Lines Model Evidence | proxy_governance.txt |
| Governance-Related Risk Disclosures | item_1A_risk_factors.txt |
