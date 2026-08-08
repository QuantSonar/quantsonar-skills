# 个股技术状态分析

Use this workflow to describe one stock's observable trend, momentum, volatility, volume,
and price structure from daily data. Treat technical indicators as transformations of price
and volume, not independent evidence of company value or guaranteed predictors.

## System contract

- **Stage:** 3. Investigate; may contribute to Stage 5 feasibility and Stage 6 monitoring
- **Consumes:** candidate or subject, horizon, `as_of`, and price-adjustment convention
- **Produces:** technical evidence for `evidence_pack` or public constraints for
  `feasibility_card`
- **Gate:** contributes to G3, G5, or G6 in [research-system.md](research-system.md)
- **Permitted next stages:** `thesis-review`, feasibility, or change monitoring

## Define the frame

Resolve with `stocks` and `trade_calendar`:

- exact suffixed symbol and `as_of` trading date;
- short, medium, and long windows, defaulting to 20, 60, and 250 trading days;
- one price convention: raw, forward-adjusted, or backward-adjusted;
- EOD analysis or a separately labeled `realtime` snapshot.

Prefer forward-adjusted prices for historical continuity unless the user requests another
convention. Never mix raw closes with adjusted moving averages or channels.

## Collect by evidence layer

| Layer | Core fields or methods | What to examine |
|---|---|---|
| Price and return | `daily`, `adj_factor` | return, drawdown, gaps, rolling highs/lows |
| Trend | `technical_factors`, `technical_factors_pro` | MA/EMA alignment and slope, ADX/DMI, consecutive up/down days |
| Momentum | MACD, RSI, KDJ, CCI, ROC, MTM, TRIX | direction, acceleration, and disagreement |
| Volatility and channels | ATR, Bollinger, Keltner, Donchian | volatility regime, range expansion, price location |
| Volume and participation | `daily`, `fundamentals`, OBV, MFI, VR | volume/amount, turnover, volume ratio, price-volume confirmation |
| Latest snapshot | `realtime` | current price and session range, with exact `trade_time` |

If `technical_factors` or `technical_factors_pro` is unavailable, calculate only transparent
price/volume statistics from `daily` and state that indicator coverage is reduced.

## Analyze

1. **Trend** — compare price with MA/EMA windows, their ordering, and their recent slopes.
   Classify the observed state as trending, ranging, or transitioning; do not predict the
   next state.
2. **Momentum** — examine indicator direction and change, not one static overbought/oversold
   threshold. Require agreement across at least two non-identical measures before calling
   momentum aligned.
3. **Volatility** — normalize ATR and channel width by price. Distinguish direction from
   volatility expansion or contraction.
4. **Participation** — compare price changes with amount, volume, turnover, OBV, or MFI.
   Treat price-volume confirmation as descriptive, not proof of investor intent.
5. **Price structure** — identify recent rolling highs/lows and channel boundaries as
   observable zones. Do not present them as guaranteed support, resistance, entry, stop, or
   target prices.
6. **Multi-window check** — show whether short-, medium-, and long-window evidence agrees.
7. **Contradictions** — surface cases such as rising price with weakening momentum, breakout
   without participation, or stronger momentum with expanding downside volatility.

## Output

1. **技术状态摘要** — trend/range/transition, strongest confirmation, strongest contradiction.
2. **多周期证据表** — short/medium/long window, metric, value, direction, and `as_of`.
3. **趋势与动量**
4. **波动与量价结构**
5. **可观察价格区域** — calculation window and method, never a promised level.
6. **失效与风险** — suspension, corporate action, stale EOD data, gap, or indicator conflict.
7. **复现信息** — methods, fields, adjustment convention, windows, and calculations.

Do not convert a golden cross, RSI threshold, MACD crossover, breakout, or any composite
technical score directly into “buy,” “sell,” a target price, or a return forecast. When the
user asks for a trading conclusion, return evidence and scenario conditions only.
