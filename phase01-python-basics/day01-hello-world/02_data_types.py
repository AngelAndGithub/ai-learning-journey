# Day 1 - 数据类型详解与操作
# 学习目标：深入理解Python的各种数据类型

print("=" * 60)
print("📚 Python数据类型详解")
print("=" * 60)
print()

# ==========================================
# 1. 数字类型（Number）
# ==========================================
print("1️⃣  数字类型")
print("-" * 60)

# 整数
print("\n【整数 int】")
age = 25
year = 2026
negative_num = -10
print(f"年龄: {age}, 类型: {type(age)}")
print(f"年份: {year}, 类型: {type(year)}")
print(f"负数: {negative_num}")

# 浮点数
print("\n【浮点数 float】")
height = 175.5
weight = 65.0
pi = 3.14159
print(f"身高: {height}, 类型: {type(height)}")
print(f"体重: {weight}, 类型: {type(weight)}")
print(f"圆周率: {pi}")

# 复数
print("\n【复数 complex】")
complex_num = 3 + 4j
print(f"复数: {complex_num}, 类型: {type(complex_num)}")
print(f"实部: {complex_num.real}, 虚部: {complex_num.imag}")

# 类型转换
print("\n【类型转换】")
print(f"int(3.14) = {int(3.14)}")
print(f"float(5) = {float(5)}")
print(f"int('10') = {int('10')}")

print()

# ==========================================
# 2. 字符串类型（String）
# ==========================================
print("2️⃣  字符串类型")
print("-" * 60)

# 字符串定义
print("\n【字符串定义】")
name = "AI学习者"
course = 'Python基础'
description = """
这是一个多行字符串
可以包含换行
和特殊字符
"""
print(f"姓名: {name}")
print(f"课程: {course}")
print(f"描述: {description}")

# 字符串操作
print("\n【字符串操作】")
text = "Hello, Python!"
print(f"原文: {text}")
print(f"长度: {len(text)}")
print(f"转大写: {text.upper()}")
print(f"转小写: {text.lower()}")
print(f"标题化: {text.title()}")
print(f"替换: {text.replace('Python', 'AI')}")
print(f"分割: {text.split(',')}")

# 字符串索引和切片
print("\n【索引和切片】")
text = "Python编程"
print(f"原文: {text}")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"前3个字符: {text[0:3]}")
print(f"最后2个字符: {text[-2:]}")
print(f"反转: {text[::-1]}")

# 字符串格式化
print("\n【字符串格式化】")
name = "张三"
age = 25
score = 95.5

# 方法1: f-string（推荐）
print(f"姓名: {name}, 年龄: {age}, 分数: {score}")

# 方法2: format()
print("姓名: {}, 年龄: {}, 分数: {}".format(name, age, score))

# 方法3: %格式化
print("姓名: %s, 年龄: %d, 分数: %.2f" % (name, age, score))

# 格式化选项
print(f"\n对齐示例：")
print(f"左对齐: {name:<10}|")
print(f"右对齐: {name:>10}|")
print(f"居中对齐: {name:^10}|")
print(f"补零: {age:05d}")
print(f"保留2位小数: {score:.2f}")

# 字符串方法
print("\n【常用字符串方法】")
text = "  hello world  "
print(f"原文: '{text}'")
print(f"去除两端空格: '{text.strip()}'")
print(f"是否全数字: {'123'.isdigit()}")
print(f"是否全字母: {'abc'.isalpha()}")
print(f"查找子串位置: {'hello world'.find('world')}")
print(f"统计出现次数: 'hello world'.count('o'): {'hello world'.count('o')}")

print()

# ==========================================
# 3. 布尔类型（Boolean）
# ==========================================
print("3️⃣  布尔类型")
print("-" * 60)

is_student = True
is_teacher = False
print(f"是学生: {is_student}, 类型: {type(is_student)}")
print(f"是老师: {is_teacher}, 类型: {type(is_teacher)}")

# 布尔运算
print("\n【布尔运算】")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# 比较运算返回布尔值
print("\n【比较运算】")
a, b = 10, 20
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= 10: {a >= 10}")
print(f"b <= 20: {b <= 20}")

# 真值测试
print("\n【真值测试】")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool([1,2,3]): {bool([1,2,3])}")

print()

# ==========================================
# 4. 类型检查与转换
# ==========================================
print("4️⃣  类型检查与转换")
print("-" * 60)

# 类型检查
value1 = 42
value2 = 3.14
value3 = "hello"
value4 = True

print(f"{value1} 的类型: {type(value1)}")
print(f"{value2} 的类型: {type(value2)}")
print(f"{value3} 的类型: {type(value3)}")
print(f"{value4} 的类型: {type(value4)}")

# isinstance检查
print("\n【isinstance检查】")
print(f"42是整数吗? {isinstance(42, int)}")
print(f"3.14是浮点数吗? {isinstance(3.14, float)}")
print(f"'hello'是字符串吗? {isinstance('hello', str)}")
print(f"True是布尔值吗? {isinstance(True, bool)}")

# 类型转换示例
print("\n【类型转换示例】")
print(f"int(3.9) = {int(3.9)}")  # 截断
print(f"float(5) = {float(5)}")
print(f"str(100) = '{str(100)}'")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"int('100') = {int('100')}")
print(f"float('3.14') = {float('3.14')}")

print()

# ==========================================
# 5. 综合练习
# ==========================================
print("5️⃣  综合练习")
print("-" * 60)

# 练习1: 用户信息卡片
print("\n【练习1: 用户信息卡片】")
user_name = "AI学习者"
user_age = 25
user_height = 175.5
is_vip = True

print("=" * 40)
print(f"{'用户信息卡':^30}")
print("=" * 40)
print(f"{'姓名:':<10}{user_name}")
print(f"{'年龄:':<10}{user_age}岁")
print(f"{'身高:':<10}{user_height}cm")
print(f"{'VIP会员:':<10}{'是' if is_vip else '否'}")
print("=" * 40)

# 练习2: 温度转换
print("\n【练习2: 温度转换】")
celsius = 36.5
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# 练习3: 字符串处理
print("\n【练习3: 字符串处理】")
email = "  AI_LEARNER@EXAMPLE.COM  "
print(f"原始邮箱: '{email}'")
email_clean = email.strip().lower()
print(f"清理后: '{email_clean}'")
print(f"域名: {email_clean.split('@')[1]}")

print()

# ==========================================
# 6. 学习总结
# ==========================================
print("=" * 60)
print("✅ 数据类型学习完成！")
print("=" * 60)
print()
print("掌握的数据类型：")
print("  ✓ 整数 (int)")
print("  ✓ 浮点数 (float)")
print("  ✓ 字符串 (str)")
print("  ✓ 布尔值 (bool)")
print("  ✓ 复数 (complex)")
print()
print("掌握的技能：")
print("  ✓ 类型转换")
print("  ✓ 字符串操作")
print("  ✓ 字符串格式化")
print("  ✓ 类型检查")
print()
print("下一步：学习列表、字典、元组、集合")
print("=" * 60)
