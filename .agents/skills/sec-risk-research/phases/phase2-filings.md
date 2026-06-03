# Phase 2 — Core Filing Retrieval

## Steps
1. Load `./dist/<TICKER>/raw/metadata.json` to get `10k_accession` and `10k_period`.
2. Record the exact 10-K accession number and fiscal year covered.
3. Record any auditor name found in metadata (use `"Not found"` if absent).
4. Verify that `item_1_business.txt`, `item_1A_risk_factors.txt`, `item_3_legal.txt` exist in `./dist/<TICKER>/raw/`.
5. If any core item is missing, note the gap and proceed using Financial Statements and Notes only.
6. Write "Filing Overview" table to report.

## Required Outputs
| Output | Source |
|--------|--------|
| 10-K Accession Number | metadata.json |
| Fiscal Year / Period of Report | metadata.json |
| Auditor Name | metadata.json |
| Filing Status (complete/partial) | File existence check |
| Missing Items Log | Derived from file checks |
