#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 5: 面向对象编程

本文件包含Python面向对象编程的练习代码
"""

# 1. 类的定义
print("=== 类的定义 ===")
class Person:
    """人员类"""
    # 类变量
    count = 0
    
    # 初始化方法
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name  # 实例变量
        self.age = age
        Person.count += 1
    
    # 实例方法
    def greet(self):
        """问候方法"""
        return f"Hello, my name is {self.name}, I'm {self.age} years old."
    
    # 类方法
    @classmethod
    def get_count(cls):
        """获取人员数量"""
        return cls.count
    
    # 静态方法
    @staticmethod
    def is_adult(age):
        """判断是否成年"""
        return age >= 18

# 创建实例
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"person1.greet(): {person1.greet()}")
print(f"person2.greet(): {person2.greet()}")
print(f"Person.get_count(): {Person.get_count()}")
print(f"Person.is_adult(18): {Person.is_adult(18)}")
print(f"Person.is_adult(17): {Person.is_adult(17)}")

# 2. 继承
print("\n=== 继承 ===")
class Student(Person):
    """学生类，继承自Person"""
    def __init__(self, name, age, student_id):
        """初始化方法"""
        super().__init__(name, age)  # 调用父类的初始化方法
        self.student_id = student_id
    
    def study(self, subject):
        """学习方法"""
        return f"{self.name} is studying {subject}."
    
    # 重写父类方法
    def greet(self):
        """重写问候方法"""
        return f"Hello, I'm {self.name}, a student with ID {self.student_id}."

# 创建学生实例
student1 = Student("Charlie", 20, "S12345")
print(f"student1.greet(): {student1.greet()}")
print(f"student1.study('Math'): {student1.study('Math')}")
print(f"Student.get_count(): {Student.get_count()}")

# 3. 多态
print("\n=== 多态 ===")
def introduce(person):
    """介绍人员"""
    print(person.greet())

# 多态：不同对象调用相同方法，表现不同行为
introduce(person1)  # Person实例
introduce(student1)  # Student实例

# 4. 封装
print("\n=== 封装 ===")
class BankAccount:
    """银行账户类"""
    def __init__(self, account_holder, balance=0):
        """初始化方法"""
        self.account_holder = account_holder
        self.__balance = balance  # 私有属性，以双下划线开头
    
    def deposit(self, amount):
        """存款方法"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """取款方法"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid withdrawal amount"
    
    def get_balance(self):
        """获取余额（通过方法访问私有属性）"""
        return self.__balance

# 创建银行账户实例
account = BankAccount("Alice", 1000)
print(f"Initial balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))
# print(account.__balance)  # 会报错，私有属性不能直接访问

# 5. 抽象类和接口
print("\n=== 抽象类和接口 ===")
from abc import ABC, abstractmethod

class Shape(ABC):
    """形状抽象类"""
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass

class Rectangle(Shape):
    """矩形类"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圆形类"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 创建形状实例
rectangle = Rectangle(10, 5)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

# 6. 特殊方法
print("\n=== 特殊方法 ===")
class Vector:
    """向量类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 加法
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # 减法
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # 乘法（标量）
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # 字符串表示
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # 长度
    def __abs__(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

# 创建向量实例
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"|v1|: {abs(v1)}")

print("\n面向对象编程练习完成！")
