# CSV Templates for ERM Report Output

All CSV tables must be embedded in fenced code blocks (```csv) in `ERM_Report.md`. 
**CRITICAL**: Do NOT include redundant columns like `Item`, `Risk_ID`, `Source`, or `Page_Ref` that repeat on every row. Put the citation `[^n]` for the data source in the Markdown header immediately preceding the table.

## Risk Factor Register

*Example Markdown Header: ### Principal Risk Factors (Item 1A) [^2]*
```csv
Risk_Category,Risk_Factor_Title,Verbatim_Excerpt
Legal and Regulatory,Regulatory Changes,"exact phrase ""..."" from 10-K"
Political,Macroeconomic Uncertainty,"exact phrase ""..."" from 10-K"
```

Columns:
- `Risk_Category` — High-level category
- `Risk_Factor_Title` — Extracted heading verbatim
- `Verbatim_Excerpt` — 50–150 word quote with exact phrase syntax

## Financial Indicators

*Example Markdown Header: ### Financial Risk Indicators (3-Year Trend) [^3]*
```csv
Metric,FY2023,FY2022,FY2021,Unit
Revenue,0,0,0,USD
Net_Income,0,0,0,USD
Profit_Margin,0,0,0,Percent
ROE,0,0,0,Percent
Efficiency_Ratio,0,0,0,Percent
NIM,0,0,0,Percent
CET1_Ratio,0,0,0,Percent
```

Columns:
- `Metric` — Short metric name
- `FY2023`, `FY2022`, `FY2021` — Fiscal year values
- `Unit` — USD, Percent, Ratio

## Credit Concentrations (Banks Only)

*Example Markdown Header: ### Credit Risk Concentrations (Note 4) [^4]*
```csv
Portfolio,Total_Exposure,Per_of_Total,Credit_Quality
Credit_Cards,0,0%,X%
Mortgages,0,0%,X%
Commercial,0,0%,X%
```

Columns:
- `Portfolio` — Counterparty type or product segment
- `Total_Exposure` — USD amount (millions)
- `Per_of_Total` — Percentage of overall portfolio
- `Credit_Quality` — Distributed / Risk-weighted / Internal Rating
