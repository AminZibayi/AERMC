# Phase 7 — Credit Risk Concentrations

## Steps
1. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "credit risk".
2. Extract Note 4 or equivalent credit risk disclosures.
3. Identify top credit exposures by counter-party type, geography, or product.
4. Note any specific portfolio mentions (e.g., Apple Card, credit cards, mortgages).
5. Extract allowance amounts, net charge-offs, past-due data.
6. If the notes are heavily truncated, use `edgartools_edgar_notes` (topic="credit") for dynamic drill-down.
7. Write "Credit Concentrations" table to report in CSV format.

## Required Outputs
| Output | Source |
|--------|--------|
| Credit Risk Management Policy Summary | relevant_notes.txt |
| Top Counterparty / Sector Exposures | relevant_notes.txt |
| Allowance for Credit Losses | relevant_notes.txt |
| Net Charge-offs / Past Due Data | relevant_notes.txt |
| Specific Portfolio References | relevant_notes.txt (e.g., Apple Card) |
