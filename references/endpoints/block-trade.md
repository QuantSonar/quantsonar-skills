# block_trade — 大宗交易

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.block_trade(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `price` | 成交价 |
| `vol` | 成交量(万股) |
| `amount` | 成交金额 |
| `buyer` | 买方营业部 |
| `seller` | 卖方营业部 |

## 示例

```python
df = qs.block_trade(symbol="600519.SH")
print(df.head())
```
