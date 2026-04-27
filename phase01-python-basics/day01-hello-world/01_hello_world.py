# Day 1 - Hello World 与环境测试
# 学习目标：完成Python环境搭建，编写第一个程序

print("=" * 50)
print("🎉 欢迎开始AI学习之旅！")
print("=" * 50)
print()

# 1. 第一个Python程序
print("📝 我的第一个Python程序：")
print("Hello, AI Learning!")
print("今天是学习AI开发工程师的第一天！")
print()

# 2. 检查Python版本
import sys
print("💻 Python环境信息：")
print(f"Python版本: {sys.version}")
print(f"Python版本信息: {sys.version_info}")
print()

# 3. 测试基本数据类型
print("🔢 基本数据类型测试：")

# 整数
age = 25
print(f"年龄(整数): {age} - 类型: {type(age)}")

# 浮点数
height = 175.5
print(f"身高(浮点数): {height} - 类型: {type(height)}")

# 字符串
name = "AI学习者"
print(f"姓名(字符串): {name} - 类型: {type(name)}")

# 布尔值
is_learning = True
print(f"是否在学习中(布尔值): {is_learning} - 类型: {type(is_learning)}")
print()

# 4. 运算符练习
print("➕ 运算符练习：")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法: a / b = {a / b}")
print(f"整除: a // b = {a // b}")
print(f"取余: a % b = {a % b}")
print(f"幂运算: a ** b = {a ** b}")
print()

# 5. 字符串操作
print("📝 字符串操作：")
greeting = f"你好，我叫{name}，今年{age}岁，身高{height}cm"
print(greeting)

print(f"字符串长度: {len(name)}")
print(f"转大写: {name.upper()}")
print(f"重复3次: {name * 3}")
print()

# 6. 条件语句练习
print("🔀 条件语句练习：")

score = 85
print(f"分数: {score}")

if score >= 90:
    grade = "A"
    print("优秀！")
elif score >= 80:
    grade = "B"
    print("良好！")
elif score >= 70:
    grade = "C"
    print("中等")
elif score >= 60:
    grade = "D"
    print("及格")
else:
    grade = "F"
    print("不及格")

print(f"等级: {grade}")
print()

# 7. for循环练习
print("🔄 for循环练习：")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("我喜欢的水果：")
for fruit in fruits:
    print(f"  - {fruit}")

print()

# range()使用
print("数字1-5：")
for i in range(1, 6):
    print(f"  数字: {i}")

print()

# 九九乘法表（简化版）
print("📊 九九乘法表（前5行）：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end=" ")
    print()

print()

# 8. while循环练习
print("⏳ while循环练习：")

count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

print()

# 9. 综合练习
print("🎯 综合练习：计算1-100的和")

# 方法1：for循环
total_for = 0
for i in range(1, 101):
    total_for += i
print(f"使用for循环: 1+2+...+100 = {total_for}")

# 方法2：数学公式
total_math = (1 + 100) * 100 // 2
print(f"使用数学公式: 1+2+...+100 = {total_math}")

print()

# 10. 学习总结
print("=" * 50)
print("✅ Day 1 学习完成！")
print("=" * 50)
print()
print("今日收获：")
print("  ✓ Python环境搭建成功")
print("  ✓ 掌握了基本数据类型")
print("  ✓ 学会了运算符使用")
print("  ✓ 理解了条件语句")
print("  ✓ 掌握了循环结构")
print()
print("明天继续学习：函数、模块与异常处理")
print("=" * 50)
