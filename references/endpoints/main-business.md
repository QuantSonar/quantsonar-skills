# main_business — 主营业务构成

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.main_business(symbol=None, start_date=None, end_date=None, period=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `period` | 报告期 YYYYMMDD（如 20251231 = 2025 年报） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `end_date` | 报告期 |
| `bz_item` | 主营业务项目 |
| `bz_sales` | 主营业务收入(元) |
| `bz_profit` | 主营业务利润(元) |
| `bz_cost` | 主营业务成本(元) |
| `curr_type` | 货币代码 |

## 示例

```python
df = qs.main_business(symbol="600519.SH")
print(df.head())
```
