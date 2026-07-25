# limit_list — 涨跌停榜单

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.limit_list(symbol=None, start_date=None, end_date=None, limit_type=None, trade_date=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `limit_type` | 涨跌停类型：U 涨停 / D 跌停 / Z 炸板 |
| `trade_date` | 单个交易日 YYYYMMDD（与 start/end 二选一） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `trade_date` | 交易日期 |
| `symbol` | 股票代码 |
| `industry` | 所属行业 |
| `name` | 股票名称 |
| `close` | 收盘价 |
| `pct_chg` | 涨跌幅(%) |
| `amount` | 成交额(千元) |
| `limit_amount` | 板上成交额(千元) |
| `float_mv` | 流通市值(万元) |
| `total_mv` | 总市值(万元) |
| `turnover_ratio` | 换手率(%) |
| `fd_amount` | 封单金额(千元) |
| `first_time` | 首次封板时间 |
| `last_time` | 最后封板时间 |
| `open_times` | 打开次数 |
| `up_stat` | 涨停统计 |
| `limit_times` | 连板天数 |
| `limit` | 涨跌停类型 U涨停 D跌停 Z炸板 |

## 示例

```python
df = qs.limit_list(symbol="600519.SH")
print(df.head())
```
