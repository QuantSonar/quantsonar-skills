# 资金与筹码行为

Use this workflow for a focused investigation of observable trading structure: order-size
flows, margin balances, Dragon-Tiger List activity, block trades, shareholders, Stock
Connect holdings, or chip cost distribution. Do not use flow labels as proof of investor
identity or intent.

## System contract

- **Stage:** 3. Investigate; may refresh evidence during Stage 6 monitoring
- **Consumes:** candidate or subject, hypothesis, comparison window, and `as_of`
- **Produces:** capital/ownership evidence for `evidence_pack` or an evidence delta for
  `change_log`
- **Gate:** contributes to G3 or G6 in [research-system.md](research-system.md)
- **Permitted next stages:** `thesis-review` or change monitoring

## Define the claim to test

Resolve the symbol, comparison window, and one or more explicit hypotheses, such as:

- recorded large-order net flow strengthened while price and turnover confirmed;
- financing balance expanded faster than price, increasing leverage sensitivity;
- shareholder count, major-holder trades, or disclosed holdings changed materially;
- market price moved relative to median or weighted chip cost.

Use `stocks` to resolve company names and `trade_calendar` to align dates.

## Collect by evidence layer

| Evidence layer | Methods | What it can establish |
|---|---|---|
| Price and liquidity | `daily`, `fundamentals` | price response, volume, turnover, market value |
| Recorded order flow | `moneyflow` | net flow by reported order-size bucket |
| Leverage | `margin` | financing and securities-lending balances and changes |
| Exceptional trading | `top_list`, `top_inst`, `block_trade` | disclosed list reasons, seats, and negotiated trades |
| Ownership | `shareholders`, `holder_trade`, `northbound_holdings`, `southbound_holdings` | disclosed holder counts, holder trades, and holdings |
| Position cost | `distribution` | cost percentiles, weighted cost, and winner rate |
| Market context | `moneyflow_hsgt`, `technical_factors`, `technical_factors_pro` | broad flow and technical confirmation |

Fetch only the layers needed for the hypothesis. Treat northbound holdings after August 2024
as low-frequency disclosure, not missing daily data.

## Analyze

1. Align each series to its own observation or disclosure date; never forward-fill a
   low-frequency holding into a claim about daily activity without labeling it.
2. Normalize flows by comparable liquidity or market-value measures when comparing different
   stocks. Preserve the raw values and units beside normalized calculations.
3. Compare rolling windows rather than interpreting one day's flow in isolation.
4. Separate price confirmation, liquidity confirmation, leverage, ownership, and chip cost.
   Call evidence “aligned” only when direction and dates support the same hypothesis.
5. Treat seat names, order-size buckets, and flow labels as classifications in the source
   data, not verified beneficial owners.

## Output

1. **结论摘要** — strongest aligned evidence and strongest contradiction.
2. **证据分层表** — metric, change, window, unit, and `as_of`.
3. **一致与背离** — where price, flow, leverage, ownership, and chips agree or diverge.
4. **替代解释** — at least one plausible non-intent explanation for unusual data.
5. **待验证事项** — missing layers, stale disclosures, and next observable checkpoints.
6. **复现信息** — methods, parameters, windows, and transformations.
