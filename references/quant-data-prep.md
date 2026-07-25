# 量化数据准备

Use this workflow to create a reproducible dataset or code path for research, factors,
backtests, or model training.

## Define the dataset contract

Resolve or explicitly default:

- universe and constituent source;
- start/end dates and frequency;
- raw, forward-adjusted, or backward-adjusted prices;
- fields and financial reporting basis;
- point-in-time requirement;
- output shape: long table, wide matrix, DataFrame, CSV, or Parquet;
- acceptable missing-data policy.

Show this contract before producing a large extraction.

## Build

1. Use `trade_calendar` as the calendar backbone.
2. Resolve the universe with `stocks`, `index_weight`, or industry/concept membership.
3. Fetch bounded market data with `daily`; use `adj_factor` only when adjustment is requested.
4. Join valuation and market-cap data from `fundamentals` on symbol and trading date.
5. Add financial data only when requested. Align it by actual announcement availability
   rather than report-end date when point-in-time correctness matters.
6. Preserve raw columns and create transformed columns under new names.
7. Sort by symbol/date and verify uniqueness of the intended primary key.

## Data-quality checks

Report:

- row count, symbol count, min/max dates;
- duplicate primary keys;
- missing rate by required field;
- unexpected date gaps versus trading calendar;
- non-numeric values and unit changes;
- adjustment method;
- look-ahead and survivorship limitations.

Do not forward-fill suspended-day prices. Do not treat suspension as a zero return unless the
chosen backtest convention explicitly defines it.

## Deliver

Provide:

1. **数据契约**
2. **可复现代码** using QuantSonar MCP for small interactive requests or the SDK for bulk
   DataFrame work
3. **字段与主键说明**
4. **质量报告**
5. **已知偏差和适用边界**

Prefer a small verified sample before a large extraction. Never print an API Key in code,
logs, notebooks, or output files; read `QUANTSONAR_TOKEN` from the environment.
