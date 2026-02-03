#!/usr/bin/env python3
"""
身心灵疗愈行业日报生成器 - 适配参考网站设计风格（含课程推荐）
"""
import os
import json
import random
from datetime import datetime
from urllib.parse import urljoin
import re

def get_daily_quote():
    """获取每日心灵寄语"""
    quotes = [
        "内心的平静是一切幸福的源泉。",
        "每一天都是重新开始的机会。",
        "静心冥想，倾听内在的声音。",
        "感恩当下，拥抱此刻的美好。",
        "爱自己，是一切治愈的开始。",
        "呼吸是生命最简单的冥想。",
        "宁静致远，淡泊明志。",
        "万物皆有时，顺其自然。",
        "慈悲是最高级的力量。",
        "每一次呼吸，都是生命的礼物。"
    ]
    authors = [
        "古代智者",
        "心灵导师",
        "冥想大师",
        "禅宗智慧",
        "道家哲学",
        "现代心理学",
        "瑜伽哲学",
        "佛学经典"
    ]
    return {
        "text": random.choice(quotes),
        "author": random.choice(authors)
    }

def get_meditation_exercise():
    """获取冥想练习"""
    titles = [
        "呼吸觉察练习",
        "身体扫描冥想",
        "慈心冥想",
        "正念行走",
        "观息法",
        "全身放松冥想",
        "觉知当下冥想",
        "感恩冥想"
    ]
    descriptions = [
        "通过简单的呼吸觉察，连接当下，平静内心。",
        "从头到脚逐一关注身体各个部位，释放紧张与压力。",
        "培养对自己和他人的慈悲心，感受内在的温暖。",
        "将正念带入每一步行走，感受与大地的连接。",
        "单纯地观察呼吸的进出，不加任何控制。",
        "通过渐进式肌肉放松，达到身心合一的平静。",
        "放下过去与未来的牵挂，全然体验当下这一刻。",
        "怀着感恩之心，感受生活中的美好与恩赐。"
    ]
    return {
        "title": random.choice(titles),
        "description": random.choice(descriptions)
    }

def get_psychology_tips():
    """获取心理调适技巧"""
    titles = [
        "情绪平衡小贴士",
        "压力管理策略",
        "自我关怀技巧",
        "焦虑缓解方法",
        "睡眠改善建议",
        "人际关系智慧",
        "自信建立方法",
        "边界设定技巧"
    ]
    contents = [
        "当感到焦虑时，尝试将注意力放在身体的感受上，观察而不评判，让情绪自然流淌。",
        '学会说"不"，为自己设立健康的界限，减少不必要的压力。',
        "每天给自己一些独处的时间，做一些让自己愉悦的事情。",
        "深呼吸练习可以帮助激活副交感神经系统，缓解焦虑情绪。",
        "建立规律的作息时间，睡前远离电子设备，创造舒适的睡眠环境。",
        "真诚地表达自己的感受和需求，同时尊重他人的界限。",
        "每天记录三件值得感激的事情，培养积极的心态。",
        "定期评估自己的精力和情绪状态，适时调整节奏。"
    ]
    return {
        "title": random.choice(titles),
        "content": random.choice(contents)
    }

def get_mindfulness_practice():
    """获取正念练习"""
    titles = [
        "日常正念时刻",
        "五感觉察练习",
        "正念饮食",
        "情绪正念",
        "正念聆听",
        "呼吸正念",
        "步行正念",
        "身体正念"
    ]
    contents = [
        "在喝水时，专注于水的温度、口感和吞咽的感觉，将意识带入当下。",
        "花几分钟时间，依次关注视觉、听觉、嗅觉、味觉、触觉，增强感官觉察力。",
        "慢慢咀嚼每一口食物，感受味道、质地和香气的变化，享受进食的过程。",
        "当情绪升起时，不评判地观察它，像天空包容云朵一样包容情绪。",
        "专心聆听周围的声音，即使是微小的声音，培养专注力和平静心。",
        "将注意力集中在呼吸上，感受气息进出鼻腔的细微感觉。",
        "走路时注意脚底与地面接触的感觉，以及身体的运动节奏。",
        "闭上眼睛，用手触摸不同的物体，专注于触觉感受。"
    ]
    return {
        "title": random.choice(titles),
        "content": random.choice(contents)
    }

def get_gratitude_items():
    """获取感恩事项"""
    items = [
        "感谢阳光透过窗户洒在脸上的温暖",
        "感谢身边朋友的陪伴与支持",
        "感谢今天遇到的一个微笑",
        "感谢自己的努力和成长",
        "感谢大自然的美丽与宁静",
        "感谢拥有的健康身体",
        "感谢每一次学习的机会",
        "感谢内心的平静时刻",
        "感谢家人的关爱",
        "感谢今天的小小成就"
    ]
    # 随机选择3个项目
    selected = random.sample(items, min(3, len(items)))
    return selected

def get_previous_reports():
    """生成往期回顾内容"""
    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    days = [str(i) for i in range(1, 31)]
    
    reports = []
    for _ in range(5):
        month = random.choice(months)
        day = random.choice(days)
        reports.append(f"{month}{day}日 • 内心探索之旅")
    
    return reports

def get_therapy_courses():
    """获取适合疗愈行业的课程"""
    courses = [
        {
            "title": "疗愈师私域流量运营实战",
            "category": "私域运营",
            "description": "针对身心灵疗愈师的私域流量建设方法，包括客户关系维护、信任建立和长期价值输出",
            "practical_significance": "疗愈行业高度依赖个人品牌和信任关系，私域运营能有效维护老客户，提高复购率和转介绍率，降低获客成本",
            "learning_insights": "通过建立疗愈社群，可以定期分享疗愈知识，增加客户粘性，同时通过一对一咨询建立深度信任关系"
        },
        {
            "title": "身心灵工作室品牌定位策略",
            "category": "品牌建设",
            "description": "身心灵疗愈工作室如何打造独特品牌形象，建立专业权威和客户信任",
            "practical_significance": "疗愈行业竞争激烈，明确的品牌定位有助于在目标客户心中建立差异化认知，提高转化率和客单价",
            "learning_insights": "通过精准定位目标人群，打造专属疗愈理念，形成口碑传播效应，提升客户忠诚度"
        },
        {
            "title": "疗愈服务定价策略与销售技巧",
            "category": "销售技巧",
            "description": "身心灵疗愈服务如何合理定价，以及在咨询过程中运用销售技巧达成交易",
            "practical_significance": "疗愈服务定价直接影响盈利能力和市场定位，合适的销售技巧能帮助客户认识到疗愈价值，提升成交率",
            "learning_insights": "通过价值包装和效果展示，让客户理解疗愈投资的重要性，同时运用咨询技巧深入了解客户需求"
        },
        {
            "title": "线上疗愈课程制作与推广",
            "category": "内容营销",
            "description": "如何制作高质量的线上疗愈课程内容，并通过多渠道进行有效推广",
            "practical_significance": "线上课程可以扩大服务范围，提升影响力，同时建立被动收入来源，增加收入多样性",
            "learning_insights": "通过系列化课程设计，循序渐进地引导学员，建立完整疗愈体系，增强用户粘性"
        },
        {
            "title": "疗愈师社交媒体营销策略",
            "category": "社交媒体",
            "description": "身心灵疗愈师如何利用微信、抖音、小红书等平台进行品牌宣传和客户获取",
            "practical_significance": "社交媒体是现代疗愈师的重要获客渠道，通过内容输出建立专业形象，吸引精准客户",
            "learning_insights": "通过分享疗愈案例（保护隐私前提下）、疗愈知识科普等方式，建立专业权威，引导潜在客户"
        },
        {
            "title": "疗愈工作室会员制运营模式",
            "category": "商业模式",
            "description": "身心灵疗愈工作室如何设计会员制度，实现客户留存和稳定收入",
            "practical_significance": "会员制模式能保证稳定现金流，提高客户生命周期价值，同时便于提供持续性疗愈服务",
            "learning_insights": "通过分级会员权益设计，满足不同客户群体需求，同时提供持续性疗愈支持"
        },
        {
            "title": "疗愈师客户沟通与信任建立",
            "category": "客户服务",
            "description": "身心灵疗愈师如何与客户建立深层信任关系，提升服务满意度和转介绍率",
            "practical_significance": "疗愈服务高度依赖信任关系，良好的沟通技巧能提升服务质量，增加客户满意度和口碑传播",
            "learning_insights": "通过倾听技巧和共情能力，深入了解客户需求，建立安全的疗愈环境，提升服务效果"
        },
        {
            "title": "疗愈行业公域流量获取策略",
            "category": "流量获取",
            "description": "身心灵疗愈师如何在各大公域平台获取精准流量，转化为私域客户",
            "practical_significance": "公域流量是私域建设的基础，通过多平台布局扩大潜在客户池，提升整体获客效率",
            "learning_insights": "通过内容营销和专业输出，建立行业影响力，吸引精准客户关注，再引导至私域深入转化"
        }
    ]
    return courses

def update_index_html():
    """更新index.html文件，保留原有设计结构"""
    # 读取当前的index.html文件
    with open('public/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取新的内容
    quote = get_daily_quote()
    meditation = get_meditation_exercise()
    psychology = get_psychology_tips()
    mindfulness = get_mindfulness_practice()
    gratitude_items = get_gratitude_items()
    previous_reports = get_previous_reports()
    
    # 随机选择一个课程
    courses = get_therapy_courses()
    selected_course = random.choice(courses)
    
    # 更新日期
    today = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S更新')
    content = re.sub(r'<time class="post-date" id="currentDate">[^<]*</time>', 
                     f'<time class="post-date" id="currentDate">{today.split()[0]}</time>', content)
    
    # 更新每日心灵寄语
    # 查找并更新第一个引用块（保持原有的引用样式）
    content = re.sub(r'<blockquote id="dailyQuote">[^<]*</blockquote>',
                     f'<blockquote id="dailyQuote">"{quote["text"]}"</blockquote>', content)
    content = re.sub(r'<cite id="quoteAuthor">[^<]*</cite>', 
                     f'<cite id="quoteAuthor">- {quote["author"]}</cite>', content)
    
    # 更新冥想练习
    content = re.sub(r'<h3 id="meditationTitle">[^<]*</h3>',
                     f'<h3 id="meditationTitle">{meditation["title"]}</h3>', content)
    content = re.sub(r'<p id="meditationDescription">[^<]*</p>',
                     f'<p id="meditationDescription">{meditation["description"]}</p>', content)
    
    # 更新心理调适
    content = re.sub(r'<h3 id="psychologyTitle">[^<]*</h3>',
                     f'<h3 id="psychologyTitle">{psychology["title"]}</h3>', content)
    content = re.sub(r'<p id="psychologyContent">[^<]*</p>',
                     f'<p id="psychologyContent">{psychology["content"]}</p>', content)
    
    # 更新正念练习
    content = re.sub(r'<h3 id="mindfulnessTitle">[^<]*</h3>',
                     f'<h3 id="mindfulnessTitle">{mindfulness["title"]}</h3>', content)
    content = re.sub(r'<p id="mindfulnessContent">[^<]*</p>',
                     f'<p id="mindfulnessContent">{mindfulness["content"]}</p>', content)
    
    # 更新感恩列表
    gratitude_html = "\n".join([f'                            <li class="gratitude-item">\n                                <span class="gratitude-emoji">💝</span>\n                                <span class="gratitude-text">{item}</span>\n                            </li>' for item in gratitude_items])
    content = re.sub(r'<ul class="gratitude-list" id="gratitudeList">[\s\S]*?</ul>',
                     f'<ul class="gratitude-list" id="gratitudeList">\n{gratitude_html}\n                        </ul>', content)
    
    # 更新往期回顾
    previous_html = "\n".join([f'                            <li><a href="#">{report}</a></li>' for report in previous_reports])
    content = re.sub(r'<ul class="archive-list" id="previousReports">[\s\S]*?</ul>',
                     f'<ul class="archive-list" id="previousReports">\n{previous_html}\n                        </ul>', content)
    
    # 创建课程推荐HTML片段
    course_html = f'''
                    <section class="section-course">
                        <h2>每日课程推荐</h2>
                        <div class="course-card">
                            <div class="course-header">
                                <h3>{selected_course["title"]}</h3>
                                <span class="course-category">{selected_course["category"]}</span>
                            </div>
                            <p class="course-description">{selected_course["description"]}</p>
                            <div class="course-details">
                                <div class="detail-section">
                                    <h4>实际业务参考意义：</h4>
                                    <p class="practical-significance">{selected_course["practical_significance"]}</p>
                                </div>
                                <div class="detail-section">
                                    <h4>学习心得：</h4>
                                    <p class="learning-insights">{selected_course["learning_insights"]}</p>
                                </div>
                            </div>
                        </div>
                    </section>'''
    
    # 查找插入位置（在感恩日记之后，往期回顾之前）
    gratitude_end_pos = content.find('</ul>') + 5  # 结束ul标签的位置
    archive_start_pos = content.find('<section class="section-archive">')
    
    if gratitude_end_pos != -1 and archive_start_pos != -1 and gratitude_end_pos < archive_start_pos:
        updated_content = content[:gratitude_end_pos] + course_html + content[archive_start_pos:]
    else:
        # 如果找不到合适位置，插入到文章内容的末尾，在归档部分之前
        content_end_marker = '\n                </div>\n            </article>'
        content_end_pos = content.find(content_end_marker)
        if content_end_pos != -1:
            updated_content = content[:content_end_pos] + course_html + content[content_end_pos:]
        else:
            updated_content = content
    
    # 写回文件
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"日报已更新: {today}")
    print(f"包含 {len(gratitude_items)} 项感恩内容")
    print(f"往期回顾包含 {len(previous_reports)} 条记录")
    print(f"推荐课程: {selected_course['title']}")
    print(f"课程类别: {selected_course['category']}")


def main():
    print("开始生成身心灵疗愈日报...")
    
    # 更新index.html文件
    update_index_html()
    
    print("身心灵疗愈日报生成完成！")


if __name__ == "__main__":
    main()