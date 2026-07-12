# income — 利润表

**所需套餐**：Starter 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.income(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)
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
| `f_ann_date` | 实际公告日期 YYYYMMDD |
| `report_type` | 报表类型：1 合并报表 / 6 母公司报表 … |
| `comp_type` | 公司类型（1 一般工商业 / 2 银行 / 3 保险 / 4 证券） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 |
| `f_ann_date` | 实际公告日期 |
| `end_date` | 报告期 |
| `report_type` | 报告类型 |
| `comp_type` | 公司类型 |
| `basic_eps` | 基本每股收益 |
| `diluted_eps` | 稀释每股收益 |
| `total_revenue` | 营业总收入 |
| `revenue` | 营业收入 |
| `total_cogs` | 营业总成本 |
| `oper_cost` | 营业成本 |
| `sell_exp` | 销售费用 |
| `admin_exp` | 管理费用 |
| `fin_exp` | 财务费用 |
| `rd_exp` | 研发费用 |
| `operate_profit` | 营业利润 |
| `non_oper_income` | 营业外收入 |
| `non_oper_exp` | 营业外支出 |
| `total_profit` | 利润总额 |
| `income_tax` | 所得税费用 |
| `n_income` | 净利润(含少数股东) |
| `n_income_attr_p` | 净利润(归母) |
| `ebit` | 息税前利润 |
| `ebitda` | 息税折旧摊销前利润 |
| `update_flag` | 更新标识 |

## 示例

```python
df = qs.income(symbol="600519.SH")
print(df.head())
```
