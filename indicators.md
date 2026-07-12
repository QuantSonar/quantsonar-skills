# indicators — 财务指标

**所需套餐**：Starter 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.indicators(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)
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
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 YYYYMMDD |
| `end_date` | 报告期 |
| `eps` | 基本每股收益（元） |
| `dt_eps` | 稀释每股收益（元） |
| `total_revenue_ps` | 每股营业总收入（元） |
| `revenue_ps` | 每股营业收入（元） |
| `bps` | 每股净资产（元） |
| `ocfps` | 每股经营现金流（元） |
| `roe` | 净资产收益率（%） |
| `roe_waa` | 加权平均净资产收益率（%） |
| `roe_dt` | 扣非净资产收益率（%） |
| `roa` | 总资产报酬率（%） |
| `gross_margin` | 毛利（万元） |
| `netprofit_margin` | 销售净利率（%） |
| `grossprofit_margin` | 销售毛利率（%） |
| `debt_to_assets` | 资产负债率（%） |
| `current_ratio` | 流动比率 |
| `quick_ratio` | 速动比率 |
| `cash_ratio` | 保守速动比率 |
| `assets_turn` | 总资产周转率 |
| `inv_turn` | 存货周转率 |
| `ar_turn` | 应收账款周转率 |
| `roic` | 投入资本回报率（%） |
| `basic_eps_yoy` | 基本每股收益同比增长（%） |
| `dt_eps_yoy` | 稀释每股收益同比增长（%） |
| `netprofit_yoy` | 归母净利润同比增长（%） |
| `dt_netprofit_yoy` | 扣非净利润同比增长（%） |
| `rd_exp` | 研发费用（万元） |

## 示例

```python
df = qs.indicators(symbol="600519.SH")
print(df.head())
```
