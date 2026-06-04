# Phase 7 — Credit Risk Concentrations

## Steps

1. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "credit risk".
2. Extract Note 4 or equivalent credit risk disclosures with sector-specific data.
3. Identify top credit exposures by counterparty type, geography, or product.
4. Note any specific portfolio mentions (e.g., Apple Card, credit cards, mortgages).
5. Extract allowance amounts, net charge-offs, past-due data.
6. If the notes are heavily truncated (fewer than 500 words for credit section), use `edgartools_edgar_notes` (topic="credit") for dynamic drill-down.
7. Write the Credit Concentrations CSV to `./dist/<TICKER>/artifacts/credit_concentrations.csv` with columns: Portfolio, Total_Exposure, Per_of_Total, Credit_Quality.
8. In the report, reference the artifact file path instead of embedding the CSV.

## Required Outputs

| Output | Source |
|--------|--------|
| Credit Risk Management Policy Summary | relevant_notes.txt |
| Top Sector / Counterparty Exposures (on + off-balance sheet) | relevant_notes.txt |
| Allowance for Credit Losses | relevant_notes.txt |
| Net Charge-offs / Past Due Data | relevant_notes.txt |
| Credit Concentrations CSV | `./dist/<TICKER>/artifacts/credit_concentrations.csv` |
| Report citation | Markdown header with `[^n]` referencing the artifact path |

## Critical Rules

- Credit exposure tables MUST show both on-balance-sheet AND off-balance-sheet amounts
- Percentages must sum to 100% — verify: Sum(All_Pct_Total) = 100%. If not, state "subtotal may not sum to 100% due to rounding"
- Allowance for credit losses = Allowance for loan losses + Allowance for lending-related commitments. State this formula explicitly.
- For the "ACL/Total Credit Exposure" ratio, use: Total Allowance for Credit Losses ÷ Total Credit Exposure (gross)
- If Note 4 was truncated, the "off-balance sheet" column may be missing — do NOT infer it from other sources. Write "OFF-BALANCE SHEET data not retrievable — on-balance sheet only shown."
- Specific portfolio names (e.g., "Apple Card") must be quoted verbatim from Note 4
- Place the source citation `[^n]` in the markdown header line immediately before the reference. Do NOT embed the CSV data in the report body.
