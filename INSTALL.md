# QuantSonar 安装与配置指南（交给 Agent 执行）

> 给用户：将本文件完整发送给具备终端和文件访问权限的 Agent，并告诉它：
> “请严格按照这份文件安装、配置并验证 QuantSonar。”
>
> Agent 如果没有终端或本机文件访问权限，不得声称安装成功；应改为输出适合当前
> 操作系统的人工执行命令。

## 给 Agent 的任务

在当前机器上安装 QuantSonar Agent Skill，配置一种可用的数据访问方式，并完成
一次不包含投资建议的真实数据查询。执行过程中遵守以下规则：

1. 不打印、记录或提交用户的完整 API Key。
2. 不把 API Key 写入 Git 仓库、Markdown、代码示例或公开配置文件。
3. 不删除或覆盖已有的同名 Skill；如果已安装，只验证现状并询问用户是否更新。
4. 不编造安装结果、工具调用或金融数据。
5. 需要用户登录、输入密钥或批准系统权限时，暂停并明确说明下一步。

## 第一步：检查运行环境

确认当前机器具有 Node.js、`npx` 和 Git：

```bash
node --version
npx --version
git --version
```

如果其中任何命令不存在，先向用户说明缺失项。不要擅自修改系统级软件或使用
管理员权限安装依赖。

检查 npm、GitHub 和 QuantSonar 是否可以访问：

```bash
npm view skills version
git ls-remote https://github.com/QuantSonar/quantsonar-skills.git HEAD
curl -fsS https://quantsonar.com/health
```

Windows PowerShell 如果没有 `curl`，可以使用：

```powershell
Invoke-WebRequest https://quantsonar.com/health -UseBasicParsing
```

## 第二步：只读检查远程 Skill

先确认仓库可访问，并且安装器能发现名为 `quantsonar` 的 Skill：

```bash
npx --yes skills add QuantSonar/quantsonar-skills --list
```

预期结果应包含：

```text
Source: https://github.com/QuantSonar/quantsonar-skills.git
Found 1 skill
quantsonar
```

`QuantSonar/quantsonar-skills` 是 Skills CLI 支持的 GitHub `owner/repo` 简写。
如需避免歧义，可以使用完整地址：

```bash
npx --yes skills add https://github.com/QuantSonar/quantsonar-skills --list
```

如果检查结果没有 `quantsonar`，停止安装并报告原始错误。

## 第三步：安装 Skill

先检查全局安装状态：

```bash
npx --yes skills list --global
```

如果尚未安装，执行：

```bash
npx --yes skills add QuantSonar/quantsonar-skills --skill quantsonar --global --yes
```

Skills CLI 会检测当前机器支持的 Agent。若检测到多个 Agent，只为当前正在执行任务
的 Agent 安装；可以通过 `--agent <agent-name>` 明确指定。不要无条件使用
`--agent '*'`。

安装后再次检查：

```bash
npx --yes skills list --global
```

结果必须包含 `quantsonar`。如果当前 Agent 需要重启或新建会话才能载入 Skill，
明确告诉用户。

## 第四步：准备 API Key

QuantSonar 的 REST API、Python SDK 和 MCP 共用同一个 API Key。没有 Key 时，提示
用户前往以下页面创建：

<https://quantsonar.com/register?utm_source=agent_install&utm_medium=referral&utm_campaign=agent_ecosystem&utm_content=install_md>

优先让用户通过当前 Agent 的安全密钥设置、环境变量或 MCP 密钥输入框提供 Key。
不要要求用户把完整 Key 写进本文件。

临时环境变量示例：

macOS / Linux：

```bash
export QUANTSONAR_TOKEN="qs_你的密钥"
```

Windows PowerShell：

```powershell
$env:QUANTSONAR_TOKEN = "qs_你的密钥"
```

除非用户明确同意，否则不要把 Key 永久写入 shell 配置文件。

## 第五步：配置数据访问

优先配置远程 MCP；如果当前 Agent 不支持带自定义请求头的远程 HTTP MCP，再使用
Python SDK 回退。

### 方式 A：远程 MCP（推荐）

- 传输类型：Streamable HTTP
- URL：`https://quantsonar.com/mcp`
- 请求头：`X-API-Key: <用户的 API Key>`

使用当前 Agent 官方支持的 MCP 配置界面或命令添加以上服务器。不要猜测不支持的
配置语法。

Claude Code 可以直接执行：

```bash
claude mcp add --transport http quantsonar https://quantsonar.com/mcp \
  --header "X-API-Key: qs_你的密钥"
```

配置完成后，确认 MCP 工具列表中出现 QuantSonar 工具。工具名应与 Python SDK
方法名一致，例如 `stocks`、`trade_calendar` 和 `daily`。

### 方式 B：Python SDK（回退）

当 MCP 无法配置，但当前 Agent 可以运行 Python 时：

```bash
python -m pip install --upgrade quantsonar
```

验证导入和环境变量，不要输出 Key：

```bash
python -c "import os, quantsonar; assert os.getenv('QUANTSONAR_TOKEN'); print('QuantSonar SDK ready')"
```

如果机器使用 `python3`，将上述命令中的 `python` 替换为 `python3`。

## 第六步：执行真实查询验证

让当前 Agent 执行以下任务：

```text
使用 QuantSonar 查询 600519.SH 最近 5 个已完成交易日的交易日期和收盘价。
先通过交易日历确认适用日期，注明数据最新日期和使用的访问方式。
如果没有可用数据或权限不足，明确报告，不要编造结果。
这只是数据连接测试，不提供投资建议。
```

验证成功必须同时满足：

1. Agent 明确调用了 QuantSonar MCP 工具或 Python SDK；
2. 结果包含实际交易日期和数据最新日期；
3. 没有把 API Key 输出到终端记录或回答中；
4. 没有把查询结果描述成收益承诺或投资建议。

## 第七步：向用户报告

完成后只报告以下内容，不得报告完整 API Key：

```text
QuantSonar 安装结果
- Skill：已安装 / 已存在 / 失败
- 安装范围：全局 / 项目
- 当前 Agent：<名称>
- 数据访问：MCP / Python SDK / 未配置
- API Key：已配置 / 未配置（不显示具体值）
- 验证查询：成功 / 失败
- 数据最新日期：<YYYY-MM-DD 或不可用>
- 需要用户处理：<无，或明确的下一步>
```

## 常见问题

### GitHub 或 npm 访问超时

保留原始报错，并提示用户检查代理、公司网络限制或 GitHub/npm 可用性。不要在未经
用户同意的情况下修改系统代理或全局 npm 配置。

### Skill 已安装但 Agent 没有加载

确认安装目标是当前 Agent，并按该 Agent 的要求重启或新建会话。Skill 安装成功
不等于 MCP 已配置成功。

### MCP 不支持自定义请求头

不要把 API Key 放入 URL。改用 Python SDK，或让用户在支持安全请求头的 MCP
客户端中完成配置。

### 查询返回无权限

报告所需数据和当前权限不匹配；不要重复调用同一个接口，也不要用虚构数据补全。

