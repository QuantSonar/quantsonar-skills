# 公开研究任务定义

Use this workflow at the start of a multi-stage request or when the research universe,
horizon, benchmark, exclusions, or evidence policy is unclear. Define a public research
contract without collecting personal financial or account information.

## System contract

- **Stage:** 0. Configure
- **Consumes:** the user's research question and any stated public research preferences
- **Produces:** `research_mandate`
- **Gate:** G0 in [research-system.md](research-system.md)
- **Permitted next stages:** market observation, discovery, direct investigation, or dataset
  preparation

## Resolve the mandate

Define or explicitly default:

1. **Objective** — the research question and intended research artifact, not a personal
   investment decision.
2. **Universe** — A shares, an industry, an index snapshot, named securities, or named funds.
3. **Horizon** — intraday, weeks, quarters, or years, plus the historical evidence window.
4. **Benchmark** — exact index when comparison matters; use `index-research` if it must be
   resolved or evaluated.
5. **Exclusions** — inactive securities, boards, ST status, unavailable fields, or other
   public-data rules relevant to the question.
6. **Evidence policy** — required QuantSonar evidence, optional external inputs, point-in-time
   rules, price adjustment, and missing-data treatment.
7. **Time boundary** — use `trade_calendar` to establish the applicable `as_of` date.
8. **Review cadence** — event-driven, daily, weekly, reporting-cycle, or one-time.

Use `stocks`, `industries`, `index_weight`, `basic`, or `tracking_indices` only when needed to
make the universe or benchmark reproducible. Do not turn an ambiguous request into a large
unbounded data pull.

## Defaults and questions

Prefer visible, reversible defaults when they do not materially change the research question.
Ask for clarification only when different choices would produce incompatible artifacts, such
as stock versus ETF universe or intraday versus long-horizon research. Record every default in
the artifact.

Do not ask for holdings, cost basis, position size, account value, transactions, taxes,
liquidity needs, loss tolerance, or personal risk profile. If the user supplies them, state
that the Phase 1 system will not process or persist them and continue with the public portion.

## Output

Emit a `research_mandate` using the common envelope in
[research-system.md](research-system.md), then include:

1. **研究目标与目标产物**
2. **研究范围、期限和基准**
3. **排除规则与缺失值规则**
4. **证据政策与时点要求**
5. **复核节奏**
6. **显式默认项和外部证据缺口**
7. **G0 结果** — pass, partial, or fail with the exact missing field

The mandate may describe a style such as quality, dividend, value, trend, event-driven, or
quantitative research, but it must not imply suitability for the user's personal finances.
