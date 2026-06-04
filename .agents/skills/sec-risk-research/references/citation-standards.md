# Citation Standards & Reference Rules

## 16. Reference Standards

1. **DENSE, FREQUENT CITATIONS (CRITICAL)**: You must write in a highly rigorous, scientific, academic style. **Do NOT** wait until the end of a paragraph to cite. **Every single** factual claim, quantitative figure, and risk description MUST be immediately followed by a numbered citation `[^n]`.
   - *Bad:* JPM's revenue increased. They face cyber risks and regulatory challenges. [^1]
   - *Good:* JPM's revenue increased to $182.4B in FY2025 [^1]. The bank faces elevated cybersecurity risks [^2] and complex regulatory challenges [^3].

2. **Strict Academic Reference Formatting (CRITICAL)**: The final reference list must look like a professional academic bibliography (e.g., IEEE or APA format tailored for financial filings). **Never include meta-commentary, tool names, or extraction mechanics.**
   - *Bad:* Metadata extracted via risk_research.py, June 4, 2026
   - *Bad:* EDGAR full-text search for "cybersecurity incident" in 8-K filings — 0 results
   - *Bad:* Proxy governance text — risk committee not separately identified
   - *Bad:* JPMorgan Chase & Co., Form 10-K, Item 1A. Risk Factors, FY 2025 (lines 1–1331)
   - *Good:* JPMorgan Chase & Co. (2026). *Form 10-K for the Fiscal Year Ended December 31, 2025* (Accession No. 0001628280-26-008131). U.S. Securities and Exchange Commission.
   - *Good:* JPMorgan Chase & Co. (2026). *Form 10-K, Item 1A. Risk Factors*.
   - *Good:* JPMorgan Chase & Co. (2026). *Form 10-K, Note 30 — Litigation*.
   - *Good:* JPMorgan Chase & Co. (2026). *Schedule 14A (Proxy Statement)* (Accession No. 0000019617-26-000096). U.S. Securities and Exchange Commission.

8. **Artifact Citations**: When referencing CSV or Mermaid artifact files in the report, place the `[^n]` citation in the markdown header line immediately before the artifact reference. Do NOT embed raw data in the report body. The citation anchors the data source for the entire artifact.
   - *Good:* `### Financial Risk Indicators (3-Year Trend) [^3]` followed by `> Full data: ./dist/JPM/artifacts/financial_indicators.csv`
   - *Good:* `### Risk Cascade Diagram [^5]` followed by `> Artifact: ./dist/JPM/artifacts/risk_cascade.mermaid`
   - *Bad:* Embedding the raw CSV rows or Mermaid code block directly in `ERM_Report.md`
8. **File Section in References**: When citing SEC filings, always include the specific section or item number in the reference (e.g., *Item 1A*, *Note 30*, *Controls and Procedures*). This is crucial for verifying the exact location of the information within the massive filings.
   - *Good:* Yahoo Finance. (2026, June 4). *JPMorgan Chase & Co. (JPM) Institutional Holders*. Retrieved from https://finance.yahoo.com/quote/JPM/holders.

3. **Verbatim Citations**: All extracted quotes must use exact-text citation format:
   > exact phrase "..." from `Source` (Section, Item, or Note reference) [^n]

4. **Page Numbers**: If pagination is unavailable, only reference the Item or Note number. Do not fabricate page numbers.

5. **Source Priority**: 10-K > Proxy > 8-K > Yahoo Finance > Tavily (for ERM content).

6. **Framework Citations**: When naming frameworks (COSO, ISO 31000, Basel III, NIST), cite the exact wording found in the filing [^n], even if paraphrased labels are used.

7. **Reference Numbering**: Maintain a consistent numbering system for all citations (e.g., [^1], [^2], [^3]) in the final report's Reference section at the very end.

## 17. Prohibited Practices

1. **NO META-COMMENTARY**: Never mention scripts (`risk_research.py`), MCP tools (`tavily`, `edgartools`), line numbers, or extraction mechanics in the final report. Hide the analytical sausage-making. Present the data as if you manually read the filings.

2. **No Fabrication**: Do not quote content not present in the raw SEC filing text or Yahoo Finance data.

3. **No Paraphrase Without Source**: Any statement summarizing risk content must be traceable to a verbatim quote in the report.

4. **No SEC/SEC.gov URLs**: Do not generate, guess, or embed any SEC.gov URLs — reference only by accession number and form type.

5. **No Secret Logging**: Do not include API keys, credentials, or environment variables in the report output.

6. **No Out-of-Scope Recommendations**: Do not recommend specific investment actions. Limit analysis to risk assessment per the 13-phase protocol.

7. **No Inferred Numbers Without Label**: Any derived ratio or metric must be labeled "Derived" in the Source column of output tables.

8. **No Semantic Leakage**: Do not infer facts not supported by the source text. If information is absent, state "Not disclosed in filing."
