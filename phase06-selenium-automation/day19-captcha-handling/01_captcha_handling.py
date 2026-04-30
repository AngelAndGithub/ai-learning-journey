# Day 19: 验证码处理
# 验证码处理示例

print("Day 19: 验证码处理")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import base64
from PIL import Image
import pytesseract
import requests
import json

# 1. 验证码类型介绍
print("\n1. 验证码类型介绍:")
print("   - 文本验证码: 包含字母、数字的图片验证码")
print("   - 图片验证码: 需要选择特定图片的验证码")
print("   - 滑块验证码: 需要拖动滑块到指定位置的验证码")
print("   - 行为验证码: 分析用户行为的验证码")
print("   - 语音验证码: 通过语音识别的验证码")

# 2. 简单验证码识别
print("\n2. 简单验证码识别:")

class SimpleCaptchaSolver:
    """简单验证码解决器"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def get_captcha_image(self, captcha_locator):
        """获取验证码图片"""
        try:
            # 找到验证码元素
            captcha_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(captcha_locator)
            )
            
            # 获取验证码图片的base64编码
            captcha_base64 = self.driver.execute_script("""
                var canvas = document.createElement('canvas');
                var context = canvas.getContext('2d');
                var img = arguments[0];
                canvas.height = img.naturalHeight;
                canvas.width = img.naturalWidth;
                context.drawImage(img, 0, 0);
                return canvas.toDataURL('image/png').substring(22);
            """, captcha_element)
            
            # 保存验证码图片
            if not os.path.exists("captcha_images"):
                os.makedirs("captcha_images")
            
            captcha_path = os.path.join("captcha_images", f"captcha_{int(time.time())}.png")
            with open(captcha_path, "wb") as f:
                f.write(base64.b64decode(captcha_base64))
            
            print(f"   ✓ 保存验证码图片: {captcha_path}")
            return captcha_path
        except Exception as e:
            print(f"   ✗ 获取验证码图片失败: {e}")
            return None
    
    def solve_text_captcha(self, captcha_image_path):
        """解决文本验证码"""
        try:
            # 使用pytesseract识别验证码
            img = Image.open(captcha_image_path)
            captcha_text = pytesseract.image_to_string(img)
            captcha_text = captcha_text.strip()
            print(f"   ✓ 识别验证码: {captcha_text}")
            return captcha_text
        except Exception as e:
            print(f"   ✗ 识别验证码失败: {e}")
            return None
    
    def solve_captcha(self, captcha_locator, input_locator):
        """完整的验证码解决流程"""
        # 获取验证码图片
        captcha_image = self.get_captcha_image(captcha_locator)
        if not captcha_image:
            return False
        
        # 识别验证码
        captcha_text = self.solve_text_captcha(captcha_image)
        if not captcha_text:
            return False
        
        # 输入验证码
        try:
            input_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(input_locator)
            )
            input_element.clear()
            input_element.send_keys(captcha_text)
            print(f"   ✓ 输入验证码: {captcha_text}")
            return True
        except Exception as e:
            print(f"   ✗ 输入验证码失败: {e}")
            return False

# 3. 第三方服务集成
print("\n3. 第三方服务集成:")

class ThirdPartyCaptchaSolver:
    """第三方验证码解决服务"""
    
    def __init__(self, api_key):
        """初始化"""
        self.api_key = api_key
    
    def solve_with_2captcha(self, captcha_image_path):
        """使用2Captcha解决验证码"""
        try:
            # 2Captcha API endpoint
            url = "http://2captcha.com/in.php"
            
            # 读取验证码图片
            with open(captcha_image_path, "rb") as f:
                captcha_data = f.read()
            
            # 发送请求
            response = requests.post(url, files={"file": captcha_data}, data={
                "key": self.api_key,
                "method": "post"
            })
            
            if response.ok:
                captcha_id = response.text.split('|')[1]
                print(f"   ✓ 提交验证码到2Captcha，ID: {captcha_id}")
                
                # 等待结果
                for i in range(10):
                    time.sleep(2)
                    result_url = f"http://2captcha.com/res.php?key={self.api_key}&action=get&id={captcha_id}"
                    result_response = requests.get(result_url)
                    if result_response.text.startswith("OK|"):
                        captcha_text = result_response.text.split('|')[1]
                        print(f"   ✓ 2Captcha返回结果: {captcha_text}")
                        return captcha_text
                
                print("   ✗ 2Captcha超时")
                return None
            else:
                print(f"   ✗ 2Captcha请求失败: {response.text}")
                return None
        except Exception as e:
            print(f"   ✗ 使用2Captcha失败: {e}")
            return None
    
    def solve_with_anti_captcha(self, captcha_image_path):
        """使用Anti-Captcha解决验证码"""
        try:
            # Anti-Captcha API endpoint
            url = "https://api.anti-captcha.com/createTask"
            
            # 读取验证码图片
            with open(captcha_image_path, "rb") as f:
                captcha_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            # 发送请求
            payload = {
                "clientKey": self.api_key,
                "task": {
                    "type": "ImageToTextTask",
                    "body": captcha_base64,
                    "phrase": False,
                    "case": True,
                    "numeric": 0,
                    "math": 0,
                    "minLength": 0,
                    "maxLength": 0
                }
            }
            
            response = requests.post(url, json=payload)
            if response.ok:
                result = response.json()
                task_id = result.get("taskId")
                print(f"   ✓ 提交验证码到Anti-Captcha，ID: {task_id}")
                
                # 等待结果
                for i in range(10):
                    time.sleep(2)
                    result_url = "https://api.anti-captcha.com/getTaskResult"
                    result_payload = {
                        "clientKey": self.api_key,
                        "taskId": task_id
                    }
                    result_response = requests.post(result_url, json=result_payload)
                    if result_response.ok:
                        result_data = result_response.json()
                        if result_data.get("status") == "ready":
                            captcha_text = result_data.get("solution", {}).get("text")
                            print(f"   ✓ Anti-Captcha返回结果: {captcha_text}")
                            return captcha_text
                
                print("   ✗ Anti-Captcha超时")
                return None
            else:
                print(f"   ✗ Anti-Captcha请求失败: {response.text}")
                return None
        except Exception as e:
            print(f"   ✗ 使用Anti-Captcha失败: {e}")
            return None

# 4. 验证码绕过策略
print("\n4. 验证码绕过策略:")

class CaptchaBypass:
    """验证码绕过策略"""
    
    @staticmethod
    def use_test_environment():
        """使用测试环境"""
        print("   - 使用测试环境，验证码已禁用或固定")
        print("   - 优点: 100%成功率，速度快")
        print("   - 缺点: 与生产环境有差异")
    
    @staticmethod
    def use_captcha_whitelist():
        """使用验证码白名单"""
        print("   - 向开发团队申请IP白名单")
        print("   - 优点: 100%成功率，无需处理验证码")
        print("   - 缺点: 需要开发团队配合")
    
    @staticmethod
    def use_api_directly():
        """直接使用API"""
        print("   - 绕过前端，直接调用后端API")
        print("   - 优点: 无需处理验证码，速度快")
        print("   - 缺点: 需要了解API接口，可能需要认证")
    
    @staticmethod
    def use_cookies():
        """使用Cookies"""
        print("   - 手动登录获取Cookies，在测试中使用")
        print("   - 优点: 一次登录，多次使用")
        print("   - 缺点: Cookies有过期时间")
    
    @staticmethod
    def use_headless_browser():
        """使用无头浏览器"""
        print("   - 一些验证码对无头浏览器有特殊处理")
        print("   - 优点: 可能绕过某些验证码")
        print("   - 缺点: 不是所有验证码都有效")

# 5. 滑块验证码处理
print("\n5. 滑块验证码处理:")

class SliderCaptchaSolver:
    """滑块验证码解决器"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def solve_slider_captcha(self, slider_locator, track_locator):
        """解决滑块验证码"""
        try:
            # 找到滑块和轨道
            slider = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(slider_locator)
            )
            track = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(track_locator)
            )
            
            # 获取轨道长度
            track_width = track.size['width']
            print(f"   ✓ 轨道宽度: {track_width}")
            
            # 模拟拖动
            # 这里只是示例，实际的滑块验证码可能需要更复杂的算法
            print("   - 模拟拖动滑块")
            
            # 使用JavaScript模拟拖动
            self.driver.execute_script("""
                var slider = arguments[0];
                var track = arguments[1];
                var trackWidth = track.offsetWidth;
                
                // 模拟鼠标按下
                var mouseDownEvent = new MouseEvent('mousedown', {
                    clientX: slider.getBoundingClientRect().left + slider.offsetWidth / 2,
                    clientY: slider.getBoundingClientRect().top + slider.offsetHeight / 2,
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                slider.dispatchEvent(mouseDownEvent);
                
                // 模拟拖动
                for (var i = 0; i < trackWidth; i += 5) {
                    var mouseMoveEvent = new MouseEvent('mousemove', {
                        clientX: slider.getBoundingClientRect().left + i,
                        clientY: slider.getBoundingClientRect().top + slider.offsetHeight / 2 + Math.sin(i / 10) * 5,
                        bubbles: true,
                        cancelable: true,
                        view: window
                    });
                    slider.dispatchEvent(mouseMoveEvent);
                }
                
                // 模拟鼠标释放
                var mouseUpEvent = new MouseEvent('mouseup', {
                    clientX: slider.getBoundingClientRect().left + trackWidth,
                    clientY: slider.getBoundingClientRect().top + slider.offsetHeight / 2,
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                slider.dispatchEvent(mouseUpEvent);
            """, slider, track)
            
            print("   ✓ 模拟拖动完成")
            return True
        except Exception as e:
            print(f"   ✗ 解决滑块验证码失败: {e}")
            return False

# 6. 实际应用示例
print("\n6. 实际应用示例:")

# 测试简单验证码识别
def test_simple_captcha():
    """测试简单验证码识别"""
    print("   - 测试简单验证码识别:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开验证码测试页面
        driver.get("https://www.google.com/recaptcha/api2/demo")
        print("     打开reCAPTCHA测试页面")
        
        # 这里只是示例，实际的reCAPTCHA需要特殊处理
        print("     注意：reCAPTCHA需要特殊处理，这里只是示例")
        
    finally:
        driver.quit()

# 测试滑块验证码
def test_slider_captcha():
    """测试滑块验证码"""
    print("   - 测试滑块验证码:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开滑块验证码测试页面
        driver.get("https://www.geetest.com/en/demo")
        print("     打开极验滑块验证码测试页面")
        
        # 初始化滑块验证码解决器
        slider_solver = SliderCaptchaSolver(driver)
        
        # 这里只是示例，实际的极验验证码需要更复杂的处理
        print("     注意：极验验证码需要特殊处理，这里只是示例")
        
    finally:
        driver.quit()

# 运行测试
print("\n运行验证码处理测试:")
test_simple_captcha()
test_slider_captcha()

# 7. 验证码处理最佳实践
print("\n7. 验证码处理最佳实践:")
print("   - 优先使用测试环境或白名单")
print("   - 其次考虑直接使用API")
print("   - 最后才考虑验证码识别")
print("   - 对于生产环境测试，使用第三方服务")
print("   - 定期更新验证码处理策略")
print("   - 记录验证码处理的成功率")
print("   - 处理验证码时添加适当的异常处理")

# 8. 常见问题及解决方案
print("\n8. 常见问题及解决方案:")
print("   - 验证码识别成功率低: 使用更高级的OCR服务或第三方服务")
print("   - 滑块验证码无法通过: 分析滑块轨迹，模拟更真实的人类行为")
print("   - 验证码频繁变化: 动态调整识别策略")
print("   - 验证码加载失败: 添加显式等待，确保验证码完全加载")
print("   - 第三方服务费用高: 合理使用，只在必要时使用")

# 9. 验证码处理框架
print("\n9. 验证码处理框架:")

class CaptchaHandler:
    """验证码处理框架"""
    
    def __init__(self, driver, api_key=None):
        """初始化"""
        self.driver = driver
        self.api_key = api_key
        self.simple_solver = SimpleCaptchaSolver(driver)
        self.slider_solver = SliderCaptchaSolver(driver)
        if api_key:
            self.third_party_solver = ThirdPartyCaptchaSolver(api_key)
        else:
            self.third_party_solver = None
    
    def handle_captcha(self, captcha_type, **kwargs):
        """处理验证码"""
        if captcha_type == "text":
            return self._handle_text_captcha(**kwargs)
        elif captcha_type == "slider":
            return self._handle_slider_captcha(**kwargs)
        elif captcha_type == "recaptcha":
            return self._handle_recaptcha(**kwargs)
        else:
            print(f"   ✗ 不支持的验证码类型: {captcha_type}")
            return False
    
    def _handle_text_captcha(self, captcha_locator, input_locator, use_third_party=False):
        """处理文本验证码"""
        if use_third_party and self.third_party_solver:
            # 使用第三方服务
            captcha_image = self.simple_solver.get_captcha_image(captcha_locator)
            if captcha_image:
                captcha_text = self.third_party_solver.solve_with_2captcha(captcha_image)
                if captcha_text:
                    try:
                        input_element = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located(input_locator)
                        )
                        input_element.clear()
                        input_element.send_keys(captcha_text)
                        print(f"   ✓ 使用第三方服务输入验证码: {captcha_text}")
                        return True
                    except Exception as e:
                        print(f"   ✗ 输入验证码失败: {e}")
                        return False
        else:
            # 使用简单识别
            return self.simple_solver.solve_captcha(captcha_locator, input_locator)
    
    def _handle_slider_captcha(self, slider_locator, track_locator):
        """处理滑块验证码"""
        return self.slider_solver.solve_slider_captcha(slider_locator, track_locator)
    
    def _handle_recaptcha(self, **kwargs):
        """处理reCAPTCHA"""
        print("   - reCAPTCHA需要特殊处理")
        # 这里可以集成第三方服务处理reCAPTCHA
        return False

# 测试验证码处理框架
def test_captcha_handler():
    """测试验证码处理框架"""
    print("   - 测试验证码处理框架:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开测试页面
        driver.get("https://www.google.com/recaptcha/api2/demo")
        print("     打开测试页面")
        
        # 初始化验证码处理框架
        captcha_handler = CaptchaHandler(driver)
        
        # 这里只是示例
        print("     验证码处理框架初始化成功")
        
    finally:
        driver.quit()

# 运行验证码处理框架测试
print("\n运行验证码处理框架测试:")
test_captcha_handler()

# 10. 安全性考虑
print("\n10. 安全性考虑:")
print("   - 验证码处理应仅用于合法的测试目的")
print("   - 不要使用验证码处理来绕过生产环境的安全措施")
print("   - 遵守网站的使用条款和机器人政策")
print("   - 保护第三方服务的API密钥")
print("   - 合理使用验证码处理服务，避免过度请求")

# 清理测试目录
print("\n清理测试目录:")
if os.path.exists("captcha_images"):
    import shutil
    shutil.rmtree("captcha_images")
    print("   ✓ 清理验证码图片目录")

print("\n验证码处理示例完成！")
print("\n学习要点：")
print("1. 验证码类型:")
print("   - 文本验证码
   - 图片验证码
   - 滑块验证码
   - 行为验证码
   - 语音验证码
2. 验证码处理方法:")
print("   - 简单OCR识别
   - 第三方服务集成
   - 验证码绕过策略
   - 滑块验证码处理
3. 最佳实践:")
print("   - 优先使用测试环境或白名单
   - 其次考虑直接使用API
   - 最后才考虑验证码识别
   - 记录成功率和性能
4. 实际应用:")
print("   - 验证码处理框架
   - 异常处理
   - 安全性考虑")