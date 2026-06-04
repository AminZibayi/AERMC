# Phase 8 — Litigation & Contingencies

## Steps
1. Read `./dist/<TICKER>/raw/item_3_legal.txt` in full.
2. List all material legal proceedings by name, court, status.
3. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "litigation" and "contingencies".
4. Extract Note 30 or equivalent contingency disclosures.
5. Apply ASC 450 / IAS 37 classification: Probable / Reasonably Possible / Remote.
6. Record estimated loss ranges if disclosed.
7. If item_3_legal.txt is "Not found" or fewer than 200 words, use `edgartools_edgar_read` sections=["legal"] for dynamic drill-down.
8. If Note 30 is not in relevant_notes.txt, use `edgartools_edgar_notes` topic="litigation" retry.
9. Write "Litigation & Contingency Risk" section.

## Required Outputs

| Output | Source |
|--------|--------|
| Legal Proceedings List | item_3_legal.txt |
| Contingency Note Reference | relevant_notes.txt (Note 30 or equivalent) |
| ASC 450 Classification | Derived |
| Estimated Loss Range | relevant_notes.txt |
| Legal Expenses (if disclosed) | Income Statement or Item 3 |

## Critical Rules
- Material proceedings MUST include: case name, court/jurisdiction, current status (e.g., "on appeal", "pending", "settled")
- If the filing states "The Company is involved in numerous legal proceedings" but does not list individual cases, note this explicitly as "Individual proceedings not itemized in item_3_legal.txt"
- The range of reasonably possible losses (in excess of accrued reserves) is a KEY data point — extract this figure verbatim
- Do NOT use "N/A" for litigation — use "Not itemized" or "Not disclosed"
- Legal expenses if disclosed in the Income Statement must be called out as a trend (3-year if available)
