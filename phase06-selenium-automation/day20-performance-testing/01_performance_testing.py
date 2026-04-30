# Day 20: 性能测试基础
# 性能测试基础示例

print("Day 20: 性能测试基础")

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
import statistics
from datetime import datetime

# 1. 性能测试概念
print("\n1. 性能测试概念:")
print("   - 性能测试是测试应用程序在特定条件下的响应时间、稳定性和资源使用情况")
print("   - 在Selenium中，性能测试主要关注：")
print("     - 页面加载时间")
print("     - 元素定位性能")
print("     - 测试执行效率")
print("     - 浏览器资源使用")

# 2. 页面加载时间测量
print("\n2. 页面加载时间测量:")

class PageLoadTimeMeasurer:
    """页面加载时间测量器"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def measure_page_load_time(self, url):
        """测量页面加载时间"""
        try:
            # 开始时间
            start_time = time.time()
            
            # 打开页面
            self.driver.get(url)
            
            # 等待页面完全加载
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # 结束时间
            end_time = time.time()
            
            # 计算加载时间
            load_time = end_time - start_time
            print(f"   ✓ 页面加载时间: {load_time:.2f} 秒")
            return load_time
        except Exception as e:
            print(f"   ✗ 测量页面加载时间失败: {e}")
            return None
    
    def measure_page_load_time_with_performance_log(self, url):
        """使用性能日志测量页面加载时间"""
        try:
            # 启用性能日志
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
            caps = DesiredCapabilities.CHROME
            caps["goog:loggingPrefs"] = {
                "performance": "ALL"
            }
            
            # 创建新的driver实例
            options = Options()
            options.merge(caps)
            performance_driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
            
            # 打开页面
            performance_driver.get(url)
            
            # 等待页面加载完成
            WebDriverWait(performance_driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # 获取性能日志
            performance_logs = performance_driver.get_log("performance")
            
            # 分析日志
            load_event_end = None
            navigation_start = None
            
            for log in performance_logs:
                try:
                    log_message = json.loads(log["message"])
                    if "message" in log_message:
                        message = log_message["message"]
                        if "params" in message and "response" in message["params"]:
                            if "timing" in message["params"]["response"]:
                                timing = message["params"]["response"]["timing"]
                                if "navigationStart" in timing:
                                    navigation_start = timing["navigationStart"] / 1000
                                if "loadEventEnd" in timing and timing["loadEventEnd"] > 0:
                                    load_event_end = timing["loadEventEnd"] / 1000
                except:
                    pass
            
            if navigation_start and load_event_end:
                load_time = load_event_end - navigation_start
                print(f"   ✓ 使用性能日志测量页面加载时间: {load_time:.2f} 秒")
                performance_driver.quit()
                return load_time
            else:
                print("   ✗ 无法从性能日志获取加载时间")
                performance_driver.quit()
                return None
        except Exception as e:
            print(f"   ✗ 使用性能日志测量页面加载时间失败: {e}")
            return None
    
    def measure_multiple_load_times(self, url, iterations=5):
        """多次测量页面加载时间"""
        load_times = []
        
        for i in range(iterations):
            print(f"   测量第 {i+1} 次...")
            load_time = self.measure_page_load_time(url)
            if load_time:
                load_times.append(load_time)
            # 等待一下再进行下一次测量
            time.sleep(2)
        
        if load_times:
            average_load_time = statistics.mean(load_times)
            min_load_time = min(load_times)
            max_load_time = max(load_times)
            std_dev = statistics.stdev(load_times) if len(load_times) > 1 else 0
            
            print(f"\n   测量结果:")
            print(f"   平均加载时间: {average_load_time:.2f} 秒")
            print(f"   最小加载时间: {min_load_time:.2f} 秒")
            print(f"   最大加载时间: {max_load_time:.2f} 秒")
            print(f"   标准差: {std_dev:.2f} 秒")
            
            return {
                "average": average_load_time,
                "min": min_load_time,
                "max": max_load_time,
                "std_dev": std_dev,
                "times": load_times
            }
        else:
            print("   ✗ 所有测量都失败了")
            return None

# 3. 元素定位性能
print("\n3. 元素定位性能:")

class ElementLocationPerformance:
    """元素定位性能分析"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def measure_location_time(self, locator, iterations=10):
        """测量元素定位时间"""
        try:
            # 确保元素存在
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            
            times = []
            for i in range(iterations):
                start_time = time.time()
                element = self.driver.find_element(*locator)
                end_time = time.time()
                times.append(end_time - start_time)
            
            average_time = statistics.mean(times)
            min_time = min(times)
            max_time = max(times)
            
            print(f"   元素定位性能 (\n{locator[0]}, {locator[1]}):")
            print(f"     平均定位时间: {average_time:.6f} 秒")
            print(f"     最小定位时间: {min_time:.6f} 秒")
            print(f"     最大定位时间: {max_time:.6f} 秒")
            
            return {
                "average": average_time,
                "min": min_time,
                "max": max_time,
                "times": times
            }
        except Exception as e:
            print(f"   ✗ 测量元素定位时间失败: {e}")
            return None
    
    def compare_locator_performance(self, locators, iterations=10):
        """比较不同定位器的性能"""
        results = {}
        
        for name, locator in locators.items():
            print(f"\n   测试定位器: {name}")
            result = self.measure_location_time(locator, iterations)
            if result:
                results[name] = result
        
        if results:
            # 找出最快的定位器
            fastest_locator = min(results, key=lambda x: results[x]["average"])
            print(f"\n   最快的定位器: {fastest_locator}")
            print(f"   平均定位时间: {results[fastest_locator]["average"]:.6f} 秒")
        
        return results

# 4. 测试执行效率
print("\n4. 测试执行效率:")

class TestExecutionEfficiency:
    """测试执行效率分析"""
    
    def __init__(self):
        """初始化"""
        self.test_results = []
    
    def measure_test_execution_time(self, test_function, test_name):
        """测量测试执行时间"""
        start_time = time.time()
        try:
            test_function()
            success = True
            message = "测试通过"
        except Exception as e:
            success = False
            message = f"测试失败: {e}"
        end_time = time.time()
        execution_time = end_time - start_time
        
        result = {
            "test_name": test_name,
            "execution_time": execution_time,
            "success": success,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        
        self.test_results.append(result)
        print(f"   测试 '{test_name}' 执行时间: {execution_time:.2f} 秒 - {'成功' if success else '失败'}")
        
        return result
    
    def get_test_results(self):
        """获取测试结果"""
        return self.test_results
    
    def analyze_results(self):
        """分析测试结果"""
        if not self.test_results:
            print("   没有测试结果")
            return
        
        total_tests = len(self.test_results)
        successful_tests = sum(1 for result in self.test_results if result["success"])
        total_execution_time = sum(result["execution_time"] for result in self.test_results)
        average_execution_time = total_execution_time / total_tests
        
        print(f"\n   测试分析结果:")
        print(f"   总测试数: {total_tests}")
        print(f"   成功测试数: {successful_tests}")
        print(f"   失败测试数: {total_tests - successful_tests}")
        print(f"   总执行时间: {total_execution_time:.2f} 秒")
        print(f"   平均执行时间: {average_execution_time:.2f} 秒")
        
        # 找出执行时间最长的测试
        if self.test_results:
            longest_test = max(self.test_results, key=lambda x: x["execution_time"])
            print(f"   执行时间最长的测试: {longest_test['test_name']} ({longest_test['execution_time']:.2f} 秒)")
    
    def save_results(self, filename="test_results.json"):
        """保存测试结果"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.test_results, f, ensure_ascii=False, indent=2)
        print(f"   测试结果已保存到: {filename}")

# 5. 性能优化技巧
print("\n5. 性能优化技巧:")

class PerformanceOptimizer:
    """性能优化器"""
    
    @staticmethod
    def optimize_driver(driver):
        """优化Driver配置"""
        # 设置页面加载策略
        from selenium.webdriver.chrome.options import Options
        options = Options()
        # 选择合适的页面加载策略: normal, eager, none
        options.page_load_strategy = "eager"
        return options
    
    @staticmethod
    def optimize_element_location(driver, locator):
        """优化元素定位"""
        # 使用显式等待代替隐式等待
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element
    
    @staticmethod
    def optimize_test_execution():
        """优化测试执行"""
        tips = [
            "使用无头浏览器",
            "使用并行测试执行",
            "减少不必要的等待时间",
            "使用更高效的定位器",
            "优化测试数据准备",
            "使用测试夹具共享资源",
            "减少页面导航次数"
        ]
        print("   性能优化技巧:")
        for tip in tips:
            print(f"     - {tip}")

# 6. 实际应用示例
print("\n6. 实际应用示例:")

# 测试页面加载时间
def test_page_load_time():
    """测试页面加载时间"""
    print("   - 测试页面加载时间:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 初始化页面加载时间测量器
        measurer = PageLoadTimeMeasurer(driver)
        
        # 测试不同网站的加载时间
        websites = [
            "https://www.baidu.com",
            "https://www.google.com",
            "https://www.sogou.com"
        ]
        
        for website in websites:
            print(f"\n     测试网站: {website}")
            measurer.measure_multiple_load_times(website, 3)
            
    finally:
        driver.quit()

# 测试元素定位性能
def test_element_location_performance():
    """测试元素定位性能"""
    print("   - 测试元素定位性能:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开测试页面
        driver.get("https://www.baidu.com")
        print("     打开百度首页")
        
        # 初始化元素定位性能分析器
        analyzer = ElementLocationPerformance(driver)
        
        # 定义不同的定位器
        locators = {
            "ID": (By.ID, "kw"),
            "Name": (By.NAME, "wd"),
            "CSS": (By.CSS_SELECTOR, "#kw"),
            "XPath": (By.XPATH, "//input[@id='kw']")
        }
        
        # 比较定位器性能
        analyzer.compare_locator_performance(locators, 20)
        
    finally:
        driver.quit()

# 测试执行效率
def test_execution_efficiency():
    """测试执行效率"""
    print("   - 测试执行效率:")
    
    # 初始化测试执行效率分析器
    analyzer = TestExecutionEfficiency()
    
    # 定义测试函数
    def test_baidu_search():
        """测试百度搜索"""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            driver.get("https://www.baidu.com")
            driver.find_element(By.ID, "kw").send_keys("Selenium")
            driver.find_element(By.ID, "su").click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result"))
            )
        finally:
            driver.quit()
    
    def test_google_search():
        """测试谷歌搜索"""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            driver.get("https://www.google.com")
            driver.find_element(By.NAME, "q").send_keys("Selenium")
            driver.find_element(By.NAME, "btnK").click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
        finally:
            driver.quit()
    
    # 测量测试执行时间
    analyzer.measure_test_execution_time(test_baidu_search, "百度搜索测试")
    analyzer.measure_test_execution_time(test_google_search, "谷歌搜索测试")
    
    # 分析结果
    analyzer.analyze_results()
    
    # 保存结果
    analyzer.save_results()

# 运行测试
print("\n运行性能测试:")
test_page_load_time()
test_element_location_performance()
test_execution_efficiency()

# 7. 性能测试最佳实践
print("\n7. 性能测试最佳实践:")
print("   - 建立性能基线，用于比较不同版本的性能变化")
print("   - 在相同的环境下进行测试，确保结果的可比性")
print("   - 多次测试取平均值，减少偶然因素的影响")
print("   - 关注关键用户路径的性能，而不是所有页面")
print("   - 结合前端性能工具（如Lighthouse）进行综合分析")
print("   - 定期运行性能测试，及时发现性能回归")
print("   - 分析性能瓶颈，提供优化建议")
print("   - 考虑不同网络条件下的性能表现")

# 8. 性能测试工具
print("\n8. 性能测试工具:")
print("   - Selenium内置性能日志")
print("   - Chrome DevTools Protocol")
print("   - Lighthouse")
print("   - WebPageTest")
print("   - JMeter (用于负载测试)")
print("   - Gatling (用于负载测试)")

# 9. 实际项目应用
print("\n9. 实际项目应用:")

class PerformanceTestSuite:
    """性能测试套件"""
    
    def __init__(self):
        """初始化"""
        self.results = {}
    
    def run_performance_tests(self):
        """运行性能测试"""
        # 测试页面加载性能
        print("   - 运行页面加载性能测试")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        measurer = PageLoadTimeMeasurer(driver)
        
        # 测试关键页面
        key_pages = [
            {"name": "首页", "url": "https://www.baidu.com"},
            {"name": "搜索结果页", "url": "https://www.baidu.com/s?wd=selenium"}
        ]
        
        page_load_results = {}
        for page in key_pages:
            print(f"     测试 {page['name']}")
            result = measurer.measure_multiple_load_times(page['url'], 3)
            if result:
                page_load_results[page['name']] = result
        
        driver.quit()
        
        # 测试元素定位性能
        print("   - 运行元素定位性能测试")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.baidu.com")
        analyzer = ElementLocationPerformance(driver)
        
        locators = {
            "搜索框(ID)": (By.ID, "kw"),
            "搜索按钮(ID)": (By.ID, "su"),
            "搜索框(CSS)": (By.CSS_SELECTOR, "#kw"),
            "搜索按钮(CSS)": (By.CSS_SELECTOR, "#su")
        }
        
        location_results = analyzer.compare_locator_performance(locators, 10)
        driver.quit()
        
        # 保存结果
        self.results = {
            "page_load": page_load_results,
            "element_location": location_results,
            "timestamp": datetime.now().isoformat()
        }
        
        # 保存到文件
        with open("performance_test_results.json", "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        
        print("   ✓ 性能测试完成，结果已保存")
        return self.results
    
    def generate_report(self):
        """生成性能测试报告"""
        if not self.results:
            print("   没有测试结果")
            return
        
        print("\n   性能测试报告:")
        print("   ===================================")
        print(f"   测试时间: {self.results.get('timestamp', 'N/A')}")
        print("   ")
        
        # 页面加载性能
        print("   页面加载性能:")
        page_load = self.results.get('page_load', {})
        for page, result in page_load.items():
            print(f"     {page}:")
            print(f"       平均加载时间: {result['average']:.2f} 秒")
            print(f"       最小加载时间: {result['min']:.2f} 秒")
            print(f"       最大加载时间: {result['max']:.2f} 秒")
        
        # 元素定位性能
        print("   ")
        print("   元素定位性能:")
        element_location = self.results.get('element_location', {})
        for locator, result in element_location.items():
            print(f"     {locator}:")
            print(f"       平均定位时间: {result['average']:.6f} 秒")
        
        print("   ===================================")

# 运行性能测试套件
print("\n运行性能测试套件:")
test_suite = PerformanceTestSuite()
test_suite.run_performance_tests()
test_suite.generate_report()

# 10. 总结
print("\n10. 总结:")
print("   - 性能测试是确保应用程序质量的重要组成部分")
print("   - Selenium提供了多种方法来测量和分析性能")
print("   - 定期进行性能测试可以及时发现性能问题")
print("   - 性能优化应该是一个持续的过程")
print("   - 结合多种工具进行综合性能分析")

print("\n性能测试基础示例完成！")
print("\n学习要点：")
print("1. 页面加载时间测量:")
print("   - 基本时间测量
   - 使用性能日志
   - 多次测量取平均值
2. 元素定位性能:")
print("   - 测量不同定位器的性能
   - 选择最优的定位器
   - 定位器性能比较
3. 测试执行效率:")
print("   - 测量测试执行时间
   - 分析测试执行效率
   - 优化测试执行
4. 性能优化:")
print("   - 优化Driver配置
   - 优化元素定位
   - 优化测试执行
5. 实际应用:")
print("   - 性能测试套件
   - 生成性能测试报告
   - 持续性能监控")