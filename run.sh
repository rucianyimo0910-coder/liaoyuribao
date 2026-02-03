#!/bin/bash
# 身心灵疗愈日报生成脚本

set -e  # 遇到错误时停止执行

echo "开始设置身心灵疗愈日报环境..."

# 检查是否已安装所需依赖
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 python3"
    exit 1
fi

# 安装依赖（如果尚未安装）
if [ -f "requirements.txt" ]; then
    echo "安装依赖包..."
    pip3 install -r requirements.txt || {
        echo "警告: 无法安装依赖，将使用基础功能"
    }
fi

echo "生成今日日报..."
cd src
python3 generate_report.py

echo "日报已生成到 public/index.html"
echo "完成！"