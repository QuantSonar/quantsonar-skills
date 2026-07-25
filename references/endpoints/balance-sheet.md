# balance_sheet — 资产负债表

**所需套餐**：Starter 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.balance_sheet(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, report_type=None, comp_type=None)
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
| `total_cur_assets` | 流动资产合计 |
| `money_cap` | 货币资金 |
| `notes_receiv` | 应收票据 |
| `accounts_receiv` | 应收账款 |
| `inventories` | 存货 |
| `total_nca` | 非流动资产合计 |
| `fa_avail_for_sale` | 可供出售金融资产 |
| `lt_eqt_invest` | 长期股权投资 |
| `fix_assets` | 固定资产 |
| `cip` | 在建工程 |
| `intan_assets` | 无形资产 |
| `goodwill` | 商誉 |
| `total_assets` | 资产总计 |
| `total_cur_liab` | 流动负债合计 |
| `st_borr` | 短期借款 |
| `notes_payable` | 应付票据 |
| `acct_payable` | 应付账款 |
| `total_ncl` | 非流动负债合计 |
| `lt_borr` | 长期借款 |
| `bond_payable` | 应付债券 |
| `total_liab` | 负债合计 |
| `total_hldr_eqy_exc_min_int` | 股东权益(不含少数) |
| `total_hldr_eqy_inc_min_int` | 股东权益(含少数) |
| `minority_int` | 少数股东权益 |
| `update_flag` | 更新标识 |

## 示例

```python
df = qs.balance_sheet(symbol="600519.SH")
print(df.head())
```
