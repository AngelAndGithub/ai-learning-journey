# Day 04: 浏览器操作
# 浏览器操作示例

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

print("Day 04: 浏览器操作")

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. 窗口管理
print("\n1. 窗口管理:")

# 设置窗口大小
print("   - 设置窗口大小:")
driver.set_window_size(1366, 768)
print("   ✓ 设置窗口大小为1366x768")
time.sleep(1)

# 最大化窗口
print("   - 最大化窗口:")
driver.maximize_window()
print("   ✓ 窗口最大化")
time.sleep(1)

# 最小化窗口
print("   - 最小化窗口:")
driver.minimize_window()
print("   ✓ 窗口最小化")
time.sleep(1)

# 恢复窗口
print("   - 恢复窗口:")
driver.set_window_position(0, 0)
driver.set_window_size(1366, 768)
print("   ✓ 窗口恢复")
time.sleep(1)

# 2. 页面导航
print("\n2. 页面导航:")

# 打开第一个页面
driver.get("https://www.baidu.com")
print("   ✓ 打开百度首页")
time.sleep(2)

# 打开第二个页面
driver.get("https://www.google.com")
print("   ✓ 打开谷歌首页")
time.sleep(2)

# 后退
print("   - 后退操作:")
driver.back()
print("   ✓ 后退到百度首页")
time.sleep(2)

# 前进
print("   - 前进操作:")
driver.forward()
print("   ✓ 前进到谷歌首页")
time.sleep(2)

# 刷新
print("   - 刷新操作:")
driver.refresh()
print("   ✓ 刷新页面")
time.sleep(2)

# 获取当前URL
current_url = driver.current_url
print(f"   ✓ 当前URL: {current_url}")

# 获取页面标题
page_title = driver.title
print(f"   ✓ 页面标题: {page_title}")

# 3. 多窗口操作
print("\n3. 多窗口操作:")

# 打开新窗口
driver.execute_script("window.open('https://www.github.com');")
print("   ✓ 打开新窗口")
time.sleep(2)

# 获取所有窗口句柄
window_handles = driver.window_handles
print(f"   ✓ 窗口数量: {len(window_handles)}")

# 切换到第一个窗口
driver.switch_to.window(window_handles[0])
print("   ✓ 切换到第一个窗口")
print(f"   ✓ 当前窗口标题: {driver.title}")
time.sleep(1)

# 切换到第二个窗口
driver.switch_to.window(window_handles[1])
print("   ✓ 切换到第二个窗口")
print(f"   ✓ 当前窗口标题: {driver.title}")
time.sleep(1)

# 关闭当前窗口
driver.close()
print("   ✓ 关闭当前窗口")
time.sleep(1)

# 切换回第一个窗口
driver.switch_to.window(window_handles[0])
print("   ✓ 切换回第一个窗口")

# 4. 截图功能
print("\n4. 截图功能:")

# 创建截图目录
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# 全屏截图
print("   - 全屏截图:")
screenshot_path = "screenshots/full_page.png"
driver.save_screenshot(screenshot_path)
print(f"   ✓ 全屏截图保存到: {screenshot_path}")

# 元素截图
print("   - 元素截图:")
try:
    search_box = driver.find_element(By.NAME, "q")
    element_screenshot_path = "screenshots/search_box.png"
    search_box.screenshot(element_screenshot_path)
    print(f"   ✓ 元素截图保存到: {element_screenshot_path}")
except Exception as e:
    print(f"   ✗ 元素截图失败: {e}")

# 5. 浏览器信息
print("\n5. 浏览器信息:")

# 获取浏览器名称
browser_name = driver.name
print(f"   ✓ 浏览器名称: {browser_name}")

# 获取页面源码
page_source = driver.page_source
print(f"   ✓ 页面源码长度: {len(page_source)} 字符")

# 6. 执行JavaScript
print("\n6. 执行JavaScript:")

try:
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("   ✓ 滚动到页面底部")
    time.sleep(2)
    
    # 滚动到页面顶部
    driver.execute_script("window.scrollTo(0, 0);")
    print("   ✓ 滚动到页面顶部")
    time.sleep(2)
    
    # 执行自定义JavaScript
    result = driver.execute_script("return document.title;")
    print(f"   ✓ JavaScript执行结果: {result}")
    
except Exception as e:
    print(f"   ✗ JavaScript执行失败: {e}")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")
print("\n学习要点：")
print("1. 窗口管理:")
print("   - set_window_size() 设置窗口大小")
print("   - maximize_window() 最大化窗口")
print("   - minimize_window() 最小化窗口")
print("2. 页面导航:")
print("   - get() 打开页面")
print("   - back() 后退")
print("   - forward() 前进")
print("   - refresh() 刷新")
print("3. 多窗口操作:")
print("   - window_handles 获取窗口句柄")
print("   - switch_to.window() 切换窗口")
print("   - close() 关闭当前窗口")
print("4. 截图功能:")
print("   - save_screenshot() 全屏截图")
print("   - screenshot() 元素截图")
print("5. 执行JavaScript:")
print("   - execute_script() 执行JS脚本")