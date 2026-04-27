#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 3: 函数详解

本文件包含Python函数的练习代码
"""

# 1. 基本函数定义
print("=== 基本函数定义 ===")
def greet():
    """无参数无返回值的函数"""
    print("Hello, World!")

def greet_with_name(name):
    """有参数无返回值的函数"""
    print(f"Hello, {name}!")

def add(a, b):
    """有参数有返回值的函数"""
    return a + b

# 调用函数
greet()
greet_with_name("Alice")
result = add(3, 5)
print(f"3 + 5 = {result}")

# 2. 默认参数
print("\n=== 默认参数 ===")
def greet_with_default(name="World"):
    """带默认参数的函数"""
    print(f"Hello, {name}!")

greet_with_default()  # 使用默认参数
greet_with_default("Bob")  # 使用自定义参数

# 3. 可变参数
print("\n=== 可变参数 ===")
def sum_numbers(*args):
    """可变参数函数"""
    total = 0
    for num in args:
        total += num
    return total

print(f"sum(1, 2, 3): {sum_numbers(1, 2, 3)}")
print(f"sum(1, 2, 3, 4, 5): {sum_numbers(1, 2, 3, 4, 5)}")

# 4. 关键字参数
print("\n=== 关键字参数 ===")
def print_person_info(name, age, city):
    """关键字参数函数"""
    print(f"Name: {name}, Age: {age}, City: {city}")

# 位置参数调用
print_person_info("Alice", 30, "New York")
# 关键字参数调用
print_person_info(name="Bob", age=25, city="London")
print_person_info(city="Paris", name="Charlie", age=35)  # 可以改变顺序

# 5. 可变关键字参数
print("\n=== 可变关键字参数 ===")
def print_kwargs(**kwargs):
    """可变关键字参数函数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(product="Apple", price=5.99, quantity=10)

# 6. 函数作为参数
print("\n=== 函数作为参数 ===")
def apply_function(func, x, y):
    """将函数作为参数"""
    return func(x, y)

def multiply(a, b):
    return a * b

print(f"apply_function(add, 3, 5): {apply_function(add, 3, 5)}")
print(f"apply_function(multiply, 3, 5): {apply_function(multiply, 3, 5)}")

# 7. 函数返回多个值
print("\n=== 函数返回多个值 ===")
def get_min_max(numbers):
    """返回最小值和最大值"""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"最小值: {min_val}, 最大值: {max_val}")

# 8. 局部变量和全局变量
print("\n=== 局部变量和全局变量 ===")
global_var = "全局变量"

def test_scope():
    local_var = "局部变量"
    print(f"函数内访问局部变量: {local_var}")
    print(f"函数内访问全局变量: {global_var}")

test_scope()
print(f"函数外访问全局变量: {global_var}")
# print(f"函数外访问局部变量: {local_var}")  # 会报错，局部变量在函数外不可访问

# 9. 递归函数
print("\n=== 递归函数 ===")
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

print("\n函数练习完成！")
