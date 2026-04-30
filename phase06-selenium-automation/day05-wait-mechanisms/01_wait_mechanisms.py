# Day 05: 等待机制
# 等待机制示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

print("Day 05: 等待机制")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. 隐式等待
print("\n1. 隐式等待:")

# 设置隐式等待时间为10秒
driver.implicitly_wait(10)
print("   ✓ 设置隐式等待时间为10秒")

# 打开测试网站
driver.get("https://demoqa.com/dynamic-properties")
print("   ✓ 打开动态属性测试页面")

# 尝试点击一个需要等待的按钮
print("   - 点击可见按钮:")
try:
    visible_button = driver.find_element(By.ID, "visibleAfter")
    visible_button.click()
    print("   ✓ 成功点击可见按钮")
except Exception as e:
    print(f"   ✗ 点击失败: {e}")

# 2. 显式等待
print("\n2. 显式等待:")

# 等待按钮变为可点击
print("   - 等待按钮变为可点击:")
try:
    enable_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    enable_button.click()
    print("   ✓ 成功点击启用按钮")
except TimeoutException:
    print("   ✗ 等待超时，按钮未启用")
except Exception as e:
    print(f"   ✗ 操作失败: {e}")

# 等待元素可见
print("   - 等待元素可见:")
try:
    visible_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    print("   ✓ 元素已可见")
except TimeoutException:
    print("   ✗ 等待超时，元素未可见")
except Exception as e:
    print(f"   ✗ 操作失败: {e}")

# 3. 常用的Expected Conditions
print("\n3. 常用的Expected Conditions:")

# 导航到新页面进行测试
driver.get("https://demoqa.com/elements")
print("   ✓ 打开元素测试页面")

# 元素存在
print("   - 元素存在:")
try:
    element_present = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main-header"))
    )
    print("   ✓ 元素存在")
except TimeoutException:
    print("   ✗ 元素不存在")

# 元素文本包含
print("   - 元素文本包含:")
try:
    text_present = WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "main-header"), "Elements"
        )
    )
    print("   ✓ 元素文本包含'Elements'")
except TimeoutException:
    print("   ✗ 元素文本不包含指定内容")

# 标题包含
print("   - 标题包含:")
try:
    title_contains = WebDriverWait(driver, 5).until(
        EC.title_contains("Demo Q")
    )
    print("   ✓ 标题包含'Demo Q'")
except TimeoutException:
    print("   ✗ 标题不包含指定内容")

# 4. 自定义等待条件
print("\n4. 自定义等待条件:")

def element_has_css_class(driver, locator, class_name):
    """自定义等待条件：元素是否包含指定的CSS类"""
    try:
        element = driver.find_element(*locator)
        return class_name in element.get_attribute("class")
    except:
        return False

# 测试自定义等待条件
print("   - 自定义等待条件测试:")
try:
    custom_wait = WebDriverWait(driver, 5)
    result = custom_wait.until(
        lambda driver: element_has_css_class(
            driver, (By.CLASS_NAME, "main-header"), "main-header"
        )
    )
    print("   ✓ 自定义等待条件测试成功")
except TimeoutException:
    print("   ✗ 自定义等待条件测试失败")

# 5. 等待策略对比
print("\n5. 等待策略对比:")

# 对比隐式等待和显式等待
print("   - 隐式等待:")
print("     ✓ 全局设置，适用于所有元素定位")
print("     ✓ 代码简洁")
print("     ✗ 不够灵活，只能等待元素存在")

print("   - 显式等待:")
print("     ✓ 灵活，可以等待各种条件")
print("     ✓ 可以设置不同的等待时间")
print("     ✗ 代码相对复杂")

print("   - 最佳实践:")
print("     ✓ 结合使用隐式等待和显式等待")
print("     ✓ 对关键操作使用显式等待")
print("     ✓ 合理设置等待时间，避免过长或过短")

# 6. 等待时间设置建议
print("\n6. 等待时间设置建议:")
print("   - 隐式等待: 5-10秒")
print("   - 显式等待: 根据具体操作复杂度设置")
print("   - 网络较慢时: 适当增加等待时间")
print("   - CI/CD环境: 可能需要更长的等待时间")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. 隐式等待:")
print("   - implicitly_wait() 设置全局等待时间")
print("   - 适用于所有元素定位操作")
print("2. 显式等待:")
print("   - WebDriverWait 类")
print("   - expected_conditions 模块")
print("   - 可以等待各种条件")
print("3. 常用的Expected Conditions:")
print("   - presence_of_element_located: 元素存在")
print("   - visibility_of_element_located: 元素可见")
print("   - element_to_be_clickable: 元素可点击")
print("   - text_to_be_present_in_element: 文本存在")
print("4. 自定义等待条件:")
print("   - 使用lambda表达式")
print("   - 定义自定义函数")
print("5. 等待策略:")
print("   - 结合使用隐式和显式等待")
print("   - 根据操作复杂度设置合理的等待时间")