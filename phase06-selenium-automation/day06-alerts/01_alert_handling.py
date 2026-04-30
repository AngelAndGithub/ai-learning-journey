# Day 06: 处理弹窗
# 弹窗处理示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Day 06: 处理弹窗")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开测试网站
driver.get("https://demoqa.com/alerts")
print("已打开弹窗测试页面")

# 等待页面加载
time.sleep(2)

# 1. 警告框（Alert）
print("\n1. 警告框（Alert）:")

try:
    # 点击触发警告框的按钮
    alert_button = driver.find_element(By.ID, "alertButton")
    alert_button.click()
    print("   ✓ 点击触发警告框")
    
    # 等待警告框出现
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"   ✓ 警告框出现，文本: {alert.text}")
    
    # 接受警告框
    alert.accept()
    print("   ✓ 已接受警告框")
    
except Exception as e:
    print(f"   ✗ 警告框处理失败: {e}")

# 2. 确认框（Confirm）
print("\n2. 确认框（Confirm）:")

try:
    # 点击触发确认框的按钮
    confirm_button = driver.find_element(By.ID, "confirmButton")
    confirm_button.click()
    print("   ✓ 点击触发确认框")
    
    # 等待确认框出现
    confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"   ✓ 确认框出现，文本: {confirm.text}")
    
    # 接受确认框
    confirm.accept()
    print("   ✓ 已接受确认框")
    
    # 验证结果
    result = driver.find_element(By.ID, "confirmResult").text
    print(f"   ✓ 确认结果: {result}")
    
except Exception as e:
    print(f"   ✗ 确认框处理失败: {e}")

# 3. 取消确认框
print("\n3. 取消确认框:")

try:
    # 再次点击触发确认框的按钮
    confirm_button = driver.find_element(By.ID, "confirmButton")
    confirm_button.click()
    print("   ✓ 点击触发确认框")
    
    # 等待确认框出现
    confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
    
    # 取消确认框
    confirm.dismiss()
    print("   ✓ 已取消确认框")
    
    # 验证结果
    result = driver.find_element(By.ID, "confirmResult").text
    print(f"   ✓ 确认结果: {result}")
    
except Exception as e:
    print(f"   ✗ 取消确认框失败: {e}")

# 4. 提示框（Prompt）
print("\n4. 提示框（Prompt）:")

try:
    # 点击触发提示框的按钮
    prompt_button = driver.find_element(By.ID, "promtButton")
    prompt_button.click()
    print("   ✓ 点击触发提示框")
    
    # 等待提示框出现
    prompt = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print(f"   ✓ 提示框出现，文本: {prompt.text}")
    
    # 输入文本并接受
    input_text = "Selenium测试"
    prompt.send_keys(input_text)
    prompt.accept()
    print(f"   ✓ 已输入文本并接受: {input_text}")
    
    # 验证结果
    result = driver.find_element(By.ID, "promptResult").text
    print(f"   ✓ 提示结果: {result}")
    
except Exception as e:
    print(f"   ✗ 提示框处理失败: {e}")

# 5. 等待弹窗出现
print("\n5. 等待弹窗出现:")

try:
    # 点击5秒后出现的警告框
    timer_alert_button = driver.find_element(By.ID, "timerAlertButton")
    timer_alert_button.click()
    print("   ✓ 点击触发定时警告框")
    
    # 等待警告框出现（最多等待10秒）
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print(f"   ✓ 定时警告框出现，文本: {alert.text}")
    
    # 接受警告框
    alert.accept()
    print("   ✓ 已接受定时警告框")
    
except Exception as e:
    print(f"   ✗ 定时警告框处理失败: {e}")

# 6. 弹窗处理最佳实践
print("\n6. 弹窗处理最佳实践:")
print("   - 使用显式等待等待弹窗出现")
print("   - 处理弹窗前先验证其存在")
print("   - 记录弹窗的文本内容")
print("   - 根据业务逻辑选择接受或取消")
print("   - 处理完弹窗后验证操作结果")

# 7. 常见弹窗类型
print("\n7. 常见弹窗类型:")
print("   - Alert: 只有确定按钮的警告框")
print("   - Confirm: 有确定和取消按钮的确认框")
print("   - Prompt: 可以输入文本的提示框")
print("   - 自定义弹窗: 网页自定义的模态框")

# 8. 处理自定义弹窗
print("\n8. 处理自定义弹窗:")

try:
    # 导航到模态框测试页面
    driver.get("https://demoqa.com/modal-dialogs")
    print("   ✓ 打开模态框测试页面")
    time.sleep(2)
    
    # 点击打开小模态框
    small_modal_button = driver.find_element(By.ID, "showSmallModal")
    small_modal_button.click()
    print("   ✓ 打开小模态框")
    time.sleep(1)
    
    # 获取模态框内容
    modal_content = driver.find_element(By.CLASS_NAME, "modal-body").text
    print(f"   ✓ 模态框内容: {modal_content}")
    
    # 关闭模态框
    close_button = driver.find_element(By.ID, "closeSmallModal")
    close_button.click()
    print("   ✓ 关闭小模态框")
    
except Exception as e:
    print(f"   ✗ 自定义弹窗处理失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. 警告框处理:")
print("   - alert = driver.switch_to.alert")
print("   - alert.accept() 接受警告")
print("   - alert.text 获取警告文本")
print("2. 确认框处理:")
print("   - confirm.accept() 确认")
print("   - confirm.dismiss() 取消")
print("3. 提示框处理:")
print("   - prompt.send_keys() 输入文本")
print("   - prompt.accept() 确认")
print("4. 等待弹窗:")
print("   - EC.alert_is_present() 等待弹窗出现")
print("5. 自定义弹窗:")
print("   - 使用常规元素定位方法")
print("   - 不需要switch_to.alert")