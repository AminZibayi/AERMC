# Phase 12 — Risk Interconnections

## Steps

1. Review all risks extracted in Phases 3–11.
2. Identify causal links and cascading effects between risk domains (e.g., Macro Shock → Credit Default → Liquidity constraint).
3. For each interconnection, document: Trigger risk, Cascades to, Amplifier.
4. Generate Mermaid diagrams and write each diagram's source code to a separate artifact file:
   - Risk cascade graph → `./dist/<TICKER>/artifacts/risk_cascade.mermaid`
   - Governance risk map → `./dist/<TICKER>/artifacts/governance_risk_map.mermaid`
   - Financial trend chart → `./dist/<TICKER>/artifacts/financial_trend.mermaid`
   - Credit concentration pie chart → `./dist/<TICKER>/artifacts/credit_pie.mermaid`
5. In the report, reference each artifact file path with a descriptive caption. Do NOT embed Mermaid code blocks in the report body.

## Required Outputs

| Output | Source |
|--------|--------|
| Risk Cascade Graph (graph LR) | Risk factor register + nexus analysis → `risk_cascade.mermaid` |
| Governance Risk Map (graph TD) | Governance structure from Phase 5 → `governance_risk_map.mermaid` |
| Financial Trend Chart (xychart-beta) | Financial data from Phase 6 → `financial_trend.mermaid` |
| Credit Concentration Chart (pie) | Credit exposure data from Phase 7 → `credit_pie.mermaid` |
| Report references | Markdown captions with file paths and `[^n]` |

## Critical Rules

- Each Mermaid diagram MUST have a plain text caption in the report describing what it shows and linking to the artifact file
- Node labels in Mermaid must be derived from the filing — do not use generic labels like "Risk 1" or "Company A"
- The cascade graph must include at least 5 distinct risk nodes from the 10-K risk factors
- The `pie` chart must show Top 5 exposures only (not all 20+ sectors) — group the rest as "Other"
- Data in diagrams must match the numbers in the accompanying tables/CSVs exactly
- Include a "Cascade Scenario" paragraph for the most significant 2 cascades, describing the full causal chain
- Do NOT embed Mermaid code blocks in `ERM_Report.md`. Write diagram source to `.mermaid` artifact files and reference them by path.
