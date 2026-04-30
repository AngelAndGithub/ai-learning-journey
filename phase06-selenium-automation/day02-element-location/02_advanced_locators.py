# Day 02: 元素定位基础
# 高级定位器示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print("Day 02: 元素定位基础 - 高级定位器")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开测试网站
driver.get("https://demoqa.com/automation-practice-form")
print("已打开demoqa表单测试页面")

# 等待页面加载
time.sleep(2)

# 1. CSS Selector定位
print("\n1. CSS Selector定位:")

# 通过ID定位
print("   - 通过ID定位:")
try:
    first_name = driver.find_element(By.CSS_SELECTOR, "#firstName")
    first_name.send_keys("张")
    print("   ✓ CSS ID定位成功")
except Exception as e:
    print(f"   ✗ CSS ID定位失败: {e}")

# 通过Class定位
print("   - 通过Class定位:")
try:
    last_name = driver.find_element(By.CSS_SELECTOR, ".form-control")
    last_name.send_keys("三")
    print("   ✓ CSS Class定位成功")
except Exception as e:
    print(f"   ✗ CSS Class定位失败: {e}")

# 通过属性定位
print("   - 通过属性定位:")
try:
    email = driver.find_element(By.CSS_SELECTOR, "[type='email']")
    email.send_keys("test@example.com")
    print("   ✓ CSS属性定位成功")
except Exception as e:
    print(f"   ✗ CSS属性定位失败: {e}")

# 通过层级关系定位
print("   - 通过层级关系定位:")
try:
    gender = driver.find_element(By.CSS_SELECTOR, ".custom-control-label")
    print(f"   ✓ CSS层级定位成功: {gender.text}")
except Exception as e:
    print(f"   ✗ CSS层级定位失败: {e}")

# 2. XPath定位
print("\n2. XPath定位:")

# 绝对路径（不推荐）
print("   - 绝对路径:")
try:
    mobile = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[2]/input")
    mobile.send_keys("13800138000")
    print("   ✓ XPath绝对路径定位成功")
except Exception as e:
    print(f"   ✗ XPath绝对路径定位失败: {e}")

# 相对路径
print("   - 相对路径:")
try:
    address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    address.send_keys("北京市朝阳区")
    print("   ✓ XPath相对路径定位成功")
except Exception as e:
    print(f"   ✗ XPath相对路径定位失败: {e}")

# 包含文本
print("   - 包含文本:")
try:
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    print("   ✓ XPath包含文本定位成功")
except Exception as e:
    print(f"   ✗ XPath包含文本定位失败: {e}")

# 逻辑运算符
print("   - 逻辑运算符:")
try:
    hobbies = driver.find_element(By.XPATH, "//label[text()='Sports' or text()='Reading']")
    print(f"   ✓ XPath逻辑运算符定位成功: {hobbies.text}")
except Exception as e:
    print(f"   ✗ XPath逻辑运算符定位失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. CSS Selector:")
print("   - #id: 通过ID定位")
print("   - .class: 通过Class定位")
print("   - [attribute='value']: 通过属性定位")
print("   - parent > child: 通过父子关系定位")
print("2. XPath:")
print("   - //tagname: 相对路径")
print("   - /tagname: 绝对路径")
print("   - [@attribute='value']: 属性条件")
print("   - contains(text(), 'value'): 包含文本")
print("   - and/or: 逻辑运算符")
print("3. 定位器选择建议:")
print("   - 优先使用ID和Name")
print("   - 其次使用CSS Selector")
print("   - 最后使用XPath")