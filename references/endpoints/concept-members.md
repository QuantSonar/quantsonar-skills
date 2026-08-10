# concept_members — 概念/题材板块成分股

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.concept_members(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 类型 | 说明 |
|---|---|---|
| `symbol` | `string` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `con_symbol` | `string` | 成分证券代码（带后缀），如 000001.SZ |
| `start_date` | `string` | 起始日期 YYYYMMDD |
| `end_date` | `string` | 结束日期 YYYYMMDD |
| `trade_date` | `string` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `trade_date` | 交易日期 |
| `symbol` | 概念代码 |
| `con_symbol` | 成分股代码 |
| `name` | 成分股名称 |

## 示例

```python
df = qs.concept_members(symbol='BK0425.DC', con_symbol='600519.SH')
print(df.head())
```
