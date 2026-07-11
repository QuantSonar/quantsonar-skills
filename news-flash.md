# news_flash — 财经快讯（实时）

实时财经快讯，三个独立来源：cls（财联社）/ jin10（金十）/ sina（新浪）。按发布时间倒序，延迟约 60 秒。

## SDK 方法

```python
qs.news_flash(source=None, start_date=None, end_date=None, importance=None)
```

返回 `pandas.DataFrame`；无数据时返回空 DataFrame。

## 参数

| 参数 | 说明 |
|---|---|
| `source` | 快讯来源：cls / jin10 / sina **（必填）** |
| `start_date` | 起始日期 YYYYMMDD |
| `end_date` | 结束日期 YYYYMMDD |
| `importance` | 仅返回重要度 ≥ 此值的快讯（1 = 仅重要） |

## 返回字段

| 字段 | 说明 |
|---|---|
| `source` | 来源：cls 财联社 / jin10 金十 / sina 新浪 |
| `publish_time` | 发布时间 |
| `content_cn` | 快讯内容（中文） |
| `tags` | 标签 |
| `importance` | 重要度 |
| `url` | 原文链接 |

## 示例

```python
df = qs.news_flash()
print(df.head())
```
