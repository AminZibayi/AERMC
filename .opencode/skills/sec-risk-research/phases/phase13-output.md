# Phase 13 — Final Report Assembly

## Steps
1. Assemble all sections into `./dist/<TICKER>/ERM_Report.md`.
2. Include mandatory CSV tables embedded in fenced blocks:
   - Risk Factor Register CSV
   - Financial Indicators CSV
   - Credit Concentrations CSV (banks only; omit for non-banks)
3. Apply reference numbering system per `references/citation-standards.md`. All factual claims MUST use academic numbered referencing `[^1]` tracing back to the specific SEC filing/note.
4. Include all Mermaid diagrams generated in Phase 12.
5. Verify all verbatim quotes use `exact phrase "..." from <source>` format.
6. Check Prohibited Practices: Do not invent quantitative likelihood/impact scores without explicit formulas. Do not fill gaps (if a framework/committee isn't disclosed, state "Not disclosed"). Ensure no missing citations.

## Required Outputs
| Output | Format |
|--------|--------|
| Final ERM Report | Markdown file at `./dist/<TICKER>/ERM_Report.md` |
| Risk Factor Register | CSV fenced block |
| Financial Indicators | CSV fenced block |
| Credit Concentrations | CSV fenced block (if applicable) |
| Mermaid Diagrams | Mermaid fenced blocks (`graph LR`, `graph TD`, `xychart-beta`, `pie`) |
| Full Reference List | Numbered list appended at the end |
