#!/bin/bash

# 一键推送脚本 - 在仓库创建后使用

echo "🌿 身心灵疗愈日报 - 一键推送至 GitHub"
echo "====================================="

# 检查仓库是否存在
if ! ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    echo "❌ SSH认证失败，请检查SSH密钥配置"
    exit 1
fi

# 获取用户名
GITHUB_USER=$(ssh -T git@github.com 2>&1 | grep -oE "Hi [^!]*!" | cut -d' ' -f2 | tr -d '!')

if [ -z "$GITHUB_USER" ]; then
    echo "❌ 无法获取GitHub用户名"
    exit 1
fi

REPO_URL="git@github.com:$GITHUB_USER/healtherly-daily-report.git"

# 检查远程仓库是否已设置
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null)

if [ "$CURRENT_REMOTE" != "$REPO_URL" ]; then
    git remote set-url origin $REPO_URL
    echo "📡 设置远程仓库: $REPO_URL"
fi

# 确保是main分支
git checkout main

# 推送代码
echo "📤 正在推送代码到GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功推送代码到GitHub!"
    echo "🔗 仓库地址: https://github.com/$GITHUB_USER/healtherly-daily-report"
    echo ""
    echo "✨ 恭喜！您的身心灵疗愈日报项目已成功部署到GitHub！"
    echo ""
    echo "下一步建议："
    echo "1. 在GitHub仓库中启用 GitHub Pages (Settings > Pages)"
    echo "2. 设置源码为 'Deploy from a branch'，分支选择 'main'"
    echo "3. 您将可以通过 https://$GITHUB_USER.github.io/healtherly-daily-report 访问您的应用"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "请确认："
    echo "- 仓库 https://github.com/$GITHUB_USER/healtherly-daily-report 已存在"
    echo "- 您有推送权限"
    echo "- 网络连接正常"
    echo ""
fi