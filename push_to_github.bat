@echo off
chcp 65001 >nul

set REPO_NAME=zhihu-hot-topics
set GITHUB_USER=ljz621
set GITHUB_URL=https://github.com/%GITHUB_USER%/%REPO_NAME%.git

cd /d "%~dp0"

echo ====================================
echo 推送到GitHub - zhihu-hot-topics
echo ====================================
echo.

git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到Git
    echo.
    echo 请先安装Git:
    echo 1. 下载: https://git-scm.com
    echo 2. 安装时勾选 "Git Bash Here"
    echo.
    pause
    exit /b 1
)

echo [1/5] 初始化Git仓库...
if not exist ".git" (
    git init
    git checkout -b main
)

echo [2/5] 配置Git用户...
git config user.email "ljz621@github.com"
git config user.name "ljz621"

echo [3/5] 添加文件...
git add -A

echo [4/5] 提交文件...
git commit -m "Initial commit: zhihu-hot-topics skill for opencode" --allow-empty

echo [5/5] 推送到GitHub...
git remote add origin %GITHUB_URL% 2>nul
git push -u origin main --force

echo.
echo ====================================
echo 完成! 仓库地址: %GITHUB_URL%
echo ====================================
pause