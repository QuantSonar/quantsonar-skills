# southbound_holdings — 南向（港股通）持股明细

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

南向持股明细为 T+1 披露：最新数据滞后一个交易日。

## SDK 方法

```python
qs.southbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（板块/外汇/港股等） |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `trade_date` | 交易日期 |
| `symbol` | 股票代码 |
| `name` | 股票名称 |
| `vol` | 持股数量(股) |
| `ratio` | 持股占比(%) |
| `exchange` | 交易所(SH/SZ) |

## 示例

```python
df = qs.southbound_holdings(symbol="600519.SH")
print(df.head())
```
