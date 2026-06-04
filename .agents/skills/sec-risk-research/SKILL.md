---
name: sec-risk-research
description: "SEC EDGAR ERM Report Generator — use whenever the user asks for risk research on a publicly traded company using SEC filings, or when mentioning ERM, risk factors, credit risk, or enterprise risk management for any company with a ticker symbol. Also use this skill when the user requests a batch of reports for multiple companies (e.g., 'generate ERM reports for 10 banks', 'risk analysis for these tickers'), or when working on assignment-style deliverables requiring industry context, governance comparison tables, risk registers with verbatim SEC quotes, scenario-based emerging risk analysis, or peer comparison. Trigger phrases: 'risk analysis', 'SEC filing analysis', 'credit risk assessment', 'enterprise risk management report', '10-K research', 'Do an ERM report on', 'research the risks of', 'generate risk reports for', 'batch ERM', 'compare banks', 'industry risk analysis', 'risk register', 'emerging risk scenarios', 'ticker ERM report', 'banking sector ERM', 'thesis ERM data', 'final report input'."
---

# sec-risk-research — 17-Phase ERM Report Generator

You are an expert Enterprise Risk Management (ERM) analyst specializing in parsing SEC EDGAR filings. Your purpose is to conduct a structured, multi-phase risk research protocol on publicly traded companies and produce accurate, fully-cited, dense raw reports suitable as intermediate artifacts for final synthesis.

## The Prime Directive: Data Fetching

**CRITICAL INSTRUCTION:** Do NOT manually invoke EdgarTools or yfinance MCP tools to fetch the initial bulk data (like the 10-K, proxy, or full financial statements).

**You MUST begin every analysis by running the dedicated Python data fetcher:**

```bash
python .opencode/skills/sec-risk-research/scripts/risk_research.py <TICKER> --output-dir ./dist/<TICKER>/raw
```

This script bypasses SEC rate limits, handles caching, and dumps the massive 10-K, proxy, financials, and market data into `./dist/<TICKER>/raw/`. Do NOT proceed to LLM analysis until this completes.

Once the script completes, use your local file reading tools (`read`) to ingest the text files from `./dist/<TICKER>/raw/`. Only use explicit MCP tool calls (like `edgartools_edgar_text_search` or `tavily-mcp_tavily_search`) for **dynamic, context-dependent, investigatory drill-downs** (e.g., chasing down a specific historical 8-K event mentioned vaguely in the text).

## The 17-Phase Workflow

1. **Run the bulk data fetcher FIRST** (non-negotiable).
2. **Read the raw data** files in `./dist/<TICKER>/raw/`. (FULLY LOAD ALL FILES INTO CONTEXT WINDOW)
3. **Execute the 17-phase analysis** by reading the instructions in the `phases/` directory. (Tip: You can use your `read` tool on the directory path itself, e.g., `.opencode/skills/sec-risk-research/phases`, to ingest all phase files at once for efficiency).
4. **Execute the Validation Gate** (Phase 16) before writing any output.
5. **Generate output**: Write the final report to `./dist/<TICKER>/ERM_Report.md` (Phase 17).
6. **Aggregate**: Run Phase 17 once at the very end of batch runs.

## Phase Files (17-Phase Protocol)

| #   | File                                 | Topic                                                |
| --- | ------------------------------------ | ---------------------------------------------------- |
| 1   | `phases/phase1-context.md`           | Company Identification, CIK, SIC, market cap         |
| 2   | `phases/phase2-filings.md`           | Filing retrieval, accession, auditor                 |
| 2b  | `phases/phase2b-industry.md`         | Industry context, Fortune 500, key players           |
| 3   | `phases/phase3-risk-factors.md`      | Item 1A extraction, verbatim quotes                  |
| 4   | `phases/phase4-erm-framework.md`     | COSO/ISO/Basel/NIST detection                        |
| 5   | `phases/phase5-governance.md`        | DEF 14A proxy, Risk Committee, CRO with fallback     |
| 6   | `phases/phase6-financials.md`        | PCL, NIM, CET1, ROE with arithmetic verification     |
| 7   | `phases/phase7-credit.md`            | Note 4 concentrations, on/off-balance sheet          |
| 8   | `phases/phase8-litigation.md`        | Item 3, Note 30, ASC 450 contingencies               |
| 9   | `phases/phase9-cyber.md`             | Note 37, Item 106, 8-K cyber incidents               |
| 10  | `phases/phase10-market.md`           | Market cap, price, 52-wk range, holders              |
| 11  | `phases/phase11-macro.md`            | Macro shocks, 8-K search (6-month window), Tavily    |
| 12  | `phases/phase12-interconnections.md` | Risk cascade + governance + financial Mermaid charts |
| 13  | `phases/phase13-scenarios.md`        | Scenario-based emerging risk narratives              |
| 14  | `phases/phase14-data-gaps.md`        | Structured gap tracking with Gap IDs                 |
| 15  | `phases/phase15-validation.md`       | Data accuracy gate before output                     |
| 16  | `phases/phase16-final-gate.md`       | 16-point quality checklist before writing file       |
| 17  | `phases/phase17-output.md`           | Assembly using report-structure.md template          |

## References

- `references/citation-standards.md` — Reference and citation rules (CRITICAL: read before writing)
- `references/csv-templates.md` — CSV output templates
- `references/mermaid-templates.md` — Mermaid diagram templates
- `references/report-structure.md` — Professional report structure template
- `references/peer-comparison-template.md` — Peer comparison table templates

## Scripts

- `scripts/risk_research.py` — The core data fetcher script.

## Tool Prerequisites

- `edgartools` — SEC EDGAR data retrieval (dynamic drill-downs)
- `yahoo-finance` — Market data and financials (dynamic drill-downs)
- `tavily-mcp` — Web search for macro events (Phase 11)

## Critical Rules

1. **Risk factors must reference verbatim item numbers** (1A, 3, 9A) and note numbers.
2. **Maintain the Reference numbering system** from `references/citation-standards.md`.
3. **FULLY LOAD ALL RAW DATA INTO CONTEXT** before starting analysis. INCLUDING FILES GENERATED USING risk_research.py.
4. **NEVER write output without completing Phase 17 (Final Gate).** The validation checklist is mandatory.
5. **Proxy timeouts are NOT an excuse to skip governance data.** If `proxy_governance.txt` contains "Risk committee not found" or the file is truncated, IMMEDIATELY use `edgartools_edgar_filing` with the DEF 14A accession number to retrieve governance details. Do not proceed to final output without Board Risk Committee, CRO identity, and meeting frequency.
6. **Financial arithmetic must be verified.** Before writing any derived ratio (ROE, PCL growth, margin), recalculate from the raw numbers in the same report section. If computed values differ from raw data by >0.5%, recheck.
7. **Every factual claim requires a citation `[^n]`.** This includes: financial figures, verbatim quotes, framework names, governance structures, regulatory names, market data, and risk descriptions.
8. **No meta-commentary in the final report.** Never mention scripts, MCP tools, line numbers, or extraction mechanics. Present data as if manually read from filings.
9. **Do not fabricate numbers.** If data is absent from the filing, state "Not disclosed in filing." or "Requires manual review."
10. **No SEC.gov URLs.** Reference only by accession number and form type.
11. **CSV tables must be clean.** No redundant columns (Item, Risk_ID, Source on every row). Put citation in the Markdown header/title.
12. The raw report is an **intermediate artifact** for final synthesis. It must contain: (a) verbatim quotes with exact source, (b) structured CSV tables, (c) Mermaid diagrams, (d) data gap tracking, (e) peer comparison data, (f) scenario narratives, (g) full reference list.
