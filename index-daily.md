# index_daily — 指数日线（默认上证综指）

**所需套餐**：FREE（免费档即可用）

## SDK 方法

```python
qs.index_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 指数代码（带后缀），如 000300.SH；缺省 000001.SH |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 指数代码 |
| `trade_date` | 交易日期 YYYYMMDD |
| `close` | 收盘点位 |
| `open` | 开盘点位 |
| `high` | 最高点位 |
| `low` | 最低点位 |
| `pre_close` | 昨日收盘点 |
| `change` | 涨跌点 |
| `pct_chg` | 涨跌幅(%) |
| `vol` | 成交量(手) |
| `amount` | 成交金额(千元) |

## 示例

```python
df = qs.index_daily(symbol="600519.SH")
print(df.head())
```
