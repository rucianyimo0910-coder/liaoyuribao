# 身心灵疗愈日报 - Healtherly Daily Report

一个自动生成的身心灵疗愈行业日报，每日更新最新资讯、心理健康知识、自然疗法、冥想指导等内容。

## 项目结构

```
healtherly-daily-report/
├── src/                    # 源代码目录
│   └── generate_report.py  # 日报生成脚本
├── public/                 # 静态网站输出目录
│   └── index.html          # 生成的日报页面
├── .github/workflows/      # GitHub Actions 工作流
│   └── deploy.yml          # 自动部署配置
└── README.md               # 项目说明
```

## 功能特点

- 🧘‍♀️ **疗愈资讯**: 最新的身心灵疗愈行业动态
- 🧠 **心理健康**: 心理学研究与情绪管理技巧
- 🌿 **自然疗法**: 芳香疗法、森林浴等自然疗愈方法
- 💭 **冥想静心**: 冥想指导与正念练习
- 📚 **推荐阅读**: 疗愈类书籍与音乐推荐

## 自动部署

- 使用 GitHub Actions 每日自动生成报告
- 自动部署到 GitHub Pages
- 每日更新时间为北京时间下午 4 点

## 手动运行

如果需要手动运行生成日报：

```bash
cd healtherly-daily-report
python src/generate_report.py
```

生成的报告将位于 `public/index.html`。

## 自定义配置

你可以修改以下内容来定制日报：

1. `src/generate_report.py`: 修改数据源和内容生成逻辑
2. `public/index.html`: 修改页面样式和布局
3. `.github/workflows/deploy.yml`: 修改部署时间和频率

## 扩展功能

日报目前包含以下板块：

- 疗愈资讯
- 心理健康
- 自然疗法
- 冥想静心
- 推荐阅读

未来可以扩展更多板块，如瑜伽指导、营养疗愈、艺术治疗等。

## 许可证

MIT License