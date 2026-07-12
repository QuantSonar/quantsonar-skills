# distribution — 筹码分布与胜率

**所需套餐**：Expert 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.distribution(symbol=None, start_date=None, end_date=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `trade_date` | 交易日期 |
| `his_low` | 历史最低价 |
| `his_high` | 历史最高价 |
| `cost_5pct` | 5分位成本 |
| `cost_15pct` | 15分位成本 |
| `cost_50pct` | 50分位成本 |
| `cost_85pct` | 85分位成本 |
| `cost_95pct` | 95分位成本 |
| `weight_avg` | 加权平均成本 |
| `winner_rate` | 胜率 |

## 示例

```python
df = qs.distribution(symbol="600519.SH")
print(df.head())
```
