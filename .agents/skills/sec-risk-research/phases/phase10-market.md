# Phase 10 — Market & Ownership Data

## Steps
1. Load `./dist/<TICKER>/raw/metadata.json` for current market cap, price, and employees.
2. Load `./dist/<TICKER>/raw/institutional_holders.json` (top 5 holders).
3. If missing from the raw dumps, dynamically use `yahoo-finance_yfinance_get_ticker_info` to get current price, market cap, beta, 52-wk range, P/E.
4. Note ownership concentration from the holders file.
5. Write "Market Snapshot" section to report.

## Required Outputs

| Output | Source |
|--------|--------|
| Current Price, 52-wk High / Low | metadata.json or yahoo-finance |
| Market Cap, Beta, P/E | metadata.json or yahoo-finance |
| Top 5 Institutional Holders | institutional_holders.json |
| Ownership Concentration | Derived from holders data |

## Critical Rules
- Use the values provided by `risk_research.py` in metadata.json as the primary source; only use fallback yfinance if metadata.json fields are empty
- Market cap and price reflect the snapshot at the time the script ran — note this in the report as "as of [script run date]"
