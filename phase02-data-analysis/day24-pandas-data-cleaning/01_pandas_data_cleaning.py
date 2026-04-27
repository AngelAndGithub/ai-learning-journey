#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 24: Pandas数据清洗

本文件包含Pandas数据清洗操作的练习代码
"""

import pandas as pd
import numpy as np

# 1. 数据加载
print("=== 数据加载 ===")

# 创建示例数据
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'age': [25, 30, np.nan, 40, 28, 32, np.nan, 45],
    'salary': [50000, 60000, 70000, np.nan, 55000, 65000, 80000, 90000],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'London', 'New York', 'Paris', 'Tokyo'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'join_date': ['2020-01-01', '2019-03-15', '2018-07-20', '2020-05-10', 
                 '2019-11-05', '2018-09-30', '2020-02-14', '2019-06-20']
}

df = pd.DataFrame(data)
print(f"原始数据:\n{df}")

# 2. 数据探索
print("\n=== 数据探索 ===")
print(f"数据基本信息:\n{df.info()}")
print(f"\n数据统计描述:\n{df.describe()}")
print(f"\n缺失值情况:\n{df.isnull().sum()}")
print(f"\n唯一值情况:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} 个唯一值")

# 3. 缺失值处理
print("\n=== 缺失值处理 ===")

# 3.1 删除缺失值
print("\n3.1 删除缺失值")
print(f"删除所有含有缺失值的行:\n{df.dropna()}")
print(f"\n删除所有值都为缺失值的行:\n{df.dropna(how='all')}")
print(f"\n删除缺失值数量超过2个的行:\n{df.dropna(thresh=6)}")
print(f"\n删除age列含有缺失值的行:\n{df.dropna(subset=['age'])}")

# 3.2 填充缺失值
print("\n3.2 填充缺失值")
# 填充固定值
print(f"用0填充缺失值:\n{df.fillna(0)}")
# 填充均值
print(f"\n用均值填充数值型列的缺失值:\n{df.fillna(df.mean())}")
# 填充中位数
print(f"\n用中位数填充数值型列的缺失值:\n{df.fillna(df.median())}")
# 填充众数
print(f"\n用众数填充缺失值:\n{df.fillna(df.mode().iloc[0])}")
# 前向填充
print(f"\n前向填充缺失值:\n{df.fillna(method='ffill')}")
# 后向填充
print(f"\n后向填充缺失值:\n{df.fillna(method='bfill')}")

# 3.3 插值填充
print("\n3.3 插值填充")
print(f"线性插值填充:\n{df.interpolate()}")
print(f"\n多项式插值填充:\n{df.interpolate(method='polynomial', order=2)}")

# 4. 重复值处理
print("\n=== 重复值处理 ===")

# 创建含有重复值的数据
df_duplicate = df.append(df.iloc[0:2], ignore_index=True)
print(f"含有重复值的数据:\n{df_duplicate}")

# 检测重复值
print(f"\n重复值检测:\n{df_duplicate.duplicated()}")
print(f"\n重复值数量: {df_duplicate.duplicated().sum()}")

# 删除重复值
print(f"\n删除重复值后:\n{df_duplicate.drop_duplicates()}")
print(f"\n基于特定列删除重复值:\n{df_duplicate.drop_duplicates(subset=['name', 'city'])}")
print(f"\n保留最后一个重复值:\n{df_duplicate.drop_duplicates(keep='last')}")

# 5. 异常值处理
print("\n=== 异常值处理 ===")

# 创建含有异常值的数据
df_outlier = df.copy()
df_outlier.loc[0, 'salary'] = 1000000  # 添加异常值
print(f"含有异常值的数据:\n{df_outlier}")

# 5.1 基于统计方法检测异常值
print("\n5.1 基于统计方法检测异常值")
# IQR方法
Q1 = df_outlier['salary'].quantile(0.25)
Q3 = df_outlier['salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"异常值边界: [{lower_bound}, {upper_bound}]")
print(f"异常值:\n{df_outlier[(df_outlier['salary'] < lower_bound) | (df_outlier['salary'] > upper_bound)]}")

# Z-score方法
z_scores = np.abs((df_outlier['salary'] - df_outlier['salary'].mean()) / df_outlier['salary'].std())
print(f"\nZ-score异常值检测:\n{df_outlier[z_scores > 3]}")

# 5.2 异常值处理
print("\n5.2 异常值处理")
# 删除异常值
df_no_outlier = df_outlier[(df_outlier['salary'] >= lower_bound) & (df_outlier['salary'] <= upper_bound)]
print(f"删除异常值后:\n{df_no_outlier}")

# 替换异常值
df_replace_outlier = df_outlier.copy()
df_replace_outlier.loc[(df_replace_outlier['salary'] < lower_bound) | (df_replace_outlier['salary'] > upper_bound), 'salary'] = df_outlier['salary'].median()
print(f"\n替换异常值后:\n{df_replace_outlier}")

# 6. 数据类型转换
print("\n=== 数据类型转换 ===")
print(f"原始数据类型:\n{df.dtypes}")

# 6.1 转换为数值型
print("\n6.1 转换为数值型")
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
print(f"转换后的数据类型:\n{df.dtypes}")

# 6.2 转换为日期型
print("\n6.2 转换为日期型")
df['join_date'] = pd.to_datetime(df['join_date'])
print(f"转换后的数据类型:\n{df.dtypes}")
print(f"\n日期类型数据:\n{df['join_date']}")

# 6.3 转换为分类型
print("\n6.3 转换为分类型")
df['department'] = df['department'].astype('category')
df['city'] = df['city'].astype('category')
print(f"转换后的数据类型:\n{df.dtypes}")

# 7. 文本数据处理
print("\n=== 文本数据处理 ===")

# 创建含有文本数据的DataFrame
text_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com'],
    'address': ['123 Main St, New York', '456 Oak Ave, London', '789 Pine Rd, Paris', '321 Maple Dr, Tokyo', '654 Cedar Ln, London'],
    'phone': ['(123) 456-7890', '44 20 1234 5678', '33 1 2345 6789', '81 3 1234 5678', '44 20 9876 5432']
}
df_text = pd.DataFrame(text_data)
print(f"文本数据:\n{df_text}")

# 7.1 字符串操作
print("\n7.1 字符串操作")
# 转换为大写
print(f"邮箱转换为大写:\n{df_text['email'].str.upper()}")
# 转换为小写
print(f"\n地址转换为小写:\n{df_text['address'].str.lower()}")
# 去除空格
print(f"\n去除姓名两端空格:\n{df_text['name'].str.strip()}")
# 分割字符串
print(f"\n分割地址:\n{df_text['address'].str.split(', ')}")
# 提取城市
print(f"\n提取城市:\n{df_text['address'].str.split(', ').str[1]}")
# 替换字符串
print(f"\n替换邮箱域名:\n{df_text['email'].str.replace('example.com', 'company.com')}")
# 包含子串
print(f"\n包含'London'的地址:\n{df_text[df_text['address'].str.contains('London')]}")
# 以特定字符开头
print(f"\n以'1'开头的电话号码:\n{df_text[df_text['phone'].str.startswith('(')]}")

# 7.2 正则表达式
print("\n7.2 正则表达式")
# 提取数字
print(f"\n提取电话号码中的数字:\n{df_text['phone'].str.extract('(\\d+)', expand=False)}")
# 提取邮箱用户名
print(f"\n提取邮箱用户名:\n{df_text['email'].str.extract('(.*)@', expand=False)}")

# 8. 数据标准化
print("\n=== 数据标准化 ===")

# 8.1  Min-Max标准化
print("\n8.1 Min-Max标准化")
df_normalized = df.copy()
df_normalized['salary_normalized'] = (df['salary'] - df['salary'].min()) / (df['salary'].max() - df['salary'].min())
print(f"Min-Max标准化后:\n{df_normalized[['salary', 'salary_normalized']]}")

# 8.2 Z-score标准化
print("\n8.2 Z-score标准化")
df_normalized['salary_zscore'] = (df['salary'] - df['salary'].mean()) / df['salary'].std()
print(f"Z-score标准化后:\n{df_normalized[['salary', 'salary_zscore']]}")

# 9. 数据集成
print("\n=== 数据集成 ===")

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
df3 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'performance': [85, 90, 75, 80]
})

print(f"DataFrame 1:\n{df1}")
print(f"\nDataFrame 2:\n{df2}")
print(f"\nDataFrame 3:\n{df3}")

# 9.1 合并数据
print("\n9.1 合并数据")
# 合并两个DataFrame
merged = pd.merge(df1, df2, on='name', how='outer')
print(f"合并两个DataFrame:\n{merged}")

# 合并三个DataFrame
merged_all = pd.merge(merged, df3, on='name', how='outer')
print(f"\n合并三个DataFrame:\n{merged_all}")

# 9.2 连接数据
print("\n9.2 连接数据")
# 行连接
concatenated = pd.concat([df1, df2])
print(f"行连接:\n{concatenated}")

# 列连接
concatenated_cols = pd.concat([df1, df2.set_index('name')], axis=1)
print(f"\n列连接:\n{concatenated_cols}")

# 10. 实际应用示例
print("\n=== 实际应用示例 ===")

# 10.1 完整的数据清洗流程
print("\n10.1 完整的数据清洗流程")
# 创建一个更复杂的数据集
complex_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'age': [25, 30, np.nan, 40, 28, 32, np.nan, 45, 35, 29],
    'salary': [50000, 60000, 70000, np.nan, 55000, 65000, 80000, 90000, 75000, 60000],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'London', 'New York', 'Paris', 'Tokyo', 'London', 'New York'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'join_date': ['2020-01-01', '2019-03-15', '2018-07-20', '2020-05-10', 
                 '2019-11-05', '2018-09-30', '2020-02-14', '2019-06-20',
                 '2020-03-10', '2019-12-01'],
    'performance': [85, 90, 75, 80, 88, 92, 79, 83, 87, 91]
}

df_complex = pd.DataFrame(complex_data)
print(f"原始复杂数据:\n{df_complex}")

# 1. 处理缺失值
df_clean = df_complex.copy()
df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())
df_clean['salary'] = df_clean['salary'].fillna(df_clean['salary'].mean())

# 2. 转换数据类型
df_clean['join_date'] = pd.to_datetime(df_clean['join_date'])
df_clean['department'] = df_clean['department'].astype('category')
df_clean['city'] = df_clean['city'].astype('category')

# 3. 检测和处理异常值
salary_Q1 = df_clean['salary'].quantile(0.25)
salary_Q3 = df_clean['salary'].quantile(0.75)
salary_IQR = salary_Q3 - salary_Q1
salary_lower = salary_Q1 - 1.5 * salary_IQR
salary_upper = salary_Q3 + 1.5 * salary_IQR

# 4. 添加新特征
df_clean['tenure_years'] = (pd.Timestamp.now() - df_clean['join_date']).dt.days / 365.25
df_clean['salary_per_age'] = df_clean['salary'] / df_clean['age']

# 5. 数据标准化
df_clean['salary_normalized'] = (df_clean['salary'] - df_clean['salary'].mean()) / df_clean['salary'].std()
df_clean['performance_normalized'] = (df_clean['performance'] - df_clean['performance'].mean()) / df_clean['performance'].std()

print(f"\n清洗后的复杂数据:\n{df_clean}")
print(f"\n清洗后的数据信息:\n{df_clean.info()}")

print("\nPandas数据清洗练习完成！")
