# 股息与分红研究

Use this workflow to evaluate dividend history, yield, continuity, implementation status,
and financial support. A historical dividend record does not guarantee a future dividend.

## System contract

- **Stage:** 3. Investigate; may refresh distribution evidence during Stage 6 monitoring
- **Consumes:** candidate or subject, history, yield convention, and `as_of`
- **Produces:** dividend evidence for `evidence_pack` or an evidence delta for `change_log`
- **Gate:** contributes to G3 or G6 in [research-system.md](research-system.md)
- **Permitted next stages:** `thesis-review` or change monitoring

## Resolve the scope

Resolve the company with `stocks`, the requested history, and whether the user cares about
cash yield, dividend growth, payout stability, total return, or upcoming implementation
dates. Default to at least five completed fiscal years when available.

## Collect

- corporate actions: `dividend` for proposal, implementation status, per-share cash or stock
  distribution, record date, ex-date, and payment date;
- market denominator: `daily` and `fundamentals` for contemporaneous prices and reported
  dividend-yield fields;
- financial support: `income`, `cash_flow`, and optionally `balance_sheet`;
- near-term uncertainty: `forecast` when a recent earnings preview can change the picture;
- total-return preparation: `adj_factor` when the user requests adjusted returns.

## Analyze

1. Filter out cancelled, unimplemented, or duplicate plan rows before counting paid
   dividends. Preserve their status in a separate exceptions table.
2. Group dividends by fiscal year and distinguish announcement, record, ex-, and payment
   dates.
3. Calculate yield only with an explicitly named price date and cash-dividend basis. Do not
   mix a current price with a historical dividend and call it realized yield.
4. Compare cash dividends with net income and operating/free cash flow only when units and
   reporting periods are compatible. Label any payout ratio calculation and formula.
5. Assess continuity with paid years, cuts, omissions, and growth; do not reduce the record
   to one average.
6. Use adjusted-price data for total return. Do not add cash dividends to an already
   dividend-adjusted return series.

## Output

1. **股息画像** — continuity, current evidence, and main sustainability uncertainty.
2. **历年分红表** — fiscal year, cash dividend per share, status, key dates, and `as_of`.
3. **收益率与增长** — formulas, denominator dates, and exceptions.
4. **盈利与现金流支撑**
5. **未来观察项** — announced but unpaid plans and financial variables, not predictions.
6. **数据与口径** — transformations, adjustment convention, missing years, and units.
