# Professional Report Structure Template

Use this as the guiding architecture for `ERM_Report.md`. It covers all 17 phases in a unified, readable flow. The agent has creative latitude to embed Markdown tables and Mermaid diagrams inline where they serve readability, and to write long structured datasets to `./dist/<TICKER>/artifacts/` as separate files when the data volume warrants it. Do NOT shatter the reading experience with file-path references for every small table — only lengthy raw datasets (full risk registers, full credit tables, full peer comparisons) belong in artifacts.

---

# Enterprise Risk Management Report: [COMPANY NAME]

**Ticker:** [TICKER] | **CIK:** [CIK] | **[EXCHANGE]**
**Reporting Period:** Fiscal Year Ended [DATE]
**10-K Accession:** [ACCESSION] | **Auditor:** [AUDITOR]
**Report Generation Date:** [DATE]

---

## Executive Summary

[A tight, citation-dense paragraph: what the company does, where it stands financially (key figures), its most significant material risks, and the most important emerging/forward-looking risks. Ground everything in retrieved data.]

---

## 1. Business & Industry Context

### 1.1 Company Overview

[Who the company is, what it does, regulatory status (BHC/FHC status, primary regulators — Fed/OCC/FDIC), geographic footprint, employee count.]

### 1.2 Industry & Competitive Position

[Industry structure, key competitors, the company's relative position (market share, asset rank, revenue rank). Pull from Item 1 and peer comparison data. Note any material industry trends.]

---

## 2. Enterprise Risk Framework & Governance

### 2.1 ERM Framework

[Which framework(s) the company uses (COSO, Basel III, NIST, OCC Heightened Standards). Quote verbatim. Flag where evidence is implicit rather than explicit.]

### 2.2 Governance Structure

[Board oversight architecture: Board → Risk Committee → CRO. Include the Risk Committee name, CRO identity, and meeting frequency where retrievable. Flag gaps transparently.]

### 2.3 Regulatory Capital & Compliance Posture

[CET1 ratio, SCB, CCAR, Basel III endgame exposure, consent orders or enforcement matters. Ground in Item 1 and Item 7A.]

---

## 3. Principal Risk Factors

Present the material risk factor categories extracted from Item 1A. For each category, provide a concise narrative summary (2–4 sentences) grounded in verbatim quotes, then list the key sub-factors.

> **Embedding guidance:** For companies with many risk sub-factors (e.g., JPM's 30+ RF-IDs), embed the detailed register table directly below each category heading rather than sending the reader to an artifact file. Reserve artifact files for extraordinarily long registers (50+ items) or when the report is intended as a data product for downstream processing.

---

## 4. Financial & Credit Risk Profile

### 4.1 Financial Performance — Three-Year Trend

[Revenue, net income, NII, PCL, EPS, ROE, efficiency ratio — presented as a concise Markdown table with YoY change column. Include a brief narrative on the trend direction and what's driving it.]

> **Mermaid:** Embed a `xychart-beta` showing Revenue and Net Income over the 3-year period directly inline if it adds visual clarity. If the chart is complex (multiple series), write to `./dist/<TICKER>/artifacts/financial_trend.mermaid` and reference it.

### 4.2 Credit Concentrations (Note 4)

[Top 5–10 sector concentrations with on-balance-sheet and off-balance-sheet amounts. Highlight any single-name or sector concentrations above 5–10% of total exposure. Note any pending acquisitions or transactions that would materially alter concentrations (e.g., Apple Card).]

> **Embedding guidance:** Embed the full top-10 table directly. For very large peer-bank reports where the full 20+ sector table is needed for completeness, write to `./dist/<TICKER>/artifacts/credit_concentrations.csv` and embed the Top 5 summary table inline.
> **Mermaid:** Embed a concise `pie` chart for the top 5 exposures inline.

### 4.3 Allowance for Credit Losses

[Allowance for loan losses, allowance for lending-related commitments, total ACL. Show the roll-forward beginning → provision → charge-offs → ending. Compute ACL/Total Credit Exposure ratio.]

---

## 5. Operational, Cyber & Litigation Risk

### 5.1 Cybersecurity & Third-Party Risk

[Note 37 disclosure summary (mandatory for FY ending on/after Jan 15, 2025). AI/technology risk exposure, third-party/vendor risk language, recent 8-K cyber incidents. Cite Item 106 and Item 1A verbatim quotes.]

### 5.2 Litigation & Contingencies (Item 3 / Note 30)

[Material proceedings: name, jurisdiction, status, estimated loss ranges. ASC 450 classification. Aggregate reasonably possible loss range.]

### 5.3 Model & Data Risk

[Model risk governance, data management, control environment deficiencies — drawn from Item 1A operational risk factors and any available Note.]

---

## 6. Macroeconomic Shocks & Interconnections

### 6.1 Key Macro Risk Drivers

[Current macro environment: interest rate path, geopolitical flashpoints (Iran, Russia, China), tariff/trade policy, CRE stress, AI disruption. Connect each macro theme to the firm's specific disclosed exposures.]

### 6.2 Risk Cascade Map

[Write 1–3 cascade narratives describing how macro shocks propagate through the firm's risk architecture. E.g., "Rate spike → NIM compression → earnings haircut → dividend coverage pressure → capital constraint."]

> **Mermaid:** Embed the `graph TD` or `graph LR` risk cascade diagram directly inline in the report body using ` ```mermaid ` fenced code blocks. All Mermaid diagrams are embedded inline — there are no `.mermaid` artifact files.

---

## 7. Emerging Risk Scenarios

Present 3–5 forward-looking scenario narratives. Each scenario must be anchored in at least 2 verifiable sources from the 10-K, proxy, or 8-K filings.

### Required scenario types (include those applicable):

1. **Geopolitical / Trade Shock** — sanctions, tariffs, military escalation
2. **Technology Disruption** — AI, quantum computing, fintech
3. **Regulatory / Capital Rule Change**
4. **Climate / Physical Risk** (if applicable)
5. **Systemic Credit Cycle** — recession, counterparty failure

> **Format:** Write the cross-scenario synthesis table inline (5 rows, 5 columns). Write a CSV with the full scenario register to `./dist/<TICKER>/artifacts/scenario_synthesis.csv` if the narratives are extensive.

---

## 8. Market & Ownership Snapshot

[Current price, bid/ask, 52-week range, market cap, beta, P/E, P/B, dividend yield. Top 5 institutional holders with concentration analysis.]

---

## 9. Data Gaps & Limitations

[Tables are acceptable here — this is the designated gap-tracking section. Include both Gap IDs and a Filled Data table.]

> Write to `./dist/<TICKER>/artifacts/data_gaps.csv` if the gap list exceeds 10 items or if this report is part of a multi-report batch.

---

## 10. References

All `[^n]` numbers used in the report body MUST appear here. Use the academic filing format established in `references/citation-standards.md`.

[^1]: [Company Name] (2026). _Form 10-K for the Fiscal Year Ended [DATE]_ (Accession No. [ACCESSION]). U.S. Securities and Exchange Commission. Item 1: Business and Supervision and Regulation.

[^2]:
    [Company Name] (2026). _Form 10-K, Item 1A — Risk Factors_.
    ...

---

## Appendix: Structured Data Artifacts

All structured data artifacts for this report are stored in `./dist/<TICKER>/artifacts/`.

| Artifact                         | Path                                                    |
| -------------------------------- | ------------------------------------------------------- |
| Risk Factor Register (full CSV)  | `./dist/<TICKER>/artifacts/risk_register.csv`           |
| Financial Indicators (CSV)       | `./dist/<TICKER>/artifacts/financial_indicators.csv`    |
| Credit Concentrations (full CSV) | `./dist/<TICKER>/artifacts/credit_concentrations.csv`   |
| Peer Comparison (CSV)            | `./dist/<TICKER>/artifacts/peer_comparison.csv`         |
| Risk Cascade Diagram | Embedded inline in `ERM_Report.md` |
| Governance Risk Map | Embedded inline in `ERM_Report.md` |
| Financial Trend Chart | Embedded inline in `ERM_Report.md` |
| Credit Pie Chart | Embedded inline in `ERM_Report.md` |
| Scenario Synthesis (CSV)         | `./dist/<TICKER>/artifacts/scenario_synthesis.csv`      |
| Data Gaps (CSV)                  | `./dist/<TICKER>/artifacts/data_gaps.csv`               |

---

## Embedding vs. Artifact Decision Guide

The agent has discretion over what goes inline and what becomes an artifact file. Use this guidance:

- **Embed inline (Markdown table):** Tables with ≤15 rows; tables that the reader needs to see in context (financial summary, Top 5 concentrations, risk factor categories, market snapshot).
- **Embed inline (Mermaid):** Diagrams with ≤20 nodes and ≤2 levels of depth; diagrams that reference specific company names and risk titles rather than generic labels.
- **Write to artifact file:** Tables with 20+ rows; CSVs intended for spreadsheet/database import; Mermaid diagrams that are complex or need to be viewed in a dedicated renderer; the full risk factor register when the filing has 30+ sub-factors; peer comparison tables for 5+ companies.
- **Write inline AND artifact:** For key data tables — embed a Top 5 summary inline and write the full dataset to an artifact CSV for reference.
