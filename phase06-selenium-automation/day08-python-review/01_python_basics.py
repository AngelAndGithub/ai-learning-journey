# Day 08: Python基础回顾
# Python基础知识回顾

print("Day 08: Python基础回顾")

# 1. 函数
print("\n1. 函数:")

# 基本函数定义
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 调用函数
print(f"   - 基本函数调用: {greet('Selenium')}")

# 带默认参数的函数
def calculate_area(length, width=10):
    """计算面积"""
    return length * width

print(f"   - 默认参数函数: {calculate_area(5)}")
print(f"   - 自定义参数函数: {calculate_area(5, 8)}")

# 可变参数函数
def sum_numbers(*args):
    """计算多个数的和"""
    return sum(args)

print(f"   - 可变参数函数: {sum_numbers(1, 2, 3, 4, 5)}")

# 关键字参数函数
def print_info(**kwargs):
    """打印信息"""
    for key, value in kwargs.items():
        print(f"   - {key}: {value}")

print("   - 关键字参数函数:")
print_info(name="张三", age=25, city="北京")

# 2. 类
print("\n2. 类:")

class Person:
    """人员类"""
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    
    def greet(self):
        """问候方法"""
        return f"Hello, my name is {self.name}, I'm {self.age} years old."
    
    def celebrate_birthday(self):
        """庆祝生日"""
        self.age += 1
        return f"Happy birthday! Now I'm {self.age} years old."

# 创建对象
person = Person("张三", 25)
print(f"   - 类初始化: {person.greet()}")
print(f"   - 方法调用: {person.celebrate_birthday()}")

# 继承
class Student(Person):
    """学生类，继承自Person"""
    
    def __init__(self, name, age, student_id):
        """初始化方法"""
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self, subject):
        """学习方法"""
        return f"{self.name} is studying {subject}."

# 创建学生对象
student = Student("李四", 20, "2023001")
print(f"   - 继承: {student.greet()}")
print(f"   - 子类方法: {student.study('Python')}")

# 3. 异常处理
print("\n3. 异常处理:")

# 基本异常处理
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   - 捕获异常: {e}")
else:
    print("   - 没有异常")
finally:
    print("   - 无论是否有异常都会执行")

# 多个异常处理
try:
    value = int("abc")
except ValueError as e:
    print(f"   - 捕获值错误: {e}")
except Exception as e:
    print(f"   - 捕获其他异常: {e}")

# 自定义异常
class CustomError(Exception):
    """自定义异常"""
    pass

try:
    raise CustomError("这是一个自定义异常")
except CustomError as e:
    print(f"   - 捕获自定义异常: {e}")

# 4. 文件操作
print("\n4. 文件操作:")

# 写入文件
try:
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Hello, Selenium!\n")
        f.write("Python基础回顾\n")
    print("   - 文件写入成功")
except Exception as e:
    print(f"   - 文件写入失败: {e}")

# 读取文件
try:
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print("   - 文件读取成功:")
    print(f"   {content}")
except Exception as e:
    print(f"   - 文件读取失败: {e}")

# 追加文件
try:
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write("追加的内容\n")
    print("   - 文件追加成功")
except Exception as e:
    print(f"   - 文件追加失败: {e}")

# 读取文件行
try:
    with open("test.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("   - 按行读取文件:")
    for i, line in enumerate(lines, 1):
        print(f"   第{i}行: {line.strip()}")
except Exception as e:
    print(f"   - 按行读取失败: {e}")

# 5. 实际应用示例
print("\n5. 实际应用示例:")

# 配置文件读写
def save_config(config, filename="config.json"):
    """保存配置到文件"""
    import json
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"   - 保存配置失败: {e}")
        return False

def load_config(filename="config.json"):
    """从文件加载配置"""
    import json
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"   - 加载配置失败: {e}")
        return {}

# 测试配置文件操作
config = {
    "browser": "chrome",
    "timeout": 10,
    "base_url": "https://www.example.com"
}

print("   - 保存配置:")
save_config(config)

print("   - 加载配置:")
loaded_config = load_config()
print(f"   {loaded_config}")

# 日志文件
import logging

# 配置日志
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# 记录日志
logging.info("这是一条信息日志")
logging.warning("这是一条警告日志")
logging.error("这是一条错误日志")

print("   - 日志记录成功")

# 6. 与Selenium结合的示例
print("\n6. 与Selenium结合的示例:")

class SeleniumHelper:
    """Selenium辅助类"""
    
    def __init__(self, browser="chrome"):
        """初始化"""
        self.browser = browser
    
    def get_driver(self):
        """获取WebDriver"""
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        try:
            if self.browser == "chrome":
                return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            else:
                raise Exception("不支持的浏览器")
        except Exception as e:
            print(f"   - 获取驱动失败: {e}")
            return None
    
    def take_screenshot(self, driver, filename="screenshot.png"):
        """截图"""
        try:
            driver.save_screenshot(filename)
            print(f"   - 截图保存成功: {filename}")
            return True
        except Exception as e:
            print(f"   - 截图失败: {e}")
            return False

# 测试SeleniumHelper
helper = SeleniumHelper()
driver = helper.get_driver()
if driver:
    try:
        driver.get("https://www.baidu.com")
        helper.take_screenshot(driver, "baidu.png")
    finally:
        driver.quit()

print("\nPython基础回顾完成！")
print("\n学习要点：")
print("1. 函数:")
print("   - 基本函数定义和调用")
print("   - 默认参数、可变参数、关键字参数")
print("2. 类:")
print("   - 类的定义和初始化")
print("   - 方法和属性")
print("   - 继承和多态")
print("3. 异常处理:")
print("   - try-except-finally结构")
print("   - 多个异常处理")
print("   - 自定义异常")
print("4. 文件操作:")
print("   - 打开和关闭文件")
print("   - 读取和写入文件")
print("   - 上下文管理器 (with语句)")
print("5. 实际应用:")
print("   - 配置文件读写")
print("   - 日志记录")
print("   - 与Selenium结合")