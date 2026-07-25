---
name: quantsonar
description: Research Chinese A-share companies and markets with QuantSonar data. Use when the user asks to analyze or compare an A-share company, create a daily market brief, screen stocks from natural-language conditions, prepare point-in-time quant datasets or Python code, or retrieve A-share prices, fundamentals, financial statements, valuation, money flow, chips, Dragon-Tiger List, realtime quotes, and market news. Use the QuantSonar MCP tools first and the Python SDK as a fallback.
---

# QuantSonar

Turn the user's research question into a reproducible data workflow. Use QuantSonar for
facts and deterministic calculations; use reasoning only to explain what the evidence means.

## Route the request

Read exactly one primary workflow unless the request clearly combines tasks:

| User intent | Read |
|---|---|
| Understand one company, its fundamentals, valuation, price, capital behavior, or risks | [references/stock-research.md](references/stock-research.md) |
| Summarize today's or a specified day's A-share market | [references/market-brief.md](references/market-brief.md) |
| Find stocks matching natural-language conditions | [references/stock-screening.md](references/stock-screening.md) |
| Build, export, or prepare data for research, factors, or backtests | [references/quant-data-prep.md](references/quant-data-prep.md) |

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
4. Validate empty results, duplicate rows, units, reporting periods, and each dataset's
latest available date before calculating.
5. Use `scripts/metrics.py` for return, volatility, drawdown, and percentile calculations
when applicable.
6. Present the conclusion first, then evidence, limitations, and data timestamps.

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
