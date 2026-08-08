---
name: quantsonar
description: "Provide two connected public-data China A-share research services with QuantSonar: individual-stock research and sector research across Shenwan industries, concepts/themes, and published indices. Route each request through a gated lifecycle from mandate and market context to evidence, thesis challenge, feasibility, monitoring, and review. Use for company fundamentals, valuation, technical indicators, capital behavior, dividends, sector breadth, leadership, concentration, ETFs, events, point-in-time datasets, backtests, or direct retrieval. Use QuantSonar MCP first and the Python SDK as fallback. Do not collect private holdings, transactions, account balances, cost basis, taxes, or personal risk profiles."
---

# QuantSonar

Turn the user's research question into a reproducible data workflow. Use QuantSonar for
facts and deterministic calculations; use reasoning only to explain what the evidence means.

## Official resources

- [Website](https://quantsonar.com/?utm_source=skills_directory&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_md)
- [API documentation](https://quantsonar.com/docs?utm_source=skills_directory&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_md)
- [Create a free API key](https://quantsonar.com/register?utm_source=skills_directory&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=skill_md)
- [Python SDK on PyPI](https://pypi.org/project/quantsonar/)

## Route the request

Read [references/research-system.md](references/research-system.md) first for any request that
spans more than one lifecycle stage. It defines artifact dependencies, stage gates, and the
feedback loop. Then use [references/skill-matrix.md](references/skill-matrix.md) to identify
the available atomic capability, QuantSonar-native evidence, external inputs, and deferred
private-data capabilities. For a narrow data-analysis task, read exactly one primary workflow:

| User intent | Read |
|---|---|
| Define a public research objective, universe, horizon, benchmark, and evidence policy | [references/research-mandate.md](references/research-mandate.md) |
| Understand one company, its fundamentals, valuation, price, or risks | [references/stock-research.md](references/stock-research.md) |
| Research an industry, concept/theme, or index-like sector and its internal structure | [references/sector-research.md](references/sector-research.md) |
| Summarize today's or a specified day's A-share market | [references/market-brief.md](references/market-brief.md) |
| Find stocks matching natural-language conditions | [references/stock-screening.md](references/stock-screening.md) |
| Analyze one stock's trend, momentum, volatility, volume, or technical indicators | [references/technical-analysis.md](references/technical-analysis.md) |
| Explain money flow, margin, chips, holdings, Dragon-Tiger, or shareholder behavior | [references/capital-behavior.md](references/capital-behavior.md) |
| Analyze or compare ETFs, NAV, scale, liquidity, tracking, or holdings | [references/etf-research.md](references/etf-research.md) |
| Analyze dividends, yield, payout continuity, or dividend sustainability | [references/dividend-research.md](references/dividend-research.md) |
| Monitor realtime price moves, news, disclosures, limits, or unusual trading | [references/event-monitor.md](references/event-monitor.md) |
| Analyze an index, its constituents, weights, concentration, or benchmark behavior | [references/index-research.md](references/index-research.md) |
| Build, export, or prepare data for research, factors, or backtests | [references/quant-data-prep.md](references/quant-data-prep.md) |
| Turn a completed evidence pack into bull/base/bear cases, catalysts, and falsifiers | [references/thesis-review.md](references/thesis-review.md) |
| Assess public liquidity, volatility, gaps, limits, suspension, or observable price constraints | [references/market-feasibility.md](references/market-feasibility.md) |
| Review a research chain, screen, hypothesis, backtest, or paper watchlist | [references/research-review.md](references/research-review.md) |

For a direct factual request such as “600519.SH 最近 20 个交易日收盘价”, skip the
workflow and inspect [references/data-catalog.md](references/data-catalog.md).

## Access data

1. Prefer configured QuantSonar MCP tools. Tool names match the SDK method names.
2. If MCP is unavailable, use the Python SDK:

```python
import quantsonar as qs  # reads QUANTSONAR_TOKEN
df = qs.daily(symbol="600519.SH", start_date="20260101")
```

3. If neither access path is configured, explain that an API Key is required and point to
`https://quantsonar.com/register`. Never invent data to complete the answer.

Remote MCP endpoint: `https://quantsonar.com/mcp`, authenticated with the
`X-API-Key` request header.

## Execute every workflow

1. Resolve company names to suffixed symbols with `stocks`; never guess a symbol.
2. Define the requested period and obtain the latest applicable trading date with
   `trade_calendar`.
3. Fetch only the data required by the selected workflow. Avoid “fetch everything.”
4. Check the minimum tier in the skill matrix before using optional datasets. If access is
   unavailable, continue with the supported core rather than repeatedly calling the same tool.
5. Validate empty results, duplicate rows, units, reporting periods, and each dataset's
   latest available date before calculating.
6. Use `scripts/metrics.py` for return, volatility, drawdown, and percentile calculations
   when applicable.
7. Present the conclusion first, then evidence, limitations, and data timestamps.
8. Do not request or persist holdings, transactions, cost basis, account balance, taxes, or
   personal risk-profile data. Mark personalized portfolio, execution, exit, and performance
   requests as outside the current Skill scope.
9. For a multi-stage request, preserve the typed artifact envelope and evaluate the gate in
   `research-system.md`. A failed gate must return a partial artifact and recovery requirement;
   it must not be bypassed with invented assumptions.

## Research rules

- Label statements as **data fact**, **calculation**, or **interpretation** when ambiguity
  is possible.
- Give each data family its own `as_of` date. Do not imply that market, financial, holdings,
  and news data update simultaneously.
- Use only fields actually returned. Treat missing, stale, or inaccessible data as
  unavailable; do not estimate it silently.
- Preserve source units. State any scaling, annualization, adjustment, winsorization, or
  forward filling.
- For financial analysis, prefer announced point-in-time information. Do not use a later
  report in an earlier backtest period.
- Treat screens and signals as research candidates, not conclusions. Never promise returns,
  issue direct buy/sell instructions, or present capital-flow labels as proof of intent.
- Treat a research report, a portfolio decision, and a brokerage action as separate stages.
  QuantSonar may support evidence and planning but does not execute brokerage orders.
- When asked “should I buy/sell”, do not answer yes or no and do not substitute a generic
  valuation threshold for the user's decision. Offer a scenario framework tied only to
  verified data, and state which personal constraints remain unknown.
- If no QuantSonar data can be accessed, stop before making company-specific claims. Explain
  the missing access or inputs and provide only the reproducible data plan; do not fill the
  report with remembered company facts, invented thresholds, or demo values.
- If a tool returns a tier or rate-limit error, report it accurately. Do not bypass access
  control or replace unavailable QuantSonar data with fabricated values.
- Match the user's language. Keep raw tables compact and offer code or export-ready output
  when useful.

## Conventions

- Symbols require exchange suffixes: `600519.SH`, `000001.SZ`, `430047.BJ`.
- Dates use `YYYYMMDD`.
- Prefer bounded `start_date` and `end_date`; use `trade_date` for one-day cross sections.
- MCP responses may be truncated for AI context safety. Use narrower filters or the SDK for
  larger datasets.
- Endpoint parameters and return fields are generated in
  [references/data-catalog.md](references/data-catalog.md).
