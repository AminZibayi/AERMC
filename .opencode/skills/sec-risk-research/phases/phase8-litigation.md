# Phase 8 — Litigation & Contingencies

## Steps
1. Read `./dist/<TICKER>/raw/item_3_legal.txt` in full.
2. List all material legal proceedings by name, court, status.
3. Read `./dist/<TICKER>/raw/relevant_notes.txt` and search for "litigation" and "contingencies".
4. Extract Note 30 or equivalent contingency disclosures.
5. Apply ASC 450 / IAS 37 classification: Probable / Reasonably Possible / Remote.
6. Record estimated loss ranges if disclosed.
7. If the notes are missing/truncated, use `edgartools_edgar_notes` (topic="litigation" or "contingencies") for dynamic drill-down.
8. Write "Litigation Register" to report.

## Required Outputs
| Output | Source |
|--------|--------|
| Legal Proceedings List | item_3_legal.txt |
| Contingency Note Reference | relevant_notes.txt (Note 30 or equivalent) |
| ASC 450 / IAS 37 Classification | Derived |
| Estimated Loss Range | relevant_notes.txt |
| Materiality Threshold | Derived from 10-K or stated as assumed |
