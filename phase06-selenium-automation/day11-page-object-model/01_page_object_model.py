# Day 11: 页面对象模式
# 页面对象模式示例

print("Day 11: 页面对象模式")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 基础页面类
print("\n1. 基础页面类:")

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
    
    def get_attribute(self, by, value, attribute):
        """获取元素属性"""
        element = self.find_element(by, value)
        return element.get_attribute(attribute)
    
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
    
    def get_current_url(self):
        """获取当前URL"""
        return self.driver.current_url

# 2. 登录页面类
print("\n2. 登录页面类:")

class LoginPage(BasePage):
    """登录页面类"""
    # 元素定位器
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
    
    def is_error_displayed(self):
        """判断错误信息是否显示"""
        return self.is_displayed(*self.ERROR_MESSAGE)

# 3. 首页页面类
print("\n3. 首页页面类:")

class HomePage(BasePage):
    """首页页面类"""
    # 元素定位器
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断首页是否加载"""
        return self.is_displayed(*self.INVENTORY_LIST)
    
    def get_products_title(self):
        """获取产品标题"""
        return self.get_text(*self.PRODUCTS_TITLE)
    
    def click_cart(self):
        """点击购物车"""
        self.click(*self.CART_BUTTON)
    
    def logout(self):
        """退出登录"""
        self.click(*self.MENU_BUTTON)
        self.click(*self.LOGOUT_LINK)

# 4. 购物车页面类
print("\n4. 购物车页面类:")

class CartPage(BasePage):
    """购物车页面类"""
    # 元素定位器
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        """初始化"""
        super().__init__(driver)
    
    def is_loaded(self):
        """判断购物车页面是否加载"""
        return self.is_displayed(*self.CART_LIST)
    
    def get_cart_title(self):
        """获取购物车标题"""
        return self.get_text(*self.CART_TITLE)
    
    def click_checkout(self):
        """点击结账按钮"""
        self.click(*self.CHECKOUT_BUTTON)
    
    def click_continue_shopping(self):
        """点击继续购物按钮"""
        self.click(*self.CONTINUE_SHOPPING_BUTTON)

# 5. 测试用例
print("\n5. 测试用例:")

class TestLogin:
    """登录测试类"""
    def __init__(self):
        """初始化"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
    
    def test_successful_login(self):
        """测试成功登录"""
        print("   - 测试成功登录:")
        
        # 打开登录页面
        self.login_page.open()
        print("     ✓ 打开登录页面")
        
        # 登录
        self.login_page.login("standard_user", "secret_sauce")
        print("     ✓ 输入登录信息并提交")
        
        # 验证登录成功
        if self.home_page.is_loaded():
            print("     ✓ 登录成功，首页加载")
            print(f"     ✓ 页面标题: {self.home_page.get_products_title()}")
        else:
            print("     ✗ 登录失败，首页未加载")
    
    def test_invalid_login(self):
        """测试无效登录"""
        print("   - 测试无效登录:")
        
        # 打开登录页面
        self.login_page.open()
        
        # 使用无效凭据登录
        self.login_page.login("invalid_user", "wrong_password")
        print("     ✓ 输入无效登录信息")
        
        # 验证错误信息
        if self.login_page.is_error_displayed():
            error_message = self.login_page.get_error_message()
            print(f"     ✓ 错误信息显示: {error_message}")
        else:
            print("     ✗ 错误信息未显示")
    
    def test_navigation(self):
        """测试页面导航"""
        print("   - 测试页面导航:")
        
        # 登录
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        
        # 从首页导航到购物车
        self.home_page.click_cart()
        print("     ✓ 从首页导航到购物车")
        
        # 验证购物车页面
        if self.cart_page.is_loaded():
            print(f"     ✓ 购物车页面加载: {self.cart_page.get_cart_title()}")
        else:
            print("     ✗ 购物车页面未加载")
        
        # 从购物车返回首页
        self.cart_page.click_continue_shopping()
        print("     ✓ 从购物车返回首页")
        
        # 验证首页
        if self.home_page.is_loaded():
            print("     ✓ 首页加载")
        else:
            print("     ✗ 首页未加载")
        
        # 退出登录
        self.home_page.logout()
        print("     ✓ 退出登录")
        
        # 验证返回登录页
        if "saucedemo.com" in self.login_page.get_current_url():
            print("     ✓ 已返回登录页")
        else:
            print("     ✗ 未返回登录页")
    
    def close(self):
        """关闭浏览器"""
        self.driver.quit()
        print("     ✓ 浏览器已关闭")

# 6. 运行测试
print("\n6. 运行测试:")
test = TestLogin()
test.test_successful_login()
test.test_invalid_login()
test.test_navigation()
test.close()

# 7. 页面对象模式的优势
print("\n7. 页面对象模式的优势:")
print("   - 代码复用: 页面元素和操作被封装，可在多个测试用例中复用")
print("   - 可维护性: 当页面结构变化时，只需要修改对应的页面类")
print("   - 可读性: 测试代码更加清晰，易于理解")
print("   - 可扩展性: 容易添加新的页面和功能")
print("   - 减少重复代码: 避免在多个测试中重复编写相同的定位和操作代码")

# 8. 页面对象模式的最佳实践
print("\n8. 页面对象模式的最佳实践:")
print("   - 每个页面创建一个对应的类")
print("   - 将元素定位器定义为类变量")
print("   - 封装页面的所有操作方法")
print("   - 基础页面类包含通用方法")
print("   - 页面方法应该返回其他页面对象，支持方法链")
print("   - 页面类应该只包含页面相关的逻辑，不包含测试逻辑")
print("   - 使用显式等待确保元素可见")
print("   - 为每个页面提供加载状态验证方法")

# 9. 高级页面对象模式
print("\n9. 高级页面对象模式:")

# 链式调用示例
class AdvancedLoginPage(BasePage):
    """高级登录页面类"""
    def login(self, username, password):
        """登录方法，返回首页对象"""
        self.input_text(By.ID, "user-name", username)
        self.input_text(By.ID, "password", password)
        self.click(By.ID, "login-button")
        return HomePage(self.driver)  # 返回首页对象

# 测试链式调用
print("   - 链式调用示例:")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    advanced_login = AdvancedLoginPage(driver)
    advanced_login.open_url("https://www.saucedemo.com/")
    # 链式调用
    home_page = advanced_login.login("standard_user", "secret_sauce")
    print(f"     ✓ 链式调用成功，首页标题: {home_page.get_products_title()}")
finally:
    driver.quit()

print("\n页面对象模式示例完成！")
print("\n学习要点：")
print("1. 页面对象模式的基本概念:")
print("   - 将页面元素和操作封装到类中")
print("   - 每个页面对应一个类")
print("   - 测试代码与页面操作分离")
print("2. 基础页面类:")
print("   - 包含通用的页面操作方法")
print("   - 提供元素定位和操作的基础方法")
print("3. 具体页面类:")
print("   - 继承基础页面类")
print("   - 定义页面特有的元素和操作")
print("4. 测试用例:")
print("   - 使用页面对象进行测试")
print("   - 关注测试逻辑，不关注页面实现细节")
print("5. 最佳实践:")
print("   - 元素定位器集中管理")
print("   - 方法返回页面对象支持链式调用")
print("   - 提供页面加载状态验证")
print("   - 页面类只包含页面相关逻辑")