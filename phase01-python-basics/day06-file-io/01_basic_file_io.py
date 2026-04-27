#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 6: 文件IO操作

本文件包含Python文件IO操作的练习代码
"""

import os

# 1. 文件写入
print("=== 文件写入 ===")

# 方法1：使用write()方法
print("\n1.1 使用write()方法")
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    f.write("Python file IO is easy.\n")
print("File written successfully.")

# 方法2：使用writelines()方法
print("\n1.2 使用writelines()方法")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("test2.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
print("Lines written successfully.")

# 2. 文件读取
print("\n=== 文件读取 ===")

# 方法1：使用read()方法
print("\n2.1 使用read()方法")
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"File content:\n{content}")

# 方法2：使用readline()方法
print("\n2.2 使用readline()方法")
with open("test.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
print(f"Line 1: {line1.strip()}")
print(f"Line 2: {line2.strip()}")
print(f"Line 3: {line3.strip()}")

# 方法3：使用readlines()方法
print("\n2.3 使用readlines()方法")
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("All lines:")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")

# 方法4：直接遍历文件对象
print("\n2.4 直接遍历文件对象")
with open("test.txt", "r", encoding="utf-8") as f:
    print("File content:")
    for line in f:
        print(line.strip())

# 3. 文件追加
print("\n=== 文件追加 ===")
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("This is an appended line.\n")
    f.write("Another appended line.\n")
print("Content appended successfully.")

# 验证追加结果
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"Updated file content:\n{content}")

# 4. 二进制文件操作
print("\n=== 二进制文件操作 ===")

# 写入二进制文件
with open("test.bin", "wb") as f:
    f.write(b"Hello, Binary World!")
print("Binary file written successfully.")

# 读取二进制文件
with open("test.bin", "rb") as f:
    binary_content = f.read()
print(f"Binary content: {binary_content}")
print(f"Decoded content: {binary_content.decode('utf-8')}")

# 5. 文件定位
print("\n=== 文件定位 ===")
with open("test.txt", "r", encoding="utf-8") as f:
    # 获取当前位置
    print(f"Initial position: {f.tell()}")
    
    # 读取前10个字符
    content = f.read(10)
    print(f"Read: {content}")
    print(f"Position after reading: {f.tell()}")
    
    # 移动到文件开头
    f.seek(0)
    print(f"Position after seek(0): {f.tell()}")
    
    # 读取一行
    line = f.readline()
    print(f"First line: {line.strip()}")

# 6. 文件操作相关函数
print("\n=== 文件操作相关函数 ===")

# 检查文件是否存在
print(f"test.txt exists: {os.path.exists('test.txt')}")
print(f"non_existent.txt exists: {os.path.exists('non_existent.txt')}")

# 获取文件大小
print(f"test.txt size: {os.path.getsize('test.txt')} bytes")

# 获取文件修改时间
import time
mod_time = os.path.getmtime('test.txt')
print(f"test.txt modified time: {time.ctime(mod_time)}")

# 重命名文件
os.rename("test2.txt", "renamed_test.txt")
print("File renamed from test2.txt to renamed_test.txt")

# 删除文件
os.remove("renamed_test.txt")
os.remove("test.bin")
print("Files deleted: renamed_test.txt, test.bin")

# 7. 目录操作
print("\n=== 目录操作 ===")

# 创建目录
os.makedirs("test_dir", exist_ok=True)
print("Directory 'test_dir' created")

# 写入文件到目录
with open("test_dir/file_in_dir.txt", "w", encoding="utf-8") as f:
    f.write("File in directory")
print("File written to test_dir")

# 列出目录内容
print(f"test_dir contents: {os.listdir('test_dir')}")

# 删除目录及其内容
import shutil
shutil.rmtree("test_dir")
print("Directory 'test_dir' and its contents deleted")

# 8. CSV文件操作
print("\n=== CSV文件操作 ===")
import csv

# 写入CSV文件
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "London"])
    writer.writerow(["Charlie", 35, "Paris"])
print("CSV file written successfully.")

# 读取CSV文件
print("\nReading CSV file:")
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 9. 上下文管理器
print("\n=== 上下文管理器 ===")

# 使用contextmanager装饰器创建上下文管理器
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """文件管理器上下文管理器"""
    print(f"Opening file {filename}")
    f = open(filename, mode, encoding="utf-8")
    try:
        yield f
    finally:
        print(f"Closing file {filename}")
        f.close()

# 使用自定义上下文管理器
with file_manager("test_with.txt", "w") as f:
    f.write("Using context manager\n")
    f.write("This is a test\n")
print("Context manager test completed")

# 清理测试文件
for file in ["test.txt", "data.csv", "test_with.txt"]:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted {file}")

print("\n文件IO操作练习完成！")
