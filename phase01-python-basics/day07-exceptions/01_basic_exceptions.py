#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7: 异常处理

本文件包含Python异常处理的练习代码
"""

# 1. 基本异常处理
print("=== 基本异常处理 ===")

# 示例1：除零异常
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero")

# 示例2：类型错误
try:
    result = "10" + 5
    print(f"Result: {result}")
except TypeError:
    print("Error: Type mismatch")

# 示例3：索引错误
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range")

# 2. 捕获多个异常
print("\n=== 捕获多个异常 ===")

try:
    # 可能引发多种异常的代码
    choice = int(input("Enter a number: "))
    result = 10 / choice
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input, please enter a number")
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print(f"Error: {e}")

# 3. else和finally子句
print("\n=== else和finally子句 ===")

try:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        raise ValueError("Number must be positive")
    result = 100 / num
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print(f"Success! Result: {result}")
finally:
    print("Execution completed")

# 4. 自定义异常
print("\n=== 自定义异常 ===")

class NegativeNumberError(Exception):
    """自定义异常：负数错误"""
    pass

class InsufficientFundsError(Exception):
    """自定义异常：资金不足"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance={balance}, amount={amount}")

# 使用自定义异常
try:
    balance = 100
    amount = 150
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    print("Withdrawal successful")
except InsufficientFundsError as e:
    print(f"Error: {e}")

# 5. 异常链
print("\n=== 异常链 ===")

try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("A value error occurred") from e
except ValueError as e:
    print(f"Caught: {e}")
    print(f"Cause: {e.__cause__}")

# 6. 断言
print("\n=== 断言 ===")

def calculate_square_root(n):
    """计算平方根"""
    assert n >= 0, "Input must be non-negative"
    return n ** 0.5

try:
    print(f"Square root of 4: {calculate_square_root(4)}")
    print(f"Square root of -1: {calculate_square_root(-1)}")
except AssertionError as e:
    print(f"Assertion error: {e}")

# 7. 异常处理最佳实践
print("\n=== 异常处理最佳实践 ===")

# 实践1：具体异常优先于通用异常
try:
    # 代码
    pass
except ValueError:
    # 处理值错误
    pass
except TypeError:
    # 处理类型错误
    pass
except Exception:
    # 处理其他所有异常
    pass

# 实践2：使用with语句自动处理资源
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")

# 实践3：记录异常信息
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    1 / 0
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print("An error occurred, please check the logs")

# 8. 异常处理的应用场景
print("\n=== 异常处理的应用场景 ===")

# 场景1：用户输入验证
def get_user_age():
    """获取用户年龄"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# 场景2：文件操作
def read_file(filename):
    """读取文件内容"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

# 场景3：网络请求模拟
def simulate_network_request():
    """模拟网络请求"""
    import random
    try:
        # 模拟网络延迟
        import time
        time.sleep(0.5)
        
        # 模拟随机错误
        if random.random() < 0.3:
            raise ConnectionError("Network connection failed")
        return "Success: Data received"
    except ConnectionError as e:
        print(f"Network error: {e}")
        return "Failed: Network error"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed: Unexpected error"

# 测试场景
try:
    print("\nTesting get_user_age:")
    # age = get_user_age()  # 注释掉以避免交互式输入
    # print(f"Your age is: {age}")
    
    print("\nTesting read_file:")
    content = read_file("test.txt")
    print(f"File content length: {len(content)}")
    
    print("\nTesting simulate_network_request:")
    for i in range(3):
        result = simulate_network_request()
        print(f"Attempt {i+1}: {result}")
except KeyboardInterrupt:
    print("\nOperation cancelled by user")

print("\n异常处理练习完成！")
