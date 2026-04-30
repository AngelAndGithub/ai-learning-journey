# Day 03: 元素操作
# 复杂元素操作示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

print("Day 03: 元素操作 - 复杂操作")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. 下拉框操作
print("\n1. 下拉框操作:")
try:
    driver.get("https://demoqa.com/select-menu")
    print("已打开下拉框测试页面")
    time.sleep(2)
    
    # 普通下拉框
    print("   - 普通下拉框:")
    old_select = driver.find_element(By.ID, "oldSelectMenu")
    select = Select(old_select)
    
    # 通过索引选择
    select.select_by_index(1)
    print("   ✓ 通过索引选择成功")
    time.sleep(1)
    
    # 通过值选择
    select.select_by_value("4")
    print("   ✓ 通过值选择成功")
    time.sleep(1)
    
    # 通过可见文本选择
    select.select_by_visible_text("Magenta")
    print("   ✓ 通过可见文本选择成功")
    
    # 获取所有选项
    options = select.options
    print(f"   ✓ 下拉框选项数量: {len(options)}")
    
    # 获取当前选中项
    selected_option = select.first_selected_option
    print(f"   ✓ 当前选中项: {selected_option.text}")
    
except Exception as e:
    print(f"   ✗ 下拉框操作失败: {e}")

# 2. 复选框操作
print("\n2. 复选框操作:")
try:
    driver.get("https://demoqa.com/checkbox")
    print("已打开复选框测试页面")
    time.sleep(2)
    
    # 点击主复选框
    main_checkbox = driver.find_element(By.CLASS_NAME, "rct-icon-check")
    main_checkbox.click()
    print("   ✓ 点击主复选框成功")
    time.sleep(2)
    
    # 再次点击取消选择
    main_checkbox.click()
    print("   ✓ 取消选择成功")
    
    # 点击具体选项
    home_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
    home_checkbox.click()
    print("   ✓ 点击Home选项成功")
    
except Exception as e:
    print(f"   ✗ 复选框操作失败: {e}")

# 3. 单选按钮操作
print("\n3. 单选按钮操作:")
try:
    driver.get("https://demoqa.com/radio-button")
    print("已打开单选按钮测试页面")
    time.sleep(2)
    
    # 选择Yes选项
    yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio.click()
    print("   ✓ 选择Yes选项成功")
    time.sleep(1)
    
    # 选择Impressive选项
    impressive_radio = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio.click()
    print("   ✓ 选择Impressive选项成功")
    
    # 验证选中状态
    yes_selected = driver.find_element(By.ID, "yesRadio").is_selected()
    impressive_selected = driver.find_element(By.ID, "impressiveRadio").is_selected()
    no_enabled = driver.find_element(By.ID, "noRadio").is_enabled()
    
    print(f"   ✓ Yes选中状态: {yes_selected}")
    print(f"   ✓ Impressive选中状态: {impressive_selected}")
    print(f"   ✓ No启用状态: {no_enabled}")
    
except Exception as e:
    print(f"   ✗ 单选按钮操作失败: {e}")

# 4. 滑块操作
print("\n4. 滑块操作:")
try:
    driver.get("https://demoqa.com/slider")
    print("已打开滑块测试页面")
    time.sleep(2)
    
    slider = driver.find_element(By.CLASS_NAME, "range-slider")
    
    # 使用JavaScript设置滑块值
    driver.execute_script("arguments[0].value = 75;", slider)
    print("   ✓ 设置滑块值为75成功")
    
    # 获取滑块值
    slider_value = driver.find_element(By.ID, "sliderValue").get_attribute("value")
    print(f"   ✓ 当前滑块值: {slider_value}")
    
except Exception as e:
    print(f"   ✗ 滑块操作失败: {e}")

# 5. 日期选择器操作
print("\n5. 日期选择器操作:")
try:
    driver.get("https://demoqa.com/date-picker")
    print("已打开日期选择器测试页面")
    time.sleep(2)
    
    # 选择日期
    date_input = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_input.click()
    time.sleep(1)
    
    # 选择月份
    month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month_select.select_by_index(5)  # 6月
    
    # 选择年份
    year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_select.select_by_value("2023")
    
    # 选择日期
    day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]")
    day.click()
    
    print("   ✓ 日期选择成功")
    print(f"   ✓ 选中日期: {date_input.get_attribute('value')}")
    
except Exception as e:
    print(f"   ✗ 日期选择器操作失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. 下拉框操作:")
print("   - Select类的使用")
print("   - select_by_index()、select_by_value()、select_by_visible_text()")
print("   - options属性获取所有选项")
print("2. 复选框操作:")
print("   - click()方法切换状态")
print("   - is_selected()方法检查状态")
print("3. 单选按钮操作:")
print("   - click()方法选择")
print("   - is_selected()方法检查状态")
print("4. 滑块操作:")
print("   - 使用JavaScript设置值")
print("5. 日期选择器操作:")
print("   - 分步选择：月份 -> 年份 -> 日期")