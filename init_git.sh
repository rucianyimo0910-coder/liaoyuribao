#!/bin/bash
# 初始化 GitHub 仓库脚本

echo "初始化 Git 仓库..."

git init
git add .
git commit -m "Initial commit: Healtherly Daily Report"

echo "请按照以下步骤将项目推送到 GitHub:"
echo "1. 在 GitHub 上创建一个新仓库"
echo "2. 运行以下命令（将 <your-repository-url> 替换为你的仓库地址）:"
echo "   git remote add origin <your-repository-url>"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "设置 GitHub Pages:"
echo "1. 进入仓库设置页面"
echo "2. 找到 'Pages' 选项"
echo "3. 将源设置为 'Deploy from a branch'"
echo "4. 选择 'gh-pages' 分支，'/root' 文件夹"
echo ""
echo "或者使用 GitHub Actions 自动部署:"
echo "1. 在仓库中启用 Actions"
echo "2. 工作流文件已创建在 .github/workflows/deploy.yml"
echo "3. 它将在每天北京时间下午 4 点自动生成并部署新的日报"