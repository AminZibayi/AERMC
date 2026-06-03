# Phase 11 — Macro & Market Risks

## Steps

1. Identify current top macro risks: interest rates, inflation, FX, geopolitical, regulatory.
2. Use `edgartools_edgar_text_search` to dynamically search 8-K filings for risk-related events in the last 3 months.
3. Use `tavily-mcp_tavily_search` or any other search tool to dynamically search for recent macro shocks affecting the industry. Focus on impacts from Iran-US conflict, Rate Volatility, Tariffs, CRE stress.
4. Cross-reference any disclosed macro sensitivity from `./dist/<TICKER>/raw/item_1A_risk_factors.txt`.
5. Note climate / ESG disclosures if relevant.
6. Write "Macro Risk Landscape" section to report.

## Required Outputs

| Output                                     | Source                           |
| ------------------------------------------ | -------------------------------- |
| Key Macro Risk Factors (identified themes) | edgartools 8-K search + Tavily   |
| Relevant 8-K Filings (last 3 months)       | edgartools dynamic filing search |
| Industry-Specific Macro Shocks             | Tavily web search                |
| Climate / ESG Exposure                     | 10-K or 20-F disclosures         |
| Macro Sensitivity Statement                | Verbatim from Item 1A / MDA      |
