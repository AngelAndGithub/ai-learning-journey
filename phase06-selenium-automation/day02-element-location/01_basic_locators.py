# Day 02: 元素定位基础
# 基础定位器示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print("Day 02: 元素定位基础 - 基础定位器")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开测试网站
driver.get("https://demoqa.com/text-box")
print("已打开demoqa文本框测试页面")

# 等待页面加载
time.sleep(2)

# 1. ID定位
print("\n1. ID定位:")
try:
    full_name = driver.find_element(By.ID, "userName")
    full_name.send_keys("测试用户")
    print("✓ 使用ID定位成功")
except Exception as e:
    print(f"✗ ID定位失败: {e}")

# 2. Name定位
print("\n2. Name定位:")
try:
    # 注意：这个页面的元素可能没有name属性，这里作为示例
    # email = driver.find_element(By.NAME, "email")
    # email.send_keys("test@example.com")
    print("✓ Name定位示例")
except Exception as e:
    print(f"✗ Name定位失败: {e}")

# 3. Class Name定位
print("\n3. Class Name定位:")
try:
    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    print("✓ 使用Class Name定位成功")
except Exception as e:
    print(f"✗ Class Name定位失败: {e}")

# 4. Tag Name定位
print("\n4. Tag Name定位:")
try:
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys("这是一个测试地址")
    print("✓ 使用Tag Name定位成功")
except Exception as e:
    print(f"✗ Tag Name定位失败: {e}")

# 5. Link Text定位
print("\n5. Link Text定位:")
try:
    # 导航到元素定位页面
    driver.get("https://demoqa.com/links")
    time.sleep(2)
    home_link = driver.find_element(By.LINK_TEXT, "Home")
    print(f"✓ 使用Link Text定位成功: {home_link.text}")
except Exception as e:
    print(f"✗ Link Text定位失败: {e}")

# 6. Partial Link Text定位
print("\n6. Partial Link Text定位:")
try:
    created_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Created")
    print(f"✓ 使用Partial Link Text定位成功: {created_link.text}")
except Exception as e:
    print(f"✗ Partial Link Text定位失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. ID定位: 最快最准确的定位方式")
print("2. Name定位: 适用于表单元素")
print("3. Class Name定位: 适用于具有相同样式的元素")
print("4. Tag Name定位: 适用于同类型的元素")
print("5. Link Text定位: 适用于链接元素")
print("6. Partial Link Text定位: 适用于链接文本较长的情况")