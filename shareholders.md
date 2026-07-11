# shareholders — 股东户数

## SDK 方法

```python
qs.shareholders(symbol=None, start_date=None, end_date=None, enddate=None, ann_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `enddate` | 统计截止日 YYYYMMDD |
| `ann_date` | 公告日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 |
| `end_date` | 截止日期 |
| `holder_num` | 股东户数 |

## 示例

```python
df = qs.shareholders(symbol="600519.SH")
print(df.head())
```
