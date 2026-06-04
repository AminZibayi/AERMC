# Phase 6 — Financial Statement Analysis

## Steps

1. Read `./dist/<TICKER>/raw/financial_statements.txt` (Income Statement, Balance Sheet).
2. Extract: Revenue, Net Income, Gross Profit, Operating Income, EPS (if available) for FY2023, FY2024, FY2025.
3. Calculate or extract ratios: Profit Margin, Asset Turnover, ROE, Efficiency Ratio.
4. For banks: additionally extract Net Interest Margin (NIM), CET1 Ratio, Tangible Common Equity.
5. For lenders: extract Provision for Credit Losses (PCL) or Provision for Loan Losses.
6. Write the Financial Indicators CSV to `./dist/<TICKER>/artifacts/financial_indicators.csv` with columns: Metric, FY2023, FY2022, FY2021, Unit, Source.
7. In the report, reference the artifact file path instead of embedding the CSV.

## Required Outputs

| Output | Source |
|--------|--------|
| Revenue, Net Income, EPS (3-year trend) | financial_statements.txt |
| Profit Margin, ROE, Efficiency Ratio | Derived |
| NIM, CET1, Tangible Common Equity (banks) | financial_statements.txt or Item 7A |
| PCL / Provision for Loan Losses | financial_statements.txt |
| Financial Indicators CSV | `./dist/<TICKER>/artifacts/financial_indicators.csv` |
| Report citation | Markdown header with `[^n]` referencing the artifact path |

## Critical Rules

- **ARITHMETIC VERIFICATION:** Before writing any derived ratio, recalculate from the raw numbers in the same section. If your computed ROE differs from a board-reported value by >0.5 pp, use the board-reported value and note the discrepancy.
- All financial figures must use consistent units (convert $K → $M → $B consistently within a table)
- FY2023 must be included even if not in `financial_statements.txt` — use `edgartools_edgar_trends` if needed
- Net Income must be AFTER tax; differentiate from Pre-Tax Income
- ROE formula: Net Income (annual) ÷ Average Stockholders' Equity. If average equity unavailable, use ending equity balance and label "(ending balance)"
- For Efficiency Ratio: Total Noninterest Expense ÷ (Net Interest Income + Noninterest Income). If Noninterest Expense is missing, use "Total Noninterest Expense" line from Income Statement
- Place the source citation `[^n]` in the markdown header line immediately before the reference. Do NOT embed the CSV data in the report body.
