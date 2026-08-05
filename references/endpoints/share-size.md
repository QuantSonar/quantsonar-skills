# share_size — ETF 份额与规模

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.share_size(symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |
| `exchange` | 交易所：SSE 上交所 / SZSE 深交所 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `trade_date` | 交易日期 |
| `symbol` | ETF代码 |
| `etf_name` | 基金名称 |
| `total_share` | 总份额(万份) |
| `total_size` | 总规模(万元) |
| `nav` | 份额净值 |
| `close` | 收盘价 |
| `exchange` | SSE/SZSE/BSE |

## 示例

```python
df = qs.share_size(symbol="600519.SH")
print(df.head())
```
