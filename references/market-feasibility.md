# 公开市场可行性检查

Use this workflow after a public thesis exists or when the user explicitly asks about
liquidity, volatility, suspension, price limits, gaps, or observable trading constraints.
Assess market feasibility without producing a brokerage instruction.

## System contract

- **Stage:** 5. Feasibility
- **Consumes:** `research_mandate`, `thesis_card`, and relevant market evidence; for a narrow
  request, an explicit subject, horizon, and `as_of` are sufficient
- **Produces:** `feasibility_card`
- **Gate:** G5 in [research-system.md](research-system.md)
- **Permitted next stages:** public monitoring or research review

## Collect the minimum evidence

| Constraint | Core methods | What to establish |
|---|---|---|
| Recent liquidity | `daily`, `fundamentals` | traded amount/volume, turnover, zero-volume days, and stability over a stated window |
| Volatility and gaps | `daily`, `technical_factors`, `technical_factors_pro` | realized volatility, ATR or range behavior, gaps, and drawdown over the mandate horizon |
| Current session | `realtime` | exact snapshot time, current range, volume, and stored/live status |
| Market constraints | `limit_list`, `trade_calendar` | limit-up/down, trading date, and observable suspension/limit evidence |
| ETF feasibility | `etf_daily`, `nav`, `share_size` | secondary-market liquidity, reported NAV relationship, and scale on compatible dates |

Use only the rows relevant to the security type and question. Do not infer available order-book
depth, broker fills, transaction costs, or borrow availability unless verified data explicitly
supports them.

## Analyze

1. Calculate median and lower-percentile traded amount/volume over a visible window; do not
   use one active day as representative liquidity.
2. Describe volatility, gaps, and range expansion using a consistent adjusted or raw series.
3. Record recent limit events, zero-volume days, or suspension evidence and their dates.
4. When price zones are requested, describe historical rolling highs/lows, channels, or volume
   areas with their calculation windows. Label them observations, not guaranteed support,
   resistance, entry, stop, or target prices.
5. Separate verified public constraints from unknown execution inputs such as order size,
   broker, fees, latency, and market impact.
6. Compare feasibility evidence with the thesis horizon: daily noise should not silently
   override a multi-year thesis, but severe tradability constraints must remain visible.

## Output

Emit a `feasibility_card` using the common envelope in
[research-system.md](research-system.md), then include:

1. **可行性摘要**
2. **流动性证据** — window, median, lower percentile, zero-volume observations, `as_of`
3. **波动、缺口与价格结构**
4. **涨跌停、停牌和交易日约束**
5. **可观察价格区域及计算口径**
6. **未知执行变量与数据限制**
7. **G5 结果** — pass, partial, or fail

Never emit an order quantity, personalized entry/exit decision, target price, stop-loss order,
or an assertion that a trade can be filled.
