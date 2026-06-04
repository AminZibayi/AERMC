# Phase 14 — Data Gaps & Limitations (Structured Gap Tracking)

## Purpose
This phase produces a structured, machine-readable log of every data item that could NOT be fully retrieved, replacing the informal "Data Gaps" section with a rigorous tracking system.

## Steps

1. **Audit each Phase's Required Outputs table** (from Phases 1–13)
2. For every entry marked "Not found", "Not disclosed in filing", or flagged as partial:
   - Assign a Gap ID (e.g., GAP-001)
   - Record the specific data item
   - Record the file location where it should exist (e.g., `item_3_legal.txt`, `proxy_governance.txt`, Note 30)
   - Record the exact retrieval command needed (e.g., `edgar_notes topic="litigation"`)
   - Assign priority: `HIGH` (blocks final report section), `MEDIUM` (section partially complete), `LOW` (nice-to-have)
3. **Write the "Data Gaps & Limitations" section** at the end of the report using this format:

```markdown
## Data Gaps & Limitations

| Gap ID | Data Item | Location | Priority | Action Required |
|--------|-----------|----------|----------|-----------------|
| GAP-001 | [Specific data] | Item 3: Legal Proceedings | HIGH | `edgar_read` sections=["legal"] retry |
| GAP-002 | [Specific data] | Note 37 | MEDIUM | `edgar_notes` topic="cybersecurity" |
```

4. **Also write a "Filled Data" section** for items that were successfully retrieved:
   | Data Item | Source | Reference |
   |---|---|---|
   | [Item name] | retrieval command | [^n] |

## Required Outputs

| Output | Format |
|--------|--------|
| Data Gaps Table | Markdown table in report |
| Filled Data Table | Markdown table in report |
| Gap ID count | Log for Phase 16 check |

## Critical Rules
- Do NOT use "timeout", "MCP failed", or "LLM limitation" as reasons — use specific file/section descriptions
- Every gap MUST map to a concrete retrieval action
- If a gap is marked HIGH and the report section cannot be completed without it, the report MUST be flagged as "PARTIAL — requires manual completion"
