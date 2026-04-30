# Day 15: 浏览器高级操作
# 浏览器高级操作示例

print("Day 15: 浏览器高级操作")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# 1. 浏览器配置
print("\n1. 浏览器配置:")

class BrowserConfig:
    """浏览器配置类"""
    
    @staticmethod
    def get_chrome_options():
        """获取Chrome选项"""
        options = Options()
        
        # 基本配置
        options.add_argument("--start-maximized")  # 最大化窗口
        options.add_argument("--no-sandbox")  # 禁用沙箱
        options.add_argument("--disable-dev-shm-usage")  # 禁用/dev/shm使用
        options.add_argument("--disable-extensions")  # 禁用扩展
        options.add_argument("--disable-gpu")  # 禁用GPU加速
        options.add_argument("--ignore-certificate-errors")  # 忽略证书错误
        
        return options
    
    @staticmethod
    def get_chrome_options_with_proxy(proxy):
        """获取带代理的Chrome选项"""
        options = Options()
        options.add_argument(f"--proxy-server={proxy}")
        return options
    
    @staticmethod
    def get_firefox_options():
        """获取Firefox选项"""
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        return options

# 测试浏览器配置
print("   - 测试浏览器配置:")
options = BrowserConfig.get_chrome_options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ 浏览器配置成功，页面标题: {driver.title}")
except Exception as e:
    print(f"   ✗ 浏览器配置失败: {e}")
finally:
    driver.quit()

# 2. 无头模式
print("\n2. 无头模式:")

class HeadlessBrowser:
    """无头浏览器类"""
    
    @staticmethod
    def get_headless_chrome():
        """获取无头Chrome浏览器"""
        options = Options()
        options.add_argument("--headless")  # 无头模式
        options.add_argument("--window-size=1920,1080")  # 设置窗口大小
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    
    @staticmethod
    def get_headless_firefox():
        """获取无头Firefox浏览器"""
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return driver

# 测试无头模式
print("   - 测试无头模式:")
driver = HeadlessBrowser.get_headless_chrome()

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ 无头模式成功，页面标题: {driver.title}")
    
    # 截图验证
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot("screenshots/headless_baidu.png")
    print("   ✓ 无头模式截图成功")
except Exception as e:
    print(f"   ✗ 无头模式失败: {e}")
finally:
    driver.quit()

# 3. 移动设备模拟
print("\n3. 移动设备模拟:")

class MobileEmulation:
    """移动设备模拟类"""
    
    @staticmethod
    def get_mobile_chrome(device_name):
        """获取模拟移动设备的Chrome浏览器"""
        mobile_emulation = {
            "deviceName": device_name
        }
        
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    
    @staticmethod
    def get_custom_mobile_chrome(width, height, pixel_ratio):
        """获取自定义移动设备的Chrome浏览器"""
        mobile_emulation = {
            "deviceMetrics": {
                "width": width,
                "height": height,
                "pixelRatio": pixel_ratio
            },
            "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"
        }
        
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

# 测试移动设备模拟
print("   - 测试移动设备模拟:")

# 模拟iPhone X
driver = MobileEmulation.get_mobile_chrome("iPhone X")

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ iPhone X模拟成功，页面标题: {driver.title}")
    print(f"   ✓ 窗口大小: {driver.get_window_size()}")
    
    # 截图验证
    driver.save_screenshot("screenshots/iphone_x_baidu.png")
    print("   ✓ iPhone X模拟截图成功")
except Exception as e:
    print(f"   ✗ iPhone X模拟失败: {e}")
finally:
    driver.quit()

# 模拟iPad
driver = MobileEmulation.get_mobile_chrome("iPad")

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ iPad模拟成功，页面标题: {driver.title}")
    print(f"   ✓ 窗口大小: {driver.get_window_size()}")
    
    # 截图验证
    driver.save_screenshot("screenshots/ipad_baidu.png")
    print("   ✓ iPad模拟截图成功")
except Exception as e:
    print(f"   ✗ iPad模拟失败: {e}")
finally:
    driver.quit()

# 4. 浏览器配置文件
print("\n4. 浏览器配置文件:")

class BrowserProfile:
    """浏览器配置文件类"""
    
    @staticmethod
    def get_chrome_with_profile(profile_path):
        """使用指定配置文件的Chrome"""
        options = Options()
        options.add_argument(f"--user-data-dir={profile_path}")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    
    @staticmethod
    def get_incognito_chrome():
        """获取无痕模式的Chrome"""
        options = Options()
        options.add_argument("--incognito")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

# 测试无痕模式
print("   - 测试无痕模式:")
driver = BrowserProfile.get_incognito_chrome()

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ 无痕模式成功，页面标题: {driver.title}")
except Exception as e:
    print(f"   ✗ 无痕模式失败: {e}")
finally:
    driver.quit()

# 5. 高级浏览器操作
print("\n5. 高级浏览器操作:")

class AdvancedBrowserOps:
    """高级浏览器操作类"""
    
    @staticmethod
    def set_download_directory(driver, download_dir):
        """设置下载目录"""
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("prefs", prefs)
        
        # 注意：此方法需要在创建driver时设置
        return options
    
    @staticmethod
    def set_page_load_strategy(driver, strategy):
        """设置页面加载策略"""
        # 策略选项: normal, eager, none
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = strategy
        
        return options
    
    @staticmethod
    def enable_performance_logging(driver):
        """启用性能日志"""
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        caps = DesiredCapabilities.CHROME
        caps["goog:loggingPrefs"] = {
            "performance": "ALL"
        }
        
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.merge(caps)
        
        return options

# 测试页面加载策略
print("   - 测试页面加载策略:")
options = AdvancedBrowserOps.set_page_load_strategy(None, "eager")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.baidu.com")
    print(f"   ✓ 页面加载策略设置成功，页面标题: {driver.title}")
except Exception as e:
    print(f"   ✗ 页面加载策略设置失败: {e}")
finally:
    driver.quit()

# 6. 浏览器扩展
print("\n6. 浏览器扩展:")

class BrowserExtensions:
    """浏览器扩展类"""
    
    @staticmethod
    def add_extension(driver, extension_path):
        """添加扩展"""
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_extension(extension_path)
        
        return options

# 7. 多浏览器支持
print("\n7. 多浏览器支持:")

class MultiBrowser:
    """多浏览器支持类"""
    
    @staticmethod
    def get_driver(browser_name):
        """获取指定浏览器的driver"""
        if browser_name.lower() == "chrome":
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_name.lower() == "firefox":
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser_name.lower() == "edge":
            from selenium.webdriver.edge.service import Service as EdgeService
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise Exception(f"不支持的浏览器: {browser_name}")

# 测试多浏览器
print("   - 测试多浏览器:")
browsers = ["chrome"]  # 可以添加 "firefox", "edge"

for browser in browsers:
    try:
        driver = MultiBrowser.get_driver(browser)
        driver.get("https://www.baidu.com")
        print(f"   ✓ {browser} 浏览器成功，页面标题: {driver.title}")
        driver.quit()
    except Exception as e:
        print(f"   ✗ {browser} 浏览器失败: {e}")

# 8. 浏览器高级操作最佳实践
print("\n8. 浏览器高级操作最佳实践:")
print("   - 根据测试需求选择合适的浏览器配置")
print("   - 在CI/CD环境中使用无头模式")
print("   - 移动设备测试时使用设备模拟")
print("   - 合理设置页面加载策略以提高测试速度")
print("   - 启用性能日志进行性能分析")
print("   - 使用多浏览器测试确保兼容性")

# 9. 实际应用示例
print("\n9. 实际应用示例:")

# 跨浏览器测试
def cross_browser_test(url):
    """跨浏览器测试"""
    browsers = ["chrome"]  # 可以添加其他浏览器
    results = {}
    
    for browser in browsers:
        try:
            driver = MultiBrowser.get_driver(browser)
            driver.get(url)
            results[browser] = {
                "success": True,
                "title": driver.title,
                "error": None
            }
            driver.quit()
        except Exception as e:
            results[browser] = {
                "success": False,
                "title": None,
                "error": str(e)
            }
    
    return results

# 运行跨浏览器测试
print("   - 运行跨浏览器测试:")
test_results = cross_browser_test("https://www.baidu.com")
for browser, result in test_results.items():
    if result["success"]:
        print(f"   ✓ {browser}: {result['title']}")
    else:
        print(f"   ✗ {browser}: {result['error']}")

# 10. 性能优化
print("\n10. 性能优化:")
print("   - 使用无头模式提高执行速度")
print("   - 合理设置页面加载策略")
print("   - 禁用不必要的浏览器功能")
print("   - 使用并行测试执行")
print("   - 优化WebDriver初始化时间")

print("\n浏览器高级操作示例完成！")
print("\n学习要点：")
print("1. 浏览器配置:")
print("   - 基本配置选项
   - 代理设置
   - 安全选项
2. 无头模式:")
print("   - 适用于CI/CD环境
   - 提高执行速度
   - 节省系统资源
3. 移动设备模拟:")
print("   - 内置设备模拟
   - 自定义设备配置
   - 测试移动端网站
4. 高级浏览器操作:")
print("   - 下载目录设置
   - 页面加载策略
   - 性能日志
5. 多浏览器支持:")
print("   - Chrome、Firefox、Edge
   - 跨浏览器测试
   - 浏览器兼容性验证")