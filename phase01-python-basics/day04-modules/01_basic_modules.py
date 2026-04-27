#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 4: 模块详解

本文件包含Python模块的练习代码
"""

# 1. 导入模块
print("=== 导入模块 ===")
# 导入整个模块
import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# 导入模块中的特定函数
from math import sqrt, pow
print(f"sqrt(25) = {sqrt(25)}")
print(f"pow(2, 3) = {pow(2, 3)}")

# 导入模块中的所有内容
from math import *
print(f"sin(0) = {sin(0)}")
print(f"cos(0) = {cos(0)}")

# 给模块起别名
import math as m
print(f"m.log10(100) = {m.log10(100)}")

# 2. 创建自定义模块
print("\n=== 创建自定义模块 ===")
# 首先创建一个简单的模块文件
with open("my_module.py", "w", encoding="utf-8") as f:
    f.write('''
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

def add(a, b):
    """加法函数"""
    return a + b

PI = 3.14159
''')

# 导入自定义模块
import my_module
print(f"my_module.greet('Alice') = {my_module.greet('Alice')}")
print(f"my_module.add(3, 5) = {my_module.add(3, 5)}")
print(f"my_module.PI = {my_module.PI}")

# 3. 包的使用
print("\n=== 包的使用 ===")
# 创建包目录结构
import os

# 创建包目录
os.makedirs("my_package", exist_ok=True)

# 创建 __init__.py 文件
with open("my_package/__init__.py", "w", encoding="utf-8") as f:
    f.write('''
__version__ = "1.0.0"
''')

# 创建模块文件
with open("my_package/calculator.py", "w", encoding="utf-8") as f:
    f.write('''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
''')

with open("my_package/greeter.py", "w", encoding="utf-8") as f:
    f.write('''
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"
''')

# 导入包
import my_package
print(f"my_package.__version__ = {my_package.__version__}")

# 导入包中的模块
from my_package import calculator
print(f"calculator.add(10, 5) = {calculator.add(10, 5)}")
print(f"calculator.subtract(10, 5) = {calculator.subtract(10, 5)}")

from my_package import greeter
print(f"greeter.greet('Bob') = {greeter.greet('Bob')}")
print(f"greeter.farewell('Bob') = {greeter.farewell('Bob')}")

# 4. 标准库模块
print("\n=== 标准库模块 ===")
# os 模块
import os
print(f"当前目录: {os.getcwd()}")
print(f"当前目录下的文件: {os.listdir('.')}")

# sys 模块
import sys
print(f"Python版本: {sys.version}")
print(f"命令行参数: {sys.argv}")

# datetime 模块
import datetime
now = datetime.datetime.now()
print(f"当前时间: {now}")
print(f"格式化时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# random 模块
import random
print(f"随机数(0-1): {random.random()}")
print(f"随机整数(1-100): {random.randint(1, 100)}")
print(f"随机选择: {random.choice(['apple', 'banana', 'cherry'])}")

# 5. 第三方模块
print("\n=== 第三方模块 ===")
print("提示: 可以使用 pip install 命令安装第三方模块")
print("例如: pip install requests")
print("\n尝试导入 requests 模块 (如果已安装):")
try:
    import requests
    print("requests 模块已安装")
except ImportError:
    print("requests 模块未安装")

print("\n模块练习完成！")
