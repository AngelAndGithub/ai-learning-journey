# Day 14: 中级实战项目
# 电商网站自动化测试

print("Day 14: 中级实战项目 - 电商网站自动化测试")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import os
import json

# 1. 页面对象模式实现
print("\n1. 页面对象模式实现:")

class BasePage:
    """基础页面类"""
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
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
    
    def go_to_cart(self):
        """前往购物车"""
        self.click(*self.CART_BUTTON)

class CartPage(BasePage):
    """购物车页面类"""
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    
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
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断页面是否加载"""
        return self.is_displayed(*self.OVERVIEW_TITLE)
    
    def get_total_price(self):
        """获取总价格"""
        return self.get_text(*self.TOTAL_PRICE)
    
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

# 2. 测试数据管理
print("\n2. 测试数据管理:")

# 测试数据
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
    ]
}

# 保存测试数据
try:
    with open("test_data.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    print("   ✓ 测试数据文件创建成功")
except Exception as e:
    print(f"   ✗ 创建测试数据文件失败: {e}")

# 3. 完整的电商测试流程
print("\n3. 完整的电商测试流程:")

class EcommerceTest:
    """电商测试类"""
    def __init__(self):
        """初始化"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        # 初始化页面对象
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_overview_page = CheckoutOverviewPage(self.driver)
        self.checkout_complete_page = CheckoutCompletePage(self.driver)
    
    def test_end_to_end_flow(self):
        """测试端到端流程"""
        print("   - 测试端到端流程:")
        
        try:
            # 1. 登录
            print("     1. 登录")
            self.login_page.open()
            self.login_page.login(
                test_data["login"]["valid"]["username"],
                test_data["login"]["valid"]["password"]
            )
            
            # 验证登录成功
            assert self.products_page.is_loaded()
            print("     ✓ 登录成功")
            
            # 2. 浏览产品
            print("     2. 浏览产品")
            products_title = self.products_page.get_products_title()
            print(f"     ✓ 产品页面标题: {products_title}")
            
            # 3. 添加产品到购物车
            print("     3. 添加产品到购物车")
            self.products_page.add_product_to_cart(0)  # 添加第一个产品
            self.products_page.add_product_to_cart(1)  # 添加第二个产品
            print("     ✓ 添加产品到购物车成功")
            
            # 4. 前往购物车
            print("     4. 前往购物车")
            self.products_page.go_to_cart()
            
            # 验证购物车页面加载
            assert self.cart_page.is_loaded()
            item_count = self.cart_page.get_cart_item_count()
            print(f"     ✓ 购物车中有 {item_count} 件商品")
            
            # 5. 结账
            print("     5. 结账")
            self.cart_page.checkout()
            
            # 6. 填写结账信息
            print("     6. 填写结账信息")
            self.checkout_page.fill_checkout_form(
                test_data["checkout"]["first_name"],
                test_data["checkout"]["last_name"],
                test_data["checkout"]["postal_code"]
            )
            
            # 7. 确认订单
            print("     7. 确认订单")
            assert self.checkout_overview_page.is_loaded()
            total_price = self.checkout_overview_page.get_total_price()
            print(f"     ✓ 订单总价格: {total_price}")
            
            # 8. 完成订单
            print("     8. 完成订单")
            self.checkout_overview_page.finish_checkout()
            
            # 9. 验证订单完成
            print("     9. 验证订单完成")
            assert self.checkout_complete_page.is_loaded()
            complete_message = self.checkout_complete_page.get_complete_message()
            print(f"     ✓ 订单完成消息: {complete_message}")
            
            # 10. 返回首页
            print("     10. 返回首页")
            self.checkout_complete_page.back_to_home()
            assert self.products_page.is_loaded()
            print("     ✓ 返回首页成功")
            
            print("   ✓ 端到端测试通过")
            
        except Exception as e:
            print(f"   ✗ 测试失败: {e}")
        finally:
            self.driver.quit()
    
    def test_invalid_login(self):
        """测试无效登录"""
        print("   - 测试无效登录:")
        
        try:
            # 打开登录页面
            self.login_page.open()
            
            # 使用无效凭据登录
            self.login_page.login(
                test_data["login"]["invalid"]["username"],
                test_data["login"]["invalid"]["password"]
            )
            
            # 验证错误信息
            error_message = self.login_page.get_error_message()
            print(f"     ✓ 错误信息: {error_message}")
            assert "Epic sadface" in error_message
            print("   ✓ 无效登录测试通过")
            
        except Exception as e:
            print(f"   ✗ 测试失败: {e}")
        finally:
            self.driver.quit()

# 4. 运行测试
print("\n4. 运行测试:")

# 运行端到端测试
test = EcommerceTest()
test.test_end_to_end_flow()

# 运行无效登录测试
test = EcommerceTest()
test.test_invalid_login()

# 5. 测试报告生成
print("\n5. 测试报告生成:")
print("   - 使用pytest-html生成HTML报告")
print("   - 使用Allure生成详细报告")
print("   - 包含测试截图和日志")

# 6. 项目结构优化
print("\n6. 项目结构优化:")
print("   - 页面对象模式组织代码")
print("   - 测试数据与测试逻辑分离")
print("   - 模块化设计便于维护")
print("   - 异常处理机制")

# 7. 实战项目最佳实践
print("\n7. 实战项目最佳实践:")
print("   - 编写清晰的测试用例")
print("   - 使用页面对象模式")
print("   - 数据驱动测试")
print("   - 生成详细的测试报告")
print("   - 集成到CI/CD流程")
print("   - 定期维护测试代码")

# 8. 扩展功能
print("\n8. 扩展功能:")
print("   - 多浏览器测试")
print("   - 并行测试执行")
print("   - 移动端测试")
print("   - API测试集成")
print("   - 性能测试")

print("\n电商网站自动化测试完成！")
print("\n学习要点：")
print("1. 页面对象模式的实际应用:")
print("   - 封装页面元素和操作
   - 提高代码可维护性
   - 支持方法链调用
2. 完整的业务流程测试:")
print("   - 从登录到订单完成的全流程
   - 各个页面之间的导航
   - 数据传递和验证
3. 测试数据管理:")
print("   - 集中管理测试数据
   - 支持不同场景的测试
4. 测试框架集成:")
print("   - 结合pytest或unittest
   - 生成测试报告
   - 异常处理
5. 实战项目经验:")
print("   - 如何组织大型测试项目
   - 如何处理复杂的业务流程
   - 如何提高测试的稳定性和可靠性")