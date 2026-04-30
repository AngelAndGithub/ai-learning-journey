# Day 16: JavaScript执行
# JavaScript执行示例

print("Day 16: JavaScript执行")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 执行JavaScript脚本
print("\n1. 执行JavaScript脚本:")

class JavaScriptExecutor:
    """JavaScript执行器类"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def execute_script(self, script, *args):
        """执行JavaScript脚本"""
        return self.driver.execute_script(script, *args)
    
    def scroll_to_element(self, element):
        """滚动到元素位置"""
        script = "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});"
        self.execute_script(script, element)
    
    def scroll_to_top(self):
        """滚动到页面顶部"""
        script = "window.scrollTo({top: 0, behavior: 'smooth'});"
        self.execute_script(script)
    
    def scroll_to_bottom(self):
        """滚动到页面底部"""
        script = "window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});"
        self.execute_script(script)
    
    def get_page_height(self):
        """获取页面高度"""
        script = "return document.body.scrollHeight;"
        return self.execute_script(script)
    
    def get_element_position(self, element):
        """获取元素位置"""
        script = "return arguments[0].getBoundingClientRect();"
        return self.execute_script(script, element)
    
    def set_element_value(self, element, value):
        """设置元素值"""
        script = "arguments[0].value = arguments[1];"
        self.execute_script(script, element, value)
    
    def click_element(self, element):
        """点击元素"""
        script = "arguments[0].click();"
        self.execute_script(script, element)
    
    def get_element_attribute(self, element, attribute):
        """获取元素属性"""
        script = "return arguments[0].getAttribute(arguments[1]);"
        return self.execute_script(script, element, attribute)
    
    def set_element_attribute(self, element, attribute, value):
        """设置元素属性"""
        script = "arguments[0].setAttribute(arguments[1], arguments[2]);"
        self.execute_script(script, element, attribute, value)
    
    def remove_element_attribute(self, element, attribute):
        """移除元素属性"""
        script = "arguments[0].removeAttribute(arguments[1]);"
        self.execute_script(script, element, attribute)
    
    def get_cookie(self, name):
        """获取cookie"""
        script = "return document.cookie;"
        cookies = self.execute_script(script)
        if name:
            for cookie in cookies.split(';'):
                cookie_parts = cookie.strip().split('=')
                if cookie_parts[0] == name:
                    return cookie_parts[1]
        return cookies
    
    def set_cookie(self, name, value):
        """设置cookie"""
        script = "document.cookie = arguments[0] + '=' + arguments[1];"
        self.execute_script(script, name, value)
    
    def get_local_storage(self, key):
        """获取localStorage"""
        script = "return localStorage.getItem(arguments[0]);"
        return self.execute_script(script, key)
    
    def set_local_storage(self, key, value):
        """设置localStorage"""
        script = "localStorage.setItem(arguments[0], arguments[1]);"
        self.execute_script(script, key, value)
    
    def get_session_storage(self, key):
        """获取sessionStorage"""
        script = "return sessionStorage.getItem(arguments[0]);"
        return self.execute_script(script, key)
    
    def set_session_storage(self, key, value):
        """设置sessionStorage"""
        script = "sessionStorage.setItem(arguments[0], arguments[1]);"
        self.execute_script(script, key, value)

# 初始化浏览器和JavaScript执行器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
js_executor = JavaScriptExecutor(driver)

# 2. 基本JavaScript操作
print("\n2. 基本JavaScript操作:")

# 打开测试页面
driver.get("https://www.baidu.com")
print("   - 打开百度首页")

# 获取页面标题
page_title = js_executor.execute_script("return document.title;")
print(f"   - 页面标题: {page_title}")

# 获取URL
current_url = js_executor.execute_script("return window.location.href;")
print(f"   - 当前URL: {current_url}")

# 获取页面高度
page_height = js_executor.get_page_height()
print(f"   - 页面高度: {page_height}px")

# 3. 滚动操作
print("\n3. 滚动操作:")

# 打开一个长页面
driver.get("https://www.selenium.dev/documentation/")
print("   - 打开Selenium文档页面")
time.sleep(2)

# 滚动到页面底部
js_executor.scroll_to_bottom()
print("   - 滚动到页面底部")
time.sleep(2)

# 滚动到页面顶部
js_executor.scroll_to_top()
print("   - 滚动到页面顶部")
time.sleep(2)

# 4. 元素操作
print("\n4. 元素操作:")

# 打开百度首页
driver.get("https://www.baidu.com")
print("   - 打开百度首页")

# 查找搜索框
search_box = driver.find_element(By.ID, "kw")

# 使用JavaScript设置值
js_executor.set_element_value(search_box, "Selenium JavaScript")
print("   - 使用JavaScript设置搜索框值")
time.sleep(1)

# 使用JavaScript点击搜索按钮
search_button = driver.find_element(By.ID, "su")
js_executor.click_element(search_button)
print("   - 使用JavaScript点击搜索按钮")
time.sleep(2)

# 5. 处理复杂交互
print("\n5. 处理复杂交互:")

# 打开一个包含复杂交互的页面
driver.get("https://demoqa.com/slider")
print("   - 打开滑块测试页面")
time.sleep(2)

# 操作滑块
slider = driver.find_element(By.CLASS_NAME, "range-slider")
js_executor.execute_script("arguments[0].value = 75;", slider)
print("   - 使用JavaScript设置滑块值为75")
time.sleep(1)

# 获取滑块值
slider_value = driver.find_element(By.ID, "sliderValue").get_attribute("value")
print(f"   - 滑块当前值: {slider_value}")

# 6. 处理隐藏元素
print("\n6. 处理隐藏元素:")

# 打开测试页面
driver.get("https://demoqa.com/dynamic-properties")
print("   - 打开动态属性测试页面")
time.sleep(2)

# 查找隐藏按钮
hidden_button = driver.find_element(By.ID, "visibleAfter")

# 检查元素是否可见
is_visible = js_executor.execute_script("return arguments[0].offsetParent !== null;", hidden_button)
print(f"   - 按钮初始可见状态: {is_visible}")

# 等待按钮出现
time.sleep(5)

# 再次检查元素是否可见
is_visible = js_executor.execute_script("return arguments[0].offsetParent !== null;", hidden_button)
print(f"   - 按钮5秒后可见状态: {is_visible}")

# 7. 操作浏览器对象
print("\n7. 操作浏览器对象:")

# 获取浏览器窗口大小
window_size = js_executor.execute_script("return {width: window.innerWidth, height: window.innerHeight};")
print(f"   - 浏览器窗口大小: {window_size['width']}x{window_size['height']}")

# 打开新窗口
js_executor.execute_script("window.open('https://www.google.com', '_blank');")
print("   - 使用JavaScript打开新窗口")
time.sleep(2)

# 获取所有窗口句柄
window_handles = driver.window_handles
print(f"   - 窗口数量: {len(window_handles)}")

# 切换回第一个窗口
driver.switch_to.window(window_handles[0])
print("   - 切换回第一个窗口")

# 8. 处理Cookie和Storage
print("\n8. 处理Cookie和Storage:")

# 设置Cookie
js_executor.set_cookie("test_cookie", "test_value")
print("   - 设置测试Cookie")

# 获取Cookie
cookie_value = js_executor.get_cookie("test_cookie")
print(f"   - 获取测试Cookie值: {cookie_value}")

# 设置localStorage
js_executor.set_local_storage("test_key", "test_value")
print("   - 设置localStorage")

# 获取localStorage
local_storage_value = js_executor.get_local_storage("test_key")
print(f"   - 获取localStorage值: {local_storage_value}")

# 9. 高级JavaScript操作
print("\n9. 高级JavaScript操作:")

# 执行复杂的JavaScript脚本
complex_script = """
function getPageInfo() {
    return {
        title: document.title,
        url: window.location.href,
        links: document.querySelectorAll('a').length,
        images: document.querySelectorAll('img').length
    };
}
return getPageInfo();
"""

page_info = js_executor.execute_script(complex_script)
print(f"   - 页面信息:")
print(f"     标题: {page_info['title']}")
print(f"     URL: {page_info['url']}")
print(f"     链接数量: {page_info['links']}")
print(f"     图片数量: {page_info['images']}")

# 10. 实际应用示例
print("\n10. 实际应用示例:")

# 测试表单提交
def test_form_submission():
    """测试表单提交"""
    print("   - 测试表单提交:")
    
    driver.get("https://demoqa.com/text-box")
    print("     打开文本框测试页面")
    
    # 使用JavaScript填写表单
    js_executor.execute_script("document.getElementById('userName').value = 'John Doe';")
    js_executor.execute_script("document.getElementById('userEmail').value = 'john@example.com';")
    js_executor.execute_script("document.getElementById('currentAddress').value = '123 Main St';")
    js_executor.execute_script("document.getElementById('permanentAddress').value = '456 Main St';")
    print("     使用JavaScript填写表单")
    
    # 滚动到提交按钮
    submit_button = driver.find_element(By.ID, "submit")
    js_executor.scroll_to_element(submit_button)
    print("     滚动到提交按钮")
    
    # 点击提交按钮
    js_executor.click_element(submit_button)
    print("     使用JavaScript点击提交按钮")
    
    # 验证提交结果
    time.sleep(1)
    output = driver.find_element(By.ID, "output")
    is_displayed = output.is_displayed()
    print(f"     提交结果显示: {is_displayed}")

# 运行表单提交测试
test_form_submission()

# 11. JavaScript执行的最佳实践
print("\n11. JavaScript执行的最佳实践:")
print("   - 尽量使用Selenium内置方法，只在必要时使用JavaScript")
print("   - 执行JavaScript时要注意异常处理")
print("   - 复杂的JavaScript脚本应该封装成函数")
print("   - 执行JavaScript后要验证结果")
print("   - 避免频繁执行JavaScript，以提高性能")
print("   - 对于跨浏览器兼容性问题，要测试不同浏览器")

# 12. 常见应用场景
print("\n12. 常见应用场景:")
print("   - 处理隐藏元素")
print("   - 操作滑块、拖拽等复杂交互")
print("   - 滚动页面")
print("   - 修改元素属性")
print("   - 操作Cookie和Storage")
print("   - 执行复杂的页面操作")
print("   - 处理JavaScript生成的内容")

# 关闭浏览器
driver.quit()
print("\n浏览器已关闭")

print("\nJavaScript执行示例完成！")
print("\n学习要点：")
print("1. 基本JavaScript执行:")
print("   - execute_script()方法
   - 传递参数给JavaScript
   - 获取JavaScript执行结果
2. 页面操作:")
print("   - 滚动操作
   - 获取页面信息
   - 操作浏览器窗口
3. 元素操作:")
print("   - 设置元素值
   - 点击元素
   - 修改元素属性
   - 处理隐藏元素
4. 数据操作:")
print("   - Cookie操作
   - localStorage操作
   - sessionStorage操作
5. 高级应用:")
print("   - 执行复杂JavaScript脚本
   - 处理复杂交互
   - 跨浏览器兼容性")