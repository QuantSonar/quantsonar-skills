# daily — 日线行情（OHLC）

**所需套餐**：FREE（免费档即可用）

## SDK 方法

```python
qs.daily(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `open` | 开盘价 |
| `high` | 最高价 |
| `low` | 最低价 |
| `close` | 收盘价 |
| `pre_close` | 昨收价（除权价） |
| `change` | 涨跌额 |
| `pct_chg` | 涨跌幅 |
| `vol` | 成交量（手） |
| `amount` | 成交额（千元） |

## 示例

```python
df = qs.daily(symbol="600519.SH")
print(df.head())
```
