# Day 12: 测试框架集成
# 测试框架集成示例

print("Day 12: 测试框架集成")

import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 1. unittest框架
print("\n1. unittest框架:")

class LoginTest(unittest.TestCase):
    """登录测试类"""
    
    def setUp(self):
        """测试前的准备工作"""
        print("   - 开始测试...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_successful_login(self):
        """测试成功登录"""
        print("   - 测试成功登录")
        # 打开登录页面
        self.driver.get("https://www.saucedemo.com/")
        
        # 输入用户名和密码
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # 验证登录成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
        # 断言
        self.assertIn("inventory.html", self.driver.current_url)
        print("   ✓ 测试通过")
    
    def test_invalid_login(self):
        """测试无效登录"""
        print("   - 测试无效登录")
        # 打开登录页面
        self.driver.get("https://www.saucedemo.com/")
        
        # 输入无效的用户名和密码
        self.driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        
        # 验证错误信息
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        
        # 断言
        self.assertTrue(error_message.is_displayed())
        print("   ✓ 测试通过")
    
    def tearDown(self):
        """测试后的清理工作"""
        self.driver.quit()
        print("   - 测试结束")

# 2. pytest框架
print("\n2. pytest框架:")

class TestLoginWithPytest:
    """使用pytest的登录测试类"""
    
    def setup_method(self):
        """测试前的准备工作"""
        print("   - 开始测试...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """测试后的清理工作"""
        self.driver.quit()
        print("   - 测试结束")
    
    def test_successful_login(self):
        """测试成功登录"""
        print("   - 测试成功登录")
        # 打开登录页面
        self.driver.get("https://www.saucedemo.com/")
        
        # 输入用户名和密码
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # 验证登录成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
        # 断言
        assert "inventory.html" in self.driver.current_url
        print("   ✓ 测试通过")
    
    def test_invalid_login(self):
        """测试无效登录"""
        print("   - 测试无效登录")
        # 打开登录页面
        self.driver.get("https://www.saucedemo.com/")
        
        # 输入无效的用户名和密码
        self.driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        
        # 验证错误信息
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        
        # 断言
        assert error_message.is_displayed()
        print("   ✓ 测试通过")

# 3. 参数化测试
print("\n3. 参数化测试:")

# 使用pytest的参数化装饰器
@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", "success"),
    ("invalid_user", "secret_sauce", "failure"),
    ("standard_user", "wrong_password", "failure"),
    ("", "", "failure")
])
def test_parameterized_login(username, password, expected):
    """参数化登录测试"""
    print(f"   - 测试: {username}, {password}, {expected}")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    
    try:
        # 打开登录页面
        driver.get("https://www.saucedemo.com/")
        
        # 输入用户名和密码
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        if expected == "success":
            # 验证登录成功
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            assert "inventory.html" in driver.current_url
            print("   ✓ 登录成功测试通过")
        else:
            # 验证登录失败
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            assert error_message.is_displayed()
            print("   ✓ 登录失败测试通过")
    finally:
        driver.quit()

# 4. 测试报告生成
print("\n4. 测试报告生成:")

# pytest-html报告
print("   - pytest-html报告:")
print("   使用命令: pytest --html=report.html --self-contained-html")

# allure报告
print("   - Allure报告:")
print("   使用命令: pytest --alluredir=allure-results")
print("   查看报告: allure serve allure-results")

# 5. 测试框架集成最佳实践
print("\n5. 测试框架集成最佳实践:")
print("   - 使用测试框架的 setUp/tearDown 方法管理资源")
print("   - 使用断言验证测试结果")
print("   - 使用参数化测试提高测试覆盖率")
print("   - 生成详细的测试报告")
print("   - 使用测试夹具 (fixtures) 管理测试依赖")
print("   - 组织测试用例为逻辑分组")

# 6. 实际应用示例
print("\n6. 实际应用示例:")

# 测试夹具示例
def setup_driver():
    """创建WebDriver实例"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def teardown_driver(driver):
    """关闭WebDriver实例"""
    driver.quit()

# 使用夹具的测试
def test_with_fixture():
    """使用夹具的测试"""
    print("   - 使用夹具的测试")
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        assert "Swag Labs" in driver.title
        print("   ✓ 测试通过")
    finally:
        teardown_driver(driver)

# 7. 测试框架配置
print("\n7. 测试框架配置:")

# pytest配置示例
print("   - pytest配置文件 (pytest.ini):")
print("   [pytest]")
print("   addopts = --html=report.html --self-contained-html")
print("   testpaths = tests")
print("   python_files = test_*.py")
print("   python_classes = Test*")
print("   python_functions = test*")

# 8. 运行测试
print("\n8. 运行测试:")

# 运行unittest测试
print("   - 运行unittest测试:")
print("   python -m unittest day12-test-framework-integration/01_test_framework_integration.py")

# 运行pytest测试
print("   - 运行pytest测试:")
print("   python -m pytest day12-test-framework-integration/01_test_framework_integration.py -v")

# 运行参数化测试
print("   - 运行参数化测试:")
print("   python -m pytest day12-test-framework-integration/01_test_framework_integration.py::test_parameterized_login -v")

# 9. 测试框架对比
print("\n9. 测试框架对比:")
print("   - unittest:")
print("     ✓  Python标准库，无需额外安装")
print("     ✓  提供完整的测试框架功能")
print("     ✗  语法相对繁琐")
print("   - pytest:")
print("     ✓  语法简洁，功能强大")
print("     ✓  丰富的插件生态")
print("     ✓  支持参数化测试")
print("     ✗  需要额外安装")

# 10. 高级测试框架功能
print("\n10. 高级测试框架功能:")
print("   - 测试跳过: @unittest.skip 或 @pytest.mark.skip")
print("   - 测试预期失败: @unittest.expectedFailure 或 @pytest.mark.xfail")
print("   - 测试依赖: pytest-dependency 插件")
print("   - 测试并行执行: pytest-xdist 插件")
print("   - 测试超时: pytest-timeout 插件")

# 运行示例测试
print("\n运行示例测试:")

test_with_fixture()

print("\n测试框架集成示例完成！")
print("\n学习要点：")
print("1. unittest框架:")
print("   - 使用TestCase类
   - setUp和tearDown方法
   - 断言方法
2. pytest框架:")
print("   - 更简洁的语法
   - 强大的参数化测试
   - 丰富的插件生态
3. 测试报告:")
print("   - pytest-html生成HTML报告
   - Allure生成更丰富的报告
4. 最佳实践:")
print("   - 合理组织测试用例
   - 使用测试夹具管理资源
   - 生成详细的测试报告
   - 利用参数化测试提高覆盖率")