# moneyflow_hsgt — 沪深港通资金流向（全市场）

## SDK 方法

```python
qs.moneyflow_hsgt(start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `trade_date` | 交易日期 YYYYMMDD |
| `ggt_ss` | 港股通（上海） |
| `ggt_sz` | 港股通（深圳） |
| `hgt_ss` | 沪股通（上海） |
| `hgt_sz` | 深股通（深圳） |
| `north_money` | 北向资金 |
| `south_money` | 南向资金 |

## 示例

```python
df = qs.moneyflow_hsgt()
print(df.head())
```
