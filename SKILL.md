---
name: QuantSonar
slug: quantsonar
description: Fetch Chinese A-share market data — daily OHLC, PE/PB valuations, money flow, northbound/southbound holdings, margin trading, block trades, dragon-tiger list, shareholder data, concept sectors, financial statements, dividends, technical indicators, realtime quotes and news flash. Full A-share coverage with 10+ years of history. Requires QUANTSONAR_TOKEN environment variable.
user-invocable: true
metadata:
 {
  "openclaw": {
   "requires": {
    "env": ["QUANTSONAR_TOKEN"],
    "bins": ["python3", "pip3"]
   },
   "install": [
    {
     "id": "pip-deps",
     "kind": "python",
     "package": "quantsonar",
     "label": "Install QuantSonar Python SDK"
    }
   ]
  }
 }
---

# QuantSonar — A 股量化数据

你是 A 股市场数据助手。根据用户的问题，用 `quantsonar` Python SDK 取数并呈现结果。

## 准备

1. **API Key**：免费注册 https://quantsonar.com/register（100 次/天，无需信用卡）
2. **环境变量**：`export QUANTSONAR_TOKEN="qs_你的密钥"`
3. **安装 SDK**：`pip install quantsonar`

## 快速开始

```python
import quantsonar as qs   # 自动读取 QUANTSONAR_TOKEN

df = qs.daily(symbol="600519.SH", start_date="20260101")   # 返回 DataFrame
```

## 通用约定

- 证券代码带交易所后缀：`600519.SH`（沪）/ `000001.SZ`（深）/ `430047.BJ`（北交所）
- 日期统一 `YYYYMMDD` 字符串，如 `"20260710"`
- 大范围查询请用 `start_date`/`end_date` 收窄；单日切片用 `trade_date`
- 超出限速会抛 `quantsonar.RateLimitError`（含建议等待秒数）
- 数据仅供研究，不构成投资建议 —— 呈现结论时保持中性，不要给出买卖建议

## 备选：MCP 接入

支持 MCP 的客户端可以不装 SDK，直接添加远程 MCP 服务器：
URL `https://quantsonar.com/mcp`，请求头 `X-API-Key: qs_你的密钥`。

## 接口目录

按需查阅同目录下的接口参考文件（含参数与全部返回字段说明）：

| 方法 | 说明 | 套餐 | 参考 |
|---|---|---|---|
| `qs.daily()` | 日线行情（OHLC）（行情数据） | FREE | [daily.md](daily.md) |
| `qs.fundamentals()` | 每日指标（PE/PB/换手率/市值）（行情数据） | Starter | [fundamentals.md](fundamentals.md) |
| `qs.adj_factor()` | 复权因子（行情数据） | Starter | [adj-factor.md](adj-factor.md) |
| `qs.technical_factors()` | 技术面因子（行情数据） | PRO | [technical-factors.md](technical-factors.md) |
| `qs.technical_factors_pro()` | 技术面因子（专业版，含复权价+技术指标）（行情数据） | Expert | [technical-factors-pro.md](technical-factors-pro.md) |
| `qs.margin()` | 融资融券明细（行情数据） | PRO | [margin.md](margin.md) |
| `qs.block_trade()` | 大宗交易（行情数据） | PRO | [block-trade.md](block-trade.md) |
| `qs.top_list()` | 龙虎榜（个股）（行情数据） | PRO | [top-list.md](top-list.md) |
| `qs.top_inst()` | 龙虎榜（机构席位）（行情数据） | PRO | [top-inst.md](top-inst.md) |
| `qs.shareholders()` | 股东户数（行情数据） | PRO | [shareholders.md](shareholders.md) |
| `qs.holder_trade()` | 重要股东增减持（行情数据） | PRO | [holder-trade.md](holder-trade.md) |
| `qs.limit_list()` | 涨跌停榜单（行情数据） | PRO | [limit-list.md](limit-list.md) |
| `qs.concepts()` | 概念/题材板块指数（行情数据） | PRO | [concepts.md](concepts.md) |
| `qs.concept_members()` | 概念/题材板块成分股（行情数据） | PRO | [concept-members.md](concept-members.md) |
| `qs.moneyflow()` | 个股资金流向（资金流向） | PRO | [moneyflow.md](moneyflow.md) |
| `qs.moneyflow_hsgt()` | 沪深港通资金流向（全市场）（资金流向） | PRO | [moneyflow-hsgt.md](moneyflow-hsgt.md) |
| `qs.northbound_holdings()` | 北向持股明细（资金流向） | PRO | [northbound-holdings.md](northbound-holdings.md) |
| `qs.southbound_holdings()` | 南向（港股通）持股明细（资金流向） | PRO | [southbound-holdings.md](southbound-holdings.md) |
| `qs.distribution()` | 筹码分布与胜率（筹码分布） | Expert | [distribution.md](distribution.md) |
| `qs.index_daily()` | 指数日线（默认上证综指）（指数） | FREE | [index-daily.md](index-daily.md) |
| `qs.index_weight()` | 指数成分与权重（指数） | Starter | [index-weight.md](index-weight.md) |
| `qs.indicators()` | 财务指标（财务数据） | Starter | [indicators.md](indicators.md) |
| `qs.income()` | 利润表（财务数据） | Starter | [income.md](income.md) |
| `qs.balance_sheet()` | 资产负债表（财务数据） | Starter | [balance-sheet.md](balance-sheet.md) |
| `qs.cash_flow()` | 现金流量表（财务数据） | Starter | [cash-flow.md](cash-flow.md) |
| `qs.forecast()` | 业绩预告（财务数据） | Starter | [forecast.md](forecast.md) |
| `qs.express()` | 业绩快报（财务数据） | Starter | [express.md](express.md) |
| `qs.analyst_reports()` | 券商研报盈利预测（财务数据） | PRO | [analyst-reports.md](analyst-reports.md) |
| `qs.audit()` | 财务审计意见（财务数据） | PRO | [audit.md](audit.md) |
| `qs.main_business()` | 主营业务构成（财务数据） | PRO | [main-business.md](main-business.md) |
| `qs.disclosure_date()` | 财报披露日历（财务数据） | PRO | [disclosure-date.md](disclosure-date.md) |
| `qs.dividend()` | 分红送股（分红送股） | Starter | [dividend.md](dividend.md) |
| `qs.fx_daily()` | 外汇日线（默认 USDCNH）（外汇） | FREE | [fx-daily.md](fx-daily.md) |
| `qs.stocks()` | 股票列表（基础信息） | FREE | [stocks.md](stocks.md) |
| `qs.industries()` | 申万行业分类（基础信息） | FREE | [industries.md](industries.md) |
| `qs.trade_calendar()` | 交易日历（默认上交所）（基础信息） | FREE | [trade-calendar.md](trade-calendar.md) |
| `qs.realtime()` | 实时行情快照（实时与快讯） | Starter | [realtime.md](realtime.md) |
| `qs.news_flash()` | 财经快讯（实时）（实时与快讯） | Starter | [news-flash.md](news-flash.md) |
