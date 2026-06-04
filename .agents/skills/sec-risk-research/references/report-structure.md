# Professional Report Structure Template

Use this as the canonical section structure for `ERM_Report.md`.

---

# Enterprise Risk Management Report: [COMPANY NAME]

**Ticker:** [TICKER] | **CIK:** [CIK] | **[EXCHANGE]**
**Reporting Period:** Fiscal Year Ended [DATE]
**10-K Accession:** [ACCESSION] | **Auditor:** [AUDITOR]
**Report Generation Date:** [DATE]

---

## Executive Summary

[One paragraph: company description, key financials, most significant risks, and key emerging risks. No citations needed here — facts come from §1 and §5.]

---

## 1. Industry Context & Key Players

### 1.1 Industry Overview

[Paragraph describing the sector, its economic importance, regulatory bodies, and current trends.]

### 1.2 Key Global Players

- **[Company Name]** — Fortune 500 Rank #[X], Revenue $XX.XB, [primary business]
- [Peer 1] — Fortune 500 Rank #[X]...
- [Peer 2]...

### 1.3 Market Structure & Competitive Landscape

[Description of market concentration, competitive dynamics, and barriers to entry.]

---

## 2. Risk Governance Comparison

| شرکت / Company | ارزش بازار / Market Cap | کمیته ریسک / Risk Committee | متولی ریسک / CRO | تعداد جلسات / Meetings | دارایی‌ها / Assets | درآمد / Revenue | سود خالص / Net Income |
| -------------- | ----------------------- | --------------------------- | ---------------- | ---------------------- | ------------------ | --------------- | --------------------- |
| [Company A]    | $XXX.XB                 | Yes / [Name]                | [Name]           | [X]                    | $XX.XB             | $XX.XB          | $X.XB                 |
| [Company B]    | ...                     | ...                         | ...              | ...                    | ...                | ...             | ...                   |

_Source: 10-K Item 1 / 7A; Proxy Statement (DEF 14A); Financial Statements. [^n]_

[Optional: additional operational, trade, and financial KPI rows below the primary table.]

---

## 3. Risk Register

### 3.1 Risk Factor Summary

| Risk Category        | Primary Risk Title | Key Sub-Risk (Verbatim) | Source Section | Source Item/Note |
| -------------------- | ------------------ | ----------------------- | -------------- | ---------------- |
| Legal and Regulatory | ...                | "exact quote..."        | 10-K           | Item 1A          |
| Market               | ...                | "exact quote..."        | 10-K           | Item 1A          |
| ...                  | ...                | ...                     | ...            | ...              |

### 3.2 Detailed Risk Register (CSV)

_Source: 10-K, Item 1A — Risk Factors [^n]_

```csv
Risk_Category,Risk_Factor_Title,Verbatim_Excerpt
Legal and Regulatory,Regulatory Changes,"exact phrase ""..."" from Item 1A"
Political,Macroeconomic Uncertainty,"exact phrase ""..."" from Item 1A"
...
```

---

## 4. Emerging Risk Scenarios

### Scenario 1: [Title]

**Trigger:** [External event]

**Mechanism:** [Causal chain]

**Impact:** [Firm-specific consequence]

**Source anchors:** [^n], [^m]

### Scenario 2: [Title]

...

### Scenario 3: [Title]

...

**Cross-Scenario Synthesis:**

| Scenario | Trigger                 | Primary Risk Channel | Severity | Primary Source |
| -------- | ----------------------- | -------------------- | -------- | -------------- |
| S1       | Geopolitical escalation | Credit → Capital     | High     | [^n]           |
| S2       | AI cyber disruption     | Cyber → Operational  | High     | [^n]           |
| S3       | CRE systemic stress     | Credit → Earnings    | Medium   | [^n]           |

---

## 5. Enterprise Risk Framework & Governance

[ERM framework discussion, COSO/Basel/NIST detection, Three Lines model]

### 5.1 Risk Governance Map

[Mermaid `graph TD` or `flowchart LR` showing Board → Committee → CRO → Lines of Defense]

---

## 6. Macroeconomic Shocks & Interconnections

[Current macro risks, Fed policy, geopolitical events, interconnection analysis]

---

## 7. Financial & Credit Risk Profile

### 7.1 Financial Indicators

_Source: 10-K, Financial Statements [^n]_

```csv
Metric,FY2023,FY2024,FY2025,Unit,Source
Total_Revenue,158104,177556,182447,$M,10-K Income Statement
Net_Income,49552,58471,57048,$M,10-K Income Statement
...
```

### 7.2 Credit Risk Concentrations

_Source: 10-K, Note 4 — Credit Risk [^n]_

```csv
Sector,FY2025_M,FY2024_M,YoY_Change_M,Pct_Total
Credit Card,1425563,1234171,191392,41.7%
...
```

---

## 8. Operational, Cyber & Litigation Risk

[Cyber disclosures, Note 37, litigation proceedings, ASC 450 classification]

---

## 9. References

[^1]: JPMorgan Chase & Co. (2026). _Form 10-K for the Fiscal Year Ended December 31, 2025_ (Accession No. 0001628280-26-008131). U.S. Securities and Exchange Commission. Item 1: Business and Supervision and Regulation.

[^2]: JPMorgan Chase & Co. (2026). _Form 10-K, Item 1A — Risk Factors_.

[^3]:
    ...
    ...

---

## Data Gaps & Limitations

| Gap ID  | Data Item | Location | Priority | Action Required |
| ------- | --------- | -------- | -------- | --------------- |
| GAP-001 | ...       | ...      | HIGH     | ...             |

## Filled Data (this update)

| Data Item | Source | Reference |
| --------- | ------ | --------- |
| ...       | ...    | [^n]      |
