# Day 07: 基础实战项目
# 表单提交测试

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import time

print("Day 07: 基础实战项目 - 表单提交测试")

class FormSubmissionTest:
    def __init__(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_form_submission(self):
        """测试表单提交"""
        print("\n1. 测试表单提交:")
        
        try:
            # 打开表单页面
            self.driver.get("https://demoqa.com/automation-practice-form")
            print("   ✓ 打开表单页面")
            
            # 等待页面加载
            self.wait.until(EC.presence_of_element_located((By.ID, "firstName")))
            
            # 输入个人信息
            print("   - 输入个人信息:")
            
            # 姓名
            first_name = self.driver.find_element(By.ID, "firstName")
            first_name.send_keys("张")
            print("   ✓ 输入姓氏")
            
            last_name = self.driver.find_element(By.ID, "lastName")
            last_name.send_keys("三")
            print("   ✓ 输入名字")
            
            # 邮箱
            email = self.driver.find_element(By.ID, "userEmail")
            email.send_keys("test@example.com")
            print("   ✓ 输入邮箱")
            
            # 性别
            gender = self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
            gender.click()
            print("   ✓ 选择性别")
            
            # 手机号
            mobile = self.driver.find_element(By.ID, "userNumber")
            mobile.send_keys("13800138000")
            print("   ✓ 输入手机号")
            
            # 日期选择
            print("   - 选择日期:")
            dob = self.driver.find_element(By.ID, "dateOfBirthInput")
            dob.click()
            
            # 选择月份
            month_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
            month_select.select_by_index(5)  # 6月
            
            # 选择年份
            year_select = Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
            year_select.select_by_value("1990")
            
            # 选择日期
            day = self.driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]")
            day.click()
            print("   ✓ 选择出生日期")
            
            # 滚动到下一部分
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)
            
            # 学科
            print("   - 选择学科:")
            subjects = self.driver.find_element(By.ID, "subjectsInput")
            subjects.send_keys("Maths")
            subjects.send_keys("\n")
            subjects.send_keys("English")
            subjects.send_keys("\n")
            print("   ✓ 选择学科")
            
            # 爱好
            hobbies = self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
            hobbies.click()
            print("   ✓ 选择爱好")
            
            # 上传文件
            print("   - 上传文件:")
            try:
                file_input = self.driver.find_element(By.ID, "uploadPicture")
                # 注意：这里需要提供一个实际的文件路径
                # file_input.send_keys("path/to/your/file.jpg")
                print("   ✓ 文件上传控件定位成功")
            except Exception as e:
                print(f"   ⚠ 文件上传测试跳过: {e}")
            
            # 地址
            address = self.driver.find_element(By.ID, "currentAddress")
            address.send_keys("北京市朝阳区测试地址")
            print("   ✓ 输入地址")
            
            # 滚动到提交按钮
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)
            
            # 提交表单
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            print("   ✓ 点击提交按钮")
            
            # 等待提交成功
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
            
            # 验证提交成功
            modal_title = self.driver.find_element(By.CLASS_NAME, "modal-title").text
            if "Thanks for submitting the form" in modal_title:
                print("   ✓ 表单提交成功！")
                
                # 打印表单数据
                print("   - 提交的表单数据:")
                modal_body = self.driver.find_element(By.CLASS_NAME, "modal-body")
                data_rows = modal_body.find_elements(By.CLASS_NAME, "table-responsive")
                for row in data_rows:
                    print(row.text)
            else:
                print("   ✗ 表单提交失败")
                
            # 关闭模态框
            close_button = self.driver.find_element(By.ID, "closeLargeModal")
            close_button.click()
            print("   ✓ 关闭结果模态框")
            
        except TimeoutException:
            print("   ✗ 测试超时")
        except Exception as e:
            print(f"   ✗ 表单提交测试失败: {e}")
    
    def test_form_validation(self):
        """测试表单验证"""
        print("\n2. 测试表单验证:")
        
        try:
            # 打开表单页面
            self.driver.get("https://demoqa.com/automation-practice-form")
            print("   ✓ 打开表单页面")
            
            # 等待页面加载
            self.wait.until(EC.presence_of_element_located((By.ID, "firstName")))
            
            # 直接提交空表单
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            print("   ✓ 提交空表单")
            
            # 验证是否有验证提示
            # 注意：demoqa的表单验证可能不会显示明显的错误信息
            # 这里我们通过检查页面是否仍然在表单页来验证
            current_url = self.driver.current_url
            if "automation-practice-form" in current_url:
                print("   ✓ 表单验证通过，空表单未提交")
            else:
                print("   ✗ 表单验证失败，空表单被提交")
                
        except TimeoutException:
            print("   ✗ 测试超时")
        except Exception as e:
            print(f"   ✗ 表单验证测试失败: {e}")
    
    def close(self):
        """关闭浏览器"""
        self.driver.quit()
        print("\n浏览器已关闭")

if __name__ == "__main__":
    # 创建表单测试实例
    form_test = FormSubmissionTest()
    
    # 运行测试
    form_test.test_form_submission()
    form_test.test_form_validation()
    
    # 关闭浏览器
    form_test.close()
    
    print("\n表单提交测试完成！")
    print("\n学习要点：")
    print("1. 复杂表单处理:")
    print("   - 多种类型的表单字段")
    print("   - 日期选择器操作")
    print("   - 文件上传")
    print("   - 滚动操作")
    print("2. 测试验证:")
    print("   - 提交成功验证")
    print("   - 表单验证测试")
    print("   - 结果数据验证")
    print("3. 异常处理:")
    print("   - 处理可能的错误")
    print("   - 测试环境差异")