# forecast — 业绩预告

## SDK 方法

```python
qs.forecast(symbol=None, start_date=None, end_date=None, period=None, type=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `period` | 报告期 YYYYMMDD（如 20251231 = 2025 年报） |
| `type` | 业绩预告类型（预增/预减/扭亏/首亏等） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 |
| `end_date` | 报告期 |
| `type` | 预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减) |
| `p_change_min` | 净利润变动幅度下限(%) |
| `p_change_max` | 净利润变动幅度上限(%) |
| `net_profit_min` | 净利润下限(万元) |
| `net_profit_max` | 净利润上限(万元) |
| `last_parent_net` | 上年同期归母净利润(万元) |
| `first_ann_date` | 首次公告日期 |
| `summary` | 业绩预告摘要 |
| `change_reason` | 业绩变动原因 |

## 示例

```python
df = qs.forecast(symbol="600519.SH")
print(df.head())
```
