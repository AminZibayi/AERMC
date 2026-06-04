# Phase 1 — Company Context & Identification

## Steps
1. Load `./dist/<TICKER>/raw/metadata.json` and extract ticker, name, CIK, market cap, current price, employee count, 10k_accession, 10k_period, auditor.
2. If SIC code, NAICS, exchange, state of incorporation are missing from metadata.json, use `edgartools_edgar_company` to retrieve them.
3. Load `./dist/<TICKER>/raw/institutional_holders.json` if present.
4. Write "Company Context Brief" section to report.

## Required Outputs

| Output | Source |
|--------|--------|
| Company Name, Ticker, CIK | metadata.json |
| SIC/NAICS codes | edgar_company (fallback if missing) |
| Exchange, State, Industry | edgar_company (fallback if missing) |
| Market Cap, Current Price | metadata.json |
| Full Time Employees | metadata.json |
| Top 5 Institutional Holders | institutional_holders.json |

## Critical Rules
- CIK must be exactly 10 digits padded (e.g., CIK 0000019617, not 19617)
- Market cap and price must be the most recent available — do not use stale cached data
- If `metadata.json` lacks any key field, do NOT write "N/A" — use `edgartools_edgar_company(identifier="<TICKER>")` immediately
- All values in the Company Context table must have a marker that links to a References entry [^n]
