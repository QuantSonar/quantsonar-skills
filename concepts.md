# concepts — 概念/题材板块指数

## SDK 方法

```python
qs.concepts(symbol=None, start_date=None, end_date=None, trade_date=None, name=None, idx_type=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（板块/外汇/港股等） |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |
| `name` | 名称精确匹配 |
| `idx_type` | 板块类型 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 概念代码 |
| `trade_date` | 交易日期 |
| `name` | 概念名称 |
| `leading` | 领涨股票名称 |
| `leading_code` | 领涨股票代码 |
| `pct_change` | 涨跌幅 |
| `leading_pct` | 领涨股票涨跌幅 |
| `total_mv` | 总市值(万元) |
| `turnover_rate` | 换手率 |
| `up_num` | 上涨家数 |
| `down_num` | 下降家数 |
| `idx_type` | 板块类型 |
| `level` | 行业层级 |

## 示例

```python
df = qs.concepts(symbol="600519.SH")
print(df.head())
```
