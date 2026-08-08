# 条件选股

Use this workflow when the user asks to find, rank, filter, or build a candidate pool. A
screen produces research candidates; it does not produce investment recommendations.

## System contract

- **Stage:** 2. Discover
- **Consumes:** `research_mandate` and optional `market_context`
- **Produces:** `candidate_pool`
- **Gate:** G2 in [research-system.md](research-system.md)
- **Permitted next stages:** one evidence workflow per surviving candidate or research review

## Translate the request into explicit rules

Build a visible rule table before running the screen:

| Dimension | Examples | Typical methods |
|---|---|---|
| Universe | all A shares, an index, an industry | `stocks`, `index_weight`, `industries` |
| Market behavior | return, drawdown, turnover, volatility | `daily`, `technical_factors` |
| Valuation | PE, PB, market cap, historical percentile | `fundamentals` |
| Quality and growth | revenue/profit growth, ROE, margin, cash flow | `indicators`, `income`, `cash_flow` |
| Capital/event | money flow, margin, Dragon-Tiger, limit status | `moneyflow`, `margin`, `top_list`, `limit_list` |

State every threshold, period, sort order, exclusion, and missing-value rule. If the request
is ambiguous, use conservative defaults and disclose them instead of hiding assumptions.

## Execute in two stages

1. **Cheap cross-sectional filter**
   - Resolve the universe.
   - Use one-date market and valuation data to reduce the candidate set.
   - Exclude delisted/inactive securities and rows missing required fields.
2. **Candidate verification**
   - Pull historical or financial data only for survivors.
   - Verify reporting periods and announcement availability.
   - Recalculate derived metrics deterministically.

Default to no more than 20 final candidates unless the user requests a machine-readable full
result.

## Prevent common errors

- Do not compare incompatible reporting periods.
- Do not forward-fill financial reports before their announcement date in a historical
  screen.
- Treat non-positive PE as not meaningful when a positive-earnings valuation rule is used.
- Avoid survivorship bias when constructing a historical universe; disclose if only the
  current constituent list is available.
- Do not silently turn missing data into zero.
- Separate hard filters from ranking factors.

## Output

1. **筛选定义** — universe, date, explicit rules, exclusions.
2. **候选结果** — rank, symbol, name, each decisive metric, and `as_of`.
3. **入选原因** — one factual sentence per candidate.
4. **需要进一步验证** — risks, missing data, event sensitivity.
5. **复现信息** — methods, parameters, and calculation rules; include Python code when useful.

Never label the first-ranked candidate “best stock.” Rank means “best match to the stated
rules.”
