# Phase 12 — Risk Interconnections

## Steps

1. Review all risks extracted in Phases 3–11.
2. Identify causal links and cascading effects between risk domains (e.g., Macro Shock → Credit Default → Liquidity constraint).
3. For each interconnection, document: Trigger risk, Cascades to, Amplifier.
4. Generate Mermaid diagrams and embed each diagram directly inline in `ERM_Report.md` using ` ```mermaid ` fenced code blocks:
   - Risk cascade graph (graph TD or graph LR)
   - Governance risk map (flowchart LR or graph TD)
   - Financial trend chart (xychart-beta)
   - Credit concentration pie chart (pie)
5. Each Mermaid diagram embedded in the report MUST be followed by a descriptive plain text caption explaining what it shows and citing the data source.

## Required Outputs

| Output | Placement |
|--------|-----------|
| Risk Cascade Graph (graph LR) | Embedded inline in `ERM_Report.md` |
| Governance Risk Map (graph TD) | Embedded inline in `ERM_Report.md` |
| Financial Trend Chart (xychart-beta) | Embedded inline in `ERM_Report.md` |
| Credit Concentration Chart (pie) | Embedded inline in `ERM_Report.md` |

## Critical Rules

- Each Mermaid diagram in the report MUST be wrapped in ` ```mermaid ` fenced code blocks with a one-sentence plain text caption below it
- Node labels in Mermaid must be derived from the filing — do not use generic labels like "Risk 1" or "Company A"
- The cascade graph must include at least 5 distinct risk nodes from the 10-K risk factors
- The `pie` chart must show Top 5 exposures only (not all 20+ sectors) — group the rest as "Other"
- Data in diagrams must match the numbers in the accompanying tables/CSVs exactly
- Include a "Cascade Scenario" paragraph for the most significant 2 cascades, describing the full causal chain
- Mermaid diagrams are embedded inline in `ERM_Report.md`. Do NOT write `.mermaid` artifact files.
