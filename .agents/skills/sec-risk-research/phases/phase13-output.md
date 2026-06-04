# Phase 13 — Final Report Assembly

## Steps
1. Assemble all findings into a unified, coherent, and professional Enterprise Risk Management (ERM) Report at `./dist/<TICKER>/ERM_Report.md`. **DO NOT** just output a disjointed list of "Phase 1", "Phase 2", etc. Structure the report professionally.
2. Apply dense, scientific academic referencing throughout the narrative text using numbered references `[^1]`. **Every** factual claim, financial figure, and risk quote MUST be immediately followed by a citation.
3. Integrate Mermaid charts and figures thoughtfully into the narrative where they are most relevant, rather than clumping them together. Explain what the chart shows in the text.
4. Include mandatory CSV tables embedded in fenced blocks, but **do not include redundant columns** (e.g., remove repetitive "Item", "Source", "Risk_ID" columns). Instead, place the source citation `[^n]` in the table's Markdown header/title.

## Professional Report Structure Outline
Your final report MUST follow this cohesive professional structure:

1. **Executive Summary & Company Profile** (Phase 1, 2, 10)
   - Include Market context and basic filing metadata.
2. **Enterprise Risk Framework & Governance** (Phase 4, 5)
   - Detail the ERM Framework (COSO/ISO) and Risk Committee structure.
   - Include the Risk Governance Mermaid `graph TD` chart here.
3. **Macroeconomic Shocks & Interconnections** (Phase 11, 12)
   - Discuss external shocks and how risks interconnect.
   - Include the Risk Cascades Mermaid `graph LR` chart here.
4. **Principal Risk Factors** (Phase 3)
   - Narrative summary of key risks.
   - *Risk Factor Register CSV* (Simplified columns, source cited in table title).
5. **Financial & Credit Risk Profile** (Phase 6, 7)
   - *Financial Indicators CSV* and *Credit Concentrations CSV* (for banks).
   - Include Financial Trend Mermaid `xychart-beta` and Credit Exposure `pie` chart.
6. **Operational, Cyber & Litigation Risk** (Phase 8, 9)
   - Detail SEC Item 106 cyber disclosures and material litigations.
7. **References**
   - Full numbered list `[^1]`, `[^2]`, etc. tracing back to specific filings and notes.
   - **CRITICAL:** Use ONLY rigorous academic citations (e.g., *JPMorgan Chase & Co. (2026). Form 10-K...*). **Never** include meta-commentary about the Python script, LLM extraction mechanics, or tool executions.

## Required Outputs
| Output | Format |
|--------|--------|
| Final ERM Report | Markdown file at `./dist/<TICKER>/ERM_Report.md` following the professional structure above. |
| CSV Fenced Blocks | Cleaned tables (no redundant columns), citations in the title. |
| Mermaid Diagrams | Interwoven naturally with the text. |
| Full Reference List | Numbered list appended at the end. |
