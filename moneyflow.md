# moneyflow — 个股资金流向

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.moneyflow(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `buy_sm_vol` | 小单买入量(手) |
| `buy_sm_amount` | 小单买入金额(万元) |
| `sell_sm_vol` | 小单卖出量(手) |
| `sell_sm_amount` | 小单卖出金额(万元) |
| `buy_md_vol` | 中单买入量(手) |
| `buy_md_amount` | 中单买入金额(万元) |
| `sell_md_vol` | 中单卖出量(手) |
| `sell_md_amount` | 中单卖出金额(万元) |
| `buy_lg_vol` | 大单买入量(手) |
| `buy_lg_amount` | 大单买入金额(万元) |
| `sell_lg_vol` | 大单卖出量(手) |
| `sell_lg_amount` | 大单卖出金额(万元) |
| `buy_elg_vol` | 特大单买入量(手) |
| `buy_elg_amount` | 特大单买入金额(万元) |
| `sell_elg_vol` | 特大单卖出量(手) |
| `sell_elg_amount` | 特大单卖出金额(万元) |
| `net_mf_vol` | 净流入量(手) |
| `net_mf_amount` | 净流入额(万元) |

## 示例

```python
df = qs.moneyflow(symbol="600519.SH")
print(df.head())
```
