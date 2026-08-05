# nav — ETF 净值

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.nav(symbol=None, start_date=None, end_date=None, ann_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `ann_date` | 公告日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | ETF代码 |
| `ann_date` | 公告日期 |
| `nav_date` | 净值日期 |
| `unit_nav` | 单位净值 |
| `accum_nav` | 累计净值 |
| `accum_div` | 累计分红 |
| `net_asset` | 资产净值 |
| `total_netasset` | 合计资产净值 |
| `adj_nav` | 复权单位净值 |
| `update_flag` | 更新标志 |

## 示例

```python
df = qs.nav(symbol="600519.SH")
print(df.head())
```
