# fundamentals — 每日指标（PE/PB/换手率/市值）

**所需套餐**：Starter 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.fundamentals(symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `trade_date` | 交易日期 |
| `close` | 当日收盘价 |
| `turnover_rate` | 换手率（%） |
| `turnover_rate_f` | 换手率（自由流通股，%） |
| `volume_ratio` | 量比 |
| `pe` | 市盈率（总市值/净利润） |
| `pe_ttm` | 市盈率TTM |
| `pb` | 市净率（总市值/净资产） |
| `ps` | 市销率 |
| `ps_ttm` | 市销率TTM |
| `dv_ratio` | 股息率（%） |
| `dv_ttm` | 股息率TTM（%） |
| `total_share` | 总股本（万股） |
| `float_share` | 流通股本（万股） |
| `free_share` | 自由流通股本（万股） |
| `total_mv` | 总市值（万元） |
| `circ_mv` | 流通市值（万元） |

## 示例

```python
df = qs.fundamentals(symbol="600519.SH")
print(df.head())
```
