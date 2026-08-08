# 板块研究

Use this workflow to research an A-share industry, concept/theme, or index-like sector. Build
the sector from an explicit constituent definition, analyze its internal structure, and
identify company candidates for further research. Do not treat a sector narrative or one
leading stock as evidence that every constituent shares the same economics.

## System contract

- **Stage:** primarily 3. Investigate; may support Stage 1 context, Stage 2 discovery, and
  Stage 6 monitoring
- **Consumes:** `research_mandate`, sector definition, comparison window, benchmark, and
  constituent snapshot date
- **Produces:** a sector-subject `evidence_pack`, plus an optional member `candidate_pool` or
  sector-linked `change_log`
- **Gate:** contributes to G1, G2, G3, or G6 in
  [research-system.md](research-system.md)
- **Permitted next stages:** sector `thesis-review`, individual `stock-research` for selected
  members, public feasibility, monitoring, or research review

## Resolve what “板块” means

Classify the subject before fetching data:

| Sector type | Constituent source | Native sector series | Important limitation |
|---|---|---|---|
| Shenwan industry | `industries` filtered by L1/L2/L3 code or name | none in the current methods | returns and valuation must be labeled as member-derived proxies; classification is a current snapshot unless historical membership is supplied |
| Concept/theme | `concepts`, `concept_members` | `concepts` provides dated change, turnover, breadth, market value, and reported leader fields | membership is dated but thematic definitions may overlap and change |
| Published index | `index_weight` | `index_daily` | use `index-research` for official benchmark and weight analysis |

Resolve ambiguous names before analysis. “新能源”“AI”“消费”等 labels can match an
industry, concept, or index with materially different members. Preserve the exact code,
taxonomy level, member date, and member count.

## Build the constituent contract

1. Establish the applicable trading date with `trade_calendar`.
2. Obtain the member snapshot from `industries`, `concept_members`, or `index_weight`.
3. Join `stocks` to verify names and listing status.
4. Record additions, removals, duplicates, unmapped symbols, and members without required
   data. Do not silently substitute today's members into a historical analysis.
5. For overlapping concepts, calculate and disclose member overlap before comparing them.

If a historical industry member snapshot is unavailable, a historical test may use the
current industry membership only as a clearly labeled approximation; do not call it
point-in-time correct.

## Analyze by layer

### 1. Performance and relative strength

- For a concept, use the dated `concepts` fields when they answer the question.
- For an industry without a native series, construct an equal-weight or prior-date
  market-cap-weighted member return proxy from `daily` and `fundamentals`. State the weighting,
  rebalance rule, missing-member rule, and adjustment convention.
- Compare with the mandate benchmark from `index_daily` over identical dates.
- Report return, volatility, drawdown, and rolling relative strength only when the underlying
  series is reproducible.

Never call a member-derived proxy an official sector-index return.

### 2. Breadth and participation

- Measure advancing/declining members, proportions above selected moving averages, new
  highs/lows, limit-up/down participation, turnover, and return dispersion when fields exist.
- Use `concepts.up_num` and `concepts.down_num` for native concept breadth, then verify the
  member snapshot when drilling down.
- Distinguish broad participation from a move dominated by one or two large constituents.

### 3. Leadership and internal structure

- Rank leaders and laggards using explicit periods and metrics.
- Measure top-N market-cap concentration from `fundamentals`; for an index use official
  weights from `index_weight`.
- Call market-cap weight × return a contribution proxy unless official time-varying weights
  and divisor mechanics are available.
- Separate durable leaders, short-term price leaders, and event-driven outliers.

### 4. Valuation and operating evidence

- Use `fundamentals` to calculate member-weighted and median valuation measures. Exclude
  invalid ratios such as non-positive PE from the relevant aggregation and state coverage.
- Use `indicators`, `income`, `cash_flow`, `balance_sheet`, and `main_business` only for a
  bounded member set or explicit aggregate task. Align comparable periods and announcement
  availability.
- Never sum or average accounting ratios blindly. Aggregate additive values separately from
  ratios and disclose each formula.
- Report coverage, dispersion, and concentration; a median alone can hide a bimodal sector.

### 5. Capital, events, and catalysts

- Aggregate member `moneyflow`, `margin`, `limit_list`, `top_list`, `top_inst`, and holdings
  evidence only across a fixed, dated member set.
- Use `news_flash`, `forecast`, `express`, `disclosure_date`, `holder_trade`, and `dividend` to
  identify member events and shared catalysts.
- Treat recorded flow as trading evidence, not proof of sector-wide institutional intent.
- Distinguish a sector-wide event from a company-specific event that happens to affect a
  current leader.

## Cross-link the two services

The sector service should end with a bounded company handoff:

1. identify no more than 10 representative, leading, lagging, or anomalous members by visible
   rules;
2. explain whether each name represents sector economics, price leadership, valuation,
   financial quality, or event sensitivity;
3. emit them as an optional `candidate_pool` for `stock-research`;
4. never label the highest-return member the “best company.”

Conversely, a single-stock workflow may call this Skill for peer comparison or to determine
whether an observation is company-specific or sector-wide.

## Output

Emit an `evidence_pack` using the common envelope in
[research-system.md](research-system.md) with `subject` set to the exact industry, concept, or
index definition, then use this order:

1. **板块结论** — state strength, breadth, internal concentration, decisive evidence, and
   main uncertainty in 2–4 sentences.
2. **板块定义** — type, code/name, taxonomy level, member date/count, benchmark, and period.
3. **走势、相对强弱与回撤**
4. **广度、扩散度与内部结构**
5. **估值与经营证据** — coverage and dispersion included.
6. **资金、事件与催化剂**
7. **代表公司与个股研究入口** — visible selection role and metrics.
8. **反证条件与监测变量**
9. **数据限制与 G3 结果** — especially proxy returns and unavailable historical membership.

Do not produce direct sector or stock buy/sell instructions, personalized allocation, or an
unsupported “sector rotation” prediction.
