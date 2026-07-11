# trade_calendar — 交易日历（默认上交所）

## SDK 方法

```python
qs.trade_calendar(start_date=None, end_date=None, exchange=None, is_open=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `exchange` | 交易所：SSE 上交所 / SZSE 深交所 |
| `is_open` | 是否交易日：1 是 / 0 否 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `exchange` | 交易所代码 |
| `cal_date` | 日历日期 |
| `is_open` | 是否交易 0休市 1交易 |
| `pretrade_date` | 上一交易日 |

## 示例

```python
df = qs.trade_calendar()
print(df.head())
```
