# Phase 6 — Financial Statement Analysis

## Steps
1. Read `./dist/<TICKER>/raw/financial_statements.txt` (Income Statement, Balance Sheet).
2. Extract: Revenue, Net Income, Gross Profit, Operating Income, EPS (if available).
3. Calculate or extract ratios: Profit Margin, Asset Turnover, ROE, Efficiency Ratio.
4. For banks: additionally extract Net Interest Margin (NIM), CET1 Ratio, Tangible Common Equity, Efficiency Ratio.
5. For lenders: extract Provision for Credit Losses (PCL) or Provision for Loan Losses.
6. Write "Financial Indicators" table to report in CSV format.

## Required Outputs
| Output | Source |
|--------|--------|
| Revenue, Net Income, EPS (3-year trend) | financial_statements.txt |
| Profit Margin, ROE, Efficiency Ratio | Derived |
| NIM, CET1, Tangible Common Equity (banks) | financial_statements.txt |
| PCL / Provision for Loan Losses | financial_statements.txt |
| Peer Comparison Metrics | Derived or edgartools_edgar_compare (if peers requested) |
