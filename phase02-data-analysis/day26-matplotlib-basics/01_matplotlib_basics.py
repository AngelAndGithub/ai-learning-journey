#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 26: Matplotlib基础

本文件包含Matplotlib基础操作的练习代码
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 基本绘图
print("=== 基本绘图 ===")

# 1.1 折线图
print("\n1.1 折线图")
# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('正弦函数')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.savefig('line_plot.png')
plt.show()
print("折线图已保存为 line_plot.png")

# 1.2 散点图
print("\n1.2 散点图")
# 创建数据
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()  # 添加颜色条
plt.title('散点图')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('scatter_plot.png')
plt.show()
print("散点图已保存为 scatter_plot.png")

# 1.3 柱状图
print("\n1.3 柱状图")
# 创建数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 34]

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.title('柱状图')
plt.xlabel('类别')
plt.ylabel('值')
plt.savefig('bar_plot.png')
plt.show()
print("柱状图已保存为 bar_plot.png")

# 1.4 直方图
print("\n1.4 直方图")
# 创建数据
data = np.random.randn(1000)

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='green')
plt.title('直方图')
plt.xlabel('值')
plt.ylabel('频率')
plt.savefig('histogram.png')
plt.show()
print("直方图已保存为 histogram.png")

# 1.5 饼图
print("\n1.5 饼图")
# 创建数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # 突出显示第一个扇形

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # 确保饼图是圆的
plt.title('饼图')
plt.savefig('pie_chart.png')
plt.show()
print("饼图已保存为 pie_chart.png")

# 2. 多子图
print("\n=== 多子图 ===")

# 2.1 网格布局
print("\n2.1 网格布局")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 第一个子图
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('正弦函数')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('sin(x)')

# 第二个子图
y2 = np.cos(x)
axes[0, 1].plot(x, y2, color='red')
axes[0, 1].set_title('余弦函数')
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('cos(x)')

# 第三个子图
data = np.random.randn(1000)
axes[1, 0].hist(data, bins=30, color='green')
axes[1, 0].set_title('直方图')
axes[1, 0].set_xlabel('值')
axes[1, 0].set_ylabel('频率')

# 第四个子图
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 34]
axes[1, 1].bar(categories, values, color='skyblue')
axes[1, 1].set_title('柱状图')
axes[1, 1].set_xlabel('类别')
axes[1, 1].set_ylabel('值')

plt.tight_layout()  # 调整布局
plt.savefig('subplots.png')
plt.show()
print("多子图已保存为 subplots.png")

# 3. 样式和自定义
print("\n=== 样式和自定义 ===")

# 3.1 线条样式
print("\n3.1 线条样式")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)
plt.plot(x, y3, label='tan(x)', color='green', linestyle=':', linewidth=2)
plt.title('三角函数')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 添加图例
plt.grid(True)
plt.savefig('line_styles.png')
plt.show()
print("线条样式图已保存为 line_styles.png")

# 3.2 标记样式
print("\n3.2 标记样式")
x = np.linspace(0, 10, 20)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', markersize=8, markerfacecolor='red', markeredgecolor='blue', linestyle='--')
plt.title('带标记的折线图')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.savefig('markers.png')
plt.show()
print("标记样式图已保存为 markers.png")

# 3.3 文本和注释
print("\n3.3 文本和注释")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('正弦函数')
plt.xlabel('x')
plt.ylabel('sin(x)')

# 添加文本
plt.text(2, 0.5, '局部最大值', fontsize=12, color='red')

# 添加注释
plt.annotate('最小值', xy=(4.7, -1), xytext=(6, -0.5), arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True)
plt.savefig('text_annotation.png')
plt.show()
print("文本和注释图已保存为 text_annotation.png")

# 4. 实际应用示例
print("\n=== 实际应用示例 ===")

# 4.1 数据可视化
print("\n4.1 数据可视化")
# 创建示例数据
dates = pd.date_range('2020-01-01', periods=12, freq='M')
sales = [120, 150, 180, 200, 220, 250, 280, 300, 320, 350, 380, 400]
profits = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

# 绘制销售和利润趋势
plt.figure(figsize=(12, 6))
plt.plot(dates, sales, label='销售额', marker='o')
plt.plot(dates, profits, label='利润', marker='s')
plt.title('2020年销售趋势')
plt.xlabel('月份')
plt.ylabel('金额')
plt.legend()
plt.grid(True)
plt.savefig('sales_trend.png')
plt.show()
print("销售趋势图已保存为 sales_trend.png")

# 4.2 多数据系列柱状图
print("\n4.2 多数据系列柱状图")
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [23, 45, 56, 78, 34]
values2 = [12, 34, 45, 67, 23]

plt.figure(figsize=(10, 6))
bar_width = 0.35
x = np.arange(len(categories))

plt.bar(x - bar_width/2, values1, width=bar_width, label='系列1', color='skyblue')
plt.bar(x + bar_width/2, values2, width=bar_width, label='系列2', color='green')

plt.title('多数据系列柱状图')
plt.xlabel('类别')
plt.ylabel('值')
plt.xticks(x, categories)
plt.legend()
plt.savefig('multiple_bars.png')
plt.show()
print("多数据系列柱状图已保存为 multiple_bars.png")

# 4.3 箱线图
print("\n4.3 箱线图")
# 创建数据
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=['数据1', '数据2', '数据3', '数据4'])
plt.title('箱线图')
plt.xlabel('数据系列')
plt.ylabel('值')
plt.savefig('boxplot.png')
plt.show()
print("箱线图已保存为 boxplot.png")

# 4.4 热力图
print("\n4.4 热力图")
# 创建数据
data = np.random.rand(10, 10)

plt.figure(figsize=(10, 8))
plt.imshow(data, cmap='viridis')
plt.colorbar()
plt.title('热力图')
plt.savefig('heatmap.png')
plt.show()
print("热力图已保存为 heatmap.png")

# 5. 保存和导出
print("\n=== 保存和导出 ===")

# 5.1 不同格式保存
print("\n5.1 不同格式保存")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('正弦函数')

# 保存为不同格式
plt.savefig('sin_function.png', dpi=100, bbox_inches='tight')
plt.savefig('sin_function.pdf', bbox_inches='tight')
plt.savefig('sin_function.svg', bbox_inches='tight')
plt.close()
print("图表已保存为多种格式")

print("\nMatplotlib基础练习完成！")
