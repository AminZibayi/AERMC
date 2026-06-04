# Phase 9 — Cybersecurity & Third-Party Risk

## Steps
1. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "cybersecurity".
2. Extract Note 37 or equivalent cyber incident disclosures. If truncated, use `edgartools_edgar_notes` (topic="cybersecurity").
3. Read `./dist/<TICKER>/raw/item_1A_risk_factors.txt` and search for "cybersecurity", "data breach", "third-party", "vendor", "AI", "artificial intelligence".
4. Note third-party / vendor risk language (supply chain, cloud providers, processors).
5. Check for 8-K cyber incident filings using `edgartools_edgar_text_search` with `query="cybersecurity"` or `query="data breach"`, `forms=["8-K"]`.
6. Write "Cyber Risk Profile" section to report.

## Required Outputs

| Output | Source |
|--------|--------|
| Cyber Incidents Reported (Item 106) | item_1A_risk_factors.txt or relevant_notes.txt |
| Third-Party / Vendor Risk Disclosures | item_1A_risk_factors.txt |
| 8-K Cyber Incident Filings | edgartools dynamic search |
| Note 37 Summary | relevant_notes.txt |
| AI / Emerging Tech Exposure | item_1A_risk_factors.txt |

## Critical Rules
- Note 37 (Item 106 disclosure) was **mandatory** for fiscal years ending on or after January 15, 2025. If Note 37 is missing or truncated, this is a **material data gap** — flag as HIGH priority
- "AI" and "artificial intelligence" in risk factors are automatically emerging risks — ensure they appear in Phase 13 scenario analysis
- Do NOT state "No cyber incidents reported" without checking 8-K filings via `edgartools_edgar_text_search`
- If the risk factors mention specific threat actors (state-sponsored, cybercriminal, hacktivist), quote verbatim
- Do NOT conflate "cyber risk" with "data breach" — they are distinct
