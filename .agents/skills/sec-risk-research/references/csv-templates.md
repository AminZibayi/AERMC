# CSV Templates for ERM Artifact Files

All CSV tables must be written as standalone artifact files in `./dist/<TICKER>/artifacts/`. In `ERM_Report.md`, reference these artifact files by path — do NOT embed raw CSV rows in the report body.

**CRITICAL**: Do NOT include redundant columns like `Item`, `Risk_ID`, `Source`, or `Page_Ref` that repeat on every row. Put the citation `[^n]` for the data source in the Markdown header immediately preceding the artifact reference.

## Risk Factor Register
**Artifact:** `./dist/<TICKER>/artifacts/risk_register.csv`

```csv
Risk_Category,Risk_Factor_Title,Verbatim_Excerpt
Legal and Regulatory,Regulatory Changes,"exact phrase ""..."" from 10-K"
Political,Macroeconomic Uncertainty,"exact phrase ""..."" from 10-K"
```

Columns:
- `Risk_Category` - High-level category
- `Risk_Factor_Title` - Extracted heading verbatim
- `Verbatim_Excerpt` - 50-150 word quote with exact phrase syntax

**Report reference example:** `### Principal Risk Factors (Item 1A) [^2]` followed by `> Full register: ./dist/<TICKER>/artifacts/risk_register.csv`

## Financial Indicators
**Artifact:** `./dist/<TICKER>/artifacts/financial_indicators.csv`

```csv
Metric,FY2023,FY2022,FY2021,Unit,Source
Total_Revenue,158104,177556,182447,$M,10-K Income Statement
Net_Income,49552,58471,57048,$M,10-K Income Statement
Profit_Margin,31.3%,32.9%,31.2%,Percent,Derived
ROE,15.7%,16.1%,14.8%,Percent,Derived
```

Columns:
- `Metric` - Short metric name
- `FY2023`, `FY2022`, `FY2021` - Fiscal year values
- `Unit` - USD, Percent, Ratio
- `Source` - “10-K Income Statement”, “Derived”, etc.

## Credit Concentrations (Banks Only)
**Artifact:** `./dist/<TICKER>/artifacts/credit_concentrations.csv`

```csv
Portfolio,Total_Exposure,Per_of_Total,Credit_Quality
Credit_Cards,1425563,41.7%,Medium
Mortgages,987654,28.9%,Low
Commercial,765432,22.4%,Medium
Consumer,234567,6.9%,Low
Other,0,0%,N/A
```

Columns:
- `Portfolio` - Counterparty type or product segment
- `Total_Exposure` - USD amount (millions)
- `Per_of_Total` - Percentage of overall portfolio
- `Credit_Quality` - Distributed / Risk-weighted / Internal Rating

## Peer Comparison
**Artifact:** `./dist/<TICKER>/artifacts/peer_comparison.csv`

```csv
Company,Revenue_2025_M,NetIncome_2025_M,TotalAssets_2025_B,ROE_2025,EfficiencyRatio_2025,MarketCap_B
[JPM],182447,57048,4424.9,15.7%,N/A,802.0
[Peer1],,,,,,
[Peer2],,,,,,
```

Columns:
- `Company` - Ticker or name
- `Revenue_2025_M`, `NetIncome_2025_M`, `TotalAssets_2025_B` - Latest fiscal year values
- `ROE_2025`, `EfficiencyRatio_2025` - Derived ratios
- `MarketCap_B` - In billions (Yahoo Finance only)

## Litigation Proceedings (if extensive)
**Artifact:** `./dist/<TICKER>/artifacts/litigation_proceedings.csv`

```csv
Case_Name,Court_Jurisdiction,Status,ASC450_Classification,Estimated_Loss_Range
```

Columns:
- `Case_Name` - Name of proceeding
- `Court_Jurisdiction` - Court or regulatory body
- `Status` - Pending, On Appeal, Settled, Dismissed
- `ASC450_Classification` - Probable, Reasonably Possible, Remote
- `Estimated_Loss_Range` - Range as disclosed in filing

## Scenario Synthesis
**Artifact:** `./dist/<TICKER>/artifacts/scenario_synthesis.csv`

```csv
Scenario,Trigger,Primary_Risk_Channel,Severity,Source_Anchor
S1,Geopolitical escalation,Credit to Capital,High,[^n]
S2,AI cyber disruption,Cyber to Operational,High,[^n]
S3,CRE systemic stress,Credit to Earnings,Medium,[^n]
```

Columns:
- `Scenario` - Scenario label
- `Trigger` - External event
- `Primary_Risk_Channel` - Risk cascade path
- `Severity` - Low/Medium/High
- `Source_Anchor` - Citation number(s)

## Data Gaps
**Artifact:** `./dist/<TICKER>/artifacts/data_gaps.csv`

```csv
Gap_ID,Data_Item,Location,Priority,Action_Required
GAP-001,"","",HIGH,""
GAP-002,"","",MEDIUM,""
```

Columns:
- `Gap_ID` - Unique identifier
- `Data_Item` - What data was missing
- `Location` - File/section where data should exist
- `Priority` - HIGH/MEDIUM/LOW
- `Action_Required` - Specific retrieval command

## Critical Rules
- All financial figures MUST come from `edgartools_edgar_compare` or direct 10-K notes
- "N/A" is acceptable if a metric is not disclosed in the 10-K
- Market cap is the ONLY exception: may come from Yahoo Finance (cite with separate [^n])
- "Derived" metrics must be labeled in the `Source` column
