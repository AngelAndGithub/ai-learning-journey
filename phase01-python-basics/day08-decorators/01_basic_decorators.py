#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 8: 装饰器

本文件包含Python装饰器的练习代码
"""

# 1. 基本装饰器
print("=== 基本装饰器 ===")

def simple_decorator(func):
    """简单装饰器"""
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@simple_decorator
def hello():
    print("Hello, World!")

hello()

# 2. 带参数的装饰器
print("\n=== 带参数的装饰器 ===")

def decorator_with_args(func):
    """带参数的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

result = add(3, 5)
print(f"Result: {result}")

# 3. 带返回值的装饰器
print("\n=== 带返回值的装饰器 ===")

def return_decorator(func):
    """带返回值的装饰器"""
    def wrapper(*args, **kwargs):
        print("Wrapper: Before execution")
        result = func(*args, **kwargs)
        print("Wrapper: After execution")
        return result
    return wrapper

@return_decorator
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(f"Result: {result}")

# 4. 装饰器工厂
print("\n=== 装饰器工厂 ===")

def repeat(n):
    """重复执行函数n次的装饰器工厂"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                print(f"Execution {i+1} of {func.__name__}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

results = greet("Alice")
print(f"Results: {results}")

# 5. 类装饰器
print("\n=== 类装饰器 ===")

class Timer:
    """计时装饰器类"""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"{self.func.__name__} took {end_time - start_time:.4f} seconds")
        return result

@Timer
def slow_function():
    import time
    time.sleep(0.5)
    print("Function executed")

slow_function()

# 6. 多个装饰器
print("\n=== 多个装饰器 ===")

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before")
        result = func(*args, **kwargs)
        print("Decorator 1: After")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before")
        result = func(*args, **kwargs)
        print("Decorator 2: After")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Bob")

# 7. 保留函数元数据
print("\n=== 保留函数元数据 ===")

import functools

def decorator_with_metadata(func):
    """保留函数元数据的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_metadata
def original_function(x):
    """Original function that adds 1 to x"""
    return x + 1

print(f"Function name: {original_function.__name__}")
print(f"Function docstring: {original_function.__doc__}")
print(f"Result: {original_function(5)}")

# 8. 实用装饰器示例
print("\n=== 实用装饰器示例 ===")

# 8.1 缓存装饰器
def cache(func):
    """简单的缓存装饰器"""
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"Returning cached result for {args}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        print(f"Caching result for {args}")
        return result
    
    return wrapper

@cache
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Fibonacci(10): {fibonacci(10)}")  # 应该使用缓存

# 8.2 权限检查装饰器
def requires_permission(permission):
    """权限检查装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 模拟权限检查
            user_permissions = ["read", "write"]
            if permission in user_permissions:
                print(f"Permission {permission} granted")
                return func(*args, **kwargs)
            else:
                print(f"Permission {permission} denied")
                return "Access denied"
        return wrapper
    return decorator

@requires_permission("read")
def read_data():
    return "Data read successfully"

@requires_permission("admin")
def admin_function():
    return "Admin function executed"

print(f"read_data(): {read_data()}")
print(f"admin_function(): {admin_function()}")

# 8.3 日志装饰器
def log_function(func):
    """日志装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} raised exception: {e}")
            raise
    return wrapper

@log_function
def divide(a, b):
    return a / b

print(f"divide(10, 2): {divide(10, 2)}")
try:
    divide(10, 0)
except Exception as e:
    print(f"Caught exception: {e}")

# 9. 装饰器的应用场景
print("\n=== 装饰器的应用场景 ===")

# 场景1：性能监控
def performance_monitor(func):
    """性能监控装饰器"""
    import time
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@performance_monitor
def heavy_computation(n):
    """执行 heavy computation"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

print(f"heavy_computation(1000000): {heavy_computation(1000000)}")

# 场景2：输入验证
def validate_input(func):
    """输入验证装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 简单的输入验证
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Input cannot be negative")
        return func(*args, **kwargs)
    
    return wrapper

@validate_input
def calculate_area(length, width):
    """计算面积"""
    return length * width

print(f"calculate_area(5, 10): {calculate_area(5, 10)}")
try:
    calculate_area(-5, 10)
except ValueError as e:
    print(f"Validation error: {e}")

print("\n装饰器练习完成！")
