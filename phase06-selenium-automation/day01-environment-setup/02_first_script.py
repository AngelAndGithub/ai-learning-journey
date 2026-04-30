# Day 01: 第一个Selenium脚本
# 测试基本的Selenium功能

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print("开始执行第一个Selenium脚本...")

# 使用webdriver-manager自动管理ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

print("浏览器已启动")

# 打开测试网站
driver.get("https://www.baidu.com")
print("已打开百度首页")

# 等待页面加载
time.sleep(2)

# 获取页面标题
title = driver.title
print(f"页面标题: {title}")

# 查找搜索框
search_box = driver.find_element(By.ID, "kw")
print("已找到搜索框")

# 在搜索框中输入内容
search_box.send_keys("Selenium Python")
print("已输入搜索内容")

# 查找搜索按钮
search_button = driver.find_element(By.ID, "su")
print("已找到搜索按钮")

# 点击搜索按钮
search_button.click()
print("已点击搜索按钮")

# 等待搜索结果加载
time.sleep(3)

# 获取搜索结果数量
result_stats = driver.find_element(By.CLASS_NAME, "nums").text
print(f"搜索结果: {result_stats}")

# 截图保存
driver.save_screenshot("search_result.png")
print("已保存搜索结果截图")

# 关闭浏览器
driver.quit()
print("浏览器已关闭")

print("\n第一个Selenium脚本执行完成！")
print("\n学习要点：")
print("1. 如何初始化WebDriver")
print("2. 如何打开网页")
print("3. 如何定位元素")
print("4. 如何操作元素")
print("5. 如何获取页面信息")
print("6. 如何截图")
print("7. 如何关闭浏览器")