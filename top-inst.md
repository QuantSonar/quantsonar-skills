# top_inst — 龙虎榜（机构席位）

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.top_inst(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `exalter` | 营业部名称 |
| `buy` | 买入额(元) |
| `buy_rate` | 买入占总成交比例 |
| `sell` | 卖出额(元) |
| `sell_rate` | 卖出占总成交比例 |
| `net_buy` | 净买入额(元) |
| `side` | 买卖方向 |
| `reason` | 上榜理由 |

## 示例

```python
df = qs.top_inst(symbol="600519.SH")
print(df.head())
```
