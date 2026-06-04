# Phase 3 — Item 1A Risk Factors

## Steps

1. Read `./dist/<TICKER>/raw/item_1A_risk_factors.txt` fully.
2. Extract all risk factor headings and sub-headings.
3. For each risk factor, capture representative verbatim excerpts (50–150 words).
4. Do NOT categorize risks at this stage — list them in extracted order.
5. Count total risk factors.
6. Write "Risk Factor Register" table to report with: Risk_Category, Risk_Factor_Title, Verbatim_Excerpt.

## Required Outputs

| Output                           | Source                   |
| -------------------------------- | ------------------------ |
| Total Risk Factor Count          | Derived from headings    |
| Risk Factor Register CSV         | item_1A_risk_factors.txt |
| Verbatim Excerpts (exact quotes) | item_1A_risk_factors.txt |
| References                       | Item 1A                  |

## Critical Rules

- Every verbatim excerpt MUST be enclosed in double quotation marks AND immediately followed by `[^n]`
- Risk categories must match the filing's own organization (Legal/Regulatory,
  Political, Market, Credit, Liquidity, Capital, Operational, Strategic,
  Conduct, Reputational, Country, People, Climate/ESG, etc.)
- Do NOT paraphrase risk titles — use verbatim headings from the filing
- If a risk category (e.g., Climate) appears as a sub-factor under another heading, note the parent heading
- The CSV column order is: Risk_Category, Risk_Factor_Title, Verbatim_Excerpt
- The CSV must appear in the report under `### Risk Register (Item 1A) [^n]` heading
