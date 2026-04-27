#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 33: 数据可视化

本文件包含数据可视化的练习代码
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据准备
print("=== 1. 数据准备 ===")
np.random.seed(42)

# 创建示例数据
data = {
    'date': pd.date_range('2020-01-01', periods=12, freq='M'),
    'sales': np.random.randint(1000, 5000, 12),
    'revenue': np.random.randint(50000, 200000, 12),
    'profit': np.random.randint(5000, 50000, 12),
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home']
}

# 转换为DataFrame
df = pd.DataFrame(data)
print(f"数据形状: {df.shape}")
print(f"数据前5行:\n{df.head()}")

# 2. Matplotlib可视化
print("\n=== 2. Matplotlib可视化 ===")

# 2.1 折线图
print("\n2.1 折线图")
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['sales'], marker='o', label='销售额')
plt.plot(df['date'], df['profit'], marker='s', label='利润')
plt.title('销售趋势')
plt.xlabel('日期')
plt.ylabel('金额')
plt.legend()
plt.grid(True)
plt.savefig('matplotlib_line.png')
plt.show()
print("Matplotlib折线图已保存为 matplotlib_line.png")

# 2.2 柱状图
print("\n2.2 柱状图")
plt.figure(figsize=(12, 6))
x = np.arange(len(df['region'].unique()))
width = 0.35

# 按地区分组数据
region_data = df.groupby('region')['sales'].sum()

plt.bar(x, region_data.values, width, label='销售额')
plt.xticks(x, region_data.index)
plt.title('各地区销售额')
plt.xlabel('地区')
plt.ylabel('销售额')
plt.legend()
plt.savefig('matplotlib_bar.png')
plt.show()
print("Matplotlib柱状图已保存为 matplotlib_bar.png")

# 2.3 饼图
print("\n2.3 饼图")
plt.figure(figsize=(8, 8))
product_data = df.groupby('product')['sales'].sum()
plt.pie(product_data.values, labels=product_data.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('各产品销售额占比')
plt.savefig('matplotlib_pie.png')
plt.show()
print("Matplotlib饼图已保存为 matplotlib_pie.png")

# 3. Seaborn可视化
print("\n=== 3. Seaborn可视化 ===")

# 3.1 箱线图
print("\n3.1 箱线图")
plt.figure(figsize=(12, 6))
sns.boxplot(x='region', y='sales', data=df, hue='product')
plt.title('各地区各产品销售额分布')
plt.savefig('seaborn_boxplot.png')
plt.show()
print("Seaborn箱线图已保存为 seaborn_boxplot.png")

# 3.2 小提琴图
print("\n3.2 小提琴图")
plt.figure(figsize=(12, 6))
sns.violinplot(x='category', y='revenue', data=df)
plt.title('各类别收入分布')
plt.savefig('seaborn_violin.png')
plt.show()
print("Seaborn小提琴图已保存为 seaborn_violin.png")

# 3.3 热力图
print("\n3.3 热力图")
# 创建相关性矩阵
corr_matrix = df[['sales', 'revenue', 'profit']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('相关性热力图')
plt.savefig('seaborn_heatmap.png')
plt.show()
print("Seaborn热力图已保存为 seaborn_heatmap.png")

# 3.4 散点图
print("\n3.4 散点图")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sales', y='profit', data=df, hue='region', size='revenue')
plt.title('销售额与利润关系')
plt.savefig('seaborn_scatter.png')
plt.show()
print("Seaborn散点图已保存为 seaborn_scatter.png")

# 4. Plotly可视化
print("\n=== 4. Plotly可视化 ===")

# 4.1 交互式折线图
print("\n4.1 交互式折线图")
fig = px.line(df, x='date', y='sales', color='region', title='各地区销售趋势')
fig.write_html('plotly_line.html')
print("Plotly交互式折线图已保存为 plotly_line.html")

# 4.2 交互式柱状图
print("\n4.2 交互式柱状图")
fig = px.bar(df, x='product', y='sales', color='category', barmode='group', title='各产品销售额')
fig.write_html('plotly_bar.html')
print("Plotly交互式柱状图已保存为 plotly_bar.html")

# 4.3 交互式散点图
print("\n4.3 交互式散点图")
fig = px.scatter(df, x='sales', y='profit', color='region', size='revenue', hover_data=['product'], title='销售额与利润关系')
fig.write_html('plotly_scatter.html')
print("Plotly交互式散点图已保存为 plotly_scatter.html")

# 4.4 交互式饼图
print("\n4.4 交互式饼图")
fig = px.pie(df, values='sales', names='category', title='各类别销售额占比')
fig.write_html('plotly_pie.html')
print("Plotly交互式饼图已保存为 plotly_pie.html")

# 4.5 子图
print("\n4.5 子图")
fig = make_subplots(rows=2, cols=2, subplot_titles=('销售额趋势', '利润趋势', '各地区销售额', '各产品销售额'))

# 销售额趋势
fig.add_trace(go.Scatter(x=df['date'], y=df['sales'], mode='lines+markers', name='销售额'), row=1, col=1)

# 利润趋势
fig.add_trace(go.Scatter(x=df['date'], y=df['profit'], mode='lines+markers', name='利润'), row=1, col=2)

# 各地区销售额
region_sales = df.groupby('region')['sales'].sum().reset_index()
fig.add_trace(go.Bar(x=region_sales['region'], y=region_sales['sales'], name='地区销售额'), row=2, col=1)

# 各产品销售额
product_sales = df.groupby('product')['sales'].sum().reset_index()
fig.add_trace(go.Bar(x=product_sales['product'], y=product_sales['sales'], name='产品销售额'), row=2, col=2)

fig.update_layout(height=600, width=1000, title_text="销售数据分析")
fig.write_html('plotly_subplots.html')
print("Plotly子图已保存为 plotly_subplots.html")

# 5. 实际应用示例
print("\n=== 5. 实际应用示例 ===")

# 5.1 销售数据分析
print("\n5.1 销售数据分析")

# 创建更复杂的销售数据
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=365, freq='D')
sales_data = pd.DataFrame({
    'date': dates,
    'sales': np.random.normal(2000, 500, 365).astype(int),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 365),
    'product': np.random.choice(['A', 'B', 'C', 'D'], 365)
})

# 按月汇总
sales_monthly = sales_data.resample('M', on='date').sum().reset_index()
sales_monthly['month'] = sales_monthly['date'].dt.strftime('%Y-%m')

# 按地区和产品汇总
sales_region_product = sales_data.groupby(['region', 'product'])['sales'].sum().reset_index()

# 可视化
plt.figure(figsize=(14, 10))

# 月度销售趋势
plt.subplot(2, 2, 1)
plt.plot(sales_monthly['month'], sales_monthly['sales'], marker='o')
plt.title('月度销售趋势')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.xticks(rotation=45)

# 地区销售分布
plt.subplot(2, 2, 2)
region_totals = sales_data.groupby('region')['sales'].sum()
plt.pie(region_totals.values, labels=region_totals.index, autopct='%1.1f%%')
plt.title('地区销售分布')
plt.axis('equal')

# 产品销售分布
plt.subplot(2, 2, 3)
product_totals = sales_data.groupby('product')['sales'].sum()
plt.bar(product_totals.index, product_totals.values)
plt.title('产品销售分布')
plt.xlabel('产品')
plt.ylabel('销售额')

# 地区-产品销售热力图
plt.subplot(2, 2, 4)
pivot_data = sales_region_product.pivot(index='region', columns='product', values='sales')
sns.heatmap(pivot_data, annot=True, cmap='viridis')
plt.title('地区-产品销售热力图')

plt.tight_layout()
plt.savefig('sales_analysis.png')
plt.show()
print("销售数据分析图已保存为 sales_analysis.png")

# 5.2 客户数据分析
print("\n5.2 客户数据分析")

# 创建客户数据
customer_data = pd.DataFrame({
    'age': np.random.randint(18, 70, 200),
    'income': np.random.normal(50000, 15000, 200).astype(int),
    'spending': np.random.normal(5000, 1500, 200).astype(int),
    'gender': np.random.choice(['Male', 'Female'], 200),
    'category': np.random.choice(['High Value', 'Medium Value', 'Low Value'], 200, p=[0.2, 0.5, 0.3])
})

# 可视化
plt.figure(figsize=(14, 10))

# 年龄分布
plt.subplot(2, 2, 1)
sns.histplot(customer_data['age'], kde=True)
plt.title('客户年龄分布')
plt.xlabel('年龄')
plt.ylabel('频率')

# 收入与支出关系
plt.subplot(2, 2, 2)
sns.scatterplot(x='income', y='spending', data=customer_data, hue='gender')
plt.title('收入与支出关系')
plt.xlabel('收入')
plt.ylabel('支出')

# 不同类别的支出分布
plt.subplot(2, 2, 3)
sns.boxplot(x='category', y='spending', data=customer_data)
plt.title('不同类别客户的支出分布')
plt.xlabel('客户类别')
plt.ylabel('支出')

# 性别与类别分布
plt.subplot(2, 2, 4)
sns.countplot(x='category', data=customer_data, hue='gender')
plt.title('性别与客户类别分布')
plt.xlabel('客户类别')
plt.ylabel('数量')

plt.tight_layout()
plt.savefig('customer_analysis.png')
plt.show()
print("客户数据分析图已保存为 customer_analysis.png")

# 6. 可视化最佳实践
print("\n=== 6. 可视化最佳实践 ===")
print("1. 选择合适的图表类型")
print("   - 趋势：折线图")
print("   - 比较：柱状图、箱线图")
print("   - 分布：直方图、小提琴图")
print("   - 关系：散点图、热力图")
print("   - 占比：饼图、环形图")
print("2. 保持图表简洁清晰")
print("   - 使用适当的标题和标签")
print("   - 选择合适的颜色方案")
print("   - 避免过度装饰")
print("3. 考虑数据量和复杂度")
print("   - 大数据集使用聚合数据")
print("   - 复杂数据使用交互式图表")
print("4. 确保图表可读性")
print("   - 使用适当的字体大小")
print("   - 避免拥挤的布局")
print("   - 使用图例和注释")
print("5. 考虑受众和使用场景")
print("   - 专业报告使用静态图表")
print("   - 交互式展示使用动态图表")

# 7. 清理文件
print("\n=== 7. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['matplotlib_line.png', 'matplotlib_bar.png', 'matplotlib_pie.png',
                   'seaborn_boxplot.png', 'seaborn_violin.png', 'seaborn_heatmap.png', 'seaborn_scatter.png',
                   'plotly_line.html', 'plotly_bar.html', 'plotly_scatter.html', 'plotly_pie.html', 'plotly_subplots.html',
                   'sales_analysis.png', 'customer_analysis.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n数据可视化练习完成！")
