# Day 1 - 循环结构实战练习
# 学习目标：掌握for循环和while循环的使用

print("=" * 60)
print("🔄 循环结构实战练习")
print("=" * 60)
print()

# ==========================================
# 练习1: 基础for循环
# ==========================================
print("练习1: 基础for循环")
print("-" * 60)

# 遍历列表
print("【遍历列表】")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print(f"水果列表: {fruits}")
print("我喜欢的水果：")
for fruit in fruits:
    print(f"  🍎 {fruit}")

print()

# 遍历字符串
print("【遍历字符串】")
word = "Python"
print(f"单词: {word}")
print("字母分解：")
for letter in word:
    print(f"  {letter}")

print()

# range()函数
print("【range()函数】")
print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

print()

# ==========================================
# 练习2: 九九乘法表
# ==========================================
print("练习2: 九九乘法表")
print("-" * 60)

print("完整九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()  # 换行

print()

# ==========================================
# 练习3: 数列求和
# ==========================================
print("练习3: 数列求和")
print("-" * 60)

# 求1-100的和
total = 0
for i in range(1, 101):
    total += i
print(f"1+2+3+...+100 = {total}")

# 求1-100中偶数的和
even_sum = 0
for i in range(2, 101, 2):
    even_sum += i
print(f"2+4+6+...+100 = {even_sum}")

# 求1-100中奇数的和
odd_sum = 0
for i in range(1, 101, 2):
    odd_sum += i
print(f"1+3+5+...+99 = {odd_sum}")

print()

# ==========================================
# 练习4: 图案打印
# ==========================================
print("练习4: 图案打印")
print("-" * 60)

# 直角三角形
print("【直角三角形】")
for i in range(1, 6):
    print("*" * i)

print()

# 倒直角三角形
print("【倒直角三角形】")
for i in range(5, 0, -1):
    print("*" * i)

print()

# 等腰三角形
print("【等腰三角形】")
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print()

# 菱形
print("【菱形】")
# 上半部分
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
# 下半部分
for i in range(4, 0, -1):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print()

# ==========================================
# 练习5: 数字游戏
# ==========================================
print("练习5: 数字游戏")
print("-" * 60)

# 找出1-100中能被3或5整除的数
print("【能被3或5整除的数】")
count = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(f"{i:3d}", end=" ")
        count += 1
        if count % 10 == 0:  # 每10个换行
            print()

print(f"\n共找到 {count} 个数")

print()

# 找出1-100中的质数
print("【1-100中的质数】")
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(f"质数共 {len(primes)} 个：")
for i, prime in enumerate(primes, 1):
    print(f"{prime:3d}", end=" ")
    if i % 10 == 0:
        print()

print()

# ==========================================
# 练习6: while循环练习
# ==========================================
print("练习6: while循环练习")
print("-" * 60)

# 倒计时
print("【倒计时】")
countdown = 5
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("🚀 发射！")

print()

# 猜数字游戏
print("【猜数字游戏】")
import random
target = random.randint(1, 10)
attempts = 0
max_attempts = 3

print(f"我想了一个1-10之间的数字，你有{max_attempts}次机会猜中它。")

while attempts < max_attempts:
    guess = int(input(f"\n第{attempts + 1}次猜测，请输入数字: "))
    attempts += 1
    
    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print(f"🎉 恭喜你！猜对了！答案就是 {target}")
        break
else:
    print(f"\n😢 很遗憾，机会用完了。答案是 {target}")

print()

# ==========================================
# 练习7: break和continue
# ==========================================
print("练习7: break和continue")
print("-" * 60)

# break示例：找到第一个能被7整除的数
print("【break示例】")
print("找到1-50中第一个能被7整除的数：")
for i in range(1, 51):
    if i % 7 == 0:
        print(f"找到了！是 {i}")
        break
    print(i, end=" ")

print()

# continue示例：跳过偶数
print("\n【continue示例】")
print("1-20中的所有奇数：")
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print()

# ==========================================
# 练习8: 嵌套循环 - 数据分析
# ==========================================
print("练习8: 嵌套循环 - 学生成绩分析")
print("-" * 60)

# 学生成绩数据
students = {
    "张三": [85, 90, 78, 92],
    "李四": [75, 82, 88, 80],
    "王五": [95, 92, 90, 98],
    "赵六": [60, 65, 70, 68],
}

print("学生成绩分析：")
print("=" * 60)

for name, scores in students.items():
    total = 0
    max_score = scores[0]
    min_score = scores[0]
    
    print(f"\n{name}的成绩：")
    print(f"  各科成绩: {scores}")
    
    # 计算总分、最高分、最低分
    for score in scores:
        total += score
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
    
    average = total / len(scores)
    
    print(f"  总分: {total}")
    print(f"  平均分: {average:.1f}")
    print(f"  最高分: {max_score}")
    print(f"  最低分: {min_score}")
    
    # 等级评定
    if average >= 90:
        grade = "优秀"
    elif average >= 80:
        grade = "良好"
    elif average >= 70:
        grade = "中等"
    elif average >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    
    print(f"  等级: {grade}")

print()

# ==========================================
# 练习9: 列表推导式（预习）
# ==========================================
print("练习9: 列表推导式（第3天详细学习）")
print("-" * 60)

# 基本列表推导式
squares = [x**2 for x in range(1, 11)]
print(f"1-10的平方: {squares}")

# 带条件的列表推导式
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"1-10中偶数的平方: {even_squares}")

# 嵌套列表推导式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3乘法矩阵:")
for row in matrix:
    print(f"  {row}")

print()

# ==========================================
# 学习总结
# ==========================================
print("=" * 60)
print("✅ 循环结构练习完成！")
print("=" * 60)
print()
print("完成的练习：")
print("  ✓ 基础for循环")
print("  ✓ 九九乘法表")
print("  ✓ 数列求和")
print("  ✓ 图案打印")
print("  ✓ 数字游戏")
print("  ✓ while循环练习")
print("  ✓ break和continue")
print("  ✓ 嵌套循环 - 数据分析")
print("  ✓ 列表推导式（预习）")
print()
print("掌握的技能：")
print("  ✓ for循环遍历")
print("  ✓ range()函数使用")
print("  ✓ while循环")
print("  ✓ break和continue控制")
print("  ✓ 嵌套循环")
print("  ✓ 实际应用场景")
print()
print("Day 1 学习圆满完成！🎉")
print("=" * 60)
