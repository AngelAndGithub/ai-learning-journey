#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 2: 数据类型详解

本文件包含Python基本数据类型的练习代码
"""

# 1. 数字类型
print("=== 数字类型 ===")
# 整数
integer_num = 42
print(f"整数: {integer_num}, 类型: {type(integer_num)}")

# 浮点数
float_num = 3.14
print(f"浮点数: {float_num}, 类型: {type(float_num)}")

# 复数
complex_num = 1 + 2j
print(f"复数: {complex_num}, 类型: {type(complex_num)}")

# 数字运算
print("\n=== 数字运算 ===")
print(f"42 + 3.14 = {42 + 3.14}")
print(f"42 - 3.14 = {42 - 3.14}")
print(f"42 * 3.14 = {42 * 3.14}")
print(f"42 / 3.14 = {42 / 3.14}")
print(f"42 // 3 = {42 // 3}")  # 整除
print(f"42 % 3 = {42 % 3}")   # 取模
print(f"42 ** 3 = {42 ** 3}") # 幂运算

# 2. 字符串
print("\n=== 字符串 ===")
# 字符串定义
str1 = "Hello, World!"
str2 = 'Python is awesome'
str3 = '''多行
字符串
示例'''

print(f"str1: {str1}")
print(f"str2: {str2}")
print(f"str3: {str3}")

# 字符串操作
print("\n=== 字符串操作 ===")
print(f"字符串长度: {len(str1)}")
print(f"首字母大写: {str1.capitalize()}")
print(f"全部大写: {str1.upper()}")
print(f"全部小写: {str1.lower()}")
print(f"替换: {str1.replace('World', 'Python')}")
print(f"分割: {str1.split(', ')}")
print(f"切片: {str1[0:5]}")  # 前5个字符
print(f"拼接: {str1 + ' ' + str2}")

# 字符串格式化
print("\n=== 字符串格式化 ===")
name = "Alice"
age = 30
print(f"我的名字是{name}，今年{age}岁。")
print("我的名字是%s，今年%d岁。" % (name, age))
print("我的名字是{0}，今年{1}岁。".format(name, age))

# 3. 布尔类型
print("\n=== 布尔类型 ===")
true_value = True
false_value = False
print(f"True: {true_value}, 类型: {type(true_value)}")
print(f"False: {false_value}, 类型: {type(false_value)}")

# 布尔运算
print("\n=== 布尔运算 ===")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 4. 类型检查与转换
print("\n=== 类型检查与转换 ===")
# 类型检查
print(f"42是否为整数: {isinstance(42, int)}")
print(f"3.14是否为浮点数: {isinstance(3.14, float)}")
print(f"'Hello'是否为字符串: {isinstance('Hello', str)}")

# 类型转换
print("\n=== 类型转换 ===")
print(f"int('42'): {int('42')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(42): {str(42)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")

print("\n数据类型练习完成！")
