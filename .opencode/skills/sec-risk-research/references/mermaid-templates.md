# Mermaid Diagram Templates for ERM Report

All diagrams use Mermaid syntax inside fenced code blocks with `mermaid` language tag.

## 1. Risk Cascade Graph (`riskMap`)

```mermaid
graph TD
    RF1[Credit Risk] --> RF2[Liquidity Risk]
    RF2 --> RF3[Market Risk]
    RF1 --> RF4[Regulatory Risk]
    RF3 --> RF4
```

Use this for Stage 2 (cascade) analysis. Replace node labels with actual risk names.

## 2. Governance Risk Map Flowchart

```mermaid
flowchart LR
    Board[Board of Directors] --> RC[Risk Committee]
    RC --> CRO[Chief Risk Officer]
    CRO --> RM[Risk Managers]
    RM --> OB[Business Operations]
    OB --> IC[Internal Controls]
    IC --> IA[Internal Audit]
    IA --> RC
```

Extend with actual committee titles from proxy governance text.

## 3. Financial Risk Trend (`xychart`)

```mermaid
xychart-beta
    title "Key Financial Metrics — 3-Year Trend"
    x-axis [FY2021, FY2022, FY2023]
    y-axis "USD (B)" 0 --> 200
    line [100, 130, 160]
    line [80, 90, 100]
```

Requires at least 2 data series (e.g., Revenue and Net Income).

## 4. Credit Exposure Pie Chart

```mermaid
pie title Credit Concentrations
    "Credit Cards" : 30
    "Mortgages" : 25
    "Commercial" : 20
    "Consumer" : 15
    "Other" : 10
```

Use `per_of_total` values from Credit Concentrations CSV.

## 5. Three Lines Model Governance Graph

```mermaid
graph LR
    FL1[1st Line: Operations Management] --> FL2[2nd Line: Risk & Compliance]
    FL2 --> FL3[3rd Line: Internal Audit]
    FL3 --> Board[Board / Risk Committee]
```

Indicates the Three Lines of Defense model. Replace node labels with entity-specific titles.
