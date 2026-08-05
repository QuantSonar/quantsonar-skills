# tracking_indices — ETF 跟踪指数基础信息

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.tracking_indices(symbol=None, start_date=None, end_date=None, pub_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `pub_date` | 发布日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 指数代码 |
| `indx_name` | 指数全称 |
| `indx_csname` | 指数简称 |
| `pub_party_name` | 发布机构 |
| `pub_date` | 发布日期 |
| `base_date` | 基日 |
| `bp` | 基点 |
| `adj_circle` | 成分调整周期 |

## 示例

```python
df = qs.tracking_indices(symbol="600519.SH")
print(df.head())
```
