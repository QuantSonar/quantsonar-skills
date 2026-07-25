# holder_trade — 重要股东增减持

**所需套餐**：PRO 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.holder_trade(symbol=None, start_date=None, end_date=None, trade_type=None, holder_type=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `trade_type` | 增减持方向：IN 增持 / DE 减持 |
| `holder_type` | 股东类型：G 高管 / P 个人 / C 公司 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 证券代码（带交易所后缀） |
| `ann_date` | 公告日期 |
| `holder_name` | 股东名称 |
| `holder_type` | 股东类型(G高管/P个人/C公司) |
| `in_de` | 增减持(IN增持/DE减持) |
| `change_vol` | 变动数量 |
| `change_ratio` | 占流通比例(%) |
| `after_share` | 变动后持股 |
| `after_ratio` | 变动后占流通比例(%) |
| `avg_price` | 平均价格 |
| `total_share` | 持股总数 |
| `begin_date` | 增减持开始日期 |
| `close_date` | 增减持结束日期 |

## 示例

```python
df = qs.holder_trade(symbol="600519.SH")
print(df.head())
```
