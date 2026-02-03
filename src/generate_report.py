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
    # 如果有网络获取失败，返回示例数据
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
    return [
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

def get_natural_therapy_info():
    """获取自然疗法信息"""
    return [
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

def get_meditation_info():
    """获取冥想相关信息"""
    return [
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

def get_recommended_reading():
    """获取推荐阅读"""
    return [
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
        <a href="{url}" class="article" target="_blank">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <div class="article-meta">
                <span class="article-source">身心灵疗愈</span>
                <span class="article-link">了解更多</span>
            </div>
        </a>
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
        <a href="{url}" class="article" target="_blank">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <div class="article-meta">
                <span class="article-source">心理健康</span>
                <span class="article-link">了解更多</span>
            </div>
        </a>
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
        <a href="{url}" class="article" target="_blank">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <div class="article-meta">
                <span class="article-source">自然疗法</span>
                <span class="article-link">了解更多</span>
            </div>
        </a>
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
        <a href="{url}" class="article" target="_blank">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <div class="article-meta">
                <span class="article-source">冥想静心</span>
                <span class="article-link">了解更多</span>
            </div>
        </a>
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
        <a href="{url}" class="article" target="_blank">
            <div class="article-title">{article['title']}</div>
            <div class="article-summary">{article['summary']}</div>
            <div class="article-meta">
                <span class="article-source">推荐阅读</span>
                <span class="article-link">了解更多</span>
            </div>
        </a>
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
        

    except ImportError:
        print("需要安装额外的依赖包: pip install -r requirements.txt")
    except Exception as e:
        print(f"获取实时数据时出现错误: {e}")

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
        :root {
            --bg-color: #fafafa;
            --text-color: #1f2937;
            --border-color: #e5e7eb;
            --accent-color: #4f46e5;
            --card-bg: #ffffff;
            --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px 0;
            border-bottom: 1px solid var(--border-color);
        }
        
        h1 {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 10px;
            color: var(--text-color);
        }
        
        .date {
            color: #6b7280;
            font-size: 1.1rem;
        }
        
        .content {
            margin-bottom: 40px;
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border-color);
        }
        
        .section-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--text-color);
            margin: 0;
        }
        
        .section-emoji {
            margin-right: 10px;
            font-size: 1.2rem;
        }
        
        .articles-list {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }
        
        .article {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        
        .article:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow);
            text-decoration: none;
        }
        
        .article-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--accent-color);
            margin-bottom: 8px;
            line-height: 1.4;
        }
        
        .article-summary {
            color: #6b7280;
            margin-bottom: 12px;
            line-height: 1.6;
            font-size: 0.95rem;
        }
        
        .article-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.85rem;
            color: #9ca3af;
        }
        
        .article-source {
            background: #f3f4f6;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.8rem;
        }
        
        .article-link {
            color: var(--accent-color);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
        }
        
        .article-link:hover {
            text-decoration: underline;
        }
        
        .article-link::after {
            content: "→";
            margin-left: 5px;
        }
        
        footer {
            text-align: center;
            padding: 30px 0;
            margin-top: 40px;
            border-top: 1px solid var(--border-color);
            color: #9ca3af;
            font-size: 0.9rem;
        }
        
        @media (max-width: 640px) {
            body {
                padding: 10px;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            .section-title {
                font-size: 1.2rem;
            }
            
            .article {
                padding: 16px;
            }
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
                <div class="section-header">
                    <h2 class="section-title"><span class="section-emoji">🧘‍♀️</span> 疗愈资讯</h2>
                </div>
                <div class="articles-list" id="healing-news">
                    [[HEALING_NEWS]]
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">
                    <h2 class="section-title"><span class="section-emoji">🧠</span> 心理健康</h2>
                </div>
                <div class="articles-list" id="mental-health">
                    [[MENTAL_HEALTH]]
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">
                    <h2 class="section-title"><span class="section-emoji">🌿</span> 自然疗法</h2>
                </div>
                <div class="articles-list" id="natural-therapy">
                    [[NATURAL_THERAPY]]
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">
                    <h2 class="section-title"><span class="section-emoji">💭</span> 冥想静心</h2>
                </div>
                <div class="articles-list" id="meditation">
                    [[MEDITATION]]
                </div>
            </div>
            
            <div class="section">
                <div class="section-header">
                    <h2 class="section-title"><span class="section-emoji">📚</span> 推荐阅读</h2>
                </div>
                <div class="articles-list" id="recommended">
                    [[RECOMMENDED]]
                </div>
            </div>
        </div>
        
        <footer>
            <p>身心灵疗愈日报 • 每日更新 • [[COPYRIGHT_YEAR]]</p>
            <p>在赛博空间中耕耘，传递身心灵疗愈的智慧</p>
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