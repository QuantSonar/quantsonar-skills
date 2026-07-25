# dividend — 分红送股

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.dividend(symbol=None, start_date=None, end_date=None, record_date=None, ex_date=None, imp_ann_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `record_date` | 股权登记日 YYYYMMDD |
| `ex_date` | 除权除息日 YYYYMMDD |
| `imp_ann_date` | 实施公告日 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `end_date` | 分红年度 |
| `ann_date` | 预案公告日 |
| `div_proc` | 实施进度 |
| `stk_div` | 每股送转 |
| `stk_bo_rate` | 每股送股比例 |
| `stk_co_rate` | 每股转增比例 |
| `cash_div` | 每股分红(税前)(元) |
| `cash_div_tax` | 每股分红(税后)(元) |
| `record_date` | 股权登记日 |
| `ex_date` | 除权除息日 |
| `pay_date` | 派息日 |
| `div_listdate` | 红股上市日 |
| `imp_ann_date` | 实施公告日 |

## 示例

```python
df = qs.dividend(symbol="600519.SH")
print(df.head())
```
