# 投资论点构建与反证

Use this workflow after diligence evidence exists. Convert a compatible `evidence_pack` into
a falsifiable `thesis_card`; do not merely summarize every metric or turn the result into a
buy/sell recommendation.

## System contract

- **Stage:** 4. Challenge
- **Consumes:** `research_mandate` and `evidence_pack`
- **Produces:** `thesis_card`
- **Gate:** G4 in [research-system.md](research-system.md)
- **Permitted next stages:** public market feasibility, public monitoring, or research review

## Validate the evidence

Before synthesis, verify that:

1. the mandate and evidence refer to the same subject, horizon, and `as_of` frame;
2. price series share one adjustment convention;
3. financial periods, announcement dates, units, and missing sections are explicit;
4. claims can be traced to a QuantSonar method, calculation, or named external source;
5. contradictory evidence and unavailable qualitative diligence have not been removed.

If the pack is too incomplete to support a thesis, return the failed G3/G4 checks and the
minimum evidence required. Do not repair the pack with remembered company facts.

## Construct the thesis

1. Write one sentence stating the economic or market claim and expected horizon.
2. Select only the evidence that is decisive for that claim; separate facts, calculations,
   and interpretations.
3. Build base, bull, and bear cases from observable conditions. Do not attach unsupported
   probabilities or target prices.
4. List catalysts that could reveal whether the claim is progressing.
5. Define falsifiers as observable conditions that would invalidate or materially weaken the
   thesis. A price decline by itself is not a business-thesis falsifier.
6. Preserve contradictions and unknowns. Classify each as resolvable with QuantSonar,
   requiring an external source, or currently unknowable.
7. Convert catalysts, falsifiers, and stale evidence into dated monitoring rules.

## Output

Emit a `thesis_card` using the common envelope in
[research-system.md](research-system.md), then include:

1. **核心论点与期限**
2. **决定性证据** — claim, evidence type, value/observation, source, and `as_of`
3. **Base / Bull / Bear** — observable conditions, not promises
4. **催化剂与反证条件**
5. **矛盾、未知项与外部证据缺口**
6. **监测规则与下次复核时间**
7. **G4 结果** — pass, partial, or fail with reasons

Do not output personalized position sizing, entry/exit instructions, guaranteed returns, or
an unexplained composite score.
