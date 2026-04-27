#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 10: Git基础

本文件包含Git基础操作的练习代码和说明
"""

import os
import subprocess
import tempfile

# 1. Git基本概念
print("=== Git基本概念 ===")
print("Git是一个分布式版本控制系统，用于跟踪项目中文件的变化。")
print("主要概念：")
print("- 仓库(Repository)：存储项目代码的地方")
print("- 提交(Commit)：代码的快照")
print("- 分支(Branch)：代码的不同版本")
print("- 合并(Merge)：将不同分支的代码合并")
print("- 远程仓库(Remote)：存储在网络上的仓库")

# 2. Git初始化和配置
print("\n=== Git初始化和配置 ===")

# 创建临时目录作为测试仓库
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"创建临时目录: {temp_dir}")
    os.chdir(temp_dir)
    
    # 2.1 初始化仓库
    print("\n2.1 初始化仓库")
    result = subprocess.run(["git", "init"], capture_output=True, text=True)
    print(f"git init 输出: {result.stdout}")
    if result.stderr:
        print(f"错误: {result.stderr}")
    
    # 2.2 配置用户信息
    print("\n2.2 配置用户信息")
    subprocess.run(["git", "config", "user.name", "Test User"], capture_output=True, text=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], capture_output=True, text=True)
    
    # 查看配置
    result = subprocess.run(["git", "config", "--list"], capture_output=True, text=True)
    print(f"git config --list 输出:\n{result.stdout}")
    
    # 3. Git基本操作
    print("\n=== Git基本操作 ===")
    
    # 3.1 创建文件并添加到暂存区
    print("\n3.1 创建文件并添加到暂存区")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Test Project\n\nThis is a test project for Git practice.\n")
    
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(f"git status 输出:\n{result.stdout}")
    
    result = subprocess.run(["git", "add", "README.md"], capture_output=True, text=True)
    print(f"git add README.md 输出: {result.stdout}")
    if result.stderr:
        print(f"错误: {result.stderr}")
    
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(f"git status 输出:\n{result.stdout}")
    
    # 3.2 提交更改
    print("\n3.2 提交更改")
    result = subprocess.run(["git", "commit", "-m", "Initial commit"], capture_output=True, text=True)
    print(f"git commit 输出:\n{result.stdout}")
    if result.stderr:
        print(f"错误: {result.stderr}")
    
    # 3.3 查看提交历史
    print("\n3.3 查看提交历史")
    result = subprocess.run(["git", "log"], capture_output=True, text=True)
    print(f"git log 输出:\n{result.stdout}")
    
    # 3.4 修改文件并再次提交
    print("\n3.4 修改文件并再次提交")
    with open("README.md", "a", encoding="utf-8") as f:
        f.write("\nAdded a new line.\n")
    
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(f"git status 输出:\n{result.stdout}")
    
    result = subprocess.run(["git", "add", "README.md"], capture_output=True, text=True)
    result = subprocess.run(["git", "commit", "-m", "Update README.md"], capture_output=True, text=True)
    print(f"git commit 输出:\n{result.stdout}")
    
    result = subprocess.run(["git", "log"], capture_output=True, text=True)
    print(f"git log 输出:\n{result.stdout}")
    
    # 4. Git分支操作
    print("\n=== Git分支操作 ===")
    
    # 4.1 查看分支
    print("\n4.1 查看分支")
    result = subprocess.run(["git", "branch"], capture_output=True, text=True)
    print(f"git branch 输出:\n{result.stdout}")
    
    # 4.2 创建分支
    print("\n4.2 创建分支")
    result = subprocess.run(["git", "branch", "feature-branch"], capture_output=True, text=True)
    print(f"git branch feature-branch 输出: {result.stdout}")
    
    result = subprocess.run(["git", "branch"], capture_output=True, text=True)
    print(f"git branch 输出:\n{result.stdout}")
    
    # 4.3 切换分支
    print("\n4.3 切换分支")
    result = subprocess.run(["git", "checkout", "feature-branch"], capture_output=True, text=True)
    print(f"git checkout feature-branch 输出: {result.stdout}")
    
    # 4.4 在分支上做修改
    print("\n4.4 在分支上做修改")
    with open("feature.txt", "w", encoding="utf-8") as f:
        f.write("Feature content\n")
    
    result = subprocess.run(["git", "add", "feature.txt"], capture_output=True, text=True)
    result = subprocess.run(["git", "commit", "-m", "Add feature.txt"], capture_output=True, text=True)
    print(f"git commit 输出:\n{result.stdout}")
    
    # 4.5 切换回主分支
    print("\n4.5 切换回主分支")
    result = subprocess.run(["git", "checkout", "master"], capture_output=True, text=True)
    print(f"git checkout master 输出: {result.stdout}")
    
    # 4.6 合并分支
    print("\n4.6 合并分支")
    result = subprocess.run(["git", "merge", "feature-branch"], capture_output=True, text=True)
    print(f"git merge feature-branch 输出:\n{result.stdout}")
    
    # 4.7 删除分支
    print("\n4.7 删除分支")
    result = subprocess.run(["git", "branch", "-d", "feature-branch"], capture_output=True, text=True)
    print(f"git branch -d feature-branch 输出: {result.stdout}")
    
    result = subprocess.run(["git", "branch"], capture_output=True, text=True)
    print(f"git branch 输出:\n{result.stdout}")
    
    # 5. Git远程仓库
    print("\n=== Git远程仓库 ===")
    print("注意：以下操作需要一个真实的远程仓库，这里只展示命令")
    print("\n5.1 添加远程仓库")
    print("git remote add origin https://github.com/username/repository.git")
    
    print("\n5.2 查看远程仓库")
    print("git remote -v")
    
    print("\n5.3 推送代码到远程仓库")
    print("git push -u origin master")
    
    print("\n5.4 从远程仓库拉取代码")
    print("git pull")
    
    print("\n5.5 克隆远程仓库")
    print("git clone https://github.com/username/repository.git")

# 6. Git工作流
print("\n=== Git工作流 ===")
print("常见的Git工作流：")
print("1. 集中式工作流：所有开发都在master分支上进行")
print("2. 功能分支工作流：每个功能创建一个分支")
print("3. GitFlow工作流：使用master、develop、feature、release、hotfix分支")
print("4. Forking工作流：适用于开源项目，通过Pull Request贡献代码")

# 7. Git常用命令
print("\n=== Git常用命令 ===")
print("基础命令：")
print("- git init：初始化仓库")
print("- git add <file>：添加文件到暂存区")
print("- git commit -m "message"：提交更改")
print("- git status：查看状态")
print("- git log：查看提交历史")

print("\n分支命令：")
print("- git branch：查看分支")
print("- git branch <name>：创建分支")
print("- git checkout <branch>：切换分支")
print("- git merge <branch>：合并分支")
print("- git branch -d <branch>：删除分支")

print("\n远程命令：")
print("- git remote add <name> <url>：添加远程仓库")
print("- git push <remote> <branch>：推送代码")
print("- git pull <remote> <branch>：拉取代码")
print("- git clone <url>：克隆仓库")

print("\n其他命令：")
print("- git diff：查看更改")
print("- git reset：重置更改")
print("- git revert：撤销提交")
print("- git stash：暂存更改")

# 8. Git最佳实践
print("\n=== Git最佳实践 ===")
print("1. 提交消息要清晰明了")
print("2. 每个提交只包含一个逻辑更改")
print("3. 定期拉取和推送代码")
print("4. 使用分支管理不同功能")
print("5. 定期合并主分支到开发分支")
print("6. 使用.gitignore文件忽略不需要版本控制的文件")

# 9. 创建.gitignore文件示例
print("\n=== .gitignore文件示例 ===")
gitignore_content = '''
# Python
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Build files
build/
dist/
*.egg-info/
'''
print(f".gitignore内容:\n{gitignore_content}")

print("\nGit基础练习完成！")
