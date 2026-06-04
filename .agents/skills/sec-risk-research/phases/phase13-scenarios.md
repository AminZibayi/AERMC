# Phase 13 — Scenario-Based Emerging Risk Analysis

## Purpose

This phase generates forward-looking, scenario-based risk narratives that go beyond what is explicitly disclosed in past filings.

## Context

Standard SEC filings are backward-looking by design. Phase 13 synthesizes retrieved data with macro context to project emerging risk scenarios. Each scenario must have:

- **Trigger**: Specific macro/environmental event
- **Mechanism**: How the trigger propagates through the firm's risk architecture
- **Impact**: Quantified or qualitatively described consequence for the target company
- **Source grounding**: Every claim must link to a retrieved SEC disclosure or financial fact

## Steps

### 13.1 Identify Macro Risk Themes

From Phases 11 and 12, list 3-5 top macro/emerging risk themes (e.g., "Iran-US geopolitical escalation", "AI-driven cyber attacks", "Basel III endgame capital rule revision", "Commercial real estate systemic stress").

### 13.2 Map Each Theme to Firm-Specific Exposures

For each macro theme:

1. Identify the firm's direct exposure (e.g., "JPM has $224.9B CRE exposure per Note 4" [^n])
2. Identify the transmission mechanism (e.g., "CRE stress → higher PCL → CET1 compression → reduced capital distributions")
3. Identify any mitigating factors disclosed in the 10-K

### 13.3 Write Scenario Narratives

For each scenario, write 150–250 words following this template:

```markdown
### Scenario N: [Scenario Title]

**Trigger:** [External event description]

**Mechanism:** [How this flows through the firm's risk architecture]

**Impact:** [Specific, quantified consequence for the target company]

**Source anchors:** [List of [^n] citations grounding this scenario]
```

### 13.4 Write Cross-Scenario Synthesis

After the individual scenarios, write a 100-word synthesis table:

| Scenario   | Trigger | Primary Risk Channel | Severity (Low/Med/High) | Source |
| ---------- | ------- | -------------------- | ----------------------- | ------ |
| Scenario 1 | ...     | ...                  | ...                     | [^n]   |

## Required Scenarios (minimum 3)

1. **Geopolitical / Trade Shock**: Sanctions, tariffs, or military escalation in a key operating region
2. **Technology Disruption**: AI, quantum computing, or fintech disruption to core business model
3. **Regulatory / Capital Rule Change**: New capital, liquidity, or ESG regulations
4. **Climate / Physical Risk** (if applicable): Physical asset exposure or transition risk
5. **Systemic Credit Cycle**: Recession, unemployment spike, or systemic counterparty failure

## Required Outputs

| Output                           | Source                                         |
| -------------------------------- | ---------------------------------------------- |
| 3-5 Scenario Narratives          | Phase 11 + Phase 12 data + tavily supplemental |
| Cross-scenario synthesis table   | Derived                                        |
| Severity ratings                 | Expert judgment + 10-K disclosures             |
| Source anchors for each scenario | Mixed (10-K, 8-K, Tavily)                      |

## Critical Rules

- Every scenario MUST have at least 2 verifiable source anchors in the 10-K or proxy
- Do NOT write scenarios that are purely speculative with zero filing anchor
- Severity ratings must be justified by a quantitative threshold from the filing (e.g., "High because CRE represents 6.6% of total credit exposure [^n] and rising PCL by +33% [^n]")
- Use Tavily ONLY to confirm current macro events — the transmission mechanism must come from the filing text
