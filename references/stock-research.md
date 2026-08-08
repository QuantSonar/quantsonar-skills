# 个股研究

Use this workflow for a single listed company. Produce an evidence-led research snapshot,
not a generic company introduction.

## System contract

- **Stage:** 3. Investigate
- **Consumes:** `research_mandate` plus a candidate or explicit company request
- **Produces:** company, financial, valuation, and risk sections of an `evidence_pack`
- **Gate:** contributes to G3 in [research-system.md](research-system.md)
- **Permitted next stages:** add sector or complementary evidence, then `thesis-review`

## Connect company and sector evidence

When peer context can materially change the answer, call
[sector-research.md](sector-research.md) for the company's dated industry, concept, or chosen
benchmark group. Compare compatible periods and distinguish:

- company-specific evidence from sector-wide changes;
- price leadership from operating leadership;
- the company's valuation from the sector median, dispersion, and coverage;
- a company event from a shared sector catalyst.

Do not require sector analysis for a narrow factual company request, and do not infer peer
quality from industry membership alone.

## Resolve the question

Identify:

- company and exact suffixed symbol;
- requested period, or default to 1 year of market data and 3–5 reported periods;
- focus, if stated: fundamentals, valuation, price behavior, capital behavior, or risk.

If the user provides only a company name, call `stocks` and show the resolved symbol. If
multiple securities match, ask the user to choose.

## Collect the minimum dataset

Start with the core set and add optional data only when it changes the answer.

| Question | Core methods | Optional methods |
|---|---|---|
| Price and valuation | `daily`, `fundamentals` | `technical_factors`, `adj_factor` |
| Growth and profitability | `indicators`, `income`, `cash_flow` | `balance_sheet`, `main_business` |
| Expectations and reporting | `forecast`, `express` | `analyst_reports`, `disclosure_date`, `audit` |
| Capital behavior | `moneyflow`, `margin` | `distribution`, `top_list`, `top_inst`, `block_trade` |
| Ownership changes | `shareholders`, `holder_trade` | `northbound_holdings`, `southbound_holdings` |

Do not fail the whole report when optional methods are unavailable. Mark the corresponding
section “data unavailable under current access” and continue with supported evidence.

## Analyze

1. **Market behavior**
   - Calculate total return, annualized volatility, and maximum drawdown over the requested
     period.
   - Describe trend and drawdown; do not infer causality from price alone.
2. **Operating quality**
   - Compare revenue, profit, margins, return metrics, operating cash flow, and leverage
     across comparable reporting periods when fields are available.
   - Distinguish cumulative quarterly figures from single-quarter figures.
3. **Valuation**
   - Report current PE/PB or available valuation measures and their historical percentile.
   - Exclude invalid values such as non-positive PE from percentile calculations and disclose
     the rule.
4. **Capital and ownership**
   - Describe observable changes in money flow, margin balances, chips, holdings, and major
     shareholders.
   - Use neutral wording: “recorded net inflow” is a fact; “institutions are accumulating” is
     an interpretation requiring corroboration.
5. **Cross-check**
   - Look for contradictions such as profit growth without operating cash-flow support,
     improving fundamentals with contracting valuation, or rising prices with weakening
     breadth.

## Output

Use this order:

1. **研究摘要** — 2–4 sentences; state the strongest evidence and main uncertainty.
2. **关键数据** — compact table with value, comparison, period, and `as_of`.
3. **基本面与现金质量**
4. **估值位置**
5. **市场与资金行为**
6. **风险和待验证事项**
7. **数据说明** — methods used, periods, missing sections, transformations.

Avoid a single synthetic score unless the user explicitly requests one and the scoring
formula is shown.

If the user asks for a buy/sell decision:

- do not output “应该买入/卖出”, “暂不买入/卖出”, position sizing, or an entry price;
- do not invent PE/PB cutoffs or safety-margin thresholds;
- convert the request into evidence-based bull/base/bear conditions using verified values;
- identify personal inputs QuantSonar cannot know, such as horizon, loss tolerance,
  liquidity needs, concentration, and existing exposure;
- if verified data is unavailable, return the required data checklist and stop. Do not add a
  company assessment from memory.
