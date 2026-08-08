# 公开数据投研 Skill 矩阵

Use this matrix as the capability registry for the public-data research system. Read
[research-system.md](research-system.md) for orchestration, typed artifacts, dependencies,
stage gates, and feedback. Treat a Skill as a reusable research operator with explicit
inputs, evidence, method, output, and stopping conditions. Do not treat an API endpoint or a
report section as a Skill by itself.

## Contents

- [Support levels](#support-levels)
- [Lifecycle matrix](#lifecycle-matrix)
- [Atomic analysis Skills](#atomic-analysis-skills)
- [Composition patterns](#composition-patterns)
- [QuantSonar data coverage](#quantsonar-data-coverage)
- [Skill contract](#skill-contract)

## Phase 1 scope

Build Phase 1 entirely from public and licensed market data. The active system contains eight
continuous stages, numbered 0–7, matching [research-system.md](research-system.md). Do not
request, persist, or process the user's holdings, transactions, cost basis, account balance,
tax situation, or personal risk profile.

## Support levels

- **Native** — QuantSonar data can support the core result directly.
- **Composite** — combine several public or licensed datasets and analysis Skills.
- **External** — require data QuantSonar does not currently provide, such as full filings,
  management transcripts, or complete macro/industry datasets.
- **Deferred private** — require personal portfolio or account data and are outside Phase 1.

Never silently fill a Composite or External input with a generic assumption. Return the
missing-input contract and continue only with the supported portion.

## Lifecycle matrix

| Stage | Decision to support | Reusable Skills | Support | Required output |
|---|---|---|---|---|
| 0. Configure | What research style, horizon, universe, and benchmark define the process? | `define-research-mandate`, `classify-investment-style`, `select-benchmark` | Composite public data | `research_mandate` |
| 1. Observe | What environment and opportunity set are observable? | `scan-market-regime`, `measure-market-breadth`, `map-themes-and-events` | Native with External macro enrichment | `market_context` |
| 2. Discover | Which securities deserve research attention? | `screen-investment-universe`, `detect-market-anomalies`, `compare-funds-and-indices` | Native | `candidate_pool` |
| 3. Investigate | What economically and technically characterizes each candidate? | `analyze-financial-quality`, `value-security`, `analyze-technical-state`, `analyze-capital-behavior`, `assess-dividend-quality`, `research-fund-exposure` | Native for structured data; External for qualitative diligence | `evidence_pack` |
| 4. Challenge | What must be true, and what would disprove it? | `build-investment-thesis`, `run-bull-bear-review`, `define-catalysts-and-disconfirmers`, `test-investment-hypothesis` | Composite public data | `thesis_card` |
| 5. Feasibility | What public market constraints affect implementation? | `assess-trade-liquidity`, `check-market-constraints` | Native public data | `feasibility_card` |
| 6. Monitor | Has public evidence or market structure changed? | `monitor-investment-thesis`, `monitor-events`, `detect-risk-drift` | Composite public data | `change_log` |
| 7. Review | Which research rules worked and what should change? | `evaluate-backtest`, `review-research-decision`, `update-investment-playbook` | Public/simulated data | `research_review` |

### Deferred capabilities

Keep the following outside the active matrix until a separately governed private-data layer
exists:

| Deferred stage | Why it is disabled |
|---|---|
| Portfolio fit, construction, and position sizing | requires existing exposure, constraints, loss tolerance, and account context |
| Brokerage execution | requires broker connectivity, permissions, order state, and execution controls |
| Position-level exit and rebalance | requires holdings, cost basis, taxes, and portfolio alternatives |
| Personal performance attribution | requires transactions, cash flows, fees, and a governed attribution policy |

### Lifecycle orchestration rules

1. Use the eight artifact types and G0–G7 gates in
   [research-system.md](research-system.md); this table maps lifecycle concepts to available
   operators but does not replace the system contract.
2. Start with a public research mandate: style, horizon, universe, benchmark, exclusions,
   and review cadence. Do not collect personal financial constraints in Phase 1.
3. Do not let a strong Stage 3 company result bypass Stage 4 thesis challenge. Portfolio fit
   remains disabled until a separately governed private-data layer exists.
4. Record the thesis, falsifiers, expected horizon, and evidence timestamps before market
   feasibility or monitoring.
5. Evaluate public monitoring against the recorded thesis and evidence, not a user's purchase
   price. Feed research review back into screens, thesis checklists, and data controls.

## Atomic analysis Skills

The first service layer has two entrances: `stock-research` and `sector-research`. They share
the same supporting operators, artifacts, and gates; sector research can generate a company
candidate pool, while stock research can consume sector evidence for peer context. Treat all
workflows below as atomic Skills that can be called from several lifecycle stages:

| Atomic Skill | Lifecycle role | Read |
|---|---|---|
| `research-mandate` | Stage 0 public objective, universe, horizon, benchmark, and evidence policy | [research-mandate.md](research-mandate.md) |
| `market-brief` | Stage 1 market context and Stage 6 context refresh | [market-brief.md](market-brief.md) |
| `stock-screening` | Stage 2 idea discovery | [stock-screening.md](stock-screening.md) |
| `stock-research` | Stage 3 company, financial, valuation, and risk evidence | [stock-research.md](stock-research.md) |
| `sector-research` | Stage 1–3 sector context, breadth, leadership, aggregate evidence, and member discovery | [sector-research.md](sector-research.md) |
| `technical-analysis` | Stage 3 technical evidence, Stage 5 feasibility, and Stage 6 monitoring | [technical-analysis.md](technical-analysis.md) |
| `capital-behavior` | Stage 3 trading-structure evidence and Stage 6 monitoring | [capital-behavior.md](capital-behavior.md) |
| `etf-research` | Stage 2 fund discovery, Stage 3 exposure evidence, and Stage 5 feasibility | [etf-research.md](etf-research.md) |
| `dividend-research` | Stage 3 income evidence and Stage 6 distribution monitoring | [dividend-research.md](dividend-research.md) |
| `event-monitor` | Stage 1 event context and Stage 6 thesis-linked monitoring | [event-monitor.md](event-monitor.md) |
| `index-research` | Stage 0 benchmark definition, Stage 1 context, and Stage 7 review basis | [index-research.md](index-research.md) |
| `quant-data-prep` | Stage 3 reproducible evidence and Stage 7 hypothesis/process review | [quant-data-prep.md](quant-data-prep.md) |
| `thesis-review` | Stage 4 synthesis, challenge, falsifiers, and monitoring-rule definition | [thesis-review.md](thesis-review.md) |
| `market-feasibility` | Stage 5 public liquidity, volatility, limit, suspension, and price-structure constraints | [market-feasibility.md](market-feasibility.md) |
| `research-review` | Stage 7 public/simulated process review and feedback | [research-review.md](research-review.md) |
| `direct-data` | Narrow factual retrieval at any stage | [data-catalog.md](data-catalog.md) |

These operators remain one installable `quantsonar` package so the orchestrator can enforce
shared artifacts and gates. They may later be exposed as independently triggerable packages,
but their input/output contracts must remain compatible with this system.

## Composition patterns

### From idea to monitored thesis

`define-research-mandate` → `scan-market-regime` → `screen-investment-universe` →
`analyze-financial-quality` + `value-security` + `analyze-technical-state` → `run-bull-bear-review` →
`assess-trade-liquidity` → `monitor-investment-thesis` → `review-research-decision`

### Sector to company

`define-research-mandate` → `define-sector-and-members` → `analyze-sector-strength-and-breadth` +
`analyze-sector-fundamentals-and-events` → `select-representative-members` →
`stock-research` → `run-bull-bear-review` → shared monitoring and review

### Event-driven research

`map-themes-and-events` → `detect-market-anomalies` → `analyze-capital-behavior` →
`define-catalysts-and-disconfirmers` → `assess-trade-liquidity` → `monitor-events`

### Quantitative strategy research

`test-investment-hypothesis` → `quant-data-prep` → point-in-time feature and universe
validation → backtest with modeled costs and limits → paper watchlist monitoring →
`evaluate-backtest` → `update-investment-playbook`

### ETF selection research

`select-benchmark` → `compare-funds-and-indices` → `research-fund-exposure` →
`assess-trade-liquidity` → benchmark-relative public monitoring → `detect-risk-drift`

## QuantSonar data coverage

Use the following methods as evidence inputs, not as Skill boundaries. Every registered
method must remain assigned to at least one capability.

| Evidence family | Methods | Primary Skills |
|---|---|---|
| Security master and calendar | `stocks`, `industries`, `trade_calendar` | mandate universe, sector membership, screening, all date alignment |
| Stock prices and valuation | `daily`, `fundamentals`, `adj_factor` | market map, screening, valuation, monitoring, benchmark comparison |
| Technical and liquidity state | `technical_factors`, `technical_factors_pro`, `realtime`, `limit_list` | anomaly detection, trade liquidity, event monitoring |
| Financial statements and quality | `indicators`, `income`, `balance_sheet`, `cash_flow`, `audit`, `main_business` | financial quality, valuation inputs, risk review |
| Expectations and disclosures | `forecast`, `express`, `analyst_reports`, `disclosure_date`, `news_flash` | catalysts, thesis challenge, monitoring |
| Capital and ownership | `moneyflow`, `moneyflow_hsgt`, `margin`, `block_trade`, `top_list`, `top_inst`, `shareholders`, `holder_trade`, `northbound_holdings`, `southbound_holdings`, `distribution` | capital behavior, anomaly detection, risk drift |
| Themes and benchmarks | `concepts`, `concept_members`, `index_daily`, `index_weight`, `fx_daily` | sector research, market regime, theme map, benchmark selection, review basis |
| ETF identity and exposure | `basic`, `etf_daily`, `etf_adj_factor`, `nav`, `portfolio`, `share_size`, `tracking_indices` | fund comparison, exposure diligence, public feasibility |
| Income events | `dividend` | dividend quality, cash-flow support, distribution monitoring |

## Skill contract

Define every new Skill with the same contract:

1. **Trigger** — phrases and investment stage that should activate it.
2. **Inputs** — required market, document, research-configuration, and external inputs;
   exclude private account data in Phase 1.
3. **Evidence** — allowed datasets, timestamps, units, and freshness requirements.
4. **Method** — deterministic calculations plus bounded reasoning steps.
5. **Output** — a reusable artifact consumed by the next lifecycle stage.
6. **Stop conditions** — missing inputs, stale data, incompatible periods, or access limits.
7. **Guardrails** — no fabricated data, hidden assumptions, guaranteed returns, or autonomous
   brokerage action.
8. **Evaluation** — golden prompts, adversarial cases, numerical checks, and downstream
   compatibility.
