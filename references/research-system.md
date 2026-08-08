# 公开数据投研系统

Use this document when the request spans more than one research stage. This is the
orchestration contract for the QuantSonar Skill: workflows are reusable operators, while
versioned research artifacts and gates form the system.

## System objective

Turn a public-data research question into a traceable loop:

`research_mandate` → `market_context` → `candidate_pool` → `evidence_pack` →
`thesis_card` → `feasibility_card` → `change_log` → `research_review`

The arrows are dependency rules, not a requirement to run every stage for every request. A
narrow factual or analytical request may invoke one workflow directly. A lifecycle request
must reuse an existing upstream artifact or build the minimum missing prerequisites.

Phase 1 excludes private holdings, transactions, cost basis, account balance, tax data, and
personal risk profiles. Therefore this system ends at public market feasibility and research
monitoring; it does not size positions, place orders, decide exits, or calculate personal
performance.

## Four-layer architecture

| Layer | Responsibility | Contents |
|---|---|---|
| L1 Orchestrator | classify intent, find missing prerequisites, invoke operators, validate gates | `SKILL.md` plus this system contract |
| L2 Research state | preserve context and make each stage consumable by the next | eight versioned artifact types and G0–G7 |
| L3 Skill operators | perform one bounded research transformation | market, screening, company, sector, technical, capital, ETF, dividend, event, index, thesis, data, and review workflows |
| L4 Data adapters | retrieve facts and deterministic inputs | QuantSonar MCP methods, Python SDK fallback, and explicitly named external sources |

An API method is not a Skill; a Skill is not the system; and a narrative report is not a
state handoff unless it conforms to an artifact contract. This separation lets data methods
change without rewriting the lifecycle and lets a workflow improve without changing every
downstream consumer.

## Two service entrances

Phase 1 exposes the same research system through two user-facing entrances:

| Service | Starts from | Core research modules | Primary handoff |
|---|---|---|---|
| Individual-stock research | one named company or symbol | company fundamentals and valuation, technical state, capital behavior, dividends, events, thesis challenge, feasibility, monitoring | a stock-subject `evidence_pack` and `thesis_card` |
| Sector research | one Shenwan industry, concept/theme, or published index | constituent definition, relative strength, breadth, leadership, concentration, aggregate valuation/operations, capital/events, thesis challenge, monitoring | a sector-subject `evidence_pack` plus a bounded member `candidate_pool` |

The entrances are connected rather than isolated. Sector research sends representative or
anomalous members into individual-stock research. Individual-stock research uses sector
evidence to distinguish company-specific change from broad industry or theme movement. Both
then use the same thesis, feasibility, monitoring, and review contracts.

## Stages and gates

| Stage | System question | Primary workflows | Required artifact | Gate to continue |
|---|---|---|---|---|
| 0. Configure | What exactly is being researched? | `research-mandate`, `index-research` | `research_mandate` | G0: horizon, universe, benchmark, exclusions, `as_of`, and review cadence are explicit |
| 1. Observe | What is the dated market context? | `market-brief`, `event-monitor`, `index-research` | `market_context` | G1: every evidence family has a date; stale, missing, and intraday/EOD mixtures are labeled |
| 2. Discover | Which candidates deserve investigation? | `stock-screening`, `etf-research` | `candidate_pool` | G2: universe, rules, thresholds, ranking, exclusions, and missing-value policy are reproducible |
| 3. Investigate | What does the evidence establish? | stock, sector, technical, capital, dividend, ETF, event, and data workflows | `evidence_pack` | G3: source coverage, periods, units, contradictions, limitations, and unknowns are recorded |
| 4. Challenge | What must be true, and what would disprove it? | `thesis-review` | `thesis_card` | G4: base/bull/bear cases, catalysts, falsifiers, unknowns, and monitoring variables are explicit |
| 5. Feasibility | What public market constraints affect implementation? | `market-feasibility` with technical, ETF, event, or capital evidence as needed | `feasibility_card` | G5: liquidity, volatility, suspension/limit status, and price assumptions are evidenced; no order instruction is emitted |
| 6. Monitor | What material public evidence changed? | `event-monitor` plus relevant evidence workflow | `change_log` | G6: changes are compared with the recorded thesis, classified by materiality, and dated |
| 7. Review | What should change in the research process? | `research-review`, `quant-data-prep` | `research_review` | G7: errors, bias, useful evidence, failed rules, and proposed process changes are traceable |

A failed gate is a valid result. Stop, state the missing or conflicting inputs, and return the
partial artifact. Do not bypass a gate by filling a field from memory or with a hidden default.

## Common artifact envelope

Every artifact must carry the same header so another Skill can consume it without relying on
conversation history:

```yaml
schema_version: "1.0"
artifact_id: "<stable identifier>"
artifact_type: "<one of the eight artifact types>"
subject: "<security, fund, index, universe, or research process>"
as_of: "<YYYYMMDD or exact timestamp>"
generated_at: "<timestamp>"
upstream_ids: []
data_sources:
  - method: "<QuantSonar method or named external source>"
    as_of: "<source-specific date>"
limitations: []
```

Do not copy large raw datasets into every artifact. Preserve the query contract, important
derived values, evidence references, and transformations needed to reproduce the conclusion.

## Artifact contracts

### `research_mandate`

Required fields: research objective, universe, horizon, benchmark, exclusions, evidence
policy, `as_of`, and review cadence. The objective describes the research question; it must
not collect personal wealth, loss tolerance, holdings, or account constraints.

### `market_context`

Required fields: index direction, breadth, themes, events, uncertainty, and separate dates for
each evidence family. It is context, not a timing signal.

### `candidate_pool`

Required fields: universe snapshot, visible rules, thresholds, sort order, candidates with
supporting metrics, exclusions, and missing-data treatment. It is a queue for research, not a
recommendation list.

### `evidence_pack`

Required fields: subject, research questions, fundamental/valuation/technical/capital/event
evidence as applicable, historical comparisons, contradictions, missing evidence, and source
dates. Each section may be produced independently and merged only when symbols, periods,
units, and adjustment conventions are compatible.

### `thesis_card`

Required fields: one-sentence thesis, decisive evidence, base/bull/bear cases, catalysts,
falsifiers, contradictions, unknowns, horizon, and observable monitoring rules. A thesis is
not an investment recommendation and must not contain personalized sizing or execution.

### `feasibility_card`

Required fields: recent traded amount/volume, turnover when available, volatility and gap
behavior, suspension/limit status, observable price zones with calculation windows, data
cutoff, and constraints. Do not include an entry order, target price, stop-loss order, or
broker-specific instruction.

### `change_log`

Required fields: previous artifact IDs, what changed, old/new evidence, event timestamp,
materiality (`informational`, `watch`, or `thesis-relevant`), affected thesis fields, stale
inputs, and next review point. Do not treat price movement alone as proof that a thesis changed.

### `research_review`

Required fields: evaluated artifacts or hypothesis, benchmark or expected result, what worked,
what failed, data leakage checks, missing-data and survivorship checks, reasoning-bias review,
and proposed changes to the mandate, screen, evidence checklist, or monitoring rule. Personal
return attribution remains outside Phase 1.

## Orchestration algorithm

1. Classify the request as a direct fact, a single-stage analysis, or a lifecycle run.
2. Identify the requested output artifact and inspect any supplied upstream artifacts.
3. Validate upstream schema, subject, date, horizon, units, and adjustment conventions.
4. Build only missing prerequisites. For a narrow single-stage request, state assumed public
   research context instead of silently running the full lifecycle.
5. Invoke the minimum relevant workflows and merge compatible evidence into the target
   artifact.
6. Evaluate the stage gate. On failure, return the partial artifact plus an explicit recovery
   requirement.
7. Return the validated artifact, its limitations, and the permitted next stages.
8. During monitoring and review, reference artifact IDs so changes feed back into the mandate,
   screen, evidence checklist, or thesis rather than becoming an isolated report.

## Standard recipes

### One-stock research

`research_mandate` → company, optional sector, technical, capital, dividend, and event evidence as needed →
`evidence_pack` → `thesis_card` → optional `feasibility_card` → `change_log`

### Screen to thesis

`research_mandate` → optional `market_context` → `candidate_pool` → one `evidence_pack` per
surviving candidate → comparable `thesis_card` records.

### Sector to company research

`research_mandate` → exact sector and member snapshot → sector `evidence_pack` → bounded
member `candidate_pool` → one stock `evidence_pack` per selected role → comparable
`thesis_card` records. Feed company-specific findings back into the next sector `change_log`.

### ETF selection research

`research_mandate` with an index benchmark → `candidate_pool` of matching funds → ETF
exposure/liquidity evidence → `thesis_card` describing implementation tradeoffs →
`feasibility_card`.

### Event update

Existing `thesis_card` → event and market evidence → `change_log`. Rebuild the affected
`evidence_pack` and `thesis_card` only when the change is thesis-relevant.

### Quant hypothesis

`research_mandate` → dataset contract and quality report → point-in-time test →
`research_review` → approved changes to the screen or evidence policy. Paper results are not
personal portfolio performance.

## System invariants

- Evidence dates and artifact dependencies must remain visible.
- Screens, indicators, flows, and events are evidence; none is a standalone decision.
- Contradictory evidence is preserved, not averaged into a synthetic score by default.
- Revisions create a new artifact version and link to the prior ID.
- Private-data stages stay disabled until a separately governed privacy and suitability layer
  is designed.
- Research outputs never become autonomous brokerage actions.
