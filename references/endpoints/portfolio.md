# portfolio — ETF 持仓明细

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.portfolio(symbol=None, con_symbol=None, start_date=None, end_date=None, ann_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `con_symbol` | 成分证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `ann_date` | 公告日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | ETF代码 |
| `ann_date` | 公告日期 |
| `end_date` | 报告期 |
| `con_symbol` | 持仓证券代码 |
| `mkv` | 持仓市值(元) |
| `amount` | 持仓数量(股) |
| `stk_mkv_ratio` | 占股票市值比 |
| `stk_float_ratio` | 占流通股本比例 |

## 示例

```python
df = qs.portfolio(symbol="600519.SH")
print(df.head())
```
