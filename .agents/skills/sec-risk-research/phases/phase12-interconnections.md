# Phase 12 — Risk Interconnections

## Steps
1. Review all risks extracted in Phases 3–11.
2. Identify causal links and cascading effects between risk domains (e.g., Macro Shock → Credit Default → Liquidity constraint).
3. For each interconnection, document: Trigger risk, Cascades to, Amplifier.
4. Generate Mermaid diagrams:
   - Risk cascade graph (`graph LR` visualizing the risk cascades)
   - Governance risk map (`graph TD` showing Board/Committee to CRO to Lines of Defense cascade)
   - Financial risk xychart (`xychart-beta` for Revenue vs Net Income and/or PCL trend)
   - Credit concentration pie chart (`pie` for Top 5 exposures)
5. Embed Mermaid code blocks in the report with captions.

## Required Outputs

| Output | Source |
|--------|--------|
| Risk Cascade Graph (graph LR) | Risk factor register + nexus analysis |
| Governance Risk Map (graph TD) | Governance structure from Phase 5 |
| Financial Trend Chart (xychart-beta) | Financial data from Phase 6 |
| Credit Concentration Chart (pie) | Credit exposure data from Phase 7 |

## Critical Rules
- Each Mermaid diagram MUST have a plain text caption below it describing what it shows
- Node labels in Mermaid must be derived from the filing — do not use generic labels like "Risk 1" or "Company A"
- The cascade graph must include at least 5 distinct risk nodes from the 10-K risk factors
- The `pie` chart must show Top 5 exposures only (not all 20+ sectors) — group the rest as "Other"
- Data in diagrams must match the numbers in the accompanying tables/CSVs exactly
- Include a "Cascade Scenario" paragraph for the most significant 2 cascades, describing the full causal chain
