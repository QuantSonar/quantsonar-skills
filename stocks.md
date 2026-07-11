# stocks — 股票列表

## SDK 方法

```python
qs.stocks(symbol=None, name=None, market=None, list_status=None, exchange=None, is_hs=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 证券代码（带后缀），如 000001.SZ |
| `name` | 名称精确匹配 |
| `market` | 市场类别（主板/创业板/科创板/北交所） |
| `list_status` | 上市状态：L 上市 / D 退市 / P 暂停上市 |
| `exchange` | 交易所：SSE 上交所 / SZSE 深交所 |
| `is_hs` | 是否沪深港通标的：N 否 / H 沪股通 / S 深股通 |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | 股票代码 |
| `symbol` | 股票简称 |
| `name` | 股票名称 |
| `area` | 地域 |
| `industry` | 所属行业 |
| `fullname` | 股票全称 |
| `enname` | 英文名称 |
| `cnspell` | 拼音缩写 |
| `market` | 市场类型 |
| `exchange` | 交易所 |
| `curr_type` | 货币类型 |
| `list_status` | 上市状态 |
| `list_date` | 上市日期 |
| `delist_date` | 退市日期 |
| `is_hs` | 是否沪深港通标的 |

## 示例

```python
df = qs.stocks(symbol="600519.SH")
print(df.head())
```
