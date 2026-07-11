# cash_flow — 现金流量表

## SDK 方法

```python
qs.cash_flow(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)
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
| `f_ann_date` | 实际公告日期 YYYYMMDD |
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
| `net_profit` | 净利润 |
| `c_fr_sale_sg` | 销售商品收到的现金 |
| `c_pay_goods_purch_serv_rec` | 购买商品支付的现金 |
| `n_cashflow_act` | 经营活动现金流量净额 |
| `c_pay_acq_const_fix_intang_oasset` | 购建固定/无形资产支付的现金 |
| `c_fr_disp_fix_intang_oasset` | 处置固定/无形资产收到的现金 |
| `n_cashflow_inv_act` | 投资活动现金流量净额 |
| `c_fr_borr` | 取得借款收到的现金 |
| `c_pay_dist_dpcp_int_exp` | 分配股利/偿付利息支付的现金 |
| `n_cash_flows_fnc_act` | 筹资活动现金流量净额 |
| `n_incr_cash_cash_equ` | 现金及等价物净增加额 |
| `c_cash_equ_beg_period` | 期初现金及等价物余额 |
| `c_cash_equ_end_period` | 期末现金及等价物余额 |
| `free_cashflow` | 企业自由现金流量 |
| `update_flag` | 更新标识 |

## 示例

```python
df = qs.cash_flow(symbol="600519.SH")
print(df.head())
```
