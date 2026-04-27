# Day 1 - 条件语句实战练习
# 学习目标：掌握if-elif-else的使用

print("=" * 60)
print("🔀 条件语句实战练习")
print("=" * 60)
print()

# ==========================================
# 练习1: 成绩等级判断系统
# ==========================================
print("练习1: 成绩等级判断系统")
print("-" * 60)

def get_grade(score):
    """根据分数返回等级"""
    if score < 0 or score > 100:
        return "无效分数"
    elif score >= 90:
        return "A (优秀)"
    elif score >= 80:
        return "B (良好)"
    elif score >= 70:
        return "C (中等)"
    elif score >= 60:
        return "D (及格)"
    else:
        return "F (不及格)"

# 测试多个分数
test_scores = [95, 87, 73, 65, 45, 100, 0, -5, 105]

print(f"{'分数':<8}{'等级':<15}{'评价'}")
print("-" * 60)
for score in test_scores:
    grade = get_grade(score)
    if score >= 90:
        comment = "太棒了！"
    elif score >= 80:
        comment = "不错！"
    elif score >= 70:
        comment = "继续努力"
    elif score >= 60:
        comment = "刚好及格"
    else:
        comment = "需要加油"
    
    if 0 <= score <= 100:
        print(f"{score:<8}{grade:<15}{comment}")
    else:
        print(f"{score:<8}{grade:<15}")

print()

# ==========================================
# 练习2: 闰年判断器
# ==========================================
print("练习2: 闰年判断器")
print("-" * 60)

def is_leap_year(year):
    """判断是否为闰年"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 测试多个年份
test_years = [2024, 2023, 2000, 1900, 2020, 2100]

for year in test_years:
    if is_leap_year(year):
        print(f"{year}年 是闰年 ✓")
    else:
        print(f"{year}年 不是闰年 ✗")

print()

# ==========================================
# 练习3: 简单计算器
# ==========================================
print("练习3: 简单计算器")
print("-" * 60)

def calculator(num1, num2, operator):
    """简单的四则运算"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "错误：除数不能为0"
        return num1 / num2
    else:
        return "错误：不支持的运算符"

# 测试计算器
test_cases = [
    (10, 5, '+'),
    (10, 5, '-'),
    (10, 5, '*'),
    (10, 5, '/'),
    (10, 0, '/'),
    (10, 5, '%'),
]

print(f"{'操作数1':<10}{'操作数2':<10}{'运算符':<8}{'结果'}")
print("-" * 60)
for num1, num2, op in test_cases:
    result = calculator(num1, num2, op)
    print(f"{num1:<10}{num2:<10}{op:<8}{result}")

print()

# ==========================================
# 练习4: BMI健康评估
# ==========================================
print("练习4: BMI健康评估")
print("-" * 60)

def bmi_assessment(height_cm, weight_kg):
    """计算BMI并给出健康建议"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    print(f"身高: {height_cm}cm")
    print(f"体重: {weight_kg}kg")
    print(f"BMI指数: {bmi:.1f}")
    
    if bmi < 18.5:
        category = "偏瘦"
        advice = "建议增加营养摄入"
    elif bmi < 24:
        category = "正常"
        advice = "保持健康的生活方式"
    elif bmi < 28:
        category = "偏胖"
        advice = "建议适当运动和饮食控制"
    else:
        category = "肥胖"
        advice = "建议咨询医生制定减重计划"
    
    print(f"健康状态: {category}")
    print(f"建议: {advice}")
    return bmi

# 测试不同体型
print("案例1:")
bmi_assessment(175, 65)
print()

print("案例2:")
bmi_assessment(170, 85)
print()

# ==========================================
# 练习5: 票价计算系统
# ==========================================
print("练习5: 票价计算系统")
print("-" * 60)

def calculate_ticket_price(age, is_student=False, is_weekend=False):
    """根据年龄、身份和时间计算票价"""
    base_price = 100
    
    # 年龄优惠
    if age < 6:
        price = 0
        discount = "免费"
    elif age < 12:
        price = base_price * 0.5
        discount = "儿童5折"
    elif age >= 65:
        price = base_price * 0.6
        discount = "老人6折"
    else:
        price = base_price
        discount = "全价"
    
    # 学生优惠
    if is_student and age >= 12:
        price *= 0.8
        discount += "+学生8折"
    
    # 周末加价
    if is_weekend:
        price += 20
        discount += "+周末附加"
    
    return price, discount

# 测试不同情况
test_cases = [
    (5, False, False, "幼儿"),
    (10, False, False, "儿童"),
    (25, True, False, "学生"),
    (70, False, False, "老人"),
    (30, False, True, "周末成人"),
    (20, True, True, "周末学生"),
]

print(f"{'年龄':<8}{'学生':<8}{'周末':<8}{'类型':<10}{'票价':<10}{'优惠'}")
print("-" * 70)
for age, is_student, is_weekend, person_type in test_cases:
    price, discount = calculate_ticket_price(age, is_student, is_weekend)
    student_str = "是" if is_student else "否"
    weekend_str = "是" if is_weekend else "否"
    print(f"{age:<8}{student_str:<8}{weekend_str:<8}{person_type:<10}¥{price:<8.1f}{discount}")

print()

# ==========================================
# 练习6: 嵌套条件 - 登录系统
# ==========================================
print("练习6: 嵌套条件 - 登录系统")
print("-" * 60)

def login_system(username, password, is_vip=False):
    """模拟登录系统"""
    # 预设账号密码
    valid_users = {
        "admin": "admin123",
        "user": "user123",
        "vip": "vip123"
    }
    
    if username in valid_users:
        if password == valid_users[username]:
            print(f"✓ {username} 登录成功！")
            if is_vip:
                print("  欢迎VIP用户！")
                print("  享受专属特权")
            else:
                print("  欢迎普通用户！")
            return True
        else:
            print(f"✗ 密码错误！")
            return False
    else:
        print(f"✗ 用户名不存在！")
        return False

# 测试登录
print("测试1: 正确登录")
login_system("admin", "admin123")
print()

print("测试2: 密码错误")
login_system("admin", "wrong")
print()

print("测试3: VIP登录")
login_system("vip", "vip123", is_vip=True)
print()

print("测试4: 用户不存在")
login_system("unknown", "123")
print()

# ==========================================
# 学习总结
# ==========================================
print("=" * 60)
print("✅ 条件语句练习完成！")
print("=" * 60)
print()
print("完成的练习：")
print("  ✓ 成绩等级判断系统")
print("  ✓ 闰年判断器")
print("  ✓ 简单计算器")
print("  ✓ BMI健康评估")
print("  ✓ 票价计算系统")
print("  ✓ 登录系统（嵌套条件）")
print()
print("掌握的技能：")
print("  ✓ if-elif-else基本用法")
print("  ✓ 多重条件判断")
print("  ✓ 逻辑运算符使用")
print("  ✓ 嵌套条件语句")
print("  ✓ 实际应用场景")
print()
print("下一步：学习循环结构")
print("=" * 60)
