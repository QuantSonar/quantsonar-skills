# northbound_holdings — 北向持股明细

**所需套餐**：PRO 及以上（低档位调用返回 403）

披露节奏说明：港交所自 2024 年 8 月起不再每日披露北向持股明细，本接口数据为港交所定期披露口径（低频），历史每日数据完整保留。查询建议不带日期或用较宽日期范围。

## SDK 方法

```python
qs.northbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `trade_date` | 交易日期 |
| `symbol` | 股票代码 |
| `name` | 股票名称 |
| `vol` | 持股数量(股) |
| `ratio` | 持股占比(%) |
| `exchange` | 交易所 |

## 示例

```python
df = qs.northbound_holdings(symbol="600519.SH")
print(df.head())
```
