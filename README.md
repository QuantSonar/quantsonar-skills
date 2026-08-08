# QuantSonar Agent Skill

[Website](https://quantsonar.com/?utm_source=github&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_repo) · [Documentation](https://quantsonar.com/docs?utm_source=github&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_repo) · [Create a free API key](https://quantsonar.com/register?utm_source=github&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_repo) · [Python SDK](https://pypi.org/project/quantsonar/)

Research Chinese A-share companies and markets with reproducible, time-stamped QuantSonar data. The Skill covers company research, market briefs, stock screening and point-in-time quant data preparation, and prefers the hosted QuantSonar MCP server with the Python SDK as a fallback.

## Install

Want an Agent to perform the complete setup? Send it
[`INSTALL.md`](INSTALL.md) and ask it to follow the file exactly.

```bash
npx skills add QuantSonar/quantsonar-skills --skill quantsonar
```

## Connect the hosted MCP server

```bash
claude mcp add --transport http quantsonar https://quantsonar.com/mcp \
  --header "X-API-Key: qs_your_key"
```

The API key is shared across REST, the Python SDK and MCP. See the [online documentation](https://quantsonar.com/docs?utm_source=github&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_repo_mcp) for setup and data coverage.

## Skill contents

- `SKILL.md` routes the request and defines evidence and safety rules.
- `references/` contains research workflows plus the generated data catalog.
- `scripts/metrics.py` provides deterministic return, volatility, drawdown and percentile calculations.

This repository is generated from the QuantSonar service registry so the Skill, SDK, MCP tools and documentation stay aligned.
