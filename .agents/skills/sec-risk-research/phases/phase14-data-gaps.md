# Phase 14 — Data Gaps & Limitations

## Purpose

Write a short, human-readable gaps summary in the report body. All technical detail (retrieval attempts, commands, fills) goes to a separate artifact file.

## Track A — Report Body

Write 2–4 plain-language paragraphs under `## Data Gaps & Limitations` in `ERM_Report.md`. No tool names, no error messages, no causality chains — just state what information could not be retrieved and which report sections are affected.

That's it. No Gap ID tables, no Filled Data section, no command references.

## Track B — Artifact File

Write the full technical gap log to `./dist/<TICKER>/artifacts/data_gaps.csv`. This is the only place retrieval trails, commands, fills, and causality appear.

**Columns:**

| Column                | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| `Gap_ID`              | Unique identifier                                              |
| `Data_Item`           | What data is missing                                           |
| `Filing_Section`      | 10-K Item or Note                                              |
| `Expected_File`       | Raw data file that should contain it                           |
| `Priority`            | `HIGH` / `MEDIUM` / `LOW`                                      |
| `Status`              | `UNRESOLVED` / `PARTIAL` / `FILLED_THIS_RUN` / `UNRETRIEVABLE` |
| `Retrieval_Attempt_N` | Description of what was tried                                  |
| `Command_N`           | Exact tool call or script invocation                           |
| `Result_N`            | Success, timeout, partial, error, etc.                         |
| `Fill_Status`         | `OPEN` / `PARTIAL` / `FILLED_THIS_RUN`                         |
| `Notes`               | Context or authoritative filing reference                      |

## Required Outputs

| Output                            | Location                                            |
| --------------------------------- | --------------------------------------------------- |
| Data Gaps narrative (plain prose) | `ERM_Report.md` — end of document before references |
| Technical gap trail CSV           | `./dist/<TICKER>/artifacts/data_gaps.csv`           |

## Critical Rules

- The **report body** must contain only plain-language paragraph descriptions of gaps. No tool names, no command strings, no Filled Data table.
- The **artifact CSV** contains everything: retrieval attempts, commands, results, fill status, and notes.
- Reference the artifact once at the end of the report section: `> Technical gap trail: ./dist/<TICKER>/artifacts/data_gaps.csv`
