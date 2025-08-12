# 内容创建指南

## Hugo文章格式规范

### 标题处理规则
- **禁止重复标题**：在Hugo文章中，front matter的`title`字段已经会自动生成页面标题，正文中不应再使用相同的H1标题
- **正文开头**：直接以引言段落或核心内容开始，不需要重复标题
- **层级结构**：正文中使用H2 (`##`) 作为主要章节标题，H3 (`###`) 作为子章节

### 文章结构最佳实践
1. **Front Matter**：包含完整的元数据（title, description, tags, categories, keywords等）
2. **引言段落**：直接以粗体关键词开始，简洁介绍主题
3. **章节组织**：使用清晰的H2、H3层级结构
4. **SEO优化**：合理分布关键词，避免过度优化

### 示例格式
```markdown
+++
title = '文章标题'
description = '文章描述'
tags = ['标签1', '标签2']
categories = ['分类']
+++

**核心关键词**是文章的主要内容介绍...

## 主要章节标题

### 子章节标题

内容...
```

### 文章结尾标准格式
每篇文章结尾必须包含以下作者信息和引流内容：

```markdown
---

## 📞 关于作者

**ERIC** - 《区块链核心技术与应用》作者之一，前火币机构事业部|矿池技术主管，比特财商|Nxt Venture Capital 创始人

### 🔗 联系方式与平台

- **📧 邮箱**: [gyc567@gmail.com](mailto:gyc567@gmail.com)
- **🐦 Twitter**: [@EricBlock2100](https://twitter.com/EricBlock2100)
- **💬 微信**: 360369487
- **📱 Telegram**: [https://t.me/fatoshi_block](https://t.me/fatoshi_block)
- **📢 Telegram频道**: [https://t.me/cryptochanneleric](https://t.me/cryptochanneleric)
- **👥 加密情报TG群**: [https://t.me/btcgogopen](https://t.me/btcgogopen)
- **🎥 YouTube频道**: [https://www.youtube.com/@0XBitFinance](https://www.youtube.com/@0XBitFinance)

### 🌐 相关平台

- **📊 加密货币信息聚合网站**: [https://www.smartwallex.com/](https://www.smartwallex.com/)
- **📖 公众号**: 比特财商

*欢迎关注我的各个平台，获取最新的加密货币市场分析和投资洞察！*
```

### 避免的错误
- ❌ 在正文中重复front matter的title
- ❌ 使用H1标题作为正文开头
- ❌ 标题层级混乱
- ❌ 缺少SEO元数据
- ❌ 忘记添加文章结尾的作者信息和引流内容