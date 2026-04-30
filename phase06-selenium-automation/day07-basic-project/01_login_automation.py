# Day 07: 基础实战项目
# 登录功能自动化

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

print("Day 07: 基础实战项目 - 登录功能自动化")

class LoginAutomation:
    def __init__(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_successful_login(self):
        """测试成功登录"""
        print("\n1. 测试成功登录:")
        
        try:
            # 打开登录页面
            self.driver.get("https://www.saucedemo.com/")
            print("   ✓ 打开登录页面")
            
            # 等待页面加载
            self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
            
            # 输入用户名
            username = self.driver.find_element(By.ID, "user-name")
            username.send_keys("standard_user")
            print("   ✓ 输入用户名")
            
            # 输入密码
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("secret_sauce")
            print("   ✓ 输入密码")
            
            # 点击登录按钮
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            print("   ✓ 点击登录按钮")
            
            # 等待登录成功
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
            
            # 验证登录成功
            current_url = self.driver.current_url
            if "inventory.html" in current_url:
                print("   ✓ 登录成功！")
            else:
                print("   ✗ 登录失败，URL不正确")
                
        except TimeoutException:
            print("   ✗ 登录超时")
        except Exception as e:
            print(f"   ✗ 登录测试失败: {e}")
    
    def test_invalid_username(self):
        """测试无效用户名登录"""
        print("\n2. 测试无效用户名登录:")
        
        try:
            # 打开登录页面
            self.driver.get("https://www.saucedemo.com/")
            print("   ✓ 打开登录页面")
            
            # 输入无效用户名
            username = self.driver.find_element(By.ID, "user-name")
            username.send_keys("invalid_user")
            print("   ✓ 输入无效用户名")
            
            # 输入密码
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("secret_sauce")
            print("   ✓ 输入密码")
            
            # 点击登录按钮
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            print("   ✓ 点击登录按钮")
            
            # 等待错误信息
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            
            print(f"   ✓ 错误信息: {error_message.text}")
            print("   ✓ 无效用户名测试成功")
            
        except TimeoutException:
            print("   ✗ 测试超时")
        except Exception as e:
            print(f"   ✗ 无效用户名测试失败: {e}")
    
    def test_invalid_password(self):
        """测试无效密码登录"""
        print("\n3. 测试无效密码登录:")
        
        try:
            # 打开登录页面
            self.driver.get("https://www.saucedemo.com/")
            print("   ✓ 打开登录页面")
            
            # 输入用户名
            username = self.driver.find_element(By.ID, "user-name")
            username.send_keys("standard_user")
            print("   ✓ 输入用户名")
            
            # 输入无效密码
            password = self.driver.find_element(By.ID, "password")
            password.send_keys("invalid_password")
            print("   ✓ 输入无效密码")
            
            # 点击登录按钮
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            print("   ✓ 点击登录按钮")
            
            # 等待错误信息
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            
            print(f"   ✓ 错误信息: {error_message.text}")
            print("   ✓ 无效密码测试成功")
            
        except TimeoutException:
            print("   ✗ 测试超时")
        except Exception as e:
            print(f"   ✗ 无效密码测试失败: {e}")
    
    def test_empty_fields(self):
        """测试空字段登录"""
        print("\n4. 测试空字段登录:")
        
        try:
            # 打开登录页面
            self.driver.get("https://www.saucedemo.com/")
            print("   ✓ 打开登录页面")
            
            # 直接点击登录按钮（不输入任何内容）
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            print("   ✓ 点击登录按钮")
            
            # 等待错误信息
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
            )
            
            print(f"   ✓ 错误信息: {error_message.text}")
            print("   ✓ 空字段测试成功")
            
        except TimeoutException:
            print("   ✗ 测试超时")
        except Exception as e:
            print(f"   ✗ 空字段测试失败: {e}")
    
    def close(self):
        """关闭浏览器"""
        self.driver.quit()
        print("\n浏览器已关闭")

if __name__ == "__main__":
    # 创建登录自动化实例
    login_test = LoginAutomation()
    
    # 运行所有测试
    login_test.test_successful_login()
    login_test.test_invalid_username()
    login_test.test_invalid_password()
    login_test.test_empty_fields()
    
    # 关闭浏览器
    login_test.close()
    
    print("\n登录功能自动化测试完成！")
    print("\n学习要点：")
    print("1. 自动化测试流程:")
    print("   - 打开页面")
    print("   - 输入数据")
    print("   - 执行操作")
    print("   - 验证结果")
    print("2. 测试用例设计:")
    print("   - 正常流程测试")
    print("   - 异常流程测试")
    print("   - 边界条件测试")
    print("3. 代码组织:")
    print("   - 使用类封装测试逻辑")
    print("   - 模块化设计")
    print("   - 异常处理")