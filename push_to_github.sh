#!/bin/bash
# 推送到GitHub仓库

# 配置
REPO_NAME="zhihu-hot-topics"
GITHUB_USER="ljz621"
GITHUB_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

# 获取当前目录
CURRENT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$CURRENT_DIR"

echo "=== 初始化Git仓库 ==="

# 检查是否已经是git仓库
if [ ! -d ".git" ]; then
    git init
    echo "Git仓库已初始化"
else
    echo "已经是Git仓库"
fi

# 配置git（如果需要）
git config user.email "your-email@example.com"
git config user.name "Your Name"

# 添加所有文件
git add .
echo "已添加所有文件"

# 提交
echo "=== 提交更改 ==="
git commit -m "Initial commit: zhihu-hot-topics skill for opencode"
echo "已提交"

# 添加远程仓库
echo "=== 添加远程仓库 ==="
git remote add origin "$GITHUB_URL" 2>/dev/null || echo "远程仓库已存在"

# 推送
echo "=== 推送到GitHub ==="
git branch -M main
git push -u origin main

echo ""
echo "=== 完成！==="
echo "仓库地址: $GITHUB_URL"