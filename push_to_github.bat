@echo off
chcp 65001 >nul
set GIT=E:\Git\Git\cmd\git.exe

set REPO_NAME=zhihu-hot-topics
set GITHUB_USER=ljz621
set GITHUB_URL=https://github.com/%GITHUB_USER%/%REPO_NAME%.git

cd /d "%~dp0"

echo ====================================
echo 推送到GitHub - zhihu-hot-topics
echo ====================================
echo.

"%GIT%" --version
if %errorlevel% neq 0 (
    echo [错误] Git未找到
    cmd /k
    exit /b 1
)

echo [1/5] 初始化Git仓库...
if not exist ".git" (
    "%GIT%" init
    "%GIT%" checkout -b main
    if %errorlevel% neq 0 (
        echo 初始化失败
        cmd /k
        exit /b 1
    )
)

echo [2/5] 配置Git用户...
"%GIT%" config user.email "ljz621@github.com"
"%GIT%" config user.name "ljz621"

echo [3/5] 添加文件...
"%GIT%" add -A
if %errorlevel% neq 0 (
    echo 添加文件失败
    cmd /k
    exit /b 1
)

echo [4/5] 提交文件...
"%GIT%" commit -m "Initial commit: zhihu-hot-topics skill for opencode"

echo [5/5] 推送到GitHub...
"%GIT%" remote add origin %GITHUB_URL% 2>nul
"%GIT%" push -u origin main
if %errorlevel% neq 0 (
    echo 推送失败! 请确认:
    echo 1. 仓库 %GITHUB_URL% 是否已创建
    echo 2. 网络是否正常
    cmd /k
    exit /b 1
)

echo.
echo ====================================
echo 完成! 仓库地址: %GITHUB_URL%
echo ====================================
cmd /k