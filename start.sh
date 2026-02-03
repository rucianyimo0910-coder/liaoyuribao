#!/bin/bash

# Healtherly Daily Report 启动脚本

echo "🌿 身心灵疗愈日报 - 启动中..."
echo "=================================="

# 切换到项目目录
cd "$(dirname "$0")"

# 检查 Node.js 是否已安装
if ! command -v node &> /dev/null; then
    echo "❌ 错误: Node.js 未找到，请先安装 Node.js"
    echo "💡 提示: 访问 https://nodejs.org 下载安装"
    exit 1
fi

echo "✅ Node.js 版本: $(node --version)"

echo ""
echo "🚀 正在启动身心灵疗愈日报服务器..."

# 启动内置服务器
node server.js 3000