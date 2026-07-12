# analyst_reports — 券商研报盈利预测

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.analyst_reports(symbol=None, start_date=None, end_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `name` | 股票名称 |
| `report_date` | 研报日期 |
| `report_title` | 报告标题 |
| `report_type` | 报告类型 |
| `classify` | 报告分类 |
| `org_name` | 机构名称 |
| `author_name` | 作者 |
| `quarter` | 预测季度 |
| `op_rt` | 营业收入预测(万元) |
| `op_pr` | 营业利润预测(万元) |
| `tp` | 利润总额预测(万元) |
| `np` | 净利润预测(万元) |
| `eps` | 每股收益预测(元) |
| `pe` | 市盈率预测 |
| `rd` | 股息率预测 |
| `roe` | 净资产收益率预测 |
| `ev_ebitda` | EV/EBITDA预测 |
| `rating` | 评级(买入/增持/中性/减持/卖出) |
| `max_price` | 最高目标价 |
| `min_price` | 最低目标价 |
| `imp_dg` | 关注度 |
| `create_time` | 数据更新时间 |

## 示例

```python
df = qs.analyst_reports(symbol="600519.SH")
print(df.head())
```
