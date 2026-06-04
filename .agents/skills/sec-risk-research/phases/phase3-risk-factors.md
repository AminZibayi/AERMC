# Phase 3 — Item 1A Risk Factors

MOST IMPORTANT PHASE -- DO NOT MISS ANY RISK FACTORS OR VERBATIM EXCERPTS

## Steps

1. Read `./dist/<TICKER>/raw/item_1A_risk_factors.txt` fully.
2. Extract all risk factor headings and sub-headings.
3. For each risk factor, capture representative verbatim excerpts (50–150 words).
4. Do NOT categorize risks at this stage — list them in extracted order.
5. Count total risk factors.
6. Write the Risk Factor Register CSV to `./dist/<TICKER>/artifacts/risk_register.csv` with columns: Risk_Category, Risk_Factor_Title, Verbatim_Excerpt.
7. In the report, reference the artifact file path instead of embedding the CSV.

## Required Outputs

| Output                           | Source                                                    |
| -------------------------------- | --------------------------------------------------------- |
| Total Risk Factor Count          | Derived from headings                                     |
| Risk Factor Register CSV         | `./dist/<TICKER>/artifacts/risk_register.csv`             |
| Verbatim Excerpts (exact quotes) | item_1A_risk_factors.txt                                  |
| References                       | Item 1A                                                   |
| Report citation                  | Markdown header with `[^n]` referencing the artifact path |

## Critical Rules

- Every verbatim excerpt MUST be enclosed in double quotation marks
- Risk categories must match the filing's own organization
- Do NOT paraphrase risk titles — use verbatim headings from the filing
- If a risk category (e.g., Climate) appears as a sub-factor under another heading, note the parent heading
- The CSV column order is: Risk_Category, Risk_Factor_Title, Verbatim_Excerpt
- Place the source citation `[^n]` in the markdown header line immediately
  before the reference (e.g., `### Principal Risk Factors (Item 1A) [^2]`). Do
  NOT embed the CSV data in the report body. Instead, use a markdown table
