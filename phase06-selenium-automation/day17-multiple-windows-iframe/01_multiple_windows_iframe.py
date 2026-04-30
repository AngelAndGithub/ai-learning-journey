# Day 17: 多窗口和iframe
# 多窗口和iframe处理示例

print("Day 17: 多窗口和iframe")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 多窗口操作
print("\n1. 多窗口操作:")

class WindowManager:
    """窗口管理器类"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def get_current_window_handle(self):
        """获取当前窗口句柄"""
        return self.driver.current_window_handle
    
    def get_all_window_handles(self):
        """获取所有窗口句柄"""
        return self.driver.window_handles
    
    def switch_to_window(self, window_handle):
        """切换到指定窗口"""
        self.driver.switch_to.window(window_handle)
    
    def switch_to_window_by_index(self, index):
        """通过索引切换窗口"""
        windows = self.get_all_window_handles()
        if index < len(windows):
            self.switch_to_window(windows[index])
            return True
        return False
    
    def switch_to_window_by_title(self, title):
        """通过标题切换窗口"""
        windows = self.get_all_window_handles()
        for window in windows:
            self.switch_to_window(window)
            if title in self.driver.title:
                return True
        return False
    
    def open_new_window(self, url):
        """打开新窗口"""
        self.driver.execute_script(f"window.open('{url}', '_blank');")
    
    def close_current_window(self):
        """关闭当前窗口"""
        self.driver.close()
    
    def get_window_title(self):
        """获取当前窗口标题"""
        return self.driver.title
    
    def get_window_count(self):
        """获取窗口数量"""
        return len(self.get_all_window_handles())

# 初始化浏览器和窗口管理器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
window_manager = WindowManager(driver)

# 2. 多窗口操作示例
print("\n2. 多窗口操作示例:")

# 打开第一个窗口
driver.get("https://www.baidu.com")
print(f"   - 第一个窗口标题: {window_manager.get_window_title()}")
print(f"   - 初始窗口数量: {window_manager.get_window_count()}")

# 打开第二个窗口
window_manager.open_new_window("https://www.google.com")
time.sleep(2)
print(f"   - 打开第二个窗口后，窗口数量: {window_manager.get_window_count()}")

# 切换到第二个窗口
window_manager.switch_to_window_by_index(1)
print(f"   - 切换到第二个窗口，标题: {window_manager.get_window_title()}")

# 打开第三个窗口
window_manager.open_new_window("https://www.sogou.com")
time.sleep(2)
print(f"   - 打开第三个窗口后，窗口数量: {window_manager.get_window_count()}")

# 通过标题切换窗口
window_manager.switch_to_window_by_title("百度")
print(f"   - 通过标题切换到百度窗口，标题: {window_manager.get_window_title()}")

# 关闭当前窗口
window_manager.close_current_window()
print(f"   - 关闭当前窗口后，窗口数量: {window_manager.get_window_count()}")

# 切换到第一个窗口
window_manager.switch_to_window_by_index(0)
print(f"   - 切换到第一个窗口，标题: {window_manager.get_window_title()}")

# 3. iframe操作
print("\n3. iframe操作:")

class IframeManager:
    """iframe管理器类"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def switch_to_iframe(self, locator):
        """切换到iframe"""
        iframe = WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )
        return iframe
    
    def switch_to_iframe_by_index(self, index):
        """通过索引切换到iframe"""
        self.driver.switch_to.frame(index)
    
    def switch_to_iframe_by_name(self, name):
        """通过名称切换到iframe"""
        self.driver.switch_to.frame(name)
    
    def switch_to_iframe_by_element(self, element):
        """通过元素切换到iframe"""
        self.driver.switch_to.frame(element)
    
    def switch_to_default_content(self):
        """切换到默认内容"""
        self.driver.switch_to.default_content()
    
    def switch_to_parent_frame(self):
        """切换到父级iframe"""
        self.driver.switch_to.parent_frame()
    
    def get_iframe_count(self):
        """获取iframe数量"""
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        return len(iframes)
    
    def get_iframe_by_locator(self, locator):
        """通过定位器获取iframe元素"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

# 初始化iframe管理器
iframe_manager = IframeManager(driver)

# 4. iframe操作示例
print("\n4. iframe操作示例:")

# 打开包含iframe的页面
driver.get("https://demoqa.com/frames")
print("   - 打开frames测试页面")

# 获取iframe数量
iframe_count = iframe_manager.get_iframe_count()
print(f"   - 页面中的iframe数量: {iframe_count}")

# 切换到第一个iframe
print("   - 切换到第一个iframe")
iframe_manager.switch_to_iframe((By.ID, "frame1"))

# 在iframe中操作
iframe_text = driver.find_element(By.ID, "sampleHeading").text
print(f"   - iframe中的文本: {iframe_text}")

# 切换回默认内容
iframe_manager.switch_to_default_content()
print("   - 切换回默认内容")

# 打开嵌套iframe页面
driver.get("https://demoqa.com/nestedframes")
print("   - 打开嵌套frames测试页面")

# 切换到父iframe
print("   - 切换到父iframe")
iframe_manager.switch_to_iframe((By.ID, "frame1"))

# 获取父iframe中的文本
parent_text = driver.find_element(By.TAG_NAME, "body").text
print(f"   - 父iframe中的文本: {parent_text}")

# 切换到子iframe
print("   - 切换到子iframe")
iframe_manager.switch_to_iframe_by_index(0)

# 获取子iframe中的文本
child_text = driver.find_element(By.TAG_NAME, "p").text
print(f"   - 子iframe中的文本: {child_text}")

# 切换回父iframe
iframe_manager.switch_to_parent_frame()
print("   - 切换回父iframe")

# 切换回默认内容
iframe_manager.switch_to_default_content()
print("   - 切换回默认内容")

# 5. 多标签页管理
print("\n5. 多标签页管理:")

# 打开多个标签页
print("   - 打开多个标签页")
driver.get("https://www.baidu.com")
driver.execute_script("window.open('https://www.google.com', '_blank');")
driver.execute_script("window.open('https://www.sogou.com', '_blank');")
driver.execute_script("window.open('https://www.bing.com', '_blank');")
time.sleep(2)

# 获取所有标签页
windows = window_manager.get_all_window_handles()
print(f"   - 标签页数量: {len(windows)}")

# 遍历所有标签页
for i, window in enumerate(windows):
    window_manager.switch_to_window(window)
    print(f"   - 标签页 {i+1}: {window_manager.get_window_title()}")

# 关闭除第一个标签页外的所有标签页
print("   - 关闭除第一个标签页外的所有标签页")
for i, window in enumerate(windows):
    if i > 0:
        window_manager.switch_to_window(window)
        window_manager.close_current_window()

# 切换回第一个标签页
window_manager.switch_to_window(windows[0])
print(f"   - 最终标签页: {window_manager.get_window_title()}")
print(f"   - 最终标签页数量: {window_manager.get_window_count()}")

# 6. 实际应用示例
print("\n6. 实际应用示例:")

# 测试多窗口登录
def test_multi_window_login():
    """测试多窗口登录"""
    print("   - 测试多窗口登录:")
    
    # 打开登录页面
    driver.get("https://www.saucedemo.com/")
    print("     打开登录页面")
    
    # 打开新窗口
    window_manager.open_new_window("https://www.saucedemo.com/")
    time.sleep(1)
    
    # 获取所有窗口
    windows = window_manager.get_all_window_handles()
    print(f"     窗口数量: {len(windows)}")
    
    # 在第一个窗口登录
    window_manager.switch_to_window(windows[0])
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("     在第一个窗口登录")
    
    # 验证登录成功
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("     第一个窗口登录成功")
    
    # 在第二个窗口登录
    window_manager.switch_to_window(windows[1])
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("     在第二个窗口登录")
    
    # 验证登录失败
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    print(f"     第二个窗口登录失败: {error_message.text}")
    
    # 关闭第二个窗口
    window_manager.close_current_window()
    print("     关闭第二个窗口")
    
    # 切换回第一个窗口
    window_manager.switch_to_window(windows[0])
    print(f"     切换回第一个窗口: {window_manager.get_window_title()}")

# 运行多窗口登录测试
test_multi_window_login()

# 7. 多窗口和iframe的最佳实践
print("\n7. 多窗口和iframe的最佳实践:")
print("   - 始终记录当前窗口句柄，以便在操作后切换回来")
print("   - 使用显式等待确保窗口或iframe加载完成")
print("   - 操作完成后及时切换回默认内容或原始窗口")
print("   - 对于嵌套iframe，要注意切换层级")
print("   - 避免在多个窗口之间频繁切换，以提高测试性能")
print("   - 测试完成后要清理所有打开的窗口")

# 8. 常见问题及解决方案
print("\n8. 常见问题及解决方案:")
print("   - 窗口句柄获取失败: 使用显式等待确保窗口完全打开")
print("   - iframe切换失败: 确保iframe已加载，使用显式等待")
print("   - 切换回默认内容失败: 多次调用switch_to.default_content()")
print("   - 多窗口操作混乱: 维护窗口句柄的映射关系")

# 9. 高级技巧
print("\n9. 高级技巧:")

# 窗口句柄管理
def manage_window_handles():
    """管理窗口句柄"""
    print("   - 窗口句柄管理技巧:")
    
    # 保存初始窗口
    original_window = window_manager.get_current_window_handle()
    print(f"     初始窗口: {original_window}")
    
    # 打开新窗口
    window_manager.open_new_window("https://www.google.com")
    time.sleep(1)
    
    # 获取所有窗口
    all_windows = window_manager.get_all_window_handles()
    print(f"     所有窗口: {all_windows}")
    
    # 找到新窗口
    new_window = [window for window in all_windows if window != original_window][0]
    print(f"     新窗口: {new_window}")
    
    # 切换到新窗口
    window_manager.switch_to_window(new_window)
    print(f"     切换到新窗口: {window_manager.get_window_title()}")
    
    # 关闭新窗口
    window_manager.close_current_window()
    
    # 切换回原始窗口
    window_manager.switch_to_window(original_window)
    print(f"     切换回原始窗口: {window_manager.get_window_title()}")

# 运行窗口句柄管理示例
manage_window_handles()

# 10. iframe操作高级技巧
print("\n10. iframe操作高级技巧:")

def iframe_advanced():
    """iframe操作高级技巧"""
    print("   - iframe操作高级技巧:")
    
    # 打开包含iframe的页面
    driver.get("https://www.w3schools.com/html/html_iframe.asp")
    print("     打开包含iframe的页面")
    
    # 获取所有iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"     页面中的iframe数量: {len(iframes)}")
    
    # 遍历iframe
    for i, iframe in enumerate(iframes):
        try:
            # 切换到iframe
            iframe_manager.switch_to_iframe_by_element(iframe)
            print(f"     切换到iframe {i+1}")
            
            # 获取iframe中的内容
            try:
                body_text = driver.find_element(By.TAG_NAME, "body").text
                print(f"     iframe {i+1} 内容长度: {len(body_text)}")
            except:
                print(f"     iframe {i+1} 无法获取内容")
            
            # 切换回默认内容
            iframe_manager.switch_to_default_content()
        except Exception as e:
            print(f"     切换iframe {i+1} 失败: {e}")

# 运行iframe高级操作示例
iframe_advanced()

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")

print("\n多窗口和iframe操作示例完成！")
print("\n学习要点：")
print("1. 多窗口操作:")
print("   - 获取窗口句柄
   - 切换窗口
   - 打开新窗口
   - 关闭窗口
   - 窗口管理
2. iframe操作:")
print("   - 切换到iframe
   - 在iframe中操作
   - 切换回默认内容
   - 处理嵌套iframe
3. 多标签页管理:")
print("   - 打开多个标签页
   - 切换标签页
   - 关闭标签页
4. 最佳实践:")
print("   - 记录窗口句柄
   - 使用显式等待
   - 及时切换回原始上下文
   - 清理打开的窗口
5. 常见问题:")
print("   - 窗口句柄获取失败
   - iframe切换失败
   - 嵌套iframe处理
   - 窗口管理混乱")