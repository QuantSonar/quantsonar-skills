# margin — 融资融券明细

## SDK 方法

```python
qs.margin(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `symbol` | 证券代码（带交易所后缀） |
| `name` | 股票名称 |
| `rzye` | 融资余额(元) |
| `rqye` | 融券余额(元) |
| `rzmre` | 融资买入额(元) |
| `rqyl` | 融券余量(股) |
| `rzche` | 融资偿还额(元) |
| `rqchl` | 融券偿还量(股) |
| `rqmcl` | 融券卖出量(股) |
| `rzrqye` | 融资融券余额(元) |

## 示例

```python
df = qs.margin(symbol="600519.SH")
print(df.head())
```
