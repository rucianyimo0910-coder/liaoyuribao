#!/bin/bash

# 身心灵疗愈日报 - GitHub 设置和部署脚本

echo "🌿 身心灵疗愈日报 - GitHub 设置和部署"
echo "====================================="

# 检查是否在项目目录中
if [ ! -f "public/index.html" ]; then
    echo "❌ 错误: 未找到项目文件，请在 healtherly-daily-report 目录中运行此脚本"
    exit 1
fi

echo "✅ 检测到项目文件"

# 检查SSH连接
echo "🔍 检查SSH连接到GitHub..."
ssh_result=$(ssh -T git@github.com 2>&1 | grep -c "successfully authenticated")

if [ $ssh_result -gt 0 ]; then
    echo "✅ SSH连接成功"
else
    echo "❌ SSH连接失败"
    exit 1
fi

# 获取GitHub用户名
GITHUB_USER=$(ssh -T git@github.com 2>&1 | grep -oE "Hi [^!]*!" | cut -d' ' -f2 | tr -d '!')

if [ -z "$GITHUB_USER" ]; then
    echo "❌ 无法获取GitHub用户名"
    exit 1
fi

echo "👤 检测到GitHub用户名: $GITHUB_USER"

# 检查是否存在远程仓库
if [ -z "$(git remote -v)" ]; then
    REPO_NAME="healtherly-daily-report"
    
    # 尝试创建远程仓库或提示用户创建
    echo "📡 设置远程仓库..."
    echo "💡 如果这是新仓库，您需要先在GitHub上创建: $REPO_NAME"
    git remote add origin git@github.com:$GITHUB_USER/$REPO_NAME.git
    echo "✅ 远程仓库已设置: git@github.com:$GITHUB_USER/$REPO_NAME.git"
else
    echo "📡 已存在远程仓库配置"
    git remote -v
fi

# 确保在main分支
git checkout main

# 推送代码到GitHub
echo "📤 正在推送代码到GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功部署到 GitHub!"
    echo "🔗 您的项目地址: https://github.com/$GITHUB_USER/$REPO_NAME"
    echo ""
    echo "🌐 您也可以通过 GitHub Pages 访问您的应用 (如果启用):"
    echo "   https://$GITHUB_USER.github.io/$REPO_NAME"
    echo ""
else
    echo ""
    echo "❌ 推送失败，错误信息如下："
    echo "可能的原因："
    echo "  1. GitHub上不存在该仓库，请先在GitHub上创建仓库"
    echo "  2. 您没有对该仓库的写入权限"
    echo "  3. 仓库已存在且不为空，需要强制推送或合并"
    echo ""
    echo "解决方法："
    echo "  1. 前往 https://github.com/new 创建新仓库"
    echo "  2. 或者检查您输入的仓库名称是否正确"
    echo ""
fi