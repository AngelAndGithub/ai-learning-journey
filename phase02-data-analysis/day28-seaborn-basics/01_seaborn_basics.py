#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 28: Seaborn基础

本文件包含Seaborn基础操作的练习代码
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 基本绘图
print("=== 基本绘图 ===")

# 1.1 散点图
print("\n1.1 散点图")
# 创建数据
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

# 绘制散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(x='x', y='y', hue='category', data=data)
plt.title('Seaborn散点图')
plt.savefig('seaborn_scatter.png')
plt.show()
print("Seaborn散点图已保存为 seaborn_scatter.png")

# 1.2 折线图
print("\n1.2 折线图")
# 创建数据
dates = pd.date_range('2020-01-01', periods=30, freq='D')
data = pd.DataFrame({
    'date': dates,
    'value1': np.random.randn(30).cumsum(),
    'value2': np.random.randn(30).cumsum()
})

# 绘制折线图
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='value1', data=data, label='系列1')
sns.lineplot(x='date', y='value2', data=data, label='系列2')
plt.title('Seaborn折线图')
plt.legend()
plt.savefig('seaborn_line.png')
plt.show()
print("Seaborn折线图已保存为 seaborn_line.png")

# 1.3 柱状图
print("\n1.3 柱状图")
# 创建数据
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [23, 45, 56, 78, 34]
})

# 绘制柱状图
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='value', data=data)
plt.title('Seaborn柱状图')
plt.savefig('seaborn_bar.png')
plt.show()
print("Seaborn柱状图已保存为 seaborn_bar.png")

# 1.4 直方图
print("\n1.4 直方图")
# 创建数据
data = np.random.randn(1000)

# 绘制直方图
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=True)
plt.title('Seaborn直方图')
plt.savefig('seaborn_hist.png')
plt.show()
print("Seaborn直方图已保存为 seaborn_hist.png")

# 1.5 箱线图
print("\n1.5 箱线图")
# 创建数据
data = pd.DataFrame({
    'category': np.repeat(['A', 'B', 'C', 'D'], 50),
    'value': np.random.randn(200)
})

# 绘制箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value', data=data)
plt.title('Seaborn箱线图')
plt.savefig('seaborn_box.png')
plt.show()
print("Seaborn箱线图已保存为 seaborn_box.png")

# 2. 统计图表
print("\n=== 统计图表 ===")

# 2.1 小提琴图
print("\n2.1 小提琴图")
# 绘制小提琴图
plt.figure(figsize=(10, 6))
sns.violinplot(x='category', y='value', data=data)
plt.title('Seaborn小提琴图')
plt.savefig('seaborn_violin.png')
plt.show()
print("Seaborn小提琴图已保存为 seaborn_violin.png")

# 2.2 热力图
print("\n2.2 热力图")
# 创建相关矩阵数据
corr = np.random.rand(10, 10)

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='viridis')
plt.title('Seaborn热力图')
plt.savefig('seaborn_heatmap.png')
plt.show()
print("Seaborn热力图已保存为 seaborn_heatmap.png")

# 2.3 配对图
print("\n2.3 配对图")
# 使用内置数据集
iris = sns.load_dataset('iris')

# 绘制配对图
plt.figure(figsize=(12, 10))
sns.pairplot(iris, hue='species')
plt.title('Seaborn配对图')
plt.savefig('seaborn_pairplot.png')
plt.show()
print("Seaborn配对图已保存为 seaborn_pairplot.png")

# 2.4 联合分布图
print("\n2.4 联合分布图")
# 绘制联合分布图
plt.figure(figsize=(10, 8))
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
plt.suptitle('Seaborn联合分布图', y=1.02)
plt.savefig('seaborn_jointplot.png')
plt.show()
print("Seaborn联合分布图已保存为 seaborn_jointplot.png")

# 3. 分类图表
print("\n=== 分类图表 ===")

# 3.1 分类散点图
print("\n3.1 分类散点图")
# 创建数据
tips = sns.load_dataset('tips')

# 绘制分类散点图
plt.figure(figsize=(10, 6))
sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', jitter=True)
plt.title('Seaborn分类散点图')
plt.savefig('seaborn_stripplot.png')
plt.show()
print("Seaborn分类散点图已保存为 seaborn_stripplot.png")

# 3.2 分类箱线图
print("\n3.2 分类箱线图")
# 绘制分类箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Seaborn分类箱线图')
plt.savefig('seaborn_boxplot.png')
plt.show()
print("Seaborn分类箱线图已保存为 seaborn_boxplot.png")

# 3.3 分类柱状图
print("\n3.3 分类柱状图")
# 绘制分类柱状图
plt.figure(figsize=(10, 6))
sns.barplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Seaborn分类柱状图')
plt.savefig('seaborn_barplot.png')
plt.show()
print("Seaborn分类柱状图已保存为 seaborn_barplot.png")

# 3.4 分类点图
print("\n3.4 分类点图")
# 绘制分类点图
plt.figure(figsize=(10, 6))
sns.pointplot(x='day', y='total_bill', data=tips, hue='sex')
plt.title('Seaborn分类点图')
plt.savefig('seaborn_pointplot.png')
plt.show()
print("Seaborn分类点图已保存为 seaborn_pointplot.png")

# 4. 风格和主题
print("\n=== 风格和主题 ===")

# 4.1 不同风格
print("\n4.1 不同风格")
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

for style in styles:
    sns.set_style(style)
    plt.figure(figsize=(8, 4))
    sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species')
    plt.title(f'Seaborn风格: {style}')
    plt.savefig(f'seaborn_style_{style}.png')
    plt.close()

print("Seaborn风格图已保存")

# 4.2 不同调色板
print("\n4.2 不同调色板")
palettes = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

for palette in palettes:
    plt.figure(figsize=(8, 4))
    sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species', palette=palette)
    plt.title(f'Seaborn调色板: {palette}')
    plt.savefig(f'seaborn_palette_{palette}.png')
    plt.close()

print("Seaborn调色板图已保存")

# 5. 实际应用示例
print("\n=== 实际应用示例 ===")

# 5.1 销售数据分析
print("\n5.1 销售数据分析")
# 创建销售数据
sales_data = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=12, freq='M'),
    'sales': [120, 150, 180, 200, 220, 250, 280, 300, 320, 350, 380, 400],
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# 绘制销售趋势
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='sales', data=sales_data, hue='product', style='region')
plt.title('销售趋势分析')
plt.savefig('sales_trend.png')
plt.show()
print("销售趋势分析图已保存为 sales_trend.png")

# 5.2 客户数据分析
print("\n5.2 客户数据分析")
# 创建客户数据
customer_data = pd.DataFrame({
    'age': np.random.randint(18, 70, 100),
    'income': np.random.randint(20000, 100000, 100),
    'spending': np.random.randint(1000, 10000, 100),
    'gender': np.random.choice(['Male', 'Female'], 100),
    'category': np.random.choice(['High', 'Medium', 'Low'], 100, p=[0.2, 0.5, 0.3])
})

# 绘制客户分布
plt.figure(figsize=(12, 8))
sns.jointplot(x='income', y='spending', data=customer_data, hue='gender')
plt.suptitle('客户收入与支出分布', y=1.02)
plt.savefig('customer_analysis.png')
plt.show()
print("客户分析图已保存为 customer_analysis.png")

# 5.3 相关性分析
print("\n5.3 相关性分析")
# 计算相关矩阵
corr_matrix = customer_data[['age', 'income', 'spending']].corr()

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('客户数据相关性分析')
plt.savefig('correlation_heatmap.png')
plt.show()
print("相关性分析图已保存为 correlation_heatmap.png")

# 5.4 多子图分析
print("\n5.4 多子图分析")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 第一个子图：年龄分布
sns.histplot(customer_data['age'], ax=axes[0, 0], kde=True)
axes[0, 0].set_title('年龄分布')

# 第二个子图：收入分布
sns.histplot(customer_data['income'], ax=axes[0, 1], kde=True)
axes[0, 1].set_title('收入分布')

# 第三个子图：支出分布
sns.histplot(customer_data['spending'], ax=axes[1, 0], kde=True)
axes[1, 0].set_title('支出分布')

# 第四个子图：性别分布
sns.countplot(x='gender', data=customer_data, ax=axes[1, 1])
axes[1, 1].set_title('性别分布')

plt.tight_layout()
plt.savefig('customer_distributions.png')
plt.show()
print("客户分布分析图已保存为 customer_distributions.png")

print("\nSeaborn基础练习完成！")
