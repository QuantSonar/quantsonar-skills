# 投研流程复盘

Use this workflow to evaluate a public-data research process, screen, hypothesis, or prior
artifact chain. The object of review is the quality of the research process, not the user's
private portfolio performance.

## System contract

- **Stage:** 7. Review
- **Consumes:** prior system artifacts, a point-in-time dataset/backtest result, or a paper
  watchlist history
- **Produces:** `research_review`
- **Gate:** G7 in [research-system.md](research-system.md)
- **Permitted next stages:** revise `research_mandate`, screen rules, evidence checklist,
  thesis template, or monitoring rules

## Establish the review boundary

Record the reviewed artifact IDs, decision date, information available at that date, stated
horizon, benchmark, expected observation, and review date. If the original claim or benchmark
was never recorded, label the review as process reconstruction rather than outcome attribution.

## Review the process

1. **Evidence timing** — check announcement availability, constituent snapshots, price
   adjustment, and whether later information leaked into an earlier decision.
2. **Rule integrity** — verify the actual universe, thresholds, rankings, exclusions, and
   missing-data treatment against the recorded screen or mandate.
3. **Evidence usefulness** — identify which facts changed the thesis and which added noise or
   duplicated another indicator.
4. **Contradictions and falsifiers** — check whether adverse evidence was recorded promptly
   and whether falsifiers were observable and specific.
5. **Bias review** — look for confirmation bias, hindsight bias, narrative substitution,
   outcome bias, and silent benchmark changes.
6. **Quant validity** — when applicable, check survivorship bias, look-ahead bias, data
   snooping, modeled costs, limit/suspension constraints, and out-of-sample evidence.
7. **Feedback action** — propose one bounded, testable change at a time and name the artifact
   schema or workflow it modifies.

Use `quant-data-prep` when the review requires a reproducible dataset. Do not use current
index constituents or later financial reports to reconstruct historical availability.

## Output

Emit a `research_review` using the common envelope in
[research-system.md](research-system.md), then include:

1. **复盘对象与基准**
2. **当时可得证据与数据时间线**
3. **有效环节、失效环节和未验证环节**
4. **数据偏差与推理偏差检查**
5. **建议变更** — target artifact/workflow, exact change, expected benefit, and validation
6. **保留项** — what should not change based on one outcome
7. **G7 结果和下一轮研究入口**

Do not infer skill from one profitable outcome or failure from one loss. Never request private
holdings, transactions, cost basis, or account returns for this Phase 1 workflow.
