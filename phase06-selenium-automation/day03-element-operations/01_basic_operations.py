# Day 03: 元素操作
# 基础元素操作示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print("Day 03: 元素操作 - 基础操作")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开测试网站
driver.get("https://demoqa.com/text-box")
print("已打开demoqa文本框测试页面")

# 等待页面加载
time.sleep(2)

# 1. 输入操作
print("\n1. 输入操作:")
try:
    # 输入姓名
    full_name = driver.find_element(By.ID, "userName")
    full_name.send_keys("测试用户")
    print("✓ 输入姓名成功")
    
    # 输入邮箱
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("test@example.com")
    print("✓ 输入邮箱成功")
    
    # 输入当前地址
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("北京市朝阳区")
    print("✓ 输入当前地址成功")
    
    # 输入永久地址
    permanent_address = driver.find_element(By.ID, "permanentAddress")
    permanent_address.send_keys("上海市浦东新区")
    print("✓ 输入永久地址成功")
    
except Exception as e:
    print(f"✗ 输入操作失败: {e}")

# 2. 点击操作
print("\n2. 点击操作:")
try:
    submit_button = driver.find_element(By.ID, "submit")
    # 滚动到按钮位置
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(1)
    submit_button.click()
    print("✓ 点击提交按钮成功")
except Exception as e:
    print(f"✗ 点击操作失败: {e}")

# 3. 清除操作
print("\n3. 清除操作:")
try:
    full_name = driver.find_element(By.ID, "userName")
    full_name.clear()
    full_name.send_keys("新用户")
    print("✓ 清除并重新输入成功")
except Exception as e:
    print(f"✗ 清除操作失败: {e}")

# 4. 获取元素属性
print("\n4. 获取元素属性:")
try:
    submit_button = driver.find_element(By.ID, "submit")
    button_text = submit_button.text
    button_class = submit_button.get_attribute("class")
    print(f"✓ 按钮文本: {button_text}")
    print(f"✓ 按钮Class: {button_class}")
except Exception as e:
    print(f"✗ 获取属性失败: {e}")

# 5. 获取元素文本
print("\n5. 获取元素文本:")
try:
    # 导航到元素页面
    driver.get("https://demoqa.com/elements")
    time.sleep(2)
    
    element_title = driver.find_element(By.CLASS_NAME, "main-header")
    print(f"✓ 页面标题: {element_title.text}")
except Exception as e:
    print(f"✗ 获取文本失败: {e}")

# 6. 提交操作
print("\n6. 提交操作:")
try:
    # 导航到表单页面
    driver.get("https://demoqa.com/text-box")
    time.sleep(2)
    
    full_name = driver.find_element(By.ID, "userName")
    full_name.send_keys("提交测试")
    
    # 使用submit方法
    full_name.submit()
    print("✓ 提交操作成功")
except Exception as e:
    print(f"✗ 提交操作失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. send_keys(): 输入文本")
print("2. click(): 点击元素")
print("3. clear(): 清除文本")
print("4. get_attribute(): 获取元素属性")
print("5. text: 获取元素文本")
print("6. submit(): 提交表单")