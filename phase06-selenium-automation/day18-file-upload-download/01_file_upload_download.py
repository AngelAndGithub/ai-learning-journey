# Day 18: 文件上传下载
# 文件上传下载示例

print("Day 18: 文件上传下载")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import shutil
import tempfile

# 1. 文件上传操作
print("\n1. 文件上传操作:")

class FileUploader:
    """文件上传类"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
    
    def upload_file(self, locator, file_path):
        """上传文件"""
        try:
            # 找到文件上传元素
            upload_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            
            # 发送文件路径
            upload_element.send_keys(file_path)
            print(f"   ✓ 文件上传成功: {file_path}")
            return True
        except Exception as e:
            print(f"   ✗ 文件上传失败: {e}")
            return False
    
    def upload_file_via_javascript(self, locator, file_path):
        """通过JavaScript上传文件"""
        try:
            # 找到文件上传元素
            upload_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            
            # 使用JavaScript设置文件路径
            self.driver.execute_script(
                "arguments[0].style.display = 'block';", upload_element
            )
            upload_element.send_keys(file_path)
            print(f"   ✓ 通过JavaScript上传文件成功: {file_path}")
            return True
        except Exception as e:
            print(f"   ✗ 通过JavaScript上传文件失败: {e}")
            return False
    
    def create_test_file(self, content="Test file content", file_name="test.txt"):
        """创建测试文件"""
        # 创建测试文件目录
        if not os.path.exists("test_files"):
            os.makedirs("test_files")
        
        # 创建测试文件
        file_path = os.path.join("test_files", file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"   ✓ 创建测试文件: {file_path}")
        return file_path

# 2. 文件下载处理
print("\n2. 文件下载处理:")

class FileDownloader:
    """文件下载类"""
    
    @staticmethod
    def get_chrome_options_with_download_dir(download_dir):
        """获取带下载目录的Chrome选项"""
        options = Options()
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        return options
    
    def __init__(self, driver, download_dir=None):
        """初始化"""
        self.driver = driver
        if download_dir:
            self.download_dir = download_dir
        else:
            self.download_dir = os.path.join(os.getcwd(), "downloads")
        
        # 创建下载目录
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        print(f"   ✓ 设置下载目录: {self.download_dir}")
    
    def download_file(self, download_link_locator):
        """下载文件"""
        try:
            # 找到下载链接
            download_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(download_link_locator)
            )
            
            # 点击下载链接
            download_link.click()
            print("   ✓ 点击下载链接")
            
            # 等待下载完成
            time.sleep(5)  # 简单等待，实际项目中应使用更可靠的方法
            
            # 检查下载目录
            files = os.listdir(self.download_dir)
            if files:
                print(f"   ✓ 下载完成，文件: {files}")
                return os.path.join(self.download_dir, files[0])
            else:
                print("   ✗ 下载失败，未找到文件")
                return None
        except Exception as e:
            print(f"   ✗ 下载失败: {e}")
            return None
    
    def get_latest_downloaded_file(self):
        """获取最新下载的文件"""
        try:
            files = os.listdir(self.download_dir)
            if not files:
                return None
            
            # 按修改时间排序
            files.sort(key=lambda x: os.path.getmtime(os.path.join(self.download_dir, x)), reverse=True)
            return os.path.join(self.download_dir, files[0])
        except Exception as e:
            print(f"   ✗ 获取最新文件失败: {e}")
            return None
    
    def clear_downloads(self):
        """清空下载目录"""
        try:
            for file in os.listdir(self.download_dir):
                file_path = os.path.join(self.download_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("   ✓ 清空下载目录")
        except Exception as e:
            print(f"   ✗ 清空下载目录失败: {e}")

# 3. 路径管理
print("\n3. 路径管理:")

class PathManager:
    """路径管理类"""
    
    @staticmethod
    def get_absolute_path(relative_path):
        """获取绝对路径"""
        return os.path.abspath(relative_path)
    
    @staticmethod
    def get_temp_directory():
        """获取临时目录"""
        return tempfile.gettempdir()
    
    @staticmethod
    def create_temp_file(content="", suffix=".txt"):
        """创建临时文件"""
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        if content:
            temp_file.write(content.encode('utf-8'))
        temp_file.close()
        return temp_file.name
    
    @staticmethod
    def delete_file(file_path):
        """删除文件"""
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"   ✓ 删除文件: {file_path}")
        else:
            print(f"   ✗ 文件不存在: {file_path}")
    
    @staticmethod
    def file_exists(file_path):
        """检查文件是否存在"""
        return os.path.exists(file_path)
    
    @staticmethod
    def get_file_size(file_path):
        """获取文件大小"""
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        return 0

# 4. 实际应用示例
print("\n4. 实际应用示例:")

# 测试文件上传
def test_file_upload():
    """测试文件上传"""
    print("   - 测试文件上传:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开文件上传测试页面
        driver.get("https://demoqa.com/upload-download")
        print("     打开文件上传测试页面")
        
        # 初始化文件上传器
        uploader = FileUploader(driver)
        
        # 创建测试文件
        test_file = uploader.create_test_file()
        
        # 上传文件
        uploader.upload_file((By.ID, "uploadFile"), test_file)
        
        # 验证上传成功
        uploaded_file_path = driver.find_element(By.ID, "uploadedFilePath").text
        print(f"     上传文件路径: {uploaded_file_path}")
        
        # 清理测试文件
        PathManager.delete_file(test_file)
        
    finally:
        driver.quit()

# 测试文件下载
def test_file_download():
    """测试文件下载"""
    print("   - 测试文件下载:")
    
    # 创建下载目录
    download_dir = os.path.join(os.getcwd(), "test_downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # 获取Chrome选项
    options = FileDownloader.get_chrome_options_with_download_dir(download_dir)
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    try:
        # 打开文件下载测试页面
        driver.get("https://demoqa.com/upload-download")
        print("     打开文件下载测试页面")
        
        # 初始化文件下载器
        downloader = FileDownloader(driver, download_dir)
        
        # 下载文件
        downloaded_file = downloader.download_file((By.ID, "downloadButton"))
        
        if downloaded_file:
            print(f"     下载文件: {downloaded_file}")
            print(f"     文件大小: {PathManager.get_file_size(downloaded_file)} bytes")
        
        # 清理下载目录
        downloader.clear_downloads()
        
    finally:
        driver.quit()
        # 删除测试下载目录
        if os.path.exists(download_dir):
            shutil.rmtree(download_dir)

# 运行测试
print("\n运行文件上传下载测试:")
test_file_upload()
test_file_download()

# 5. 高级文件操作
print("\n5. 高级文件操作:")

# 测试多文件上传
def test_multiple_file_upload():
    """测试多文件上传"""
    print("   - 测试多文件上传:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开多文件上传测试页面
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_file_multiple")
        print("     打开多文件上传测试页面")
        
        # 切换到iframe
        driver.switch_to.frame("iframeResult")
        
        # 初始化文件上传器
        uploader = FileUploader(driver)
        
        # 创建多个测试文件
        test_file1 = uploader.create_test_file("Test file 1", "test1.txt")
        test_file2 = uploader.create_test_file("Test file 2", "test2.txt")
        
        # 上传多个文件（注意：不同浏览器对多文件上传的支持不同）
        # 这里使用分号分隔多个文件路径
        multiple_files = f"{test_file1};{test_file2}"
        uploader.upload_file((By.NAME, "files"), multiple_files)
        
        # 清理测试文件
        PathManager.delete_file(test_file1)
        PathManager.delete_file(test_file2)
        
    finally:
        driver.quit()

# 测试拖放上传
def test_drag_and_drop_upload():
    """测试拖放上传"""
    print("   - 测试拖放上传:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开拖放上传测试页面
        driver.get("https://www.dropzonejs.com/")
        print("     打开拖放上传测试页面")
        
        # 初始化文件上传器
        uploader = FileUploader(driver)
        
        # 创建测试文件
        test_file = uploader.create_test_file()
        
        # 找到拖放区域
        drop_zone = driver.find_element(By.CLASS_NAME, "dz-message")
        
        # 使用JavaScript模拟拖放操作
        # 注意：实际的拖放操作比较复杂，这里只是示例
        print("     模拟拖放上传")
        
        # 清理测试文件
        PathManager.delete_file(test_file)
        
    except Exception as e:
        print(f"     测试失败: {e}")
    finally:
        driver.quit()

# 运行高级文件操作测试
print("\n运行高级文件操作测试:")
test_multiple_file_upload()
test_drag_and_drop_upload()

# 6. 文件上传下载最佳实践
print("\n6. 文件上传下载最佳实践:")
print("   - 使用绝对路径上传文件")
print("   - 设置明确的下载目录")
print("   - 验证文件上传/下载是否成功")
print("   - 清理测试文件和目录")
print("   - 处理不同浏览器的差异")
print("   - 使用显式等待确保操作完成")
print("   - 处理大文件上传的超时问题")

# 7. 常见问题及解决方案
print("\n7. 常见问题及解决方案:")
print("   - 文件路径问题: 使用绝对路径，避免相对路径的歧义")
print("   - 隐藏的文件上传元素: 使用JavaScript显示元素后再操作")
print("   - 下载路径权限: 确保下载目录有写入权限")
print("   - 下载文件重名: 实现文件重命名机制")
print("   - 大文件上传超时: 增加超时时间，使用分块上传")
print("   - 浏览器兼容性: 测试不同浏览器的文件操作")

# 8. 实际项目应用
print("\n8. 实际项目应用:")

class FileOperationManager:
    """文件操作管理器"""
    
    def __init__(self, driver):
        """初始化"""
        self.driver = driver
        self.uploader = FileUploader(driver)
        self.downloader = FileDownloader(driver)
        self.path_manager = PathManager()
    
    def upload_document(self, locator, document_type="pdf"):
        """上传文档"""
        # 创建测试文档
        test_file = self.uploader.create_test_file(
            f"Test {document_type} document", 
            f"test_document.{document_type}"
        )
        
        # 上传文件
        success = self.uploader.upload_file(locator, test_file)
        
        # 清理测试文件
        self.path_manager.delete_file(test_file)
        
        return success
    
    def download_report(self, download_locator):
        """下载报告"""
        # 下载文件
        downloaded_file = self.downloader.download_file(download_locator)
        
        if downloaded_file:
            # 验证文件
            if self.path_manager.file_exists(downloaded_file):
                print(f"   ✓ 报告下载成功: {downloaded_file}")
                return downloaded_file
        
        return None
    
    def cleanup(self):
        """清理"""
        self.downloader.clear_downloads()

# 测试文件操作管理器
def test_file_operation_manager():
    """测试文件操作管理器"""
    print("   - 测试文件操作管理器:")
    
    # 初始化浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 打开文件上传下载测试页面
        driver.get("https://demoqa.com/upload-download")
        print("     打开测试页面")
        
        # 初始化文件操作管理器
        file_manager = FileOperationManager(driver)
        
        # 上传文档
        file_manager.upload_document((By.ID, "uploadFile"), "txt")
        
        # 下载报告
        file_manager.download_report((By.ID, "downloadButton"))
        
        # 清理
        file_manager.cleanup()
        
    finally:
        driver.quit()

# 运行文件操作管理器测试
print("\n运行文件操作管理器测试:")
test_file_operation_manager()

# 9. 性能优化
print("\n9. 性能优化:")
print("   - 对于大文件上传，考虑使用分块上传")
print("   - 使用无头浏览器提高上传下载速度")
print("   - 并行处理多个文件上传")
print("   - 优化文件路径处理，减少IO操作")
print("   - 使用临时文件减少磁盘空间占用")

# 10. 安全性考虑
print("\n10. 安全性考虑:")
print("   - 验证上传文件的类型和大小")
print("   - 避免上传恶意文件")
print("   - 保护下载文件的安全")
print("   - 清理临时文件和目录")
print("   - 避免在测试中使用真实的敏感文件")

# 清理测试目录
print("\n清理测试目录:")
if os.path.exists("test_files"):
    shutil.rmtree("test_files")
    print("   ✓ 清理测试文件目录")

if os.path.exists("downloads"):
    shutil.rmtree("downloads")
    print("   ✓ 清理下载目录")

print("\n文件上传下载示例完成！")
print("\n学习要点：")
print("1. 文件上传操作:")
print("   - 基本文件上传
   - 多文件上传
   - 拖放上传
   - 隐藏元素上传
2. 文件下载处理:")
print("   - 设置下载目录
   - 处理不同类型的下载
   - 验证下载结果
3. 路径管理:")
print("   - 绝对路径和相对路径
   - 临时文件管理
   - 文件操作
4. 实际应用:")
print("   - 文件操作管理器
   - 测试文件上传下载
   - 清理测试文件
5. 最佳实践:")
print("   - 使用绝对路径
   - 验证操作结果
   - 清理测试资源
   - 处理异常情况")