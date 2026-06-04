# Phase 2b — Industry Context & Key Players

## Purpose

This phase generates the Industry Context section, enabling the final report to describe the bank's operating environment, competitive landscape, and market position using ONLY factual, verifiable data.

## Steps

1. **Extract Metadata:** Read `./dist/<TICKER>/raw/metadata.json` to extract:
   - Company name, ticker, CIK, SIC code
   - Exchange listing

2. **Peer Selection via User Input:**
   - You MUST NOT guess the peer companies. Use the `question` tool to ask the user: "Which specific peer companies (tickers) should I use to rank and compare [Target Ticker] against for the industry analysis?"
   - If the user provides a list (e.g., "BAC, WFC, C, GS"), proceed to step 3.
   - If the user explicitly tells you to figure it out yourself, use `yahoo-finance_yfinance_get_top(sector="Financial Services", top_type="top_companies")` or `edgartools_edgar_screen(sic=[Target SIC])` to find the largest peers.

3. **Factual Ranking (Market & Fundamentals):**
   - **Market Cap Rank (Sector & Global):** Use `yahoo-finance_yfinance_get_top` to determine the target company's rank by market capitalization within its sector. Use `tavily-mcp_tavily_search` to acquire its Global Market Cap Rank across all sectors worldwide.
   - **Fundamental Rank (Assets, Revenue, Net Income):**
     - **Sector/Peer Rank:** Use `edgartools_edgar_compare` passing the target ticker and the peer tickers to mathematically rank them within the sector by **Total Assets**, **Revenue**, and **Net Income**.
     - **Global Rank:** Use `tavily-mcp_tavily_search` to determine the company's global rank for **Total Assets**, **Revenue**, and **Net Income** across all public companies.
   - Do NOT use generic lists without verifying the underlying financial metric. Rely on the hard financial data retrieved from the SEC and market tools to ground these rankings.

4. **Industry Overview (Strictly from 10-K):**
   - **CRITICAL:** Do NOT hallucinate or make up a generic industry review.
   - Read `./dist/<TICKER>/raw/item_1_business.txt`. Extract the company's own description of its competitive environment, market structure, and key regulatory bodies (e.g., Federal Reserve, OCC, FDIC).
   - Only state facts explicitly claimed by the company in Item 1.

5. **Write "Industry Context Brief"** as a structured markdown section. This will be extracted by the final synthesis step.

## Required Outputs

| Output                          | Source                                                 |
| ------------------------------- | ------------------------------------------------------ |
| Industry Sector / Sub-sector    | Derived from SIC + metadata                            |
| Peer Company List               | User input via `question` tool (or fallback MCP tools) |
| Sector & Global Market Cap Rank | `yfinance_get_top` & `tavily_search`                   |
| Sector & Global Asset Rank      | `edgar_compare` & `tavily_search`                      |
| Sector & Global Revenue Rank    | `edgar_compare` & `tavily_search`                      |
| Sector & Global Net Income Rank | `edgar_compare` & `tavily_search`                      |
| Industry Overview & Competition | `item_1_business.txt` (Strictly verbatim/cited)        |
| Regulatory Bodies               | `item_1_business.txt`                                  |
