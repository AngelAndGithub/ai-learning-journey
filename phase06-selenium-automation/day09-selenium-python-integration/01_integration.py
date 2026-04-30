# Day 09: Selenium与Python集成
# Selenium与Python集成示例

print("Day 09: Selenium与Python集成")

import os
import json
import logging
from datetime import datetime

# 1. 模块化设计
print("\n1. 模块化设计:")

# 基础配置模块
class Config:
    """配置类"""
    def __init__(self, config_file="config.json"):
        """初始化配置"""
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self):
        """加载配置"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            else:
                # 默认配置
                return {
                    "browser": "chrome",
                    "timeout": 10,
                    "base_url": "https://www.example.com",
                    "headless": False
                }
        except Exception as e:
            print(f"   - 加载配置失败: {e}")
            return {}
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)

# WebDriver管理模块
class WebDriverManager:
    """WebDriver管理类"""
    def __init__(self, config):
        """初始化"""
        self.config = config
        self.driver = None
    
    def get_driver(self):
        """获取WebDriver"""
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
        
        try:
            browser = self.config.get("browser", "chrome")
            headless = self.config.get("headless", False)
            
            if browser == "chrome":
                chrome_options = Options()
                if headless:
                    chrome_options.add_argument("--headless")
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--no-sandbox")
                
                self.driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()),
                    options=chrome_options
                )
                
                # 设置隐式等待
                timeout = self.config.get("timeout", 10)
                self.driver.implicitly_wait(timeout)
                
                return self.driver
            else:
                raise Exception("不支持的浏览器")
        except Exception as e:
            print(f"   - 获取WebDriver失败: {e}")
            return None
    
    def close(self):
        """关闭WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
                print("   - WebDriver已关闭")
            except Exception as e:
                print(f"   - 关闭WebDriver失败: {e}")

# 页面操作模块
class PageOperator:
    """页面操作类"""
    def __init__(self, driver, logger=None):
        """初始化"""
        self.driver = driver
        self.logger = logger
    
    def open_url(self, url):
        """打开URL"""
        try:
            self.driver.get(url)
            if self.logger:
                self.logger.info(f"打开URL: {url}")
            print(f"   - 打开URL: {url}")
            return True
        except Exception as e:
            if self.logger:
                self.logger.error(f"打开URL失败: {e}")
            print(f"   - 打开URL失败: {e}")
            return False
    
    def find_element(self, by, value):
        """查找元素"""
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, value))
            )
            if self.logger:
                self.logger.info(f"找到元素: {by}, {value}")
            return element
        except Exception as e:
            if self.logger:
                self.logger.error(f"查找元素失败: {by}, {value}, {e}")
            print(f"   - 查找元素失败: {e}")
            return None
    
    def click(self, by, value):
        """点击元素"""
        element = self.find_element(by, value)
        if element:
            try:
                element.click()
                if self.logger:
                    self.logger.info(f"点击元素: {by}, {value}")
                print(f"   - 点击元素: {by}, {value}")
                return True
            except Exception as e:
                if self.logger:
                    self.logger.error(f"点击元素失败: {e}")
                print(f"   - 点击元素失败: {e}")
                return False
        return False
    
    def input_text(self, by, value, text):
        """输入文本"""
        element = self.find_element(by, value)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                if self.logger:
                    self.logger.info(f"输入文本: {text} 到元素: {by}, {value}")
                print(f"   - 输入文本: {text}")
                return True
            except Exception as e:
                if self.logger:
                    self.logger.error(f"输入文本失败: {e}")
                print(f"   - 输入文本失败: {e}")
                return False
        return False
    
    def take_screenshot(self, filename=None):
        """截图"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            # 创建截图目录
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            screenshot_path = os.path.join("screenshots", filename)
            self.driver.save_screenshot(screenshot_path)
            if self.logger:
                self.logger.info(f"截图保存到: {screenshot_path}")
            print(f"   - 截图保存到: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            if self.logger:
                self.logger.error(f"截图失败: {e}")
            print(f"   - 截图失败: {e}")
            return None

# 2. 配置管理
print("\n2. 配置管理:")

# 创建配置实例
config = Config()
print(f"   - 浏览器: {config.get('browser')}")
print(f"   - 超时时间: {config.get('timeout')}秒")
print(f"   - 基础URL: {config.get('base_url')}")
print(f"   - 无头模式: {config.get('headless')}")

# 3. 日志系统
print("\n3. 日志系统:")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("selenium.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("selenium_test")
logger.info("开始Selenium测试")

# 4. 完整集成示例
print("\n4. 完整集成示例:")

# 创建WebDriver管理器
wd_manager = WebDriverManager(config)
driver = wd_manager.get_driver()

if driver:
    # 创建页面操作器
    page = PageOperator(driver, logger)
    
    # 测试百度搜索
    print("\n测试百度搜索:")
    page.open_url("https://www.baidu.com")
    page.input_text("id", "kw", "Selenium Python")
    page.click("id", "su")
    
    # 截图
    page.take_screenshot("baidu_search.png")
    
    # 关闭浏览器
    wd_manager.close()

# 5. 高级集成
print("\n5. 高级集成:")

# 测试框架集成示例
class TestCase:
    """测试用例类"""
    def __init__(self, name):
        """初始化"""
        self.name = name
        self.config = Config()
        self.wd_manager = WebDriverManager(self.config)
        self.driver = self.wd_manager.get_driver()
        self.page = PageOperator(self.driver, logger)
        self.passed = False
    
    def run(self):
        """运行测试"""
        logger.info(f"开始测试: {self.name}")
        print(f"   - 开始测试: {self.name}")
        
        try:
            # 测试逻辑
            self.test_logic()
            self.passed = True
            logger.info(f"测试通过: {self.name}")
            print(f"   - 测试通过: {self.name}")
        except Exception as e:
            logger.error(f"测试失败: {self.name}, {e}")
            print(f"   - 测试失败: {e}")
        finally:
            self.wd_manager.close()
        
        return self.passed
    
    def test_logic(self):
        """测试逻辑，子类实现"""
        pass

# 具体测试用例
class BaiduSearchTest(TestCase):
    """百度搜索测试"""
    def test_logic(self):
        """测试百度搜索"""
        self.page.open_url("https://www.baidu.com")
        self.page.input_text("id", "kw", "Selenium")
        self.page.click("id", "su")
        # 验证搜索结果
        element = self.page.find_element("class name", "nums")
        assert element is not None

class GoogleSearchTest(TestCase):
    """谷歌搜索测试"""
    def test_logic(self):
        """测试谷歌搜索"""
        self.page.open_url("https://www.google.com")
        self.page.input_text("name", "q", "Python")
        self.page.click("name", "btnK")
        # 验证搜索结果
        element = self.page.find_element("id", "search")
        assert element is not None

# 运行测试
print("\n运行测试用例:")
test1 = BaiduSearchTest("百度搜索测试")
test1.run()

test2 = GoogleSearchTest("谷歌搜索测试")
test2.run()

# 6. 最佳实践
print("\n6. 最佳实践:")
print("   - 使用类封装相关功能")
print("   - 配置与代码分离")
print("   - 完善的日志记录")
print("   - 异常处理机制")
print("   - 模块化设计，便于维护")
print("   - 测试用例独立运行")

logger.info("Selenium测试完成")
print("\nSelenium与Python集成示例完成！")
print("\n学习要点：")
print("1. 模块化设计:")
print("   - 将功能划分为不同的模块")
print("   - 使用类封装相关功能")
print("   - 提高代码可维护性")
print("2. 配置管理:")
print("   - 使用配置文件管理参数")
print("   - 支持不同环境的配置")
print("   - 配置热加载")
print("3. 日志系统:")
print("   - 多级别日志")
print("   - 文件和控制台输出")
print("   - 详细的日志信息")
print("4. 集成测试:")
print("   - 测试用例设计")
print("   - 测试结果验证")
print("   - 异常处理")