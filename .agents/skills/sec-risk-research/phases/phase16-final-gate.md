# Phase 16 — Final Quality Gate (Mandatory Before Output)

## Purpose

This is the LAST phase before writing `ERM_Report.md`. It is a mandatory checklist. Do NOT write the output file until ALL items below are checked.

## The 16-Point Final Gate

### Structure Completeness

- [ ] Report contains an Executive Summary / Company Profile section
- [ ] Report contains an Enterprise Risk Framework & Governance section
- [ ] Report contains Macroeconomic Shocks & Interconnections section
- [ ] Report contains Principal Risk Factors with CSV register
- [ ] Report contains Financial & Credit Risk Profile with CSVs
- [ ] Report contains Operational, Cyber & Litigation Risk section
- [ ] Report contains Scenario-Based Emerging Risk Analysis (Part 4: 3+ scenarios)
- [ ] Report contains Industry Context (Part 1: key players, sector description)
- [ ] Report contains Risk Governance Comparison Table (Part 2 format)
- [ ] Report contains Data Gaps & Limitations section
- [ ] Report contains Full References section

### Citation Completeness

Run this check mentally or with a search tool:

- [ ] Count of `[^n]` references in the report body matches or exceeds the number of factual claims
- [ ] Every dollar figure has a citation within the same sentence
- [ ] Every verbatim quote has a citation immediately after the closing quote
- [ ] Every risk category heading in §3 is cited
- [ ] Financial tables have a `[^n]` in the markdown header preceding them
- [ ] Mermaid diagram captions reference the source data

Target: >95% of factual claims have an inline citation.

### Financial Accuracy

For EACH derived metric in the report:

- [ ] Recalculate from raw data in the same report section
- [ ] Confirm the value matches within tolerance (±0.5 pp for ratios, ±1% for percentages)
- [ ] If mismatch found: correct the number, recalculate, recheck before proceeding

### Verbatim Quote Integrity

- [ ] Each verbatim quote is enclosed in quotation marks
- [ ] Each quote is followed by a citation `[^n]`
- [ ] The referenced source in the References section includes the exact Item/Note/Section
- [ ] No quote is paraphrased without also providing the verbatim version

### Data Gap Transparency

- [ ] Every "Not disclosed in filing" statement is in the Data Gaps table
- [ ] Every HIGH priority gap has an associated retrieval command
- [ ] No fabricated or hallucinated data points remain in the report
- [ ] The report's data gaps section explicitly lists what was NOT retrievable

### Mermaid Diagram Quality

- [ ] Every Mermaid diagram has a descriptive title
- [ ] Every diagram has a one-sentence caption in plain text below it explaining what it shows
- [ ] The diagram's data source is cited in the caption
- [ ] All node labels are readable (no truncation)

### CSV Table Quality

- [ ] No CSV table has redundant columns (Item, Risk_ID, Source on every row)
- [ ] Each CSV has a `[^n]` citation in the markdown header/title
- [ ] Numbers are formatted consistently (e.g., `$M` unit in header, no mixed formatting)
- [ ] Totals and subtotals match the source Note

### Reference List Quality

- [ ] All `[^n]` numbers used in the report body appear in the References section
- [ ] All references follow the academic format: _Company Name (Year). Form X-K..._
- [ ] No meta-commentary about tools, scripts, or extraction mechanics
- [ ] No SEC.gov URLs (use accession numbers only)

### Language & Professionalism

- [ ] No typos in company names, tickers, or CIK numbers
- [ ] All section headings use consistent capitalization
- [ ] No emojis or casual language
- [ ] Technical terms used consistently (e.g., "JPMorganChase" not "JPM" in body, "JPM" in tables)

### Formatting

- [ ] `#` used for title, `##` for major sections, `###for subsections
- [ ] Tables use proper Markdown alignment (`|---|`)
- [ ] CSV blocks use ` ```csv ` not ` ```tsv `
- [ ] Mermaid blocks use ` ```mermaid `

### Batch Mode (if applicable)

- [ ] If processing multiple tickers: each report is in `./dist/<TICKER>/ERM_Report.md`
- [ ] No data from one ticker leaked into another report

### No Fabrication Audit

Scan for these red flags:

- [ ] No percentages that don't sum to 100% (credit concentrations)
- [ ] No financial years beyond the filing period without disclosure
- [ ] No regulatory requirements stated as fact without source
- [ ] No "industry average" values without a cited source

### Source Priority Compliance

- [ ] 10-K filings used for all financial and risk factor data
- [ ] Proxy (DEF 14A) used for governance data
- [ ] Yahoo Finance used ONLY for market data (price, market cap, holders)
- [ ] Tavily used ONLY for macro/current events context
- [ ] No Tavily data used as primary source for risk factor claims

### Verbatim Quote Completeness

- [ ] Each risk factor category (Legal/Regulatory, Political, Market, Credit, Liquidity, Capital, Operational, Strategic, Conduct, Reputational, Country, People) has at least one verbatim quote from Item 1A
- [ ] Climate risk quote present if climate risk is listed in Item 1A
- [ ] AI/technology risk quote present if mentioned in Item 1A

### Accounting Period Consistency

- [ ] All financial data references the SAME fiscal year (e.g., FY2025)
- [ ] No mixing of CY2024 and CY2025 data without clear labels
- [ ] Period covered is explicitly stated in the Company Context section

### Number Formatting

- [ ] Dollar amounts in tables use `$X,XXX` (commas for thousands)
- [ ] Large numbers use `$XX.XB` or `$XX.XT` for billions/trillions
- [ ] Percentages use `X.X%` (one decimal place)
- [ ] Negative numbers use `−X.X%` (en dash, not hyphen)

### Final Self-Review

Before writing the file:

- [ ] Read through the entire report mentally as if you were the grader
- [ ] Confirm: "Is every claim traceable to a source?"
- [ ] Confirm: "Would a subject matter expert consider this accurate?"
- [ ] Confirm: "Is this better than the prior version of JPM's report?"

## Output of Phase 16

Write a "Validation Checklist" block before output generation, showing which checks passed and which are flagged. Example:

```markdown
## Phase 16 — Validation Checklist (COMPLETE)

| Check                        | Status     | Notes                                          |
| ---------------------------- | ---------- | ---------------------------------------------- |
| §1. Structure Completeness   | ✅ PASS    | All sections present                           |
| §2. Citation Completeness    | ⚠️ FLAGGED | 3 claims missing citations in §5.2 — corrected |
| §3. Financial Arithmetic     | ✅ PASS    | All ratios verified                            |
| §4. Verbatim Quote Integrity | ✅ PASS    | 30 quotes verified                             |

| ...
```

## Gate Rule

**Do NOT write `ERM_Report.md` until this checklist is documented as complete.**
