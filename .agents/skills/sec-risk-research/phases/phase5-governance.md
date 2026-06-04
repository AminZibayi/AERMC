# Phase 5 — Corporate Governance & Risk Committee

## Steps
1. Read `./dist/<TICKER>/raw/proxy_governance.txt` in full.
2. Search for "risk committee", "audit committee", "CRO", "Chief Risk Officer", "Three Lines".
3. **CRITICAL FALLBACK:** If `proxy_governance.txt` contains "Risk committee not found" or is truncated (fewer than 500 characters):
   a. Read `./dist/<TICKER>/raw/metadata.json` to get the proxy filing accession number
   b. Use `edgartools_edgar_filing` with that accession number to retrieve governance details
   c. Use `edgartools_edgar_read` with `form="DEF 14A"` and `sections=["governance"]` if needed
   d. Write the retrieved text to proxy_governance.txt and re-read
4. Identify explicit Board Risk Committee or equivalent.
5. **CRITICAL:** Use direct quotes (verbatim) when extracting governance data.
6. Note board oversight structure, risk reporting lines.
7. Cross-reference with item_1A_risk_factors.txt for governance-related risk disclosures.
8. Write "Governance & Risk Oversight Summary" section.

## Required Outputs

| Output | Source |
|--------|--------|
| Risk Committee Name (exact) | proxy_governance.txt (or DEF 14A retry) |
| Committee Chair | proxy_governance.txt |
| CRO Name and Title | proxy_governance.txt |
| Three Lines Model Evidence | proxy_governance.txt + Item 1 |
| Governance-Related Risk Disclosures | item_1A_risk_factors.txt |

## Critical Rules
- **DO NOT write "Proxy unavailable (timeout)" and stop.** Every required governance data point must be retrieved via fallback before proceeding to the final report.
- CRO identity: if name is not disclosed despite retry, write "CRO position exists but name not disclosed in filing." — do not leave blank
- Committee meeting count: if unavailable, write "Meeting count not disclosed in DEF 14A." — do not fabricate
- All governance data must be accompagnied by verbatim quotes from the proxy or 10-K
- If the company does NOT have a dedicated Risk Committee, identify the equivalent (e.g., Audit and Risk Committee, Risk and Capital Committee) and cite the exact committee name
