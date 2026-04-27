#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 25: Pandas高级

本文件包含Pandas高级操作的练习代码
"""

import pandas as pd
import numpy as np

# 1. 高级索引和选择
print("=== 高级索引和选择 ===")

# 创建示例数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'age': [25, 30, 35, 40, 28, 32, 38, 45],
    'salary': [50000, 60000, 70000, 80000, 55000, 65000, 75000, 90000],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'London', 'New York', 'Paris', 'Tokyo'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'join_date': pd.date_range('2020-01-01', periods=8, freq='3M')
}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(f"原始数据:\n{df}")

# 1.1 多级索引
print("\n1.1 多级索引")
# 创建多级索引
arrays = [
    ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']
]
index = pd.MultiIndex.from_arrays(arrays, names=('level1', 'level2'))
df_multi = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['value1', 'value2'])
print(f"多级索引数据:\n{df_multi}")

# 多级索引访问
print(f"\n访问level1=A的行:\n{df_multi.loc['A']}")
print(f"\n访问level1=A, level2=X的行:\n{df_multi.loc[('A', 'X')]}")
print(f"\n使用xs访问level2=X的行:\n{df_multi.xs('X', level='level2')}")

# 1.2 高级选择
print("\n1.2 高级选择")
# 使用query方法
print(f"使用query选择年龄大于30的行:\n{df.query('age > 30')}")
query_str = 'salary > 60000 and department == "IT"'
print(f"\n使用query选择工资大于60000且部门为IT的行:\n{df.query(query_str)}")

# 使用isin方法
print(f"\n使用isin选择城市为New York或London的行:\n{df[df['city'].isin(['New York', 'London'])]}")

# 使用between方法
print(f"\n使用between选择年龄在30到40之间的行:\n{df[df['age'].between(30, 40)]}")

# 2. 高级分组和聚合
print("\n=== 高级分组和聚合 ===")

# 2.1 多列分组
print("\n2.1 多列分组")
grouped = df.groupby(['city', 'department'])
print(f"按城市和部门分组的平均工资:\n{grouped['salary'].mean()}")
print(f"\n按城市和部门分组的统计信息:\n{grouped.agg(['mean', 'median', 'std'])}")

# 2.2 自定义聚合函数
print("\n2.2 自定义聚合函数")
def range_func(x):
    return x.max() - x.min()

grouped = df.groupby('city')
print(f"按城市分组的工资范围:\n{grouped['salary'].agg(range_func)}")

# 2.3 多函数聚合
print("\n2.3 多函数聚合")
grouped = df.groupby('department')
agg_result = grouped.agg({
    'age': ['mean', 'median'],
    'salary': ['mean', 'sum', range_func]
})
print(f"按部门分组的多函数聚合:\n{agg_result}")

# 2.4 变换和过滤
print("\n2.4 变换和过滤")
# 使用transform
print(f"\n按部门标准化工资:\n{grouped['salary'].transform(lambda x: (x - x.mean()) / x.std())}")

# 使用filter
def filter_func(x):
    return x['salary'].mean() > 65000

print(f"\n过滤出平均工资大于65000的部门:\n{grouped.filter(filter_func)}")

# 3. 时间序列处理
print("\n=== 时间序列处理 ===")

# 3.1 时间索引
print("\n3.1 时间索引")
# 创建时间序列数据
date_range = pd.date_range('2020-01-01', periods=365, freq='D')
time_series = pd.Series(np.random.randn(365), index=date_range)
print(f"时间序列数据:\n{time_series.head()}")

# 3.2 时间重采样
print("\n3.2 时间重采样")
print(f"按月重采样的均值:\n{time_series.resample('M').mean().head()}")
print(f"\n按季度重采样的总和:\n{time_series.resample('Q').sum().head()}")

# 3.3 移动窗口
print("\n3.3 移动窗口")
print(f"10天移动平均:\n{time_series.rolling(window=10).mean().head(20)}")
print(f"\n20天移动标准差:\n{time_series.rolling(window=20).std().head(30)}")

# 3.4 时间差计算
print("\n3.4 时间差计算")
df['tenure'] = pd.Timestamp.now() - df['join_date']
df['tenure_years'] = df['tenure'].dt.days / 365.25
print(f"计算工作年限:\n{df[['join_date', 'tenure', 'tenure_years']]}")

# 4. 高级数据操作
print("\n=== 高级数据操作 ===")

# 4.1 透视表
print("\n4.1 透视表")
pivot_table = df.pivot_table(values='salary', index='city', columns='department', aggfunc='mean')
print(f"城市和部门的平均工资透视表:\n{pivot_table}")

# 4.2 交叉表
print("\n4.2 交叉表")
cross_tab = pd.crosstab(df['city'], df['department'])
print(f"城市和部门的交叉表:\n{cross_tab}")

# 4.3 合并和连接高级操作
print("\n4.3 合并和连接高级操作")
# 创建两个DataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})
df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value2': [5, 6, 7, 8]
})

# 合并时使用不同的连接键
print(f"DataFrame 1:\n{df1}")
print(f"DataFrame 2:\n{df2}")
print(f"\n内连接:\n{pd.merge(df1, df2, on='key')}")
print(f"\n左连接:\n{pd.merge(df1, df2, on='key', how='left')}")
print(f"\n右连接:\n{pd.merge(df1, df2, on='key', how='right')}")
print(f"\n外连接:\n{pd.merge(df1, df2, on='key', how='outer')}")

# 4.4 重复数据处理
print("\n4.4 重复数据处理")
# 创建含有重复值的数据
df_duplicate = df.append(df.iloc[0:2], ignore_index=False)
print(f"含有重复值的数据:\n{df_duplicate}")
print(f"\n重复值标记:\n{df_duplicate.duplicated()}")
print(f"\n删除重复值后:\n{df_duplicate.drop_duplicates()}")

# 5. 性能优化
print("\n=== 性能优化 ===")

# 5.1 使用适当的数据类型
print("\n5.1 使用适当的数据类型")
print(f"原始数据类型:\n{df.dtypes}")

# 转换为更高效的数据类型
df_optimized = df.copy()
df_optimized['department'] = df_optimized['department'].astype('category')
df_optimized['city'] = df_optimized['city'].astype('category')

print(f"\n优化后的数据类型:\n{df_optimized.dtypes}")
print(f"\n原始数据内存使用: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
print(f"优化后数据内存使用: {df_optimized.memory_usage(deep=True).sum() / 1024:.2f} KB")

# 5.2 使用向量化操作
print("\n5.2 使用向量化操作")
import time

# 创建大数组
time_df = pd.DataFrame({'A': np.random.randn(1000000), 'B': np.random.randn(1000000)})

# 使用循环
start_time = time.time()
result_loop = []
for i in range(len(time_df)):
    result_loop.append(time_df['A'].iloc[i] + time_df['B'].iloc[i])
loop_time = time.time() - start_time
print(f"循环时间: {loop_time:.4f}秒")

# 使用向量化操作
start_time = time.time()
result_vectorized = time_df['A'] + time_df['B']
vectorized_time = time.time() - start_time
print(f"向量化操作时间: {vectorized_time:.4f}秒")
print(f"速度提升: {loop_time / vectorized_time:.2f}倍")

# 5.3 使用query和eval
print("\n5.3 使用query和eval")
# 使用布尔索引
start_time = time.time()
result_bool = time_df[(time_df['A'] > 0) & (time_df['B'] < 0)]
bool_time = time.time() - start_time
print(f"布尔索引时间: {bool_time:.4f}秒")

# 使用query
start_time = time.time()
result_query = time_df.query('A > 0 and B < 0')
query_time = time.time() - start_time
print(f"query时间: {query_time:.4f}秒")

# 6. 实际应用示例
print("\n=== 实际应用示例 ===")

# 6.1 销售数据分析
print("\n6.1 销售数据分析")
# 创建销售数据
sales_data = {
    'date': pd.date_range('2020-01-01', periods=365, freq='D'),
    'product': np.random.choice(['A', 'B', 'C', 'D'], 365),
    'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Garden'], 365),
    'sales': np.random.randint(100, 1000, 365),
    'revenue': np.random.randint(1000, 10000, 365)
}

df_sales = pd.DataFrame(sales_data)
print(f"销售数据:\n{df_sales.head()}")

# 按月汇总销售数据
monthly_sales = df_sales.resample('M', on='date').agg({
    'sales': 'sum',
    'revenue': 'sum'
})
print(f"\n按月汇总销售数据:\n{monthly_sales}")

# 按产品和类别汇总
product_category_sales = df_sales.groupby(['product', 'category']).agg({
    'sales': 'sum',
    'revenue': 'sum'
})
print(f"\n按产品和类别汇总:\n{product_category_sales}")

# 计算每月平均销售额
monthly_avg = df_sales.resample('M', on='date')['sales'].mean()
print(f"\n每月平均销售额:\n{monthly_avg}")

# 6.2 金融数据分析
print("\n6.2 金融数据分析")
# 创建金融数据
financial_data = {
    'date': pd.date_range('2020-01-01', periods=252, freq='B'),
    'stock': np.random.choice(['AAPL', 'MSFT', 'GOOGL', 'AMZN'], 252),
    'price': np.random.randn(252) + 100,
    'volume': np.random.randint(1000000, 10000000, 252)
}

df_financial = pd.DataFrame(financial_data)
print(f"金融数据:\n{df_financial.head()}")

# 计算每日收益率
df_financial['return'] = df_financial.groupby('stock')['price'].pct_change()
print(f"\n计算每日收益率:\n{df_financial.head()}")

# 计算每个股票的平均收益率和波动率
stock_stats = df_financial.groupby('stock').agg({
    'return': ['mean', 'std'],
    'volume': 'mean'
})
print(f"\n股票统计信息:\n{stock_stats}")

# 计算5日移动平均
for stock in df_financial['stock'].unique():
    mask = df_financial['stock'] == stock
    df_financial.loc[mask, '5_day_ma'] = df_financial.loc[mask, 'price'].rolling(window=5).mean()

print(f"\n添加5日移动平均:\n{df_financial.head(10)}")

print("\nPandas高级练习完成！")
