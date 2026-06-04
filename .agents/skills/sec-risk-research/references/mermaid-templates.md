# Mermaid Diagram Templates for ERM Artifact Files

All diagrams use Mermaid syntax and must be written as standalone `.mermaid` artifact files in `./dist/<TICKER>/artifacts/`. In `ERM_Report.md`, include only a descriptive caption with the artifact file path — do NOT embed Mermaid code blocks in the report body.

**Critical:** Each `.mermaid` file must contain ONLY the Mermaid code block (no markdown wrappers). Include a one-sentence caption below the file path reference in the report.

## 1. Risk Cascade Graph
**Artifact:** `./dist/<TICKER>/artifacts/risk_cascade.mermaid`

```
graph TD
RF1[Credit Risk] --> RF2[Liquidity Risk]
RF2 --> RF3[Market Risk]
RF1 --> RF4[Regulatory Risk]
RF3 --> RF4
```

Replace node labels with actual risk names. Include at least 5 distinct risk nodes from the 10-K risk factors.

## 2. Governance Risk Map
**Artifact:** `./dist/<TICKER>/artifacts/governance_risk_map.mermaid`

```
flowchart LR
Board[Board of Directors] --> RC[Risk Committee]
RC --> CRO[Chief Risk Officer]
CRO --> RM[Risk Managers]
RM --> OB[Business Operations]
OB --> IC[Internal Controls]
IC --> IA[Internal Audit]
IA --> RC
```

Extend with actual committee titles from proxy governance text. Replace node labels with entity-specific titles.

## 3. Financial Risk Trend
**Artifact:** `./dist/<TICKER>/artifacts/financial_trend.mermaid`

```
xychart-beta
title "Key Financial Metrics - 3-Year Trend"
x-axis [FY2021, FY2022, FY2023]
y-axis "USD (B)"
0 --> 200
line [100, 130, 160]
line [80, 90, 100]
```

Requires at least 2 data series (e.g., Revenue and Net Income). Label axes with units.

## 4. Credit Exposure Pie Chart
**Artifact:** `./dist/<TICKER>/artifacts/credit_pie.mermaid`

```
pie title Credit Concentrations
    "Credit Cards" : 30
    "Mortgages" : 25
    "Commercial" : 20
    "Consumer" : 15
    "Other" : 10
```

Use `per_of_total` values from Credit Concentrations CSV. Show Top 5 only.

## 5. Three Lines Model Governance Graph
**Artifact:** `./dist/<TICKER>/artifacts/three_lines_model.mermaid`

```
graph LR
FL1[1st Line: Operations Management] --> FL2[2nd Line: Risk & Compliance]
FL2 --> FL3[3rd Line: Internal Audit]
FL3 --> Board[Board / Risk Committee]
```

Indicates the Three Lines of Defense model. Replace node labels with entity-specific titles.

## Report Caption Format

For each diagram, include in `ERM_Report.md`:

> **Risk Cascade Diagram** — see artifact: `./dist/<TICKER>/artifacts/risk_cascade.mermaid` [^n]

Where `[^n]` cites the data source (e.g., 10-K Risk Factors, Proxy Statement).

## Critical Rules
- Each diagram file must contain ONLY the Mermaid code block content (no markdown fences)
- Node labels must be derived from the filing — do not use generic labels like "Risk 1"
- The cascade graph must include at least 5 distinct risk nodes
- The pie chart must show Top 5 exposures only (group the rest as "Other")
- Data in diagrams must match the numbers in the accompanying tables/CSVs exactly
- Include a "Cascade Scenario" paragraph in the report body for the most significant 2 cascades describing the full causal chain — these are text paragraphs, NOT Mermaid code
