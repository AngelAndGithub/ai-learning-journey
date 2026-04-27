#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 12: 项目实践1 - 计算器工具

本文件实现一个简单的命令行计算器
"""

def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """幂运算"""
    return a ** b

def modulus(a, b):
    """取模"""
    if b == 0:
        return "Error: Division by zero"
    return a % b

def calculate():
    """计算器主函数"""
    print("=== 计算器 ===")
    print("支持的操作:")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 幂运算 (^)")
    print("6. 取模 (%)")
    print("7. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-7): ")
        
        if choice == '7':
            print("谢谢使用，再见！")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("无效的选择，请重新输入")
            continue
        
        try:
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
        except ValueError:
            print("无效的输入，请输入数字")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        elif choice == '5':
            result = power(num1, num2)
            operation = "^"
        elif choice == '6':
            result = modulus(num1, num2)
            operation = "%"
        
        print(f"{num1} {operation} {num2} = {result}")

def advanced_calculator():
    """高级计算器，支持表达式计算"""
    print("\n=== 高级计算器 ===")
    print("支持直接输入表达式，例如: 2 + 3 * 4")
    print("输入 'exit' 退出")
    
    while True:
        expression = input("\n请输入表达式: ")
        
        if expression.lower() == 'exit':
            print("谢谢使用，再见！")
            break
        
        try:
            # 使用eval函数计算表达式
            # 注意：eval函数有安全风险，这里仅用于学习
            result = eval(expression)
            print(f"结果: {result}")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    print("=== Python计算器工具 ===")
    print("1. 基本计算器")
    print("2. 高级计算器")
    
    calc_choice = input("请选择计算器类型 (1-2): ")
    
    if calc_choice == '1':
        calculate()
    elif calc_choice == '2':
        advanced_calculator()
    else:
        print("无效的选择")
