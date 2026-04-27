#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 11: Linux常用命令

本文件包含Linux常用命令的练习代码和说明
"""

import os
import subprocess
import platform

# 检查操作系统
print(f"当前操作系统: {platform.system()}")
if platform.system() != "Linux":
    print("注意：当前不是Linux系统，以下命令可能无法正常执行")
    print("但会展示命令的用法和说明")

# 1. 目录操作命令
print("\n=== 目录操作命令 ===")

commands = [
    ("pwd", "显示当前工作目录"),
    ("ls", "列出目录内容"),
    ("ls -la", "详细列出目录内容（包括隐藏文件）"),
    ("mkdir", "创建目录"),
    ("mkdir -p", "递归创建目录"),
    ("rmdir", "删除空目录"),
    ("cd", "切换目录"),
    ("cd ..", "返回上一级目录"),
    ("cd /", "切换到根目录"),
    ("cd ~", "切换到用户主目录"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")
    if platform.system() == "Linux":
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=5)
            print(f"  输出: {result.stdout.strip()}")
            if result.stderr:
                print(f"  错误: {result.stderr.strip()}")
        except Exception as e:
            print(f"  执行失败: {e}")
    print()

# 2. 文件操作命令
print("\n=== 文件操作命令 ===")

commands = [
    ("touch", "创建空文件"),
    ("cat", "查看文件内容"),
    ("cat > file.txt", "重定向输出到文件"),
    ("cat >> file.txt", "追加内容到文件"),
    ("more", "分页查看文件内容"),
    ("less", "交互式查看文件内容"),
    ("head", "查看文件前几行"),
    ("tail", "查看文件后几行"),
    ("tail -f", "实时查看文件内容"),
    ("cp", "复制文件"),
    ("mv", "移动或重命名文件"),
    ("rm", "删除文件"),
    ("rm -f", "强制删除文件"),
    ("rm -r", "递归删除目录"),
    ("chmod", "修改文件权限"),
    ("chown", "修改文件所有者"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 3. 文件搜索命令
print("\n=== 文件搜索命令 ===")

commands = [
    ("find", "查找文件"),
    ("find /home -name "*.py"", "在/home目录下查找.py文件"),
    ("grep", "在文件中搜索内容"),
    ("grep "error" log.txt", "在log.txt中搜索包含error的行"),
    ("grep -r "pattern" /dir", "递归搜索目录中的内容"),
    ("which", "查找命令的位置"),
    ("whereis", "查找命令的位置和文档"),
    ("locate", "快速查找文件"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 4. 系统信息命令
print("\n=== 系统信息命令 ===")

commands = [
    ("uname", "显示系统信息"),
    ("uname -a", "显示详细系统信息"),
    ("lsb_release -a", "显示发行版信息"),
    ("cat /etc/os-release", "显示操作系统版本"),
    ("top", "显示系统进程"),
    ("ps", "显示当前进程"),
    ("ps aux", "显示所有进程"),
    ("kill", "终止进程"),
    ("kill -9", "强制终止进程"),
    ("free", "显示内存使用情况"),
    ("df", "显示磁盘使用情况"),
    ("df -h", "以人类可读的方式显示磁盘使用情况"),
    ("du", "显示目录大小"),
    ("du -h", "以人类可读的方式显示目录大小"),
    ("uptime", "显示系统运行时间"),
    ("who", "显示当前登录用户"),
    ("w", "显示当前登录用户和他们的活动"),
    ("last", "显示最近的登录记录"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")
    if platform.system() == "Linux":
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=5)
            print(f"  输出: {result.stdout.strip()}")
            if result.stderr:
                print(f"  错误: {result.stderr.strip()}")
        except Exception as e:
            print(f"  执行失败: {e}")
    print()

# 5. 网络命令
print("\n=== 网络命令 ===")

commands = [
    ("ifconfig", "显示网络接口信息"),
    ("ip addr", "显示网络接口信息（新版本）"),
    ("ping", "测试网络连接"),
    ("ping -c 4 google.com", "向google.com发送4个ping包"),
    ("netstat", "显示网络连接"),
    ("netstat -tuln", "显示监听的端口"),
    ("ss", "显示网络连接（新版本）"),
    ("ss -tuln", "显示监听的端口（新版本）"),
    ("curl", "发送HTTP请求"),
    ("curl -s https://api.github.com", "获取GitHub API信息"),
    ("wget", "下载文件"),
    ("wget https://example.com/file.txt", "下载文件到当前目录"),
    ("traceroute", "跟踪网络路由"),
    ("traceroute google.com", "跟踪到google.com的路由"),
    ("dig", "查询DNS信息"),
    ("dig google.com", "查询google.com的DNS信息"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 6. 包管理命令
print("\n=== 包管理命令 ===")

print("Debian/Ubuntu (apt):")
apt_commands = [
    ("sudo apt update", "更新包列表"),
    ("sudo apt upgrade", "升级包"),
    ("sudo apt install <package>", "安装包"),
    ("sudo apt remove <package>", "删除包"),
    ("sudo apt autoremove", "自动删除不需要的包"),
    ("sudo apt search <keyword>", "搜索包"),
    ("apt list --installed", "列出已安装的包"),
]

for cmd, desc in apt_commands:
    print(f"- {cmd}: {desc}")

print("\nCentOS/RHEL (yum):")
yum_commands = [
    ("sudo yum update", "更新包"),
    ("sudo yum install <package>", "安装包"),
    ("sudo yum remove <package>", "删除包"),
    ("sudo yum search <keyword>", "搜索包"),
    ("yum list installed", "列出已安装的包"),
]

for cmd, desc in yum_commands:
    print(f"- {cmd}: {desc}")

print("\nCentOS/RHEL 8+ (dnf):")
dnf_commands = [
    ("sudo dnf update", "更新包"),
    ("sudo dnf install <package>", "安装包"),
    ("sudo dnf remove <package>", "删除包"),
    ("sudo dnf search <keyword>", "搜索包"),
    ("dnf list installed", "列出已安装的包"),
]

for cmd, desc in dnf_commands:
    print(f"- {cmd}: {desc}")

# 7. 压缩和解压缩命令
print("\n=== 压缩和解压缩命令 ===")

commands = [
    ("tar -czvf archive.tar.gz dir/", "压缩目录为tar.gz文件"),
    ("tar -xzvf archive.tar.gz", "解压缩tar.gz文件"),
    ("tar -cjvf archive.tar.bz2 dir/", "压缩目录为tar.bz2文件"),
    ("tar -xjvf archive.tar.bz2", "解压缩tar.bz2文件"),
    ("zip archive.zip file1 file2", "压缩文件为zip文件"),
    ("unzip archive.zip", "解压缩zip文件"),
    ("gzip file", "压缩文件为.gz文件"),
    ("gunzip file.gz", "解压缩.gz文件"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 8. 文本处理命令
print("\n=== 文本处理命令 ===")

commands = [
    ("sort", "排序文本"),
    ("sort -n", "按数字排序"),
    ("sort -r", "反向排序"),
    ("uniq", "去重"),
    ("sort file | uniq", "排序并去重"),
    ("cut", "提取文本列"),
    ("cut -d ',' -f 1 file.csv", "提取CSV文件的第一列"),
    ("awk", "文本处理工具"),
    ("awk '{print $1}' file", "打印文件的第一列"),
    ("sed", "文本替换工具"),
    ("sed 's/old/new/g' file", "将文件中的old替换为new"),
    ("tr", "字符转换工具"),
    ("tr 'a-z' 'A-Z' < file", "将文件中的小写字母转换为大写"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 9. 其他常用命令
print("\n=== 其他常用命令 ===")

commands = [
    ("history", "显示命令历史"),
    ("history | grep 'git'", "搜索包含git的命令历史"),
    ("alias", "创建命令别名"),
    ("alias ll='ls -la'", "创建ll别名为ls -la"),
    ("unalias", "删除命令别名"),
    ("echo", "输出文本"),
    ("echo $PATH", "显示环境变量PATH"),
    ("export", "设置环境变量"),
    ("export PATH=$PATH:/new/path", "添加新路径到PATH"),
    ("source", "执行脚本并更新当前环境"),
    ("source ~/.bashrc", "重新加载bash配置"),
    ("crontab", "定时任务"),
    ("crontab -l", "查看定时任务"),
    ("crontab -e", "编辑定时任务"),
]

for cmd, desc in commands:
    print(f"- {cmd}: {desc}")

# 10. 命令行技巧
print("\n=== 命令行技巧 ===")

print("1. 命令历史:")
print("   - 按上下箭头浏览历史命令")
print("   - !n 执行第n条历史命令")
print("   - !! 执行上一条命令")
print("   - !string 执行以string开头的最近命令")

print("\n2. 命令补全:")
print("   - 按Tab键自动补全命令和文件名")
print("   - 按Tab两次显示所有可能的补全选项")

print("\n3. 重定向:")
print("   - command > file 重定向标准输出到文件")
print("   - command >> file 追加标准输出到文件")
print("   - command 2> file 重定向标准错误到文件")
print("   - command &> file 重定向标准输出和错误到文件")

print("\n4. 管道:")
print("   - command1 | command2 将command1的输出作为command2的输入")
print("   - ls -la | grep 'txt' 查找包含txt的文件")

print("\n5. 后台执行:")
print("   - command & 在后台执行命令")
print("   - bg 将前台命令移到后台")
print("   - fg 将后台命令移到前台")
print("   - jobs 查看后台运行的命令")

print("\n6. 通配符:")
print("   - * 匹配任意长度的任意字符")
print("   - ? 匹配单个字符")
print("   - [abc] 匹配a、b或c")
print("   - [0-9] 匹配0到9之间的数字")

print("\n7. 快捷键:")
print("   - Ctrl+C 终止当前命令")
print("   - Ctrl+D 结束输入（EOF）")
print("   - Ctrl+L 清屏")
print("   - Ctrl+A 移动到行首")
print("   - Ctrl+E 移动到行尾")
print("   - Ctrl+K 删除从光标到行尾的内容")
print("   - Ctrl+U 删除从光标到行首的内容")

print("\nLinux常用命令练习完成！")
