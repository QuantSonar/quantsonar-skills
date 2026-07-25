# technical_factors_pro — 技术面因子（专业版，含复权价+技术指标）

**所需套餐**：Expert 及以上（低档位每天可试用 2 次）

## SDK 方法

```python
qs.technical_factors_pro(symbol=None, start_date=None, end_date=None, trade_date=None)
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
| `open` | 开盘价 |
| `open_hfq` | 开盘价（后复权） |
| `open_qfq` | 开盘价（前复权） |
| `high` | 最高价 |
| `high_hfq` | 最高价（后复权） |
| `high_qfq` | 最高价（前复权） |
| `low` | 最低价 |
| `low_hfq` | 最低价（后复权） |
| `low_qfq` | 最低价（前复权） |
| `close` | 收盘价 |
| `close_hfq` | 收盘价（后复权） |
| `close_qfq` | 收盘价（前复权） |
| `pre_close` | 昨收价 |
| `change` | 涨跌额 |
| `pct_chg` | 涨跌幅（%） |
| `vol` | 成交量（手） |
| `amount` | 成交额（千元） |
| `turnover_rate` | 换手率（%） |
| `turnover_rate_f` | 换手率（自由流通股，%） |
| `volume_ratio` | 量比 |
| `pe` | 市盈率（总市值/净利润） |
| `pe_ttm` | 市盈率 TTM |
| `pb` | 市净率（总市值/净资产） |
| `ps` | 市销率 |
| `ps_ttm` | 市销率 TTM |
| `dv_ratio` | 股息率（%） |
| `dv_ttm` | 股息率 TTM（%） |
| `total_share` | 总股本（万股） |
| `float_share` | 流通股本（万股） |
| `free_share` | 自由流通股本（万股） |
| `total_mv` | 总市值（万元） |
| `circ_mv` | 流通市值（万元） |
| `adj_factor` | 复权因子（后复权价 = 收盘价 × 复权因子） |
| `asi_bfq` | 振动升降指标 ASI（不复权） |
| `asi_hfq` | 振动升降指标 ASI（后复权） |
| `asi_qfq` | 振动升降指标 ASI（前复权） |
| `asit_bfq` | ASI 移动平均 ASIT（不复权） |
| `asit_hfq` | ASI 移动平均 ASIT（后复权） |
| `asit_qfq` | ASI 移动平均 ASIT（前复权） |
| `atr_bfq` | 真实波幅 ATR（不复权） |
| `atr_hfq` | 真实波幅 ATR（后复权） |
| `atr_qfq` | 真实波幅 ATR（前复权） |
| `bbi_bfq` | 多空指数 BBI（不复权） |
| `bbi_hfq` | 多空指数 BBI（后复权） |
| `bbi_qfq` | 多空指数 BBI（前复权） |
| `bias1_bfq` | 乖离率 BIAS（6 日）（不复权） |
| `bias1_hfq` | 乖离率 BIAS（6 日）（后复权） |
| `bias1_qfq` | 乖离率 BIAS（6 日）（前复权） |
| `bias2_bfq` | 乖离率 BIAS（12 日）（不复权） |
| `bias2_hfq` | 乖离率 BIAS（12 日）（后复权） |
| `bias2_qfq` | 乖离率 BIAS（12 日）（前复权） |
| `bias3_bfq` | 乖离率 BIAS（24 日）（不复权） |
| `bias3_hfq` | 乖离率 BIAS（24 日）（后复权） |
| `bias3_qfq` | 乖离率 BIAS（24 日）（前复权） |
| `boll_lower_bfq` | 布林带下轨（不复权） |
| `boll_lower_hfq` | 布林带下轨（后复权） |
| `boll_lower_qfq` | 布林带下轨（前复权） |
| `boll_mid_bfq` | 布林带中轨（不复权） |
| `boll_mid_hfq` | 布林带中轨（后复权） |
| `boll_mid_qfq` | 布林带中轨（前复权） |
| `boll_upper_bfq` | 布林带上轨（不复权） |
| `boll_upper_hfq` | 布林带上轨（后复权） |
| `boll_upper_qfq` | 布林带上轨（前复权） |
| `brar_ar_bfq` | 人气指标 AR（不复权） |
| `brar_ar_hfq` | 人气指标 AR（后复权） |
| `brar_ar_qfq` | 人气指标 AR（前复权） |
| `brar_br_bfq` | 买卖意愿指标 BR（不复权） |
| `brar_br_hfq` | 买卖意愿指标 BR（后复权） |
| `brar_br_qfq` | 买卖意愿指标 BR（前复权） |
| `cci_bfq` | 顺势指标 CCI（不复权） |
| `cci_hfq` | 顺势指标 CCI（后复权） |
| `cci_qfq` | 顺势指标 CCI（前复权） |
| `cr_bfq` | 价格动量指标 CR（不复权） |
| `cr_hfq` | 价格动量指标 CR（后复权） |
| `cr_qfq` | 价格动量指标 CR（前复权） |
| `dfma_dif_bfq` | 平行线差指标 DMA 的 DIF（不复权） |
| `dfma_dif_hfq` | 平行线差指标 DMA 的 DIF（后复权） |
| `dfma_dif_qfq` | 平行线差指标 DMA 的 DIF（前复权） |
| `dfma_difma_bfq` | 平行线差指标 DMA 的 DIFMA（不复权） |
| `dfma_difma_hfq` | 平行线差指标 DMA 的 DIFMA（后复权） |
| `dfma_difma_qfq` | 平行线差指标 DMA 的 DIFMA（前复权） |
| `dmi_adx_bfq` | 平均趋向指标 ADX（不复权） |
| `dmi_adx_hfq` | 平均趋向指标 ADX（后复权） |
| `dmi_adx_qfq` | 平均趋向指标 ADX（前复权） |
| `dmi_adxr_bfq` | 趋向评估指标 ADXR（不复权） |
| `dmi_adxr_hfq` | 趋向评估指标 ADXR（后复权） |
| `dmi_adxr_qfq` | 趋向评估指标 ADXR（前复权） |
| `dmi_mdi_bfq` | 趋向指标下降方向线 -DI（不复权） |
| `dmi_mdi_hfq` | 趋向指标下降方向线 -DI（后复权） |
| `dmi_mdi_qfq` | 趋向指标下降方向线 -DI（前复权） |
| `dmi_pdi_bfq` | 趋向指标上升方向线 +DI（不复权） |
| `dmi_pdi_hfq` | 趋向指标上升方向线 +DI（后复权） |
| `dmi_pdi_qfq` | 趋向指标上升方向线 +DI（前复权） |
| `downdays` | 连跌天数 |
| `updays` | 连涨天数 |
| `dpo_bfq` | 区间震荡线 DPO（不复权） |
| `dpo_hfq` | 区间震荡线 DPO（后复权） |
| `dpo_qfq` | 区间震荡线 DPO（前复权） |
| `madpo_bfq` | DPO 移动平均 MADPO（不复权） |
| `madpo_hfq` | DPO 移动平均 MADPO（后复权） |
| `madpo_qfq` | DPO 移动平均 MADPO（前复权） |
| `ema_bfq_10` | 指数移动平均 EMA（10 日）（不复权） |
| `ema_bfq_20` | 指数移动平均 EMA（20 日）（不复权） |
| `ema_bfq_250` | 指数移动平均 EMA（250 日）（不复权） |
| `ema_bfq_30` | 指数移动平均 EMA（30 日）（不复权） |
| `ema_bfq_5` | 指数移动平均 EMA（5 日）（不复权） |
| `ema_bfq_60` | 指数移动平均 EMA（60 日）（不复权） |
| `ema_bfq_90` | 指数移动平均 EMA（90 日）（不复权） |
| `ema_hfq_10` | 指数移动平均 EMA（10 日）（后复权） |
| `ema_hfq_20` | 指数移动平均 EMA（20 日）（后复权） |
| `ema_hfq_250` | 指数移动平均 EMA（250 日）（后复权） |
| `ema_hfq_30` | 指数移动平均 EMA（30 日）（后复权） |
| `ema_hfq_5` | 指数移动平均 EMA（5 日）（后复权） |
| `ema_hfq_60` | 指数移动平均 EMA（60 日）（后复权） |
| `ema_hfq_90` | 指数移动平均 EMA（90 日）（后复权） |
| `ema_qfq_10` | 指数移动平均 EMA（10 日）（前复权） |
| `ema_qfq_20` | 指数移动平均 EMA（20 日）（前复权） |
| `ema_qfq_250` | 指数移动平均 EMA（250 日）（前复权） |
| `ema_qfq_30` | 指数移动平均 EMA（30 日）（前复权） |
| `ema_qfq_5` | 指数移动平均 EMA（5 日）（前复权） |
| `ema_qfq_60` | 指数移动平均 EMA（60 日）（前复权） |
| `ema_qfq_90` | 指数移动平均 EMA（90 日）（前复权） |
| `emv_bfq` | 简易波动指标 EMV（不复权） |
| `emv_hfq` | 简易波动指标 EMV（后复权） |
| `emv_qfq` | 简易波动指标 EMV（前复权） |
| `maemv_bfq` | EMV 移动平均 MAEMV（不复权） |
| `maemv_hfq` | EMV 移动平均 MAEMV（后复权） |
| `maemv_qfq` | EMV 移动平均 MAEMV（前复权） |
| `expma_12_bfq` | 指数平滑移动平均 EXPMA（12 日）（不复权） |
| `expma_12_hfq` | 指数平滑移动平均 EXPMA（12 日）（后复权） |
| `expma_12_qfq` | 指数平滑移动平均 EXPMA（12 日）（前复权） |
| `expma_50_bfq` | 指数平滑移动平均 EXPMA（50 日）（不复权） |
| `expma_50_hfq` | 指数平滑移动平均 EXPMA（50 日）（后复权） |
| `expma_50_qfq` | 指数平滑移动平均 EXPMA（50 日）（前复权） |
| `kdj_bfq` | KDJ 随机指标 J 值（不复权） |
| `kdj_hfq` | KDJ 随机指标 J 值（后复权） |
| `kdj_qfq` | KDJ 随机指标 J 值（前复权） |
| `kdj_d_bfq` | KDJ D 值（不复权） |
| `kdj_d_hfq` | KDJ D 值（后复权） |
| `kdj_d_qfq` | KDJ D 值（前复权） |
| `kdj_k_bfq` | KDJ K 值（不复权） |
| `kdj_k_hfq` | KDJ K 值（后复权） |
| `kdj_k_qfq` | KDJ K 值（前复权） |
| `ktn_down_bfq` | 肯特纳通道下轨（不复权） |
| `ktn_down_hfq` | 肯特纳通道下轨（后复权） |
| `ktn_down_qfq` | 肯特纳通道下轨（前复权） |
| `ktn_mid_bfq` | 肯特纳通道中轨（不复权） |
| `ktn_mid_hfq` | 肯特纳通道中轨（后复权） |
| `ktn_mid_qfq` | 肯特纳通道中轨（前复权） |
| `ktn_upper_bfq` | 肯特纳通道上轨（不复权） |
| `ktn_upper_hfq` | 肯特纳通道上轨（后复权） |
| `ktn_upper_qfq` | 肯特纳通道上轨（前复权） |
| `lowdays` | 创新低天数（250 日窗口） |
| `topdays` | 创新高天数（250 日窗口） |
| `ma_bfq_10` | 简单均线 MA（10 日）（不复权） |
| `ma_bfq_20` | 简单均线 MA（20 日）（不复权） |
| `ma_bfq_250` | 简单均线 MA（250 日）（不复权） |
| `ma_bfq_30` | 简单均线 MA（30 日）（不复权） |
| `ma_bfq_5` | 简单均线 MA（5 日）（不复权） |
| `ma_bfq_60` | 简单均线 MA（60 日）（不复权） |
| `ma_bfq_90` | 简单均线 MA（90 日）（不复权） |
| `ma_hfq_10` | 简单均线 MA（10 日）（后复权） |
| `ma_hfq_20` | 简单均线 MA（20 日）（后复权） |
| `ma_hfq_250` | 简单均线 MA（250 日）（后复权） |
| `ma_hfq_30` | 简单均线 MA（30 日）（后复权） |
| `ma_hfq_5` | 简单均线 MA（5 日）（后复权） |
| `ma_hfq_60` | 简单均线 MA（60 日）（后复权） |
| `ma_hfq_90` | 简单均线 MA（90 日）（后复权） |
| `ma_qfq_10` | 简单均线 MA（10 日）（前复权） |
| `ma_qfq_20` | 简单均线 MA（20 日）（前复权） |
| `ma_qfq_250` | 简单均线 MA（250 日）（前复权） |
| `ma_qfq_30` | 简单均线 MA（30 日）（前复权） |
| `ma_qfq_5` | 简单均线 MA（5 日）（前复权） |
| `ma_qfq_60` | 简单均线 MA（60 日）（前复权） |
| `ma_qfq_90` | 简单均线 MA（90 日）（前复权） |
| `macd_bfq` | MACD 柱（不复权） |
| `macd_hfq` | MACD 柱（后复权） |
| `macd_qfq` | MACD 柱（前复权） |
| `macd_dea_bfq` | MACD 慢线 DEA（不复权） |
| `macd_dea_hfq` | MACD 慢线 DEA（后复权） |
| `macd_dea_qfq` | MACD 慢线 DEA（前复权） |
| `macd_dif_bfq` | MACD 快线 DIF（不复权） |
| `macd_dif_hfq` | MACD 快线 DIF（后复权） |
| `macd_dif_qfq` | MACD 快线 DIF（前复权） |
| `mass_bfq` | 梅斯线 MASS（不复权） |
| `mass_hfq` | 梅斯线 MASS（后复权） |
| `mass_qfq` | 梅斯线 MASS（前复权） |
| `ma_mass_bfq` | MASS 移动平均（不复权） |
| `ma_mass_hfq` | MASS 移动平均（后复权） |
| `ma_mass_qfq` | MASS 移动平均（前复权） |
| `mfi_bfq` | 资金流量指标 MFI（不复权） |
| `mfi_hfq` | 资金流量指标 MFI（后复权） |
| `mfi_qfq` | 资金流量指标 MFI（前复权） |
| `mtm_bfq` | 动量指标 MTM（不复权） |
| `mtm_hfq` | 动量指标 MTM（后复权） |
| `mtm_qfq` | 动量指标 MTM（前复权） |
| `mtmma_bfq` | MTM 移动平均 MTMMA（不复权） |
| `mtmma_hfq` | MTM 移动平均 MTMMA（后复权） |
| `mtmma_qfq` | MTM 移动平均 MTMMA（前复权） |
| `obv_bfq` | 能量潮 OBV（不复权） |
| `obv_hfq` | 能量潮 OBV（后复权） |
| `obv_qfq` | 能量潮 OBV（前复权） |
| `psy_bfq` | 心理线 PSY（不复权） |
| `psy_hfq` | 心理线 PSY（后复权） |
| `psy_qfq` | 心理线 PSY（前复权） |
| `psyma_bfq` | 心理线均值 PSYMA（不复权） |
| `psyma_hfq` | 心理线均值 PSYMA（后复权） |
| `psyma_qfq` | 心理线均值 PSYMA（前复权） |
| `roc_bfq` | 变动率指标 ROC（不复权） |
| `roc_hfq` | 变动率指标 ROC（后复权） |
| `roc_qfq` | 变动率指标 ROC（前复权） |
| `maroc_bfq` | ROC 移动平均 MAROC（不复权） |
| `maroc_hfq` | ROC 移动平均 MAROC（后复权） |
| `maroc_qfq` | ROC 移动平均 MAROC（前复权） |
| `rsi_bfq_12` | 相对强弱指标 RSI（12 日）（不复权） |
| `rsi_bfq_24` | 相对强弱指标 RSI（24 日）（不复权） |
| `rsi_bfq_6` | 相对强弱指标 RSI（6 日）（不复权） |
| `rsi_hfq_12` | 相对强弱指标 RSI（12 日）（后复权） |
| `rsi_hfq_24` | 相对强弱指标 RSI（24 日）（后复权） |
| `rsi_hfq_6` | 相对强弱指标 RSI（6 日）（后复权） |
| `rsi_qfq_12` | 相对强弱指标 RSI（12 日）（前复权） |
| `rsi_qfq_24` | 相对强弱指标 RSI（24 日）（前复权） |
| `rsi_qfq_6` | 相对强弱指标 RSI（6 日）（前复权） |
| `taq_down_bfq` | 唐奇安通道下轨（不复权） |
| `taq_down_hfq` | 唐奇安通道下轨（后复权） |
| `taq_down_qfq` | 唐奇安通道下轨（前复权） |
| `taq_mid_bfq` | 唐奇安通道中轨（不复权） |
| `taq_mid_hfq` | 唐奇安通道中轨（后复权） |
| `taq_mid_qfq` | 唐奇安通道中轨（前复权） |
| `taq_up_bfq` | 唐奇安通道上轨（不复权） |
| `taq_up_hfq` | 唐奇安通道上轨（后复权） |
| `taq_up_qfq` | 唐奇安通道上轨（前复权） |
| `trix_bfq` | 三重指数平滑均线 TRIX（不复权） |
| `trix_hfq` | 三重指数平滑均线 TRIX（后复权） |
| `trix_qfq` | 三重指数平滑均线 TRIX（前复权） |
| `trma_bfq` | TRIX 移动平均 TRMA（不复权） |
| `trma_hfq` | TRIX 移动平均 TRMA（后复权） |
| `trma_qfq` | TRIX 移动平均 TRMA（前复权） |
| `vr_bfq` | 成交量比率 VR（不复权） |
| `vr_hfq` | 成交量比率 VR（后复权） |
| `vr_qfq` | 成交量比率 VR（前复权） |
| `wr_bfq` | 威廉指标 WR（10 日）（不复权） |
| `wr_hfq` | 威廉指标 WR（10 日）（后复权） |
| `wr_qfq` | 威廉指标 WR（10 日）（前复权） |
| `wr1_bfq` | 威廉指标 WR（6 日）（不复权） |
| `wr1_hfq` | 威廉指标 WR（6 日）（后复权） |
| `wr1_qfq` | 威廉指标 WR（6 日）（前复权） |
| `xsii_td1_bfq` | 薛斯通道 II TD1（不复权） |
| `xsii_td1_hfq` | 薛斯通道 II TD1（后复权） |
| `xsii_td1_qfq` | 薛斯通道 II TD1（前复权） |
| `xsii_td2_bfq` | 薛斯通道 II TD2（不复权） |
| `xsii_td2_hfq` | 薛斯通道 II TD2（后复权） |
| `xsii_td2_qfq` | 薛斯通道 II TD2（前复权） |
| `xsii_td3_bfq` | 薛斯通道 II TD3（不复权） |
| `xsii_td3_hfq` | 薛斯通道 II TD3（后复权） |
| `xsii_td3_qfq` | 薛斯通道 II TD3（前复权） |
| `xsii_td4_bfq` | 薛斯通道 II TD4（不复权） |
| `xsii_td4_hfq` | 薛斯通道 II TD4（后复权） |
| `xsii_td4_qfq` | 薛斯通道 II TD4（前复权） |

## 示例

```python
df = qs.technical_factors_pro(symbol="600519.SH")
print(df.head())
```
