# CSV Templates for ERM Report Output

All CSV tables must be embedded in fenced code blocks (```csv) in `ERM_Report.md`.

## Risk Factor Register

```csv
Risk_ID,Item,Page_Ref,Risk_Factor_Title,Verbatim_Excerpt,Filing_Source
R01,1A,Assumed,Risk Title,"exact phrase ""..."" from 10-K",10-K FY2024
R02,1A,Assumed,Risk Title,"exact phrase ""..."" from 10-K",10-K FY2024
```

Columns:
- `Risk_ID` — Sequential number (R01, R02…)
- `Item` — SEC item reference (1A, 3, 9A, etc.)
- `Page_Ref` — Inferred or marked "Assumed" if pagination unavailable
- `Risk_Factor_Title` — Extracted heading verbatim
- `Verbatim_Excerpt` — 50–150 word quote with exact phrase syntax
- `Filing_Source` — Form type + fiscal year

## Financial Indicators

```csv
Metric,FY2023,FY2022,FY2021,Unit,Source
Revenue,0,0,0,USD,10-K Income Statement
Net_Income,0,0,0,USD,10-K Income Statement
Profit_Margin,0,0,0,Percent,Derived
ROE,0,0,0,Percent,Derived
Efficiency_Ratio,0,0,0,Percent,Derived
NIM,0,0,0,Percent,10-K Net Interest Income / Avg Earning Assets
CET1_Ratio,0,0,0,Percent,10-K Regulatory Capital Disclosure
```

Columns:
- `Metric` — Short metric name
- `FY2023`, `FY2022`, `FY2021` — Fiscal year values
- `Unit` — USD, Percent, Ratio
- `Source` — Where data was extracted from

## Credit Concentrations (Banks Only)

```csv
Portfolio,Total_Exposure,Per_of_Total,Credit_Quality,Note_Ref,Source
Credit_Cards,0,0%,X%,4,10-K Note 4
Mortgages,0,0%,X%,4,10-K Note 4
Commercial,0,0%,X%,4,10-K Note 4
```

Columns:
- `Portfolio` — Counterparty type or product segment
- `Total_Exposure` — USD amount (millions)
- `Per_of_Total` — Percentage of overall portfolio
- `Credit_Quality` — Distributed / Risk-weighted / Internal Rating
- `Note_Ref` — Note number in 10-K
- `Source` — Exact note citation
