# basic — ETF 基础信息

**所需套餐**：FREE（免费档即可用）

## SDK 方法

```python
qs.basic(symbol=None, exchange=None, list_status=None, etf_type=None, index_code=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `symbol` | 代码原样匹配（ETF/板块/外汇/港股等） |
| `exchange` | 交易所：SSE 上交所 / SZSE 深交所 |
| `list_status` | 上市状态：L 上市 / D 退市 / P 暂停上市 |
| `etf_type` | ETF 类型，如境内、QDII |
| `index_code` | 跟踪指数代码（带后缀） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `symbol` | ETF代码 |
| `csname` | ETF中文简称 |
| `extname` | ETF扩位简称 |
| `cname` | 基金中文全称 |
| `index_code` | 跟踪指数代码 |
| `index_name` | 跟踪指数名称 |
| `setup_date` | 设立日期 |
| `list_date` | 上市日期 |
| `list_status` | L上市/D退市/P待上市 |
| `exchange` | SH/SZ |
| `mgr_name` | 基金管理人 |
| `custod_name` | 基金托管人 |
| `mgt_fee` | 管理费率 |
| `etf_type` | 境内/QDII等类型 |

## 示例

```python
df = qs.basic(symbol="600519.SH")
print(df.head())
```
