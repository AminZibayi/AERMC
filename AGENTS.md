# Risk Research Protocol — Enterprise Risk Analysis via SEC Filings

> **NOTICE: PROTOCOL REFACTORED INTO A SKILL**
> The contents of this protocol have been migrated to the `sec-risk-research` skill to reduce complexity and ensure agents always trigger the bulk data fetcher script _before_ performing analysis.

## How to use this protocol

When instructed to perform a risk analysis on a company, the AI agent must invoke the `sec-risk-research` skill.

The skill instructs the agent to:

1. **Run the Data Fetcher Script:** Execute `python risk_research.py TICKER` to bulk-download the 10-K, Proxy, and XBRL financials into `./dist/TICKER/raw/`.
2. **Read the Raw Data:** Ingest the local text files.
3. **Execute the 13-Phase Analysis:** Parse the data, map the ERM frameworks, and generate the required markdown and Mermaid deliverables.

_(For detailed execution instructions, see `.agents/skills/sec-risk-research/SKILL.md`)_
