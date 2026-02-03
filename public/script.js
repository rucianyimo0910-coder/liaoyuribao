// Healtherly Daily Report JavaScript

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    initializePage();
});

// 初始化页面
function initializePage() {
    updateCurrentDate();
    loadPreviousReports();
    loadRandomContent();
}

// 更新当前日期
function updateCurrentDate() {
    const now = new Date();
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        weekday: 'long'
    };
    const dateString = now.toLocaleDateString('zh-CN', options);
    document.getElementById('currentDate').textContent = dateString;
}

// 加载往期报告
function loadPreviousReports() {
    const previousReports = [
        { id: 1, title: "今日内心平静练习", date: "2026年2月2日" },
        { id: 2, title: "感恩与正念的力量", date: "2026年2月1日" },
        { id: 3, title: "情绪调节小技巧", date: "2026年1月31日" },
        { id: 4, title: "冥想入门指南", date: "2026年1月30日" },
        { id: 5, title: "身心灵平衡之道", date: "2026年1月29日" }
    ];
    
    const container = document.getElementById('previousReports');
    container.innerHTML = '';
    
    previousReports.forEach(report => {
        const li = document.createElement('li');
        li.className = 'nav-item';
        li.innerHTML = `
            <a href="#" onclick="loadReport(${report.id}); return false;">
                <strong>${report.title}</strong>
                <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 4px;">${report.date}</div>
            </a>
        `;
        container.appendChild(li);
    });
}

// 加载随机内容
function loadRandomContent() {
    // 随机疗愈语录
    const quotes = [
        { text: "宁静致远，心静自然凉。", author: "今日心灵寄语" },
        { text: "每一次呼吸，都是与生命的对话。", author: "正念导师" },
        { text: "内心平和，世界便温柔以待。", author: "心灵成长" },
        { text: "当下即是礼物，珍惜此刻美好。", author: "正念练习" },
        { text: "心怀感恩，生活处处是阳光。", author: "感恩练习" }
    ];
    
    // 随机冥想练习
    const meditations = [
        { title: "呼吸觉察练习", desc: "通过简单的呼吸觉察，连接当下，平静内心" },
        { title: "身体扫描冥想", desc: "从头到脚觉察身体各个部位，释放紧张感" },
        { title: "慈心冥想", desc: "培养对自己和他人的善意与慈悲" },
        { title: "正念行走", desc: "专注每一步的感受，与大地建立连接" }
    ];
    
    // 随机心理调适内容
    const psychologyTips = [
        { title: "情绪平衡小贴士", content: "当感到焦虑时，尝试将注意力放在身体的感受上，观察而不评判，让情绪自然流淌。" },
        { title: "压力缓解技巧", content: "深呼吸可以帮助激活副交感神经系统，缓解身体的压力反应。" },
        { title: "认知重构", content: "挑战消极思维，尝试从不同角度看待困难情境。" },
        { title: "自我关怀", content: "像对待好朋友一样对待自己，给予自己同样的善意和支持。" }
    ];
    
    // 随机正念练习
    const mindfulnessPractices = [
        { title: "日常正念时刻", content: "在喝水时，专注于水的温度、口感和吞咽的感觉，将意识带入当下。" },
        { title: "五感觉察", content: "花几分钟时间，依次觉察你所看到、听到、闻到、尝到和触摸到的事物。" },
        { title: "正念进食", content: "慢慢品尝食物，注意味道、质地和香气的变化。" },
        { title: "自然觉察", content: "观察一朵花、一片叶子或一棵树，全然地感受大自然的美好。" }
    ];
    
    // 随机感恩列表
    const gratitudeItems = [
        "温暖的阳光", "朋友的关怀", "内心的平静", "健康的身体",
        "美味的食物", "舒适的居所", "学习的机会", "爱与被爱的能力",
        "生命中的美好瞬间", "克服困难的勇气", "每一天的新开始", "大自然的馈赠"
    ];
    
    // 随机选择并更新内容
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    document.getElementById('dailyQuote').textContent = `"${randomQuote.text}"`;
    document.getElementById('quoteAuthor').textContent = `- ${randomQuote.author}`;
    
    const randomMeditation = meditations[Math.floor(Math.random() * meditations.length)];
    document.getElementById('meditationTitle').textContent = randomMeditation.title;
    document.getElementById('meditationDescription').textContent = randomMeditation.desc;
    
    const randomPsychology = psychologyTips[Math.floor(Math.random() * psychologyTips.length)];
    document.getElementById('psychologyTitle').textContent = randomPsychology.title;
    document.getElementById('psychologyContent').textContent = randomPsychology.content;
    
    const randomMindfulness = mindfulnessPractices[Math.floor(Math.random() * mindfulnessPractices.length)];
    document.getElementById('mindfulnessTitle').textContent = randomMindfulness.title;
    document.getElementById('mindfulnessContent').textContent = randomMindfulness.content;
    
    // 随机选择3个感恩项
    const shuffledGratitude = [...gratitudeItems].sort(() => 0.5 - Math.random());
    const selectedGratitude = shuffledGratitude.slice(0, 3);
    const gratitudeList = document.getElementById('gratitudeList');
    gratitudeList.innerHTML = '';
    selectedGratitude.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        gratitudeList.appendChild(li);
    });
}

// 开始冥想
function startMeditation() {
    // 创建冥想遮罩层
    let overlay = document.querySelector('.meditation-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'meditation-overlay';
        overlay.innerHTML = `
            <div class="meditation-modal">
                <h2>呼吸觉察练习</h2>
                <div class="breathing-guide">
                    <div class="circle">
                        <div class="inner-circle">吸气</div>
                    </div>
                </div>
                <p>跟随圆圈的节奏进行呼吸练习</p>
                <button onclick="exitMeditation()">结束冥想</button>
            </div>
        `;
        document.body.appendChild(overlay);
    }
    
    overlay.style.display = 'flex';
    
    // 开始呼吸动画
    animateBreathing();
}

// 结束冥想
function exitMeditation() {
    const overlay = document.querySelector('.meditation-overlay');
    if (overlay) {
        overlay.style.display = 'none';
    }
}

// 呼吸动画
function animateBreathing() {
    const circle = document.querySelector('.circle');
    if (!circle) return;
    
    let isExpanding = true;
    let scale = 1;
    const duration = 8000; // 8秒循环
    
    function pulse() {
        const timestamp = performance.now();
        const progress = (timestamp % duration) / duration;
        
        // 使用正弦波函数创建平滑的呼吸效果
        scale = 0.8 + 0.4 * Math.abs(Math.sin(progress * Math.PI));
        circle.style.transform = `scale(${scale})`;
        
        requestAnimationFrame(pulse);
    }
    
    pulse();
}

// 加载特定报告（模拟功能）
function loadReport(id) {
    alert(`正在加载报告 ${id}... 此功能将在完整版本中实现`);
}

// 添加冥想覆盖层样式
const meditationStyles = `
.meditation-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(24, 26, 28, 0.95);
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}

.meditation-modal {
    background: rgba(30, 32, 34, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 40px;
    text-align: center;
    max-width: 400px;
    width: 90%;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.breathing-guide {
    margin: 30px 0;
}

.circle {
    width: 200px;
    height: 200px;
    border: 2px solid rgba(94, 124, 224, 0.5);
    border-radius: 50%;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 4s ease-in-out;
}

.inner-circle {
    width: 140px;
    height: 140px;
    background: rgba(94, 124, 224, 0.1);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #a3baff;
    font-weight: 500;
    font-size: 1.1rem;
}

.meditation-modal h2 {
    color: #fff;
    margin-bottom: 20px;
    font-size: 1.5rem;
}

.meditation-modal p {
    color: #8a9ba8;
    margin-bottom: 20px;
}

.meditation-modal button {
    padding: 12px 24px;
    background: rgba(94, 124, 224, 0.15);
    border: 1px solid rgba(94, 124, 224, 0.3);
    color: #a3baff;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.meditation-modal button:hover {
    background: rgba(94, 124, 224, 0.25);
    border-color: rgba(94, 124, 224, 0.5);
    color: #fff;
}
`;

// 添加冥想样式到页面
const styleSheet = document.createElement('style');
styleSheet.textContent = meditationStyles;
document.head.appendChild(styleSheet);

// 键盘快捷键
document.addEventListener('keydown', function(e) {
    // ESC键退出冥想
    if (e.key === 'Escape') {
        exitMeditation();
    }
});