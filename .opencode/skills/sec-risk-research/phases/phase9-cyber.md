# Phase 9 — Cybersecurity & Third-Party Risk

## Steps
1. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "cybersecurity".
2. Extract Note 37 or equivalent cyber incident disclosures. If truncated, use `edgartools_edgar_notes` (topic="cybersecurity").
3. Read `./dist/<TICKER>/raw/item_1A_risk_factors.txt` and search for "cybersecurity", "data breach", "third-party", "vendor".
4. Note third-party / vendor risk language (supply chain, cloud providers, processors).
5. Check for 8-K cyber incident filings (use `edgartools_edgar_monitor` or `edgartools_edgar_text_search` dynamically).
6. Write "Cyber Risk Profile" section to report.

## Required Outputs
| Output | Source |
|--------|--------|
| Cyber Incidents Reported (Item 106) | item_1A_risk_factors.txt or relevant_notes.txt |
| Third-Party / Vendor Risk Disclosures | item_1A_risk_factors.txt |
| 8-K Cyber Incident Filings | edgartools dynamic filing search |
| Note 37 or Equivalent Summary | relevant_notes.txt |
| Recommended Controls (NIST CSF) | Derived from framework mapping |
