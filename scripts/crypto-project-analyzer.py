#!/usr/bin/env python3
"""
加密货币项目自动分析和评测生成器
每日抓取GitHub上最热门的加密货币项目，生成专业评测文章
"""

import requests
import json
import os
import datetime
from typing import List, Dict, Any
import time
import re

class CryptoProjectAnalyzer:
    def __init__(self, github_token: str = None):
        self.github_token = github_token
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'SmartWallex-Analyzer/1.0'
        }
        if github_token:
            self.headers['Authorization'] = f'token {github_token}'
    
    def search_crypto_projects(self, days_back: int = 7) -> List[Dict[str, Any]]:
        """搜索最近一周Star增长最快的加密货币项目"""
        
        # 计算日期范围
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days_back)
        date_filter = start_date.strftime('%Y-%m-%d')
        
        # 搜索关键词
        crypto_keywords = [
            'cryptocurrency', 'blockchain', 'bitcoin', 'ethereum', 
            'defi', 'web3', 'crypto', 'dapp', 'smart-contract',
            'trading', 'wallet', 'exchange', 'nft'
        ]
        
        all_projects = []
        
        for keyword in crypto_keywords[:3]:  # 限制搜索次数避免API限制
            try:
                # GitHub搜索API
                search_url = 'https://api.github.com/search/repositories'
                params = {
                    'q': f'{keyword} created:>{date_filter} stars:>10',
                    'sort': 'stars',
                    'order': 'desc',
                    'per_page': 10
                }
                
                response = requests.get(search_url, headers=self.headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    all_projects.extend(data.get('items', []))
                    time.sleep(1)  # 避免API限制
                else:
                    print(f"搜索失败: {keyword}, 状态码: {response.status_code}")
                    
            except Exception as e:
                print(f"搜索 {keyword} 时出错: {e}")
                continue
        
        # 去重并按star数排序
        unique_projects = {}
        for project in all_projects:
            repo_id = project['id']
            if repo_id not in unique_projects:
                unique_projects[repo_id] = project
        
        sorted_projects = sorted(
            unique_projects.values(), 
            key=lambda x: x['stargazers_count'], 
            reverse=True
        )
        
        return sorted_projects[:3]  # 返回前3个项目
    
    def get_project_details(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """获取项目详细信息"""
        
        repo_url = project['url']
        
        try:
            # 获取README内容
            readme_url = f"{repo_url}/readme"
            readme_response = requests.get(readme_url, headers=self.headers)
            readme_content = ""
            
            if readme_response.status_code == 200:
                readme_data = readme_response.json()
                if readme_data.get('encoding') == 'base64':
                    import base64
                    readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
            
            # 获取最近的提交信息
            commits_url = f"{repo_url}/commits"
            commits_response = requests.get(f"{commits_url}?per_page=5", headers=self.headers)
            recent_commits = []
            
            if commits_response.status_code == 200:
                commits_data = commits_response.json()
                recent_commits = [
                    {
                        'message': commit['commit']['message'][:100],
                        'date': commit['commit']['author']['date'],
                        'author': commit['commit']['author']['name']
                    }
                    for commit in commits_data[:3]
                ]
            
            # 获取语言统计
            languages_url = f"{repo_url}/languages"
            languages_response = requests.get(languages_url, headers=self.headers)
            languages = {}
            
            if languages_response.status_code == 200:
                languages = languages_response.json()
            
            return {
                'basic_info': project,
                'readme_content': readme_content[:2000],  # 限制长度
                'recent_commits': recent_commits,
                'languages': languages,
                'topics': project.get('topics', [])
            }
            
        except Exception as e:
            print(f"获取项目详情失败: {e}")
            return {'basic_info': project}
    
    def analyze_project_category(self, project_details: Dict[str, Any]) -> str:
        """分析项目类别"""
        
        basic_info = project_details['basic_info']
        readme = project_details.get('readme_content', '').lower()
        topics = project_details.get('topics', [])
        description = basic_info.get('description', '').lower()
        
        # 关键词分类
        categories = {
            'DeFi协议': ['defi', 'decentralized finance', 'yield', 'liquidity', 'amm', 'dex', 'lending'],
            '区块链基础设施': ['blockchain', 'consensus', 'validator', 'node', 'network', 'protocol'],
            '交易工具': ['trading', 'exchange', 'arbitrage', 'bot', 'strategy'],
            '钱包应用': ['wallet', 'custody', 'keys', 'seed', 'mnemonic'],
            'NFT平台': ['nft', 'non-fungible', 'collectible', 'marketplace', 'art'],
            '开发工具': ['sdk', 'api', 'framework', 'library', 'development'],
            '数据分析': ['analytics', 'data', 'metrics', 'dashboard', 'monitoring']
        }
        
        text_to_analyze = f"{description} {readme} {' '.join(topics)}"
        
        for category, keywords in categories.items():
            if any(keyword in text_to_analyze for keyword in keywords):
                return category
        
        return '其他工具'
    
    def generate_review_content(self, project_details: Dict[str, Any]) -> str:
        """生成评测文章内容"""
        
        basic_info = project_details['basic_info']
        category = self.analyze_project_category(project_details)
        
        # 基本信息
        name = basic_info['name']
        description = basic_info.get('description', '暂无描述')
        stars = basic_info['stargazers_count']
        forks = basic_info['forks_count']
        language = basic_info.get('language', '未知')
        created_at = basic_info['created_at'][:10]
        updated_at = basic_info['updated_at'][:10]
        homepage = basic_info.get('homepage', '')
        github_url = basic_info['html_url']
        
        # 生成文章内容
        content = f"""{{{{< alert >}}}}
**项目快览**: {name}是一个{category}项目，GitHub上{stars:,}个⭐，主要使用{language}开发
{{{{< /alert >}}}}

**{name}**是一个备受关注的{category}项目，在GitHub上已获得{stars:,}个星标，展现出强劲的社区关注度和发展潜力。该项目主要使用{language}开发，为加密货币生态系统提供创新解决方案。

## 🎯 项目概览

### 基本信息
- **项目名称**: {name}
- **项目类型**: {category}
- **开发语言**: {language}
- **GitHub地址**: [{github_url}]({github_url})
- **GitHub Stars**: {stars:,}
- **Fork数量**: {forks:,}
- **创建时间**: {created_at}
- **最近更新**: {updated_at}
- **官方网站**: {homepage if homepage else '暂无'}

### 项目描述
{description}

## 🛠️ 技术特点

### 开发活跃度
该项目在GitHub上表现出良好的开发活跃度：
- ⭐ **社区关注**: {stars:,}个星标显示了强劲的社区支持
- 🔄 **代码贡献**: {forks:,}个Fork表明开发者积极参与
- 📅 **持续更新**: 最近更新于{updated_at}，保持活跃开发状态

### 技术栈分析"""

        # 添加语言统计
        if 'languages' in project_details and project_details['languages']:
            content += "\n\n**主要编程语言构成**:\n"
            total_bytes = sum(project_details['languages'].values())
            for lang, bytes_count in sorted(project_details['languages'].items(), key=lambda x: x[1], reverse=True)[:5]:
                percentage = (bytes_count / total_bytes) * 100
                content += f"- {lang}: {percentage:.1f}%\n"

        # 添加最近提交信息
        if 'recent_commits' in project_details and project_details['recent_commits']:
            content += "\n\n### 最近开发动态\n"
            for commit in project_details['recent_commits']:
                commit_date = commit['date'][:10]
                content += f"- **{commit_date}**: {commit['message']} (by {commit['author']})\n"

        # 添加项目标签
        if 'topics' in project_details and project_details['topics']:
            content += f"\n\n### 🏷️ 项目标签\n"
            topics_badges = []
            for topic in project_details['topics'][:10]:
                topics_badges.append(f"`{topic}`")
            content += f"该项目被标记为: {' '.join(topics_badges)}\n"

        # 添加评测分析
        content += f"""

## 📊 项目评测

### 🎯 核心优势
1. **社区认可度高**: {stars:,}个GitHub星标证明了项目的受欢迎程度
2. **开发活跃**: 持续的代码更新显示项目处于积极开发状态
3. **技术创新**: 在{category}领域提供独特的解决方案
4. **开源透明**: 完全开源，代码可审计，增强用户信任

### ⚠️ 潜在考虑
1. **项目成熟度**: 作为相对较新的项目，需要时间验证稳定性
2. **生态建设**: 需要持续建设开发者和用户生态
3. **市场竞争**: 在{category}领域面临激烈竞争
4. **技术风险**: 新兴技术可能存在未知风险

### 💡 使用建议
- **开发者**: 适合关注{category}技术发展的开发者学习和贡献
- **投资者**: 建议深入研究项目技术和团队背景后谨慎评估
- **用户**: 可以关注项目发展，但建议等待更多实际应用案例

## 🔮 发展前景

基于当前的GitHub数据和社区反响，{name}展现出以下发展潜力：

1. **技术创新**: 在{category}领域的技术创新可能带来突破性进展
2. **社区增长**: 快速增长的星标数显示强劲的社区兴趣
3. **生态扩展**: 有潜力在加密货币生态系统中占据重要位置
4. **商业应用**: 技术成熟后可能产生实际的商业应用价值

## 📈 数据表现

| 指标 | 数值 | 说明 |
|------|------|------|
| GitHub Stars | {stars:,} | 社区关注度指标 |
| Fork数量 | {forks:,} | 开发者参与度 |
| 主要语言 | {language} | 技术栈核心 |
| 项目年龄 | {(datetime.datetime.now() - datetime.datetime.strptime(created_at, '%Y-%m-%d')).days}天 | 项目成熟度参考 |

---

*本评测基于GitHub公开数据分析生成，不构成投资建议。加密货币项目投资存在高风险，请谨慎决策并做好充分研究。*"""

        return content

def main():
    """主函数"""
    
    # 从环境变量获取GitHub token
    github_token = os.getenv('GITHUB_TOKEN')
    
    if github_token:
        # 在GitHub Actions环境中，不显示token内容
        if os.getenv('GITHUB_ACTIONS'):
            print("✅ 使用GitHub Actions内置Token")
        else:
            print(f"✅ 已获取GitHub Token: {github_token[:8]}...")
    else:
        print("⚠️  警告: 未设置GITHUB_TOKEN环境变量，API调用可能受限")
        if not os.getenv('GITHUB_ACTIONS'):
            print("💡 提示: 请在 .env.local 文件中设置 GITHUB_TOKEN=your_token")
    
    analyzer = CryptoProjectAnalyzer(github_token)
    
    print("🔍 开始搜索热门加密货币项目...")
    
    try:
        projects = analyzer.search_crypto_projects()
    except Exception as e:
        print(f"❌ 搜索项目时出错: {e}")
        return
    
    if not projects:
        print("❌ 未找到符合条件的项目")
        return
    
    print(f"✅ 找到 {len(projects)} 个热门项目")
    
    # 生成今日日期用于文件名
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 检查今日是否已生成文章
    existing_articles = len([f for f in os.listdir('content/posts') if today in f])
    if existing_articles > 0:
        print(f"ℹ️  今日已存在 {existing_articles} 篇文章，跳过生成")
        return
    
    generated_count = 0
    
    for i, project in enumerate(projects, 1):
        try:
            print(f"\n📊 分析项目 {i}: {project['name']}")
            
            # 获取详细信息
            project_details = analyzer.get_project_details(project)
            
            # 生成评测内容
            review_content = analyzer.generate_review_content(project_details)
            
            # 生成文件名和标题（处理特殊字符）
            project_name = re.sub(r'[^\w\-]', '-', project['name'].lower())
            project_name = re.sub(r'-+', '-', project_name).strip('-')
            filename = f"github-crypto-{project_name}-review-{today}.md"
            
            # 确保文件名不重复
            counter = 1
            original_filename = filename
            while os.path.exists(f"content/posts/{filename}"):
                name_part = original_filename.replace('.md', '')
                filename = f"{name_part}-{counter}.md"
                counter += 1
            
            title = f"GitHub热门项目评测：{project['name']} - {analyzer.analyze_project_category(project_details)}深度分析"
            
            # 处理描述中的特殊字符
            description = project.get('description', '')
            if description:
                description = description.replace("'", "\\'").replace('"', '\\"')[:150]
            else:
                description = f"{project['name']}项目深度评测分析"
            
            # 创建Hugo文章
            hugo_content = f"""+++
date = '{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')}'
draft = false
title = '{title.replace("'", "\\'")}'
description = '{description}。GitHub {project['stargazers_count']:,} stars，{analyzer.analyze_project_category(project_details)}领域热门开源项目深度评测。'
summary = '{project['name']}是一个备受关注的{analyzer.analyze_project_category(project_details)}项目，在GitHub上已获得{project['stargazers_count']:,}个星标。'
tags = ['GitHub', '开源项目', '加密货币', '{analyzer.analyze_project_category(project_details)}', '{project.get('language', 'Unknown')}', '项目评测']
categories = ['GitHub热门']
keywords = ['{project['name'].replace("'", "\\'")}评测', 'GitHub加密货币项目', '{analyzer.analyze_project_category(project_details)}工具', '开源区块链项目']
author = 'ERIC'
ShowToc = true
TocOpen = false
ShowReadingTime = true
ShowBreadCrumbs = true
ShowPostNavLinks = true
ShowWordCount = true
ShowShareButtons = true
cover.image = ""
cover.alt = "{project['name']} - {analyzer.analyze_project_category(project_details)}项目评测"
cover.caption = "GitHub热门加密货币项目深度分析"
cover.relative = false
cover.hidden = false
+++

{review_content}

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
"""
            
            # 确保目录存在
            os.makedirs('content/posts', exist_ok=True)
            
            # 保存文章文件
            output_path = f"content/posts/{filename}"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(hugo_content)
            
            print(f"✅ 已生成文章: {output_path}")
            generated_count += 1
            
            # 避免API限制
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ 处理项目 {project['name']} 时出错: {e}")
            continue
    
    if generated_count > 0:
        print(f"\n🎉 完成！共生成 {generated_count} 篇评测文章")
    else:
        print(f"\n⚠️  未能生成任何文章")

if __name__ == "__main__":
    main()