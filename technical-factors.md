# technical_factors — 技术面因子

**所需套餐**：PRO 及以上（低档位调用返回 403）

## SDK 方法

```python
qs.technical_factors(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `trade_date` | 交易日期 YYYYMMDD |
| `open_hfq` | 开盘价(后复权) |
| `close_hfq` | 收盘价(后复权) |
| `high_hfq` | 最高价(后复权) |
| `low_hfq` | 最低价(后复权) |
| `pre_close_hfq` | 昨收价(后复权) |
| `open_qfq` | 开盘价(前复权) |
| `close_qfq` | 收盘价(前复权) |
| `high_qfq` | 最高价(前复权) |
| `low_qfq` | 最低价(前复权) |
| `pre_close_qfq` | 昨收价(前复权) |
| `adj_factor` | 复权因子 |
| `macd_dif` | MACD_DIF |
| `macd_dea` | MACD_DEA |
| `macd` | MACD |
| `kdj_k` | KDJ_K |
| `kdj_d` | KDJ_D |
| `kdj_j` | KDJ_J |
| `rsi_6` | RSI_6 |
| `rsi_12` | RSI_12 |
| `rsi_24` | RSI_24 |
| `boll_upper` | BOLL上轨 |
| `boll_mid` | BOLL中轨 |
| `boll_lower` | BOLL下轨 |
| `cci` | CCI |

## 示例

```python
df = qs.technical_factors(symbol="600519.SH")
print(df.head())
```
