# Phase 1 — Company Context & Identification

## Steps
1. Load `./dist/<TICKER>/raw/metadata.json` and extract ticker, name, CIK, market cap, current price, and employee count.
2. If SIC code, NAICS, exchange, state of incorporation are missing from `metadata.json`, optionally use `edgartools_edgar_company` to retrieve them.
3. Load `./dist/<TICKER>/raw/institutional_holders.json` if present.
4. Write "Company Context Brief" section to report.

## Required Outputs
| Output | Source |
|--------|--------|
| Company Name, Ticker, CIK | metadata.json |
| SIC/NAICS codes | edgartools company profile (if needed) |
| Exchange, State, Industry | edgartools company profile (if needed) |
| Market Cap, Current Price | metadata.json |
| Full Time Employees | metadata.json |
| Top 5 Institutional Holders | institutional_holders.json |
