# disclosure_date — 财报披露日历

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.disclosure_date(symbol=None, start_date=None, end_date=None, pre_date=None, actual_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `pre_date` | 预计披露日 YYYYMMDD |
| `actual_date` | 实际披露日 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `ann_date` | 首次公告日 |
| `end_date` | 报告期 |
| `pre_date` | 预披露日期 |
| `actual_date` | 实际披露日期 |
| `modify_date` | 更正日期 |

## 示例

```python
df = qs.disclosure_date(symbol="600519.SH")
print(df.head())
```
