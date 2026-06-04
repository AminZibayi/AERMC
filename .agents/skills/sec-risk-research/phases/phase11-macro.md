# Phase 11 — Macro & Market Risks

## Steps
1. Identify current top macro risks: interest rates, inflation, FX, geopolitical, regulatory.
2. Use `edgartools_edgar_text_search` to dynamically search 8-K filings for risk-related events in the last 6 months.
3. Use `tavily-mcp_tavily_search` to dynamically search for recent macro shocks affecting the industry. Focus on impacts from: Iran-US conflict, Rate Volatility, Tariffs, CRE stress, AI disruption.
4. Cross-reference any disclosed macro sensitivity from `./dist/<TICKER>/raw/item_1A_risk_factors.txt`.
5. Note climate / ESG disclosures if relevant.
6. Identify specific exposures the disclosures reveal (e.g., "Russia-related sanctions have generated $439M in judgments" — use for Phase 13 scenarios).
7. Write "Macro Risk Landscape" section to report.

## Required Outputs

| Output | Source |
|--------|--------|
| Key Macro Risk Factors (identified themes) | edgar 8-K search + Tavily |
| Relevant 8-K Filings | edgar dynamic filing search |
| Industry-Specific Macro Shocks | Tavily web search |
| Climate / ESG Exposure | 10-K Item 1A or Item 1 |
| Macro Sensitivity Statement | Verbatim from Item 1A / MDA |

## Critical Rules
- Tavily data is only for **current events context** (e.g., "In June 2026, tariffs escalated on..."). Do NOT use Tavily to generate the firm's risk analysis — that must come from the 10-K.
- Each macro shock must link to a specific firm exposure (e.g., "JPM's $224.9B CRE portfolio" or "JPM's $3.4T total credit exposure")
- The 8-K search must cover at least 6 months, not 3 months, to ensure comprehensive coverage
- If no 8-K events are found, explicitly state "No risk-related 8-K filings identified in the search period"
- All findings must be forwarded to Phase 13 (Scenarios) as input
