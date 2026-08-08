# 市场简报

Use this workflow for a daily, intraday, opening, or closing A-share overview. Optimize for a
two-minute read and distinguish actionable changes from background noise.

## System contract

- **Stage:** 1. Observe; may refresh context during Stage 6 monitoring
- **Consumes:** `research_mandate` or an explicit universe/date request
- **Produces:** `market_context`
- **Gate:** G1 in [research-system.md](research-system.md)
- **Permitted next stages:** candidate discovery, event monitoring, or research review

## Establish the time boundary

1. Resolve the requested date with `trade_calendar`.
2. For an intraday request, use `realtime` and label the exact snapshot time.
3. For a closing or historical brief, use the latest completed trading day. Do not mix an
   intraday snapshot with prior-day EOD data without labeling both dates.

## Collect

Use the smallest applicable set:

- broad market: `index_daily` and the one-day cross section from `daily`;
- breadth and extremes: `limit_list`;
- capital behavior: `moneyflow_hsgt`, `margin`, `top_list`, `top_inst`;
- themes: `concepts` and `concept_members` when needed;
- events: `news_flash`;
- live snapshot: `realtime` only when the user asks for current conditions.

If a dataset follows a different publication schedule, retain its own date and explicitly
label it.

## Analyze

1. Determine direction from major indices and market breadth, not one index alone.
2. Count advancing, declining, unchanged, limit-up, and limit-down securities when the
   cross section supports it.
3. Identify leading and lagging themes from observable market data.
4. Summarize capital measures as recorded flows or balances, not verified investor intent.
5. Link major market moves to news only when timing and subject match. Otherwise present the
   news and price move separately.
6. Select at most three developments that materially changed the day's picture.

## Output

1. **一句话市场状态**
2. **指数与广度** — compact table with timestamps.
3. **主线与异常** — strongest sectors, extremes, or unusual activity.
4. **资金与交易结构**
5. **重要事件** — facts first, interpretation second.
6. **下一交易日观察项** — events or variables to monitor, not predictions.
7. **数据截止时间与缺失项**

If there is no meaningful development, say so. Do not manufacture a narrative.
