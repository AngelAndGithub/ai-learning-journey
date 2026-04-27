#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 23: Pandas基础

本文件包含Pandas基础操作的练习代码
"""

import pandas as pd
import numpy as np

# 1. Pandas对象创建
print("=== Pandas对象创建 ===")

# 1.1 Series创建
print("\n1.1 Series创建")
# 从列表创建
s1 = pd.Series([1, 2, 3, 4, 5])
print(f"从列表创建的Series:\n{s1}")
print(f"索引: {s1.index}")
print(f"值: {s1.values}")
print(f"数据类型: {s1.dtype}")

# 从字典创建
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(f"\n从字典创建的Series:\n{s2}")

# 从numpy数组创建
s3 = pd.Series(np.array([1, 2, 3, 4, 5]))
print(f"\n从numpy数组创建的Series:\n{s3}")

# 1.2 DataFrame创建
print("\n1.2 DataFrame创建")
# 从字典创建
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'London', 'Paris', 'Tokyo']
}
df1 = pd.DataFrame(data)
print(f"从字典创建的DataFrame:\n{df1}")

# 从列表创建
list_of_lists = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris'],
    ['David', 40, 'Tokyo']
]
df2 = pd.DataFrame(list_of_lists, columns=['name', 'age', 'city'])
print(f"\n从列表创建的DataFrame:\n{df2}")

# 从numpy数组创建
array = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris'],
    ['David', 40, 'Tokyo']
])
df3 = pd.DataFrame(array, columns=['name', 'age', 'city'])
print(f"\n从numpy数组创建的DataFrame:\n{df3}")

# 2. DataFrame基本操作
print("\n=== DataFrame基本操作 ===")

# 2.1 查看数据
print("\n2.1 查看数据")
print(f"前2行:\n{df1.head(2)}")
print(f"\n后2行:\n{df1.tail(2)}")
print(f"\n数据信息:\n{df1.info()}")
print(f"\n数据描述:\n{df1.describe()}")
print(f"\n列名: {df1.columns}")
print(f"\n索引: {df1.index}")
print(f"\n值:\n{df1.values}")

# 2.2 选择数据
print("\n2.2 选择数据")
# 选择列
print(f"选择name列:\n{df1['name']}")
print(f"\n选择name和age列:\n{df1[['name', 'age']]}")

# 选择行（基于标签）
print(f"\n选择索引为0的行:\n{df1.loc[0]}")
print(f"\n选择索引为0到2的行:\n{df1.loc[0:2]}")

# 选择行（基于位置）
print(f"\n选择第0行:\n{df1.iloc[0]}")
print(f"\n选择第0到2行:\n{df1.iloc[0:3]}")

# 选择特定行和列
print(f"\n选择索引为0的行的name列: {df1.loc[0, 'name']}")
print(f"\n选择索引为0到1的行的name和age列:\n{df1.loc[0:1, ['name', 'age']]}")

# 2.3 条件选择
print("\n2.3 条件选择")
print(f"年龄大于30的行:\n{df1[df1['age'] > 30]}")
print(f"\n年龄大于30且城市为Paris的行:\n{df1[(df1['age'] > 30) & (df1['city'] == 'Paris')]}")

# 3. 数据操作
print("\n=== 数据操作 ===")

# 3.1 添加列
print("\n3.1 添加列")
df1['salary'] = [50000, 60000, 70000, 80000]
print(f"添加salary列后:\n{df1}")

# 3.2 修改列
print("\n3.2 修改列")
df1['salary'] = df1['salary'] * 1.1
print(f"修改salary列后:\n{df1}")

# 3.3 删除列
print("\n3.3 删除列")
df1.drop('salary', axis=1, inplace=True)
print(f"删除salary列后:\n{df1}")

# 3.4 添加行
print("\n3.4 添加行")
new_row = {'name': 'Eve', 'age': 28, 'city': 'Berlin'}
df1 = df1.append(new_row, ignore_index=True)
print(f"添加行后:\n{df1}")

# 3.5 删除行
print("\n3.5 删除行")
df1.drop(4, axis=0, inplace=True)
print(f"删除索引为4的行后:\n{df1}")

# 4. 数据处理
print("\n=== 数据处理 ===")

# 4.1 缺失值处理
print("\n4.1 缺失值处理")
# 创建含有缺失值的数据
missing_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, np.nan, 35, 40],
    'city': ['New York', 'London', np.nan, 'Tokyo']
}
df_missing = pd.DataFrame(missing_data)
print(f"含有缺失值的数据:\n{df_missing}")

# 检测缺失值
print(f"\n缺失值检测:\n{df_missing.isnull()}")
print(f"\n每列缺失值数量:\n{df_missing.isnull().sum()}")

# 删除缺失值
print(f"\n删除含有缺失值的行:\n{df_missing.dropna()}")

# 填充缺失值
print(f"\n用均值填充缺失值:\n{df_missing.fillna(df_missing['age'].mean())}")
print(f"\n用指定值填充缺失值:\n{df_missing.fillna('Unknown')}")

# 4.2 重复值处理
print("\n4.2 重复值处理")
# 创建含有重复值的数据
duplicate_data = {
    'name': ['Alice', 'Bob', 'Alice', 'David'],
    'age': [25, 30, 25, 40],
    'city': ['New York', 'London', 'New York', 'Tokyo']
}
df_duplicate = pd.DataFrame(duplicate_data)
print(f"含有重复值的数据:\n{df_duplicate}")

# 检测重复值
print(f"\n重复值检测:\n{df_duplicate.duplicated()}")

# 删除重复值
print(f"\n删除重复值后:\n{df_duplicate.drop_duplicates()}")

# 5. 数据统计
print("\n=== 数据统计 ===")
print(f"年龄均值: {df1['age'].mean()}")
print(f"年龄中位数: {df1['age'].median()}")
print(f"年龄标准差: {df1['age'].std()}")
print(f"年龄最小值: {df1['age'].min()}")
print(f"年龄最大值: {df1['age'].max()}")
print(f"年龄总和: {df1['age'].sum()}")

# 6. 数据排序
print("\n=== 数据排序 ===")
print(f"按年龄升序排序:\n{df1.sort_values('age')}")
print(f"\n按年龄降序排序:\n{df1.sort_values('age', ascending=False)}")
print(f"\n按城市和年龄排序:\n{df1.sort_values(['city', 'age'])}")

# 7. 数据分组
print("\n=== 数据分组 ===")
# 创建分组数据
group_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'age': [25, 30, 35, 40, 28, 32],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'London', 'New York'],
    'salary': [50000, 60000, 70000, 80000, 55000, 65000]
}
df_group = pd.DataFrame(group_data)
print(f"分组数据:\n{df_group}")

# 按城市分组
grouped = df_group.groupby('city')
print(f"\n按城市分组后的均值:\n{grouped.mean()}")
print(f"\n按城市分组后的总和:\n{grouped.sum()}")
print(f"\n按城市分组后的计数:\n{grouped.count()}")

# 8. 数据合并
print("\n=== 数据合并 ===")
# 创建两个DataFrame
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Paris']
})
df2 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'David'],
    'salary': [50000, 60000, 70000],
    'department': ['HR', 'IT', 'Finance']
})
print(f"DataFrame 1:\n{df1}")
print(f"\nDataFrame 2:\n{df2}")

# 内连接
print(f"\n内连接:\n{pd.merge(df1, df2, on='name')}")

# 左连接
print(f"\n左连接:\n{pd.merge(df1, df2, on='name', how='left')}")

# 右连接
print(f"\n右连接:\n{pd.merge(df1, df2, on='name', how='right')}")

# 外连接
print(f"\n外连接:\n{pd.merge(df1, df2, on='name', how='outer')}")

# 9. 数据读写
print("\n=== 数据读写 ===")

# 9.1 写入CSV
print("\n9.1 写入CSV")
df1.to_csv('data.csv', index=False)
print("数据已写入data.csv")

# 9.2 读取CSV
print("\n9.2 读取CSV")
df_read = pd.read_csv('data.csv')
print(f"读取的数据:\n{df_read}")

# 9.3 写入Excel
print("\n9.3 写入Excel")
df1.to_excel('data.xlsx', index=False, sheet_name='Sheet1')
print("数据已写入data.xlsx")

# 9.4 读取Excel
print("\n9.4 读取Excel")
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(f"读取的数据:\n{df_excel}")

# 10. 实际应用示例
print("\n=== 实际应用示例 ===")

# 10.1 数据清洗和预处理
print("\n10.1 数据清洗和预处理")
# 创建示例数据
sample_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, np.nan, 35, 40, 28],
    'salary': [50000, 60000, np.nan, 80000, 55000],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'London']
}
df_sample = pd.DataFrame(sample_data)
print(f"原始数据:\n{df_sample}")

# 清洗数据
print(f"\n清洗后的数据:")
# 填充缺失值
df_clean = df_sample.fillna({
    'age': df_sample['age'].mean(),
    'salary': df_sample['salary'].mean()
})
print(f"\n填充缺失值后:\n{df_clean}")

# 计算新特征
df_clean['salary_per_age'] = df_clean['salary'] / df_clean['age']
print(f"\n添加新特征后:\n{df_clean}")

# 10.2 数据可视化准备
print("\n10.2 数据可视化准备")
print(f"按城市分组的平均薪资:\n{df_clean.groupby('city')['salary'].mean()}")
print(f"\n年龄分布:\n{df_clean['age'].value_counts()}")

# 清理测试文件
import os
for file in ['data.csv', 'data.xlsx']:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除测试文件: {file}")

print("\nPandas基础练习完成！")
