# Day 21: 高级实战项目
# 高级实战项目示例

print("Day 21: 高级实战项目")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import json
import csv
from datetime import datetime

# 1. 项目结构设计
print("\n1. 项目结构设计:")
print("   - 页面对象模式组织代码")
print("   - 测试数据与测试逻辑分离")
print("   - 模块化设计便于维护")
print("   - 异常处理机制")
print("   - 测试报告生成")

# 2. 页面对象实现
print("\n2. 页面对象实现:")

class BasePage:
    """基础页面类"""
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def find_element(self, by, value):
        """查找元素"""
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_elements(self, by, value):
        """查找多个元素"""
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))
    
    def click(self, by, value):
        """点击元素"""
        element = self.find_element(by, value)
        element.click()
    
    def input_text(self, by, value, text):
        """输入文本"""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by, value):
        """获取元素文本"""
        element = self.find_element(by, value)
        return element.text
    
    def is_displayed(self, by, value):
        """判断元素是否显示"""
        try:
            element = self.find_element(by, value)
            return element.is_displayed()
        except:
            return False
    
    def open_url(self, url):
        """打开URL"""
        self.driver.get(url)
    
    def get_title(self):
        """获取页面标题"""
        return self.driver.title

class LoginPage(BasePage):
    """登录页面类"""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
    
    def open(self):
        """打开登录页面"""
        self.open_url(self.url)
    
    def login(self, username, password):
        """登录方法"""
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """获取错误信息"""
        return self.get_text(*self.ERROR_MESSAGE)

class ProductsPage(BasePage):
    """产品页面类"""
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断页面是否加载"""
        return self.is_displayed(*self.INVENTORY_LIST)
    
    def get_products_title(self):
        """获取产品标题"""
        return self.get_text(*self.PRODUCTS_TITLE)
    
    def add_product_to_cart(self, product_index):
        """添加产品到购物车"""
        buttons = self.find_elements(*self.ADD_TO_CART_BUTTONS)
        if product_index < len(buttons):
            buttons[product_index].click()
            return True
        return False
    
    def add_product_by_name(self, product_name):
        """根据名称添加产品到购物车"""
        products = self.find_elements(*self.PRODUCT_NAMES)
        for i, product in enumerate(products):
            if product.text == product_name:
                buttons = self.find_elements(*self.ADD_TO_CART_BUTTONS)
                if i < len(buttons):
                    buttons[i].click()
                    return True
        return False
    
    def get_product_names(self):
        """获取所有产品名称"""
        products = self.find_elements(*self.PRODUCT_NAMES)
        return [product.text for product in products]
    
    def go_to_cart(self):
        """前往购物车"""
        self.click(*self.CART_BUTTON)

class CartPage(BasePage):
    """购物车页面类"""
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CLASS_NAME, "cart_button")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断页面是否加载"""
        return self.is_displayed(*self.CART_LIST)
    
    def get_cart_item_count(self):
        """获取购物车商品数量"""
        items = self.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def remove_item(self, item_index):
        """移除商品"""
        buttons = self.find_elements(*self.REMOVE_BUTTONS)
        if item_index < len(buttons):
            buttons[item_index].click()
            return True
        return False
    
    def checkout(self):
        """结账"""
        self.click(*self.CHECKOUT_BUTTON)

class CheckoutPage(BasePage):
    """结账页面类"""
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """填写结账表单"""
        self.input_text(*self.FIRST_NAME_INPUT, first_name)
        self.input_text(*self.LAST_NAME_INPUT, last_name)
        self.input_text(*self.POSTAL_CODE_INPUT, postal_code)
        self.click(*self.CONTINUE_BUTTON)

class CheckoutOverviewPage(BasePage):
    """结账概览页面类"""
    OVERVIEW_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断页面是否加载"""
        return self.is_displayed(*self.OVERVIEW_TITLE)
    
    def get_total_price(self):
        """获取总价格"""
        return self.get_text(*self.TOTAL_PRICE)
    
    def get_item_total(self):
        """获取商品总价"""
        return self.get_text(*self.ITEM_TOTAL)
    
    def finish_checkout(self):
        """完成结账"""
        self.click(*self.FINISH_BUTTON)

class CheckoutCompletePage(BasePage):
    """结账完成页面类"""
    COMPLETE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断页面是否加载"""
        return self.is_displayed(*self.COMPLETE_TITLE)
    
    def get_complete_message(self):
        """获取完成消息"""
        return self.get_text(*self.COMPLETE_MESSAGE)
    
    def back_to_home(self):
        """返回首页"""
        self.click(*self.BACK_HOME_BUTTON)

# 3. 测试数据管理
print("\n3. 测试数据管理:")

class TestDataManager:
    """测试数据管理器"""
    
    @staticmethod
    def load_test_data(file_path):
        """加载测试数据"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"   ✗ 加载测试数据失败: {e}")
            return {}
    
    @staticmethod
    def save_test_data(data, file_path):
        """保存测试数据"""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"   ✓ 测试数据保存成功: {file_path}")
        except Exception as e:
            print(f"   ✗ 保存测试数据失败: {e}")
    
    @staticmethod
    def generate_test_data():
        """生成测试数据"""
        test_data = {
            "login": {
                "valid": {
                    "username": "standard_user",
                    "password": "secret_sauce"
                },
                "invalid": {
                    "username": "invalid_user",
                    "password": "wrong_password"
                }
            },
            "checkout": {
                "first_name": "John",
                "last_name": "Doe",
                "postal_code": "12345"
            },
            "products": [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ],
            "test_cases": [
                {
                    "name": "成功登录",
                    "username": "standard_user",
                    "password": "secret_sauce",
                    "expected": "success"
                },
                {
                    "name": "无效登录",
                    "username": "invalid_user",
                    "password": "secret_sauce",
                    "expected": "failure"
                }
            ]
        }
        return test_data

# 4. 测试框架集成
print("\n4. 测试框架集成:")

class TestFramework:
    """测试框架"""
    
    def __init__(self, test_name):
        """初始化"""
        self.test_name = test_name
        self.test_results = []
        self.start_time = datetime.now()
        
        # 创建测试报告目录
        if not os.path.exists("test_reports"):
            os.makedirs("test_reports")
    
    def setup_driver(self, headless=False):
        """设置驱动"""
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        driver.maximize_window()
        return driver
    
    def add_test_result(self, test_case, status, message, execution_time):
        """添加测试结果"""
        result = {
            "test_case": test_case,
            "status": status,  # "PASS" or "FAIL"
            "message": message,
            "execution_time": execution_time,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
    
    def generate_report(self):
        """生成测试报告"""
        end_time = datetime.now()
        total_time = (end_time - self.start_time).total_seconds()
        
        # 统计结果
        pass_count = sum(1 for result in self.test_results if result["status"] == "PASS")
        fail_count = sum(1 for result in self.test_results if result["status"] == "FAIL")
        total_tests = len(self.test_results)
        
        # 生成报告
        report = {
            "test_name": self.test_name,
            "start_time": self.start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "total_time": total_time,
            "total_tests": total_tests,
            "pass_count": pass_count,
            "fail_count": fail_count,
            "success_rate": (pass_count / total_tests * 100) if total_tests > 0 else 0,
            "test_results": self.test_results
        }
        
        # 保存报告
        report_file = f"test_reports\{self.test_name}_{end_time.strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # 打印报告
        print("\n   测试报告:")
        print("   ===================================")
        print(f"   测试名称: {self.test_name}")
        print(f"   开始时间: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   总执行时间: {total_time:.2f} 秒")
        print(f"   总测试数: {total_tests}")
        print(f"   通过测试: {pass_count}")
        print(f"   失败测试: {fail_count}")
        print(f"   成功率: {report['success_rate']:.2f}%")
        print("   ")
        print("   测试详情:")
        for i, result in enumerate(self.test_results, 1):
            print(f"     {i}. {result['test_case']}: {result['status']} ({result['execution_time']:.2f} 秒)")
            if result['status'] == "FAIL":
                print(f"       失败原因: {result['message']}")
        print("   ===================================")
        print(f"   报告已保存到: {report_file}")

# 5. 完整的测试用例
print("\n5. 完整的测试用例:")

class EcommerceTestSuite:
    """电商测试套件"""
    
    def __init__(self):
        """初始化"""
        self.framework = TestFramework("电商网站自动化测试")
        self.test_data = TestDataManager.generate_test_data()
        
        # 保存测试数据
        TestDataManager.save_test_data(self.test_data, "test_data.json")
    
    def test_login(self):
        """测试登录"""
        print("   - 测试登录")
        
        for test_case in self.test_data["test_cases"]:
            start_time = time.time()
            driver = self.framework.setup_driver()
            
            try:
                login_page = LoginPage(driver)
                login_page.open()
                login_page.login(test_case["username"], test_case["password"])
                
                if test_case["expected"] == "success":
                    products_page = ProductsPage(driver)
                    assert products_page.is_loaded()
                    self.framework.add_test_result(
                        test_case["name"],
                        "PASS",
                        "登录成功",
                        time.time() - start_time
                    )
                else:
                    error_message = login_page.get_error_message()
                    assert "Epic sadface" in error_message
                    self.framework.add_test_result(
                        test_case["name"],
                        "PASS",
                        f"登录失败，错误信息: {error_message}",
                        time.time() - start_time
                    )
            except Exception as e:
                self.framework.add_test_result(
                    test_case["name"],
                    "FAIL",
                    str(e),
                    time.time() - start_time
                )
            finally:
                driver.quit()
    
    def test_end_to_end_flow(self):
        """测试端到端流程"""
        print("   - 测试端到端流程")
        
        start_time = time.time()
        driver = self.framework.setup_driver()
        
        try:
            # 1. 登录
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(
                self.test_data["login"]["valid"]["username"],
                self.test_data["login"]["valid"]["password"]
            )
            
            # 2. 浏览产品
            products_page = ProductsPage(driver)
            assert products_page.is_loaded()
            
            # 3. 添加产品到购物车
            for product in self.test_data["products"]:
                products_page.add_product_by_name(product)
            
            # 4. 前往购物车
            products_page.go_to_cart()
            
            # 5. 验证购物车
            cart_page = CartPage(driver)
            assert cart_page.is_loaded()
            assert cart_page.get_cart_item_count() == len(self.test_data["products"])
            
            # 6. 结账
            cart_page.checkout()
            
            # 7. 填写结账信息
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_form(
                self.test_data["checkout"]["first_name"],
                self.test_data["checkout"]["last_name"],
                self.test_data["checkout"]["postal_code"]
            )
            
            # 8. 确认订单
            overview_page = CheckoutOverviewPage(driver)
            assert overview_page.is_loaded()
            
            # 9. 完成订单
            overview_page.finish_checkout()
            
            # 10. 验证订单完成
            complete_page = CheckoutCompletePage(driver)
            assert complete_page.is_loaded()
            assert "THANK YOU FOR YOUR ORDER" in complete_page.get_complete_message()
            
            self.framework.add_test_result(
                "端到端流程测试",
                "PASS",
                "端到端流程测试通过",
                time.time() - start_time
            )
            
        except Exception as e:
            self.framework.add_test_result(
                "端到端流程测试",
                "FAIL",
                str(e),
                time.time() - start_time
            )
        finally:
            driver.quit()
    
    def test_product_management(self):
        """测试产品管理"""
        print("   - 测试产品管理")
        
        start_time = time.time()
        driver = self.framework.setup_driver()
        
        try:
            # 登录
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(
                self.test_data["login"]["valid"]["username"],
                self.test_data["login"]["valid"]["password"]
            )
            
            # 浏览产品
            products_page = ProductsPage(driver)
            assert products_page.is_loaded()
            
            # 获取产品列表
            product_names = products_page.get_product_names()
            print(f"     产品列表: {product_names}")
            assert len(product_names) > 0
            
            # 添加第一个产品
            products_page.add_product_to_cart(0)
            
            # 前往购物车
            products_page.go_to_cart()
            
            # 验证购物车
            cart_page = CartPage(driver)
            assert cart_page.is_loaded()
            assert cart_page.get_cart_item_count() == 1
            
            # 移除产品
            cart_page.remove_item(0)
            time.sleep(1)
            assert cart_page.get_cart_item_count() == 0
            
            self.framework.add_test_result(
                "产品管理测试",
                "PASS",
                "产品管理测试通过",
                time.time() - start_time
            )
            
        except Exception as e:
            self.framework.add_test_result(
                "产品管理测试",
                "FAIL",
                str(e),
                time.time() - start_time
            )
        finally:
            driver.quit()
    
    def run_all_tests(self):
        """运行所有测试"""
        print("   运行所有测试")
        self.test_login()
        self.test_end_to_end_flow()
        self.test_product_management()
        self.framework.generate_report()

# 6. 实际运行测试
print("\n6. 实际运行测试:")

test_suite = EcommerceTestSuite()
test_suite.run_all_tests()

# 7. 高级功能集成
print("\n7. 高级功能集成:")

class AdvancedFeatures:
    """高级功能"""
    
    @staticmethod
    def take_screenshot(driver, filename):
        """截图"""
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        screenshot_path = os.path.join("screenshots", filename)
        driver.save_screenshot(screenshot_path)
        print(f"   ✓ 截图保存到: {screenshot_path}")
        return screenshot_path
    
    @staticmethod
    def log_test_step(step_name):
        """记录测试步骤"""
        print(f"   - {step_name}")
    
    @staticmethod
    def handle_exception(e, test_case):
        """处理异常"""
        print(f"   ✗ {test_case} 失败: {e}")

# 8. 项目优化
print("\n8. 项目优化:")
print("   - 使用页面对象模式提高代码可维护性")
print("   - 测试数据与测试逻辑分离，便于管理")
print("   - 模块化设计，便于扩展")
print("   - 完善的异常处理机制")
print("   - 生成详细的测试报告")
print("   - 支持无头浏览器运行")
print("   - 截图功能，便于调试")
print("   - 日志记录，便于追踪")

# 9. 部署与集成
print("\n9. 部署与集成:")
print("   - CI/CD集成")
print("   - 容器化部署")
print("   - 定时执行")
print("   - 测试报告邮件通知")
print("   - 与监控系统集成")

# 10. 总结
print("\n10. 总结:")
print("   - 成功构建了完整的电商网站自动化测试框架")
print("   - 实现了登录、浏览产品、购物车、结账等完整流程测试")
print("   - 应用了页面对象模式、数据驱动测试、测试框架集成等高级技术")
print("   - 生成了详细的测试报告，便于分析和监控")
print("   - 代码结构清晰，易于维护和扩展")
print("   - 可以作为企业级自动化测试框架的基础")

print("\n高级实战项目示例完成！")
print("\n学习要点：")
print("1. 项目结构设计:")
print("   - 模块化设计
   - 代码组织
   - 目录结构
2. 页面对象模式:")
print("   - 基础页面类
   - 具体页面类
   - 元素定位管理
3. 测试数据管理:")
print("   - 数据分离
   - 数据加载
   - 数据生成
4. 测试框架集成:")
print("   - 测试执行
   - 结果收集
   - 报告生成
5. 高级功能:")
print("   - 截图功能
   - 异常处理
   - 日志记录
6. 实际应用:")
print("   - 完整业务流程测试
   - 边界情况测试
   - 异常情况测试")