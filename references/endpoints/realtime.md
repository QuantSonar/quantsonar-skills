# realtime — 实时行情快照

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

每只证券的最新盘中快照，交易时段持续刷新；非交易时段返回上一交易日收盘快照。

## SDK 方法

```python
qs.realtime(symbol=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码，逗号分隔可批量（至多 200 个）；不传返回全市场 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `name` | 证券简称 |
| `price` | 最新价 |
| `open` | 今开 |
| `high` | 最高 |
| `low` | 最低 |
| `pre_close` | 昨收 |
| `volume` | 累计成交量（股） |
| `amount` | 累计成交额（元） |
| `trade_time` | 行情时间 |
| `pct_chg` | 涨跌幅（%） |

## 示例

```python
df = qs.realtime(symbol="600519.SH")
print(df.head())
```
