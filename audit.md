# audit — 财务审计意见

## SDK 方法

```python
qs.audit(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `period` | 报告期 YYYYMMDD（如 20251231 = 2025 年报） |
| `ann_date` | 公告日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `ann_date` | 公告日期 |
| `end_date` | 报告期 |
| `audit_result` | 审计结果 |
| `audit_fees` | 审计总费用(元) |
| `audit_agency` | 会计事务所 |
| `audit_sign` | 签字会计师 |

## 示例

```python
df = qs.audit(symbol="600519.SH")
print(df.head())
```
