# Peer Comparison Table Templates

Use these templates when generating peer comparison data from `edgartools_edgar_compare`.

## Template 1: Full Multi-Company Financial Comparison (5 companies)

_Source: 10-K Consolidated Financial Statements, FY2025 [^n]_

```csv
Company,Revenue_2025_M,NetIncome_2025_M,TotalAssets_2025_B,ROE_2025,EfficiencyRatio_2025,ProvLosses_2025_M,MarketCap_B
[JPM],182447,57048,4424.9,15.7%,N/A,14212,802.0
[Peer1],,,,,,,
[Peer2],,,,,,,
[Peer3],,,,,,,
[Peer4],,,,,,,
Sector_Average,,,,,,
```

## Template 2: Target vs. Peer Averages (Narrative Table)

| Metric             | [TARGET] | Peer Average | Outperformance |
| ------------------ | -------- | ------------ | -------------- |
| Revenue Growth YoY | +X.X%    | +X.X%        | +X.X pp        |
| Net Margin         | X.X%     | X.X%         | +X.X pp        |
| ROE                | X.X%     | X.X%         | +X.X pp        |
| PCL / Total Loans  | X.X%     | X.X%         | +X.X pp        |
| CET1 Ratio         | XX.X%    | XX.X%        | +X.X pp        |

## Template 3: Governance Comparison

| Company  | Market Cap ($B) | Risk Committee | CRO Named | Annual Meetings | Total Assets ($B) | Revenue ($B) | Net Income ($B) | ROE |
| -------- | --------------- | -------------- | --------- | --------------- | ----------------- | ------------ | --------------- | --- |
| [TARGET] | XXX             | Yes / No       | Yes / No  | X               | XXXX              | XXX          | XX              | XX% |
| Peer1    | ...             | ...            | ...       | ...             | ...               | ...          | ...             | ... |

## Critical Rules

- All financial figures MUST come from `edgartools_edgar_compare` or direct 10-K notes
- "N/A" is acceptable if a metric is not disclosed in the 10-K — do not fabricate
- Market cap is the ONLY exception: may come from Yahoo Finance (cite with separate [^n])
- The [TARGET] row is always first; peers follow in alphabetical or market-cap order
- Sector Average: compute from the 4 peers, excluding the target
