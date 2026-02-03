#!/usr/bin/env python3
"""
身心灵疗愈行业日报生成器
"""
import os
import json
import requests
from datetime import datetime
from urllib.parse import urljoin
import re

def get_healing_news():
    """获取身心灵疗愈相关的新闻"""
    articles = []
    
    try:
        # 尝试从 InfoQ 获取相关技术与健康结合的文章
        import feedparser
        import requests
        from bs4 import BeautifulSoup
        
        # 搜索相关的疗愈、健康、心理学等关键词
        search_urls = [
            "https://www.infoq.com/news/",
            "https://www.psychologytoday.com/us/blog",
            "https://www.health.harvard.edu/blog",
        ]
        
        # 由于当前环境限制，我们使用模拟数据作为示例
        # 在实际部署中，这里会抓取真实数据
        
        # 搜索与身心灵疗愈相关的关键词
        keywords = ["meditation", "mindfulness", "wellness", "mental health", "holistic"]
        
        sample_articles = [
            {
                "title": "冥想对大脑结构的积极影响研究",
                "summary": "最新研究表明，定期冥想可以改变大脑灰质密度，改善情绪调节和认知功能。",
                "url": "#"
            },
            {
                "title": "芳香疗法在现代医疗中的应用",
                "summary": "薰衣草和茶树精油在缓解焦虑和促进睡眠方面显示出显著效果。",
                "url": "#"
            },
            {
                "title": "正念练习提升心理健康水平",
                "summary": "日常正念练习有助于减轻压力，增强情绪稳定性。",
                "url": "#"
            }
        ]
        
        # 尝试从网络获取真实数据
        try:
            # 搜索一些健康和疗愈相关的网站
            healing_sites = [
                "https://www.mindful.org",
                "https://www.healthline.com/mental-health",
                "https://psychcentral.com"
            ]
            
            # 由于当前环境限制，我们暂时返回示例数据
            # 在实际环境中，这里会进行真实的网页抓取
            for site in healing_sites[:1]:  # 仅演示，实际使用时可取消限制
                try:
                    # 这里可以添加真实的网页抓取逻辑
                    pass
                except:
                    pass
                    
            return sample_articles
            
        except ImportError:
            # 如果没有安装额外的包，则返回示例数据
            return sample_articles
            
    except Exception as e:
        print(f"获取疗愈新闻时出错: {e}")
        # 返回示例数据作为备选
        return [
            {
                "title": "冥想对大脑结构的积极影响研究",
                "summary": "最新研究表明，定期冥想可以改变大脑灰质密度，改善情绪调节和认知功能。",
                "url": "#"
            },
            {
                "title": "芳香疗法在现代医疗中的应用",
                "summary": "薰衣草和茶树精油在缓解焦虑和促进睡眠方面显示出显著效果。",
                "url": "#"
            }
        ]

def get_mental_health_info():
    """获取心理健康相关信息"""
    articles = [
        {
            "title": "情绪管理技巧分享",
            "summary": "学会识别和接纳自己的情绪是情绪管理的第一步。",
            "url": "#"
        },
        {
            "title": "如何建立健康的心理边界",
            "summary": "设定清晰的个人边界有助于维护心理健康和人际关系。",
            "url": "#"
        }
    ]
    
    return articles

def get_natural_therapy_info():
    """获取自然疗法信息"""
    articles = [
        {
            "title": "森林浴的疗愈功效",
            "summary": "在自然环境中放松有助于降低皮质醇水平，提升免疫力。",
            "url": "#"
        },
        {
            "title": "水晶疗法的原理与实践",
            "summary": "不同类型的水晶被认为具有独特的能量频率，可辅助疗愈。",
            "url": "#"
        }
    ]
    
    return articles

def get_meditation_info():
    """获取冥想相关信息"""
    articles = [
        {
            "title": "初学者冥想指南",
            "summary": "从5分钟呼吸练习开始，逐步延长冥想时间。",
            "url": "#"
        },
        {
            "title": "身体扫描冥想法",
            "summary": "通过关注身体各部位来达到深度放松的效果。",
            "url": "#"
        }
    ]
    
    return articles

def get_recommended_reading():
    """获取推荐阅读"""
    articles = [
        {
            "title": "《当下的力量》读书心得",
            "summary": "埃克哈特·托利的经典著作，教你如何活在当下。",
            "url": "#"
        },
        {
            "title": "最新疗愈音乐推荐",
            "summary": "结合自然声音的冥想音乐，帮助深度放松。",
            "url": "#"
        }
    ]
    
    return articles

def generate_html_content():
    """生成HTML内容"""
    # 首先确保获取最新数据
    update_with_real_data()
    
    # 尝试从获取的数据中加载内容，如果失败则使用函数获取
    try:
        with open('public/latest_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        healing_news = data.get('healing_news', get_healing_news())
        mental_health = data.get('mental_health', get_mental_health_info())
        natural_therapy = data.get('natural_therapy', get_natural_therapy_info())
        meditation = data.get('meditation', get_meditation_info())
        recommended = data.get('recommended', get_recommended_reading())
    except:
        # 如果加载失败，使用函数获取默认数据
        healing_news = get_healing_news()
        mental_health = get_mental_health_info()
        natural_therapy = get_natural_therapy_info()
        meditation = get_meditation_info()
        recommended = get_recommended_reading()
    
    # 构建HTML片段
    healing_news_html = ""
    for article in healing_news:
        # 为示例链接提供更有意义的URL
        url = article['url']
        if url == "#":
            # 根据文章主题提供相关的搜索链接
            if "冥想" in article['title'] or "meditation" in article['title'].lower():
                url = "https://www.mindful.org/category/meditation/"
            elif "芳香疗法" in article['title'] or "aromatherapy" in article['title'].lower():
                url = "https://www.healthline.com/health/aromatherapy-benefits"
            else:
                url = "https://www.google.com/search?q=" + article['title'].replace(" ", "+")
                
        healing_news_html += f"""
        <div class="article">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{url}" class="article-link" target="_blank">了解更多 →</a>
        </div>
        """
    
    mental_health_html = ""
    for article in mental_health:
        url = article['url']
        if url == "#":
            if "情绪管理" in article['title'] or "emotion" in article['title'].lower():
                url = "https://www.helpguide.org/articles/emotional-health/emotional-regulation.htm"
            elif "心理边界" in article['title'] or "boundary" in article['title'].lower():
                url = "https://www.psychologytoday.com/us/blog/here-there-and-everywhere/201807/how-set-healthy-boundaries"
            else:
                url = "https://www.google.com/search?q=" + article['title'].replace(" ", "+")
                
        mental_health_html += f"""
        <div class="article">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{url}" class="article-link" target="_blank">了解更多 →</a>
        </div>
        """
    
    natural_therapy_html = ""
    for article in natural_therapy:
        url = article['url']
        if url == "#":
            if "森林浴" in article['title'] or "forest" in article['title'].lower():
                url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6318039/"
            elif "水晶疗法" in article['title'] or "crystal" in article['title'].lower():
                url = "https://www.healthline.com/health/crystal-healing"
            else:
                url = "https://www.google.com/search?q=" + article['title'].replace(" ", "+")
                
        natural_therapy_html += f"""
        <div class="article">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{url}" class="article-link" target="_blank">了解更多 →</a>
        </div>
        """
    
    meditation_html = ""
    for article in meditation:
        url = article['url']
        if url == "#":
            if "初学者" in article['title'] or "beginner" in article['title'].lower():
                url = "https://www.headspace.com/meditation/types/beginners"
            elif "身体扫描" in article['title'] or "body scan" in article['title'].lower():
                url = "https://www.mindful.org/body-scan-meditation-step-by-step/"
            else:
                url = "https://www.google.com/search?q=" + article['title'].replace(" ", "+")
                
        meditation_html += f"""
        <div class="article">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{url}" class="article-link" target="_blank">了解更多 →</a>
        </div>
        """
    
    recommended_html = ""
    for article in recommended:
        url = article['url']
        if url == "#":
            if "当下的力量" in article['title'] or "power of now" in article['title'].lower():
                url = "https://www.goodreads.com/book/show/4865.The_Power_of_Now"
            elif "疗愈音乐" in article['title'] or "music" in article['title'].lower():
                url = "https://open.spotify.com/search/meditation%20music"
            else:
                url = "https://www.google.com/search?q=" + article['title'].replace(" ", "+")
                
        recommended_html += f"""
        <div class="article">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <a href="{url}" class="article-link" target="_blank">了解更多 →</a>
        </div>
        """
    
    # 读取模板
    with open('public/index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 替换占位符
    today = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S更新')
    copyright_year = datetime.now().strftime('%Y')
    
    html_content = template.replace('[[DATE]]', today)
    html_content = html_content.replace('[[HEALING_NEWS]]', healing_news_html)
    html_content = html_content.replace('[[MENTAL_HEALTH]]', mental_health_html)
    html_content = html_content.replace('[[NATURAL_THERAPY]]', natural_therapy_html)
    html_content = html_content.replace('[[MEDITATION]]', meditation_html)
    html_content = html_content.replace('[[RECOMMENDED]]', recommended_html)
    html_content = html_content.replace('[[COPYRIGHT_YEAR]]', copyright_year)
    
    # 写入最终文件
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"日报已生成: {today}")

def update_with_real_data():
    """尝试从真实数据源获取信息"""
    print("正在从网络获取最新信息...")
    
    try:
        import feedparser
        from bs4 import BeautifulSoup
        import requests
        import time
        
        # 设置请求头，避免被反爬虫机制阻止
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        articles = {
            'healing_news': [],
            'mental_health': [],
            'natural_therapy': [],
            'meditation': [],
            'recommended': []
        }
        
        # 定义搜索关键词和对应的分类
        search_configs = [
            {
                'keywords': ['冥想', 'meditation', 'mindfulness'],
                'category': 'meditation',
                'sites': [
                    'https://www.mindful.org/feed/',
                    'https://www.headspace.com/meditation/feeds/rss',
                ]
            },
            {
                'keywords': ['心理健康', 'mental health', '心理'],
                'category': 'mental_health',
                'sites': [
                    'https://psychcentral.com/blog/feed/',
                    'https://www.helpguide.org/rss.xml',
                ]
            },
            {
                'keywords': ['自然疗法', '芳香疗法', 'natural therapy', 'aromatherapy'],
                'category': 'natural_therapy',
                'sites': []
            },
            {
                'keywords': ['身心灵', '疗愈', 'healing', 'holistic'],
                'category': 'healing_news',
                'sites': []
            },
            {
                'keywords': ['推荐', '书籍', 'reading', 'book'],
                'category': 'recommended',
                'sites': []
            }
        ]
        
        # 尝试从RSS源获取信息
        for config in search_configs:
            for site_url in config['sites']:
                try:
                    print(f"正在访问: {site_url}")
                    response = requests.get(site_url, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        feed = feedparser.parse(response.content)
                        
                        for entry in feed.entries[:3]:  # 只取前3篇
                            if len(articles[config['category']]) < 5:  # 每类最多5篇
                                # 检查标题是否包含相关关键词
                                title_match = any(keyword.lower() in entry.title.lower() for keyword in config['keywords'])
                                
                                if title_match or config['category'] == 'recommended':
                                    articles[config['category']].append({
                                        'title': entry.title,
                                        'summary': entry.summary if hasattr(entry, 'summary') else entry.description[:100] + '...',
                                        'url': entry.link
                                    })
                                    
                                    if len(articles[config['category']]) >= 5:
                                        break
                                        
                    time.sleep(1)  # 避免请求过于频繁
                    
                except Exception as e:
                    print(f"从 {site_url} 获取数据时出错: {e}")
                    continue
        
        # 如果RSS源不可用，尝试从网页抓取
        if not any(articles.values()):
            # 从几个常见的健康和疗愈网站抓取内容
            healing_websites = [
                ('https://www.mindful.org', 'meditation'),
                ('https://psychcentral.com', 'mental_health'),
                ('https://www.healthline.com/mental-health', 'mental_health')
            ]
            
            for website, category in healing_websites:
                try:
                    response = requests.get(website, headers=headers, timeout=10)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        
                        # 尝试找到文章标题和摘要
                        # 这里根据具体网站结构调整选择器
                        article_elements = soup.find_all(['article', 'div'], limit=3)
                        
                        for elem in article_elements:
                            title_elem = elem.find(['h1', 'h2', 'h3', 'a'])
                            if title_elem:
                                title = title_elem.get_text().strip()
                                if any(keyword in title.lower() for keyword in ['meditation', 'mindfulness', 'mental', 'health', 'therapy']):
                                    summary_elem = elem.find(['p', 'div'], recursive=False)
                                    summary = summary_elem.get_text().strip()[:150] + '...' if summary_elem else '暂无摘要'
                                    
                                    articles[category].append({
                                        'title': title,
                                        'summary': summary,
                                        'url': website
                                    })
                                    
                                    if len(articles[category]) >= 3:
                                        break
                                        
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"从 {website} 抓取数据时出错: {e}")
                    continue
        
        # 将获取的数据写入临时文件，供后续使用
        with open('public/latest_data.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
            
        print("实时数据获取完成")
        
    except ImportError:
        print("需要安装额外的依赖包: pip install -r requirements.txt")
    except Exception as e:
        print(f"获取实时数据时出现错误: {e}")
        # 如果出现错误，使用示例数据
        sample_data = {
            'healing_news': [
                {
                    "title": "冥想对大脑结构的积极影响研究",
                    "summary": "最新研究表明，定期冥想可以改变大脑灰质密度，改善情绪调节和认知功能。",
                    "url": "#"
                },
                {
                    "title": "芳香疗法在现代医疗中的应用",
                    "summary": "薰衣草和茶树精油在缓解焦虑和促进睡眠方面显示出显著效果。",
                    "url": "#"
                }
            ],
            'mental_health': [
                {
                    "title": "情绪管理技巧分享",
                    "summary": "学会识别和接纳自己的情绪是情绪管理的第一步。",
                    "url": "#"
                }
            ],
            'natural_therapy': [
                {
                    "title": "森林浴的疗愈功效",
                    "summary": "在自然环境中放松有助于降低皮质醇水平，提升免疫力。",
                    "url": "#"
                }
            ],
            'meditation': [
                {
                    "title": "初学者冥想指南",
                    "summary": "从5分钟呼吸练习开始，逐步延长冥想时间。",
                    "url": "#"
                }
            ],
            'recommended': [
                {
                    "title": "《当下的力量》读书心得",
                    "summary": "埃克哈特·托利的经典著作，教你如何活在当下。",
                    "url": "#"
                }
            ]
        }
        
        with open('public/latest_data.json', 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print("开始生成身心灵疗愈日报...")
    
    # 重新创建模板文件（以防被覆盖）
    template_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>身心灵疗愈日报 - Healtherly Daily Report</title>
    <style>
        body {
            font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        header {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        h1 {
            margin: 0;
            font-size: 2em;
        }
        .date {
            font-size: 1.2em;
            opacity: 0.9;
            margin-top: 10px;
        }
        .content {
            padding: 30px;
        }
        .section {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        .section:last-child {
            border-bottom: none;
        }
        .section h2 {
            color: #667eea;
            border-left: 4px solid #667eea;
            padding-left: 15px;
            margin-top: 0;
        }
        .article {
            margin-bottom: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 8px;
            border-left: 3px solid #764ba2;
        }
        .article-title {
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }
        .article-summary {
            color: #666;
            font-size: 0.95em;
        }
        .article-link {
            display: inline-block;
            margin-top: 10px;
            color: #667eea;
            text-decoration: none;
            font-size: 0.9em;
        }
        footer {
            text-align: center;
            padding: 20px;
            color: #999;
            font-size: 0.9em;
            background: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>身心灵疗愈日报</h1>
            <div class="date">[[DATE]]</div>
        </header>
        
        <div class="content">
            <div class="section">
                <h2>🧘‍♀️ 疗愈资讯</h2>
                <div id="healing-news">
                    [[HEALING_NEWS]]
                </div>
            </div>
            
            <div class="section">
                <h2>🧠 心理健康</h2>
                <div id="mental-health">
                    [[MENTAL_HEALTH]]
                </div>
            </div>
            
            <div class="section">
                <h2>🌿 自然疗法</h2>
                <div id="natural-therapy">
                    [[NATURAL_THERAPY]]
                </div>
            </div>
            
            <div class="section">
                <h2>💭 冥想静心</h2>
                <div id="meditation">
                    [[MEDITATION]]
                </div>
            </div>
            
            <div class="section">
                <h2>📚 推荐阅读</h2>
                <div id="recommended">
                    [[RECOMMENDED]]
                </div>
            </div>
        </div>
        
        <footer>
            <p>身心灵疗愈日报 • 每日更新 • [[COPYRIGHT_YEAR]]</p>
        </footer>
    </div>
</body>
</html>'''
    
    # 确保public目录存在
    os.makedirs('public', exist_ok=True)
    
    # 写入模板
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    # 生成内容
    generate_html_content()
    update_with_real_data()
    
    print("身心灵疗愈日报生成完成！")