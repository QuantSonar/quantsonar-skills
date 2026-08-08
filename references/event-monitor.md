# 事件与异动监测

Use this workflow for a current or historical event tape that combines realtime prices,
financial news, disclosures, limits, and unusual trading. Produce a prioritized observation
list, not a prediction engine.

## System contract

- **Stage:** 1. Observe or 6. Monitor
- **Consumes:** universe/date boundary and optional `thesis_card` or prior `change_log`
- **Produces:** event evidence for `market_context` or a thesis-linked `change_log`
- **Gate:** contributes to G1 or G6 in [research-system.md](research-system.md)
- **Permitted next stages:** discovery, affected evidence refresh, or research review

## Set the monitoring boundary

Define the universe, session or date range, refresh expectation, and event types. Use
`trade_calendar` to determine whether the market is open. When the market is closed, label
`realtime` as the latest stored snapshot rather than a live quote.

## Collect by clock

- live market clock: `realtime` with its exact `trade_time`;
- news clock: `news_flash`, preserving source, `publish_time`, importance, and URL;
- completed-day structure: `limit_list`, `top_list`, `top_inst`, `block_trade`, and `margin`;
- theme context: `concepts` and `concept_members`;
- company disclosure clock: `forecast`, `express`, `disclosure_date`, `holder_trade`, and
  `dividend`.

Use all three news sources only when deduplication is useful. Do not assume a missing item
from one source did not occur.

## Correlate without inventing causality

1. Normalize timestamps and retain the original timezone and source fields.
2. Deduplicate news by time, subject, and content similarity while preserving source links.
3. Resolve mentioned companies to symbols before joining price data.
4. Define a pre/post event window before measuring price or volume response.
5. Call an event and move “temporally associated” when timing matches. Claim causality only
   when the source itself establishes it or the user supplies verified evidence.
6. Rank by observable importance, breadth, magnitude, and corroboration; do not rank by
   sensational language alone.

## Output

1. **监测摘要** — up to three developments that changed the current picture.
2. **事件时间线** — timestamp, source, subject, event, and verification status.
3. **市场反应** — price/volume window and exact quote or close timestamp.
4. **结构性异动** — limits, Dragon-Tiger, block trades, margin, or themes.
5. **待核实与下一检查点** — unresolved symbol, stale data, or upcoming disclosure.
6. **数据时钟** — separate cutoffs for quotes, news, EOD events, and disclosures.

For repeated monitoring, return a reproducible polling plan. Do not claim continuous
background monitoring unless an actual scheduler or automation has been configured.
