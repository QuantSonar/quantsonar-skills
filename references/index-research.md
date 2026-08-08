# 指数与基准研究

Use this workflow to analyze an index's performance, constituents, weights, concentration,
or role as a benchmark. Use `market-brief` instead for a broad daily market narrative.

## System contract

- **Stage:** 0. Configure or 1. Observe; supplies a benchmark during Stage 7 review
- **Consumes:** research objective or exact index, period, and constituent snapshot date
- **Produces:** benchmark fields for `research_mandate` or index evidence for
  `market_context`
- **Gate:** contributes to G0, G1, or G7 in [research-system.md](research-system.md)
- **Permitted next stages:** market observation, discovery, or research review

## Resolve the benchmark

Resolve the exact suffixed index symbol and period. Do not treat a stock symbol or an ETF
symbol as an index. Use `trade_calendar` for the period boundary and state whether the
analysis uses the latest available or a historical constituent snapshot.

## Collect

| Question | Core methods | Optional methods |
|---|---|---|
| Index performance | `index_daily` | `fx_daily` for explicitly requested currency context |
| Constituents and concentration | `index_weight` | `stocks`, `industries` |
| Constituent return contribution proxy | `index_weight`, `daily` | `fundamentals` |
| Theme exposure | `index_weight`, `industries` | `concepts`, `concept_members` |

## Analyze

1. Calculate index return, volatility, and drawdown from `index_daily` for the requested
   period.
2. Calculate top-N and Herfindahl-style weight concentration from one constituent date.
3. For industry exposure, join constituents to `industries` and sum weights. Preserve
   unmapped weights as “unclassified.”
4. Call weight × constituent return a contribution proxy unless official divisor,
   rebalancing, corporate-action, and intra-period weights are available.
5. Avoid look-ahead bias: never use today's constituents to explain or backtest a historical
   period without disclosure.
6. Use `fx_daily` only when the user requests RMB or cross-currency context; one FX series is
   not a complete macro model.

## Output

1. **基准摘要** — performance, concentration, and main exposure.
2. **收益与风险** — period, return, volatility, drawdown, and `as_of`.
3. **成分与集中度** — constituent snapshot date and top weights.
4. **行业/主题暴露**
5. **贡献线索** — explicitly label proxies and unavailable official attribution inputs.
6. **偏差与复现信息** — constituent history, rebalancing, missing mappings, methods, and dates.
