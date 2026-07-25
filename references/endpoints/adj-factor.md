# adj_factor — 复权因子

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `symbol` | 股票代码 |
| `trade_date` | 交易日期 |
| `adj_factor` | 复权因子 |

## 示例

```python
df = qs.adj_factor(symbol="600519.SH")
print(df.head())
```
