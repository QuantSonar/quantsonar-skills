# industries — 申万行业分类

**所需套餐**：FREE（免费档即可用）

## SDK 方法

```python
qs.industries(symbol=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `name` | 股票名称 |
| `l1_code` | 一级行业代码 |
| `l1_name` | 一级行业名称 |
| `l2_code` | 二级行业代码 |
| `l2_name` | 二级行业名称 |
| `l3_code` | 三级行业代码 |
| `l3_name` | 三级行业名称 |

## 示例

```python
df = qs.industries(symbol="600519.SH")
print(df.head())
```
