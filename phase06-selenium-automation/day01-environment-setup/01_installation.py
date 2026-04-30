# Day 01: Selenium环境搭建
# 安装说明

"""
Selenium环境搭建步骤：

1. 安装Python 3.8+
   - 下载地址：https://www.python.org/downloads/
   - 安装时勾选"Add Python to PATH"

2. 安装Selenium
   - pip install selenium

3. 安装WebDriver管理工具
   - pip install webdriver-manager

4. 安装其他依赖
   - pip install pytest pytest-html

5. 验证安装
   - 运行此脚本检查环境是否搭建成功
"""

import sys
from importlib import import_module

# 检查Python版本
print(f"Python版本: {sys.version}")

# 检查依赖安装情况
dependencies = ['selenium', 'webdriver_manager', 'pytest', 'pytest_html']

for dep in dependencies:
    try:
        import_module(dep)
        print(f"[OK] {dep} 已安装")
    except ImportError:
        print(f"[ERROR] {dep} 未安装")
        print(f"   请运行: pip install {dep}")

print("\n环境检查完成！")
print("\n下一步：运行 02_first_script.py 测试第一个Selenium脚本")