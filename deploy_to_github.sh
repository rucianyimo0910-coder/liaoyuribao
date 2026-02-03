#!/bin/bash

# 身心灵疗愈日报 GitHub 部署脚本

echo "🌿 身心灵疗愈日报 - GitHub 部署脚本"
echo "=================================="

# 检查是否在项目目录中
if [ ! -f "public/index.html" ]; then
    echo "❌ 错误: 未找到项目文件，请在 healtherly-daily-report 目录中运行此脚本"
    exit 1
fi

echo "✅ 检测到项目文件"

# 检查 Git 是否已安装
if ! command -v git &> /dev/null; then
    echo "❌ 错误: Git 未安装"
    exit 1
fi

echo "✅ Git 已安装"

# 检查当前 Git 状态
if [ ! -d ".git" ]; then
    echo "❌ 错误: 当前目录不是 Git 仓库"
    echo "💡 提示: 请先运行 'git init' 初始化仓库"
    exit 1
fi

echo "✅ Git 仓库已存在"

# 获取当前分支
BRANCH=$(git branch --show-current)
if [ "$BRANCH" != "main" ]; then
    echo "🔄 切换到 main 分支"
    git checkout -b main 2>/dev/null || git checkout main
fi

# 添加所有文件
echo "📁 添加所有文件到暂存区..."
git add .

# 检查是否有更改需要提交
if git diff --cached --quiet; then
    echo "✅ 没有新更改需要提交"
else
    echo "📝 提交更改..."
    git commit -m "Deploy: 身心灵疗愈日报项目更新 $(date '+%Y-%m-%d %H:%M:%S')"
    echo "✅ 更改已提交"
fi

# 获取远程仓库信息
REMOTE_URL=$(git remote get-url origin 2>/dev/null)

if [ -z "$REMOTE_URL" ]; then
    echo ""
    echo "⚠️  远程仓库未配置"
    echo ""
    echo "请按照以下步骤设置远程仓库："
    echo ""
    echo "1. 在 GitHub 上创建新仓库 (例如: healtherly-daily-report)"
    echo "2. 运行以下命令 (将 YOUR_USERNAME 替换为您的 GitHub 用户名):"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/healtherly-daily-report.git"
    echo "3. 然后重新运行此脚本"
    echo ""
    echo "或者使用 SSH 方式 (需要预先配置 SSH 密钥):"
    echo "   git remote add origin git@github.com:YOUR_USERNAME/healtherly-daily-report.git"
    echo ""
    exit 1
fi

echo "🌐 远程仓库: $REMOTE_URL"

# 检查是否为 GitHub 仓库
if [[ "$REMOTE_URL" != *"github.com"* ]]; then
    echo "⚠️  远程仓库不是 GitHub 仓库，但仍可尝试推送..."
fi

echo "📤 正在推送代码到 GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功部署到 GitHub!"
    echo "🔗 您的项目地址: $REMOTE_URL"
    echo ""
    echo "💡 提示: 如果这是首次推送，请检查 GitHub 仓库是否包含所有文件"
else
    echo ""
    echo "❌ 推送失败，请检查错误信息"
    echo ""
    echo "常见解决方案:"
    echo "- 确保您有仓库的写入权限"
    echo "- 检查网络连接"
    echo "- 如果使用 HTTPS，可能需要配置个人访问令牌"
    echo "- 如果使用 SSH，确保 SSH 密钥已正确配置"
    echo ""
fi