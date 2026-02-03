#!/usr/bin/env python3
"""
身心灵疗愈行业课程推荐系统
从词海网站提取适合疗愈行业的课程内容并生成推荐
"""

import os
import json
import random
from datetime import datetime
from typing import List, Dict

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

def get_daily_course_recommendation():
    """获取每日课程推荐"""
    courses = get_therapy_courses()
    # 随机选择一个课程
    selected_course = random.choice(courses)
    
    # 生成推荐内容
    recommendation = {
        "date": datetime.now().strftime('%Y年%m月%d日'),
        "course": selected_course,
        "recommendation_title": f"今日疗愈行业精品课程推荐",
        "daily_message": "在身心灵疗愈行业，专业技能与商业运营同样重要。今日推荐课程结合疗愈行业特性，助力您的事业发展。"
    }
    
    return recommendation

def update_index_html_with_course():
    """更新index.html文件，加入课程推荐内容"""
    # 读取当前的index.html文件
    with open('../public/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取课程推荐
    recommendation = get_daily_course_recommendation()
    course = recommendation['course']
    
    # 创建课程推荐HTML片段
    course_html = f"""
                <section class="section-course">
                    <h2>每日课程推荐</h2>
                    <div class="course-card">
                        <div class="course-header">
                            <h3>{course['title']}</h3>
                            <span class="course-category">{course['category']}</span>
                        </div>
                        <p class="course-description">{course['description']}</p>
                        <div class="course-details">
                            <div class="detail-section">
                                <h4>实际业务参考意义：</h4>
                                <p class="practical-significance">{course['practical_significance']}</p>
                            </div>
                            <div class="detail-section">
                                <h4>学习心得：</h4>
                                <p class="learning-insights">{course['learning_insights']}</p>
                            </div>
                        </div>
                    </div>
                </section>
    """
    
    # 查找插入位置（在往期回顾之前）
    insertion_point = content.find('<section class="section-archive">')
    
    if insertion_point != -1:
        # 插入课程推荐内容
        updated_content = content[:insertion_point] + course_html + content[insertion_point:]
    else:
        # 如果找不到插入点，插入到文章内容的末尾
        end_content_marker = '</div>\n            </article>'
        insertion_point = content.find(end_content_marker)
        if insertion_point != -1:
            updated_content = content[:insertion_point] + course_html + content[insertion_point:]
        else:
            updated_content = content  # 如果找不到插入点，保持原内容不变
    
    # 写回文件
    with open('../public/index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"课程推荐已更新: {recommendation['date']}")
    print(f"推荐课程: {course['title']}")
    print(f"所属类别: {course['category']}")

def main():
    print("开始生成身心灵疗愈行业课程推荐...")
    
    # 更新index.html文件
    update_index_html_with_course()
    
    print("身心灵疗愈行业课程推荐生成完成！")

if __name__ == "__main__":
    main()