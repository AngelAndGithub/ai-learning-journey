#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 30: 缺失值处理

本文件包含缺失值处理的练习代码
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 创建含有缺失值的数据集
print("=== 1. 创建含有缺失值的数据集 ===")
np.random.seed(42)

# 创建基本数据
data = {
    'age': np.random.randint(18, 70, 100),
    'income': np.random.randint(20000, 100000, 100),
    'spending_score': np.random.randint(1, 100, 100),
    'purchase_frequency': np.random.randint(1, 20, 100),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], 100),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 100)
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 随机添加缺失值
# 为age列添加10%缺失值
df.loc[np.random.choice(df.index, size=int(len(df)*0.1), replace=False), 'age'] = np.nan

# 为income列添加15%缺失值
df.loc[np.random.choice(df.index, size=int(len(df)*0.15), replace=False), 'income'] = np.nan

# 为spending_score列添加5%缺失值
df.loc[np.random.choice(df.index, size=int(len(df)*0.05), replace=False), 'spending_score'] = np.nan

# 为purchase_frequency列添加8%缺失值
df.loc[np.random.choice(df.index, size=int(len(df)*0.08), replace=False), 'purchase_frequency'] = np.nan

# 为product_category列添加3%缺失值
df.loc[np.random.choice(df.index, size=int(len(df)*0.03), replace=False), 'product_category'] = np.nan

print(f"原始数据集形状: {df.shape}")
print(f"缺失值统计:\n{df.isnull().sum()}")
print(f"\n缺失值百分比:\n{df.isnull().mean() * 100:.2f}%")

# 2. 缺失值可视化
print("\n=== 2. 缺失值可视化 ===")

# 热力图显示缺失值
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('缺失值分布热力图')
plt.savefig('missing_heatmap.png')
plt.show()
print("缺失值热力图已保存为 missing_heatmap.png")

# 条形图显示缺失值
plt.figure(figsize=(10, 6))
df.isnull().sum().plot(kind='bar')
plt.title('各列缺失值数量')
plt.xlabel('列名')
plt.ylabel('缺失值数量')
plt.savefig('missing_bar.png')
plt.show()
print("缺失值条形图已保存为 missing_bar.png")

# 3. 缺失值处理方法
print("\n=== 3. 缺失值处理方法 ===")

# 3.1 删除法
print("\n3.1 删除法")

# 删除含有缺失值的行
df_dropna = df.dropna()
print(f"删除含有缺失值的行后形状: {df_dropna.shape}")
print(f"删除了 {len(df) - len(df_dropna)} 行")

# 删除含有缺失值的列
df_dropna_col = df.dropna(axis=1)
print(f"\n删除含有缺失值的列后形状: {df_dropna_col.shape}")
print(f"删除了 {len(df.columns) - len(df_dropna_col.columns)} 列")

# 删除缺失值超过50%的列
threshold = len(df) * 0.5
df_dropna_threshold = df.dropna(axis=1, thresh=threshold)
print(f"\n删除缺失值超过50%的列后形状: {df_dropna_threshold.shape}")
print(f"删除了 {len(df.columns) - len(df_dropna_threshold.columns)} 列")

# 3.2 均值/中位数/众数填充
print("\n3.2 均值/中位数/众数填充")

# 均值填充
df_mean = df.copy()
for col in df_mean.select_dtypes(include=['float64', 'int64']).columns:
    df_mean[col] = df_mean[col].fillna(df_mean[col].mean())
print(f"均值填充后缺失值数量: {df_mean.isnull().sum().sum()}")

# 中位数填充
df_median = df.copy()
for col in df_median.select_dtypes(include=['float64', 'int64']).columns:
    df_median[col] = df_median[col].fillna(df_median[col].median())
print(f"中位数填充后缺失值数量: {df_median.isnull().sum().sum()}")

# 众数填充
df_mode = df.copy()
for col in df_mode.columns:
    df_mode[col] = df_mode[col].fillna(df_mode[col].mode()[0])
print(f"众数填充后缺失值数量: {df_mode.isnull().sum().sum()}")

# 3.3 前向/后向填充
print("\n3.3 前向/后向填充")

# 前向填充
df_ffill = df.copy()
df_ffill = df_ffill.fillna(method='ffill')
print(f"前向填充后缺失值数量: {df_ffill.isnull().sum().sum()}")

# 后向填充
df_bfill = df.copy()
df_bfill = df_bfill.fillna(method='bfill')
print(f"后向填充后缺失值数量: {df_bfill.isnull().sum().sum()}")

# 3.4 插值填充
print("\n3.4 插值填充")

# 线性插值
df_interpolate = df.copy()
for col in df_interpolate.select_dtypes(include=['float64', 'int64']).columns:
    df_interpolate[col] = df_interpolate[col].interpolate()
print(f"线性插值填充后缺失值数量: {df_interpolate.isnull().sum().sum()}")

# 多项式插值
df_poly = df.copy()
for col in df_poly.select_dtypes(include=['float64', 'int64']).columns:
    df_poly[col] = df_poly[col].interpolate(method='polynomial', order=2)
print(f"多项式插值填充后缺失值数量: {df_poly.isnull().sum().sum()}")

# 3.5 基于模型的填充
print("\n3.5 基于模型的填充")

# SimpleImputer
df_impute = df.copy()
numeric_cols = df_impute.select_dtypes(include=['float64', 'int64']).columns

# 均值填充
imputer_mean = SimpleImputer(strategy='mean')
df_impute[numeric_cols] = imputer_mean.fit_transform(df_impute[numeric_cols])
print(f"SimpleImputer均值填充后缺失值数量: {df_impute.isnull().sum().sum()}")

# KNN填充
df_knn = df.copy()
knn_imputer = KNNImputer(n_neighbors=5)
df_knn[numeric_cols] = knn_imputer.fit_transform(df_knn[numeric_cols])
print(f"KNN填充后缺失值数量: {df_knn.isnull().sum().sum()}")

# 迭代填充
df_iterative = df.copy()
iterative_imputer = IterativeImputer(random_state=42)
df_iterative[numeric_cols] = iterative_imputer.fit_transform(df_iterative[numeric_cols])
print(f"迭代填充后缺失值数量: {df_iterative.isnull().sum().sum()}")

# 3.6 分类变量缺失值处理
print("\n3.6 分类变量缺失值处理")

# 创建新类别
df_category = df.copy()
for col in df_category.select_dtypes(include=['object']).columns:
    df_category[col] = df_category[col].fillna('Unknown')
print(f"分类变量填充为'Unknown'后缺失值数量: {df_category.isnull().sum().sum()}")

# 众数填充分类变量
df_category_mode = df.copy()
for col in df_category_mode.select_dtypes(include=['object']).columns:
    df_category_mode[col] = df_category_mode[col].fillna(df_category_mode[col].mode()[0])
print(f"分类变量众数填充后缺失值数量: {df_category_mode.isnull().sum().sum()}")

# 4. 缺失值处理效果评估
print("\n=== 4. 缺失值处理效果评估 ===")

# 原始数据的描述性统计
print("\n原始数据的描述性统计:")
print(df.describe())

# 不同填充方法的描述性统计
print("\n均值填充后的描述性统计:")
print(df_mean.describe())

print("\n中位数填充后的描述性统计:")
print(df_median.describe())

print("\nKNN填充后的描述性统计:")
print(df_knn.describe())

# 5. 实际应用示例
print("\n=== 5. 实际应用示例 ===")

# 5.1 完整的缺失值处理流程
print("\n5.1 完整的缺失值处理流程")

# 步骤1: 识别缺失值
print("步骤1: 识别缺失值")
missing_stats = df.isnull().sum()
missing_percent = df.isnull().mean() * 100
print(f"缺失值统计:\n{missing_stats}")
print(f"缺失值百分比:\n{missing_percent:.2f}%")

# 步骤2: 根据缺失率选择处理方法
print("\n步骤2: 根据缺失率选择处理方法")

# 创建处理后的DataFrame
df_processed = df.copy()

# 处理数值型变量
numeric_cols = df_processed.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    missing_rate = df_processed[col].isnull().mean()
    if missing_rate < 0.05:
        # 缺失率低，使用KNN填充
        imputer = KNNImputer(n_neighbors=5)
        df_processed[col] = imputer.fit_transform(df_processed[[col]])
    elif missing_rate < 0.2:
        # 缺失率中等，使用中位数填充
        df_processed[col] = df_processed[col].fillna(df_processed[col].median())
    else:
        # 缺失率高，考虑删除或使用其他方法
        print(f"警告: {col}列缺失率较高 ({missing_rate:.2f}%)")

# 处理分类型变量
categorical_cols = df_processed.select_dtypes(include=['object']).columns
for col in categorical_cols:
    missing_rate = df_processed[col].isnull().mean()
    if missing_rate < 0.05:
        # 缺失率低，使用众数填充
        df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0])
    else:
        # 缺失率高，创建新类别
        df_processed[col] = df_processed[col].fillna('Unknown')

print(f"\n处理后缺失值数量: {df_processed.isnull().sum().sum()}")

# 5.2 缺失值处理对模型的影响
print("\n5.2 缺失值处理对模型的影响")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 准备数据
X = df_processed.drop('spending_score', axis=1)
y = df_processed['spending_score']

# 独热编码分类变量
X_encoded = pd.get_dummies(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"模型性能 - MSE: {mse:.2f}, R²: {r2:.2f}")

# 6. 最佳实践
print("\n=== 6. 最佳实践 ===")
print("1. 首先识别缺失值的模式和原因")
print("2. 根据缺失率选择合适的处理方法")
print("3. 对于数值型变量，优先考虑KNN或迭代填充")
print("4. 对于分类型变量，考虑创建新类别或使用众数填充")
print("5. 评估缺失值处理对模型性能的影响")
print("6. 记录缺失值处理的过程和方法")

# 7. 清理文件
print("\n=== 7. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['missing_heatmap.png', 'missing_bar.png']
for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n缺失值处理练习完成！")
