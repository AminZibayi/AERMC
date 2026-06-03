# Phase 10 — Market & Ownership Data

## Steps
1. Load `./dist/<TICKER>/raw/metadata.json` for current market cap, price, and employees.
2. Load `./dist/<TICKER>/raw/institutional_holders.json` (top 5 holders).
3. If missing from the raw dumps, dynamically use `yahoo-finance_yfinance_get_ticker_info` to get current price, market cap, beta, 52-wk range, P/E.
4. Note ownership concentration from the holders file.
5. Write "Market Snapshot" to report.

## Required Outputs
| Output | Source |
|--------|--------|
| Current Price, 52-wk High / Low | metadata.json or yahoo-finance |
| Market Cap, Beta, P/E | metadata.json or yahoo-finance |
| Top 5 Institutional Holders | institutional_holders.json |
| Ownership Concentration | Derived from holders data |
