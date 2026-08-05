# 数据能力目录

只在需要确定方法、参数或返回字段时读取本文件；分析工作流优先读取对应的
`stock-research.md`、`market-brief.md`、`stock-screening.md` 或
`quant-data-prep.md`。

MCP 工具名与 Python SDK 方法名一致。每个方法的完整参数和返回字段位于
`endpoints/` 对应文件。

| 方法 / MCP 工具 | 说明 | 数据类别 | 套餐 | 完整参考 |
|---|---|---|---|---|
| `daily` | 日线行情（OHLC） | 行情数据 | FREE | [查看](endpoints/daily.md) |
| `fundamentals` | 每日指标（PE/PB/换手率/市值） | 行情数据 | Starter | [查看](endpoints/fundamentals.md) |
| `adj_factor` | 复权因子 | 行情数据 | Starter | [查看](endpoints/adj-factor.md) |
| `technical_factors` | 技术面因子 | 行情数据 | PRO | [查看](endpoints/technical-factors.md) |
| `technical_factors_pro` | 技术面因子（专业版，含复权价+技术指标） | 行情数据 | Expert | [查看](endpoints/technical-factors-pro.md) |
| `margin` | 融资融券明细 | 行情数据 | PRO | [查看](endpoints/margin.md) |
| `block_trade` | 大宗交易 | 行情数据 | PRO | [查看](endpoints/block-trade.md) |
| `top_list` | 龙虎榜（个股） | 行情数据 | PRO | [查看](endpoints/top-list.md) |
| `top_inst` | 龙虎榜（机构席位） | 行情数据 | PRO | [查看](endpoints/top-inst.md) |
| `shareholders` | 股东户数 | 行情数据 | PRO | [查看](endpoints/shareholders.md) |
| `holder_trade` | 重要股东增减持 | 行情数据 | PRO | [查看](endpoints/holder-trade.md) |
| `limit_list` | 涨跌停榜单 | 行情数据 | PRO | [查看](endpoints/limit-list.md) |
| `concepts` | 概念/题材板块指数 | 行情数据 | PRO | [查看](endpoints/concepts.md) |
| `concept_members` | 概念/题材板块成分股 | 行情数据 | PRO | [查看](endpoints/concept-members.md) |
| `basic` | ETF 基础信息 | ETF | FREE | [查看](endpoints/basic.md) |
| `etf_daily` | ETF 日线行情 | ETF | FREE | [查看](endpoints/etf-daily.md) |
| `etf_adj_factor` | ETF 复权因子 | ETF | FREE | [查看](endpoints/etf-adj-factor.md) |
| `nav` | ETF 净值 | ETF | Starter | [查看](endpoints/nav.md) |
| `portfolio` | ETF 持仓明细 | ETF | PRO | [查看](endpoints/portfolio.md) |
| `share_size` | ETF 份额与规模 | ETF | Starter | [查看](endpoints/share-size.md) |
| `tracking_indices` | ETF 跟踪指数基础信息 | ETF | Starter | [查看](endpoints/tracking-indices.md) |
| `moneyflow` | 个股资金流向 | 资金流向 | PRO | [查看](endpoints/moneyflow.md) |
| `moneyflow_hsgt` | 沪深港通资金流向（全市场） | 资金流向 | PRO | [查看](endpoints/moneyflow-hsgt.md) |
| `northbound_holdings` | 北向持股明细 | 资金流向 | PRO | [查看](endpoints/northbound-holdings.md) |
| `southbound_holdings` | 南向（港股通）持股明细 | 资金流向 | PRO | [查看](endpoints/southbound-holdings.md) |
| `distribution` | 筹码分布与胜率 | 筹码分布 | Expert | [查看](endpoints/distribution.md) |
| `index_daily` | 指数日线（默认上证综指） | 指数 | FREE | [查看](endpoints/index-daily.md) |
| `index_weight` | 指数成分与权重 | 指数 | Starter | [查看](endpoints/index-weight.md) |
| `indicators` | 财务指标 | 财务数据 | Starter | [查看](endpoints/indicators.md) |
| `income` | 利润表 | 财务数据 | Starter | [查看](endpoints/income.md) |
| `balance_sheet` | 资产负债表 | 财务数据 | Starter | [查看](endpoints/balance-sheet.md) |
| `cash_flow` | 现金流量表 | 财务数据 | Starter | [查看](endpoints/cash-flow.md) |
| `forecast` | 业绩预告 | 财务数据 | Starter | [查看](endpoints/forecast.md) |
| `express` | 业绩快报 | 财务数据 | Starter | [查看](endpoints/express.md) |
| `analyst_reports` | 券商研报盈利预测 | 财务数据 | PRO | [查看](endpoints/analyst-reports.md) |
| `audit` | 财务审计意见 | 财务数据 | PRO | [查看](endpoints/audit.md) |
| `main_business` | 主营业务构成 | 财务数据 | PRO | [查看](endpoints/main-business.md) |
| `disclosure_date` | 财报披露日历 | 财务数据 | PRO | [查看](endpoints/disclosure-date.md) |
| `dividend` | 分红送股 | 分红送股 | Starter | [查看](endpoints/dividend.md) |
| `fx_daily` | 外汇日线（默认 USDCNH） | 外汇 | FREE | [查看](endpoints/fx-daily.md) |
| `stocks` | 股票列表 | 基础信息 | FREE | [查看](endpoints/stocks.md) |
| `industries` | 申万行业分类 | 基础信息 | FREE | [查看](endpoints/industries.md) |
| `trade_calendar` | 交易日历（默认上交所） | 基础信息 | FREE | [查看](endpoints/trade-calendar.md) |
| `realtime` | 实时行情快照 | 实时与快讯 | Starter | [查看](endpoints/realtime.md) |
| `news_flash` | 财经快讯（实时） | 实时与快讯 | Starter | [查看](endpoints/news-flash.md) |
