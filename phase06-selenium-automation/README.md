# Selenium + Python 自动化测试学习项目

## 项目简介

本项目是一个完整的Selenium + Python自动化测试学习体系，从基础到企业级框架的完整学习路线。

## 学习路线

### 学习周期：45天

### 学习阶段
1. **第1-7天**：Selenium基础
2. **第8-14天**：Python与Selenium结合
3. **第15-21天**：高级功能
4. **第22-28天**：框架构建
5. **第29-35天**：企业级应用
6. **第36-45天**：高级主题和项目实战

## 项目结构

```
phase06-selenium-automation/
├── day01-environment-setup/      # 第1天：环境搭建
├── day02-element-location/        # 第2天：元素定位
├── day03-element-operations/      # 第3天：元素操作
├── ...
├── day45-final-project/           # 第45天：最终项目
├── framework/                     # 自动化测试框架
│   ├── config/                    # 配置文件
│   ├── pages/                     # 页面对象
│   ├── tests/                     # 测试用例
│   ├── utils/                     # 工具类
│   └── reports/                   # 测试报告
├── notebooks/                     # Jupyter笔记本
├── requirements.txt               # 依赖包
└── README.md                      # 项目说明
```

## 环境搭建

### 1. 安装依赖

```bash
# 安装所有依赖
pip install -r requirements.txt
```

### 2. 验证环境

```bash
# 运行环境检查脚本
python day01-environment-setup/01_installation.py
```

### 3. 运行第一个脚本

```bash
# 运行第一个Selenium脚本
python day01-environment-setup/02_first_script.py
```

## 学习资源

### 官方文档
- Selenium官方文档：https://www.selenium.dev/documentation/
- Python官方文档：https://docs.python.org/3/

### 实践网站
- https://the-internet.herokuapp.com/ (Selenium练习网站)
- https://demoqa.com/ (测试练习平台)
- https://www.saucedemo.com/ (电商测试平台)

## 每日学习任务

### Day 01: 环境搭建
- 安装Selenium和WebDriver
- 配置开发环境
- 运行第一个Selenium脚本

### Day 02: 元素定位基础
- ID、Name、Class定位
- Link Text、Partial Link Text定位
- Tag Name、CSS Selector定位

### Day 03: 元素操作
- 点击、输入、提交操作
- 下拉框选择
- 复选框和单选按钮

### 后续每日任务将在相应目录中提供

## 框架构建

在学习过程中，我们将逐步构建一个完整的企业级自动化测试框架，包括：

- 页面对象模式(POM)
- 数据驱动测试
- 配置管理系统
- 日志系统
- 报告系统
- CI/CD集成

## 预期成果

通过45天的学习，您将：

1. 掌握Selenium核心概念和操作
2. 熟练使用Python进行Web自动化测试
3. 构建企业级自动化测试框架
4. 实现CI/CD集成
5. 具备独立完成自动化测试项目的能力

## 注意事项

1. 确保网络连接正常
2. 定期更新WebDriver版本
3. 遇到问题时参考官方文档
4. 实践是最好的学习方式

---

**开始您的Selenium自动化测试之旅！**