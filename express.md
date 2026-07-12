# express — 业绩快报

**所需套餐**：Starter 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.express(symbol=None, start_date=None, end_date=None, period=None)
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
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 |
| `end_date` | 报告期 |
| `revenue` | 营业收入(元) |
| `operate_profit` | 营业利润(元) |
| `total_profit` | 利润总额(元) |
| `n_income` | 净利润(元) |
| `total_assets` | 总资产(元) |
| `total_hldr_eqy_exc_min_int` | 股东权益(不含少数)(元) |
| `diluted_eps` | 每股收益(摊薄) |
| `diluted_roe` | 净资产收益率(摊薄)(%) |
| `yoy_net_profit` | 去年同期净利润增长率(%) |
| `bps` | 每股净资产(元) |
| `perf_summary` | 业绩简要说明 |
| `update_flag` | 更新标识 |

## 示例

```python
df = qs.express(symbol="600519.SH")
print(df.head())
```
