# fx_daily — 外汇日线（默认 USDCNH）

**所需套餐**：FREE（免费档即可用）

## SDK 方法

```python
qs.fx_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（板块/外汇/港股等）；缺省 USDCNH.FXCM |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 外汇代码 |
| `trade_date` | 交易日期 YYYYMMDD |
| `bid_open` | 买入开盘价 |
| `bid_close` | 买入收盘价 |
| `bid_high` | 买入最高价 |
| `bid_low` | 买入最低价 |
| `ask_open` | 卖出开盘价 |
| `ask_close` | 卖出收盘价 |
| `ask_high` | 卖出最高价 |
| `ask_low` | 卖出最低价 |
| `tick_qty` | 报价笔数 |

## 示例

```python
df = qs.fx_daily(symbol="600519.SH")
print(df.head())
```
