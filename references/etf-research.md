# ETF 研究

Use this workflow to analyze or compare exchange-traded funds by mandate, market behavior,
liquidity, NAV, scale, tracking benchmark, or disclosed portfolio.

## System contract

- **Stage:** 2. Discover or 3. Investigate; may contribute to Stage 5 feasibility
- **Consumes:** `research_mandate`, fund candidates, benchmark, period, and `as_of`
- **Produces:** ETF candidate metrics, fund evidence for `evidence_pack`, or public liquidity
  constraints for `feasibility_card`
- **Gate:** contributes to G2, G3, or G5 in [research-system.md](research-system.md)
- **Permitted next stages:** `thesis-review`, feasibility, or monitoring

## Resolve the funds and benchmark

1. Use `basic` to resolve ETF names to exact symbols and verify listing status, exchange,
   ETF type, manager, fee, and tracking-index metadata.
2. Use `tracking_indices` or the `index_code` returned by `basic` to identify the stated
   benchmark. Do not infer the benchmark from the fund name alone.
3. Resolve the requested comparison period with `trade_calendar`.

## Collect the minimum dataset

| Question | Core methods | Optional methods |
|---|---|---|
| Return and liquidity | `etf_daily` | `etf_adj_factor` |
| NAV and market-price relationship | `nav`, `etf_daily` | `share_size` |
| Scale and fund flows | `share_size` | `nav`, `etf_daily` |
| Portfolio exposure | `portfolio` | `basic`, `tracking_indices` |
| Benchmark comparison | `index_daily`, `etf_daily` | `tracking_indices` |

## Analyze

1. Calculate returns from an explicitly chosen raw or adjusted series. State the adjustment
   convention and do not mix close, unit NAV, accumulated NAV, and adjusted NAV.
2. Measure liquidity from traded amount and volume over a window; do not equate fund scale
   with secondary-market liquidity.
3. Compare price with NAV only on matching dates and compatible units. Label the result a
   price-to-reported-NAV difference, not an intraday indicative premium, unless intraday IOPV
   data is actually available.
4. Describe share and scale changes separately. A share increase can be observed; investor
   motivation cannot.
5. Calculate portfolio concentration from one disclosed report date. Never present stale
   portfolio holdings as today's holdings.
6. Compare each fund with the same benchmark and date window before ranking.

## Output

1. **比较结论** — the most decision-relevant differences without naming a universal winner.
2. **基金身份与基准** — symbol, type, manager, fee, benchmark, and metadata date.
3. **收益、波动与回撤**
4. **流动性、规模与净值关系**
5. **持仓暴露与集中度** — include portfolio report date.
6. **适用边界** — missing IOPV, tracking-error inputs, stale holdings, or incompatible funds.
7. **复现信息** — methods, dates, adjustment rules, and calculations.
