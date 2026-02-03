// 身心灵疗愈日报 - 交互功能

// 冥想练习数据
const meditations = [
    {
        title: "呼吸觉察练习",
        desc: "通过简单的呼吸觉察，连接当下，平静内心。"
    },
    {
        title: "身体扫描冥想",
        desc: "从头到脚逐一关注身体各个部位，释放紧张与压力。"
    },
    {
        title: "慈心冥想",
        desc: "培养对自己和他人的慈悲心，感受内在的温暖。"
    },
    {
        title: "正念行走",
        desc: "将正念带入每一步行走，感受与大地的连接。"
    },
    {
        title: "观息法",
        desc: "单纯地观察呼吸的进出，不加任何控制。"
    },
    {
        title: "全身放松冥想",
        desc: "通过渐进式肌肉放松，达到身心合一的平静。"
    },
    {
        title: "觉知当下冥想",
        desc: "放下过去与未来的牵挂，全然体验当下这一刻。"
    },
    {
        title: "感恩冥想",
        desc: "怀着感恩之心，感受生活中的美好与恩赐。"
    }
];

// 心理调适技巧
const psychologyTips = [
    {
        title: "情绪平衡小贴士",
        content: "当感到焦虑时，尝试将注意力放在身体的感受上，观察而不评判，让情绪自然流淌。"
    },
    {
        title: "压力管理策略",
        content: "学会说"不"，为自己设立健康的界限，减少不必要的压力。"
    },
    {
        title: "自我关怀技巧",
        content: "每天给自己一些独处的时间，做一些让自己愉悦的事情。"
    },
    {
        title: "焦虑缓解方法",
        content: "深呼吸练习可以帮助激活副交感神经系统，缓解焦虑情绪。"
    },
    {
        title: "睡眠改善建议",
        content: "建立规律的作息时间，睡前远离电子设备，创造舒适的睡眠环境。"
    },
    {
        title: "人际关系智慧",
        content: "真诚地表达自己的感受和需求，同时尊重他人的界限。"
    },
    {
        title: "自信建立方法",
        content: "每天记录三件值得感激的事情，培养积极的心态。"
    },
    {
        title: "边界设定技巧",
        content: "定期评估自己的精力和情绪状态，适时调整节奏。"
    }
];

// 正念练习
const mindfulnessPractices = [
    {
        title: "日常正念时刻",
        content: "在喝水时，专注于水的温度、口感和吞咽的感觉，将意识带入当下。"
    },
    {
        title: "五感觉察练习",
        content: "花几分钟时间，依次关注视觉、听觉、嗅觉、味觉、触觉，增强感官觉察力。"
    },
    {
        title: "正念饮食",
        content: "慢慢咀嚼每一口食物，感受味道、质地和香气的变化，享受进食的过程。"
    },
    {
        title: "情绪正念",
        content: "当情绪升起时，不评判地观察它，像天空包容云朵一样包容情绪。"
    },
    {
        title: "正念聆听",
        content: "专心聆听周围的声音，即使是微小的声音，培养专注力和平静心。"
    },
    {
        title: "呼吸正念",
        content: "将注意力集中在呼吸上，感受气息进出鼻腔的细微感觉。"
    },
    {
        title: "步行正念",
        content: "走路时注意脚底与地面接触的感觉，以及身体的运动节奏。"
    },
    {
        title: "身体正念",
        content: "闭上眼睛，用手触摸不同的物体，专注于触觉感受。"
    }
];

// 每日心灵寄语
const dailyQuotes = [
    {
        text: "内心的平静是一切幸福的源泉。",
        author: "古代智者"
    },
    {
        text: "每一天都是重新开始的机会。",
        author: "心灵导师"
    },
    {
        text: "静心冥想，倾听内在的声音。",
        author: "冥想大师"
    },
    {
        text: "感恩当下，拥抱此刻的美好。",
        author: "禅宗智慧"
    },
    {
        text: "爱自己，是一切治愈的开始。",
        author: "现代心理学"
    },
    {
        text: "呼吸是生命最简单的冥想。",
        author: "瑜伽哲学"
    },
    {
        text: "宁静致远，淡泊明志。",
        author: "道家哲学"
    },
    {
        text: "万物皆有时，顺其自然。",
        author: "佛学经典"
    },
    {
        text: "慈悲是最高级的力量。",
        author: "佛教智慧"
    },
    {
        text: "每一次呼吸，都是生命的礼物。",
        author: "生命哲学"
    }
];

// 感恩事项
const gratitudeItems = [
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
];

// 往期回顾
const previousReports = [
    "1月30日 • 内心平静之道",
    "1月31日 • 自我关怀实践",
    "2月1日 • 正念生活",
    "2月2日 • 情绪管理",
    "2月3日 • 今日疗愈之旅"
];

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 随机显示冥想练习
    const randomMeditation = meditations[Math.floor(Math.random() * meditations.length)];
    document.getElementById('meditationTitle').textContent = randomMeditation.title;
    document.getElementById('meditationDescription').textContent = randomMeditation.desc;
    
    // 随机显示心理调适技巧
    const randomPsychology = psychologyTips[Math.floor(Math.random() * psychologyTips.length)];
    document.getElementById('psychologyTitle').textContent = randomPsychology.title;
    document.getElementById('psychologyContent').textContent = randomPsychology.content;
    
    // 随机显示正念练习
    const randomMindfulness = mindfulnessPractices[Math.floor(Math.random() * mindfulnessPractices.length)];
    document.getElementById('mindfulnessTitle').textContent = randomMindfulness.title;
    document.getElementById('mindfulnessContent').textContent = randomMindfulness.content;
    
    // 随机显示每日寄语
    const randomQuote = dailyQuotes[Math.floor(Math.random() * dailyQuotes.length)];
    document.querySelector('#dailyQuote').textContent = `"${randomQuote.text}"`;
    document.getElementById('quoteAuthor').textContent = `- ${randomQuote.author}`;
    
    // 显示感恩事项（随机选择3项）
    const shuffledGratitude = [...gratitudeItems].sort(() => 0.5 - Math.random());
    const selectedGratitude = shuffledGratitude.slice(0, 3);
    const gratitudeContainer = document.querySelector('.gratitude-grid');
    if (gratitudeContainer) {
        gratitudeContainer.innerHTML = '';
        selectedGratitude.forEach(item => {
            const gratitudeElement = document.createElement('div');
            gratitudeElement.className = 'gratitude-item';
            gratitudeElement.innerHTML = `
                <span class="gratitude-icon">💝</span>
                <span class="gratitude-text">${item}</span>
            `;
            gratitudeContainer.appendChild(gratitudeElement);
        });
    }
    
    // 显示往期回顾（最近5项）
    const archiveContainer = document.querySelector('.archive-grid');
    if (archiveContainer) {
        archiveContainer.innerHTML = '';
        previousReports.slice(0, 4).forEach(report => {
            const archiveElement = document.createElement('a');
            archiveElement.href = '#';
            archiveElement.className = 'archive-item';
            archiveElement.textContent = report;
            archiveContainer.appendChild(archiveElement);
        });
    }
    
    // 更新日期
    const now = new Date();
    const dateStr = now.getFullYear() + '年' + 
                   (now.getMonth() + 1) + '月' + 
                   now.getDate() + '日 ' + 
                   String(now.getHours()).padStart(2, '0') + ':' + 
                   String(now.getMinutes()).padStart(2, '0') + ':' + 
                   String(now.getSeconds()).padStart(2, '0') + '更新';
    document.querySelector('.date-text').textContent = dateStr;
});

// 冥想功能
function startMeditation() {
    // 创建冥想遮罩层
    let overlay = document.querySelector('.meditation-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'meditation-overlay';
        overlay.innerHTML = `
            <div class="meditation-modal">
                <h2>冥想引导</h2>
                <p>找一个安静的地方坐下，闭上眼睛，跟随呼吸的节奏...</p>
                <div class="breathing-animation">
                    <div class="circle"></div>
                </div>
                <p class="instruction">吸气... 屏息... 呼气...</p>
                <button onclick="exitMeditation()">结束冥想</button>
            </div>
        `;
        document.body.appendChild(overlay);
    }
    
    // 显示遮罩层
    overlay.style.display = 'flex';
    
    // 开始呼吸动画
    animateBreathing();
}

function exitMeditation() {
    const overlay = document.querySelector('.meditation-overlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}

function animateBreathing() {
    const circle = document.querySelector('.breathing-animation .circle');
    if (!circle) return;
    
    // 呼吸动画循环
    function breathe() {
        circle.animate([
            { transform: 'scale(1)', backgroundColor: 'rgba(94, 124, 224, 0.3)' },
            { transform: 'scale(1.5)', backgroundColor: 'rgba(94, 124, 224, 0.6)' },
            { transform: 'scale(1)', backgroundColor: 'rgba(94, 124, 224, 0.3)' }
        ], {
            duration: 6000, // 6秒一个循环
            iterations: Infinity
        });
    }
    
    breathe();
}

// 添加冥想样式到页面
const meditationStyles = `
.meditation-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.meditation-modal {
    background: var(--bg-panel);
    padding: 2rem;
    border-radius: var(--radius-xl);
    text-align: center;
    max-width: 90%;
    width: 500px;
    border: var(--border);
    box-shadow: var(--shadow-lg);
    position: relative;
}

.meditation-modal h2 {
    margin-bottom: 1rem;
    color: var(--accent-primary);
    font-size: var(--font-xl);
}

.meditation-modal p {
    margin-bottom: 1.5rem;
    color: var(--text-secondary);
}

.breathing-animation {
    margin: 2rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.breathing-animation .circle {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: rgba(94, 124, 224, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}

.instruction {
    font-style: italic;
    color: var(--text-tertiary);
    margin-bottom: 1.5rem;
}

.meditation-modal button {
    background: var(--accent-primary);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-md);
    cursor: pointer;
    font-weight: 500;
    transition: var(--transition-fast);
}

.meditation-modal button:hover {
    background: var(--accent-secondary);
}
`;

// 将冥想样式注入到页面
const styleSheet = document.createElement('style');
styleSheet.textContent = meditationStyles;
document.head.appendChild(styleSheet);

// 侧边栏导航交互
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        
        // 移除所有活动状态
        document.querySelectorAll('.nav-link').forEach(l => {
            l.classList.remove('active');
        });
        
        // 添加活动状态到当前链接
        this.classList.add('active');
        
        // 这里可以添加页面内容切换逻辑
        console.log('导航到:', this.querySelector('.nav-text').textContent);
    });
});

// 档案项点击事件
document.querySelectorAll('.archive-item').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        console.log('查看档案:', this.textContent);
    });
});