# top_list — 龙虎榜（个股）

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.top_list(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `close` | 收盘价 |
| `pct_change` | 涨跌幅(%) |
| `turnover_rate` | 换手率(%) |
| `amount` | 龙虎榜成交额(元) |
| `l_sell` | 龙虎榜卖出额(元) |
| `l_buy` | 龙虎榜买入额(元) |
| `l_amount` | 龙虎榜净买入额(元) |

## 示例

```python
df = qs.top_list(symbol="600519.SH")
print(df.head())
```
