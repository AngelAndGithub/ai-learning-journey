#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 31: 异常值检测

本文件包含异常值检测的练习代码
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 创建含有异常值的数据集
print("=== 1. 创建含有异常值的数据集 ===")
np.random.seed(42)

# 创建正常数据
n_samples = 100
X = np.random.randn(n_samples, 2) * 0.3 + np.array([2, 2])

# 添加异常值
n_outliers = 10
outliers = np.random.randn(n_outliers, 2) * 2 + np.array([-2, -2])
X = np.vstack([X, outliers])
y = np.zeros(n_samples + n_outliers, dtype=int)
y[-n_outliers:] = 1  # 异常值标记为1

# 转换为DataFrame
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['label'] = y

print(f"数据集形状: {df.shape}")
print(f"异常值数量: {df['label'].sum()}")

# 2. 可视化数据
print("\n=== 2. 可视化数据 ===")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='feature1', y='feature2', data=df, hue='label', palette='viridis')
plt.title('数据分布（含异常值）')
plt.savefig('data_with_outliers.png')
plt.show()
print("数据分布图已保存为 data_with_outliers.png")

# 3. 统计方法检测异常值
print("\n=== 3. 统计方法检测异常值 ===")

# 3.1 IQR方法
print("\n3.1 IQR方法")

def detect_outliers_iqr(data, column, threshold=1.5):
    """使用IQR方法检测异常值"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# 检测feature1的异常值
outliers_feature1, lower1, upper1 = detect_outliers_iqr(df, 'feature1')
print(f"feature1异常值数量: {len(outliers_feature1)}")
print(f"feature1异常值边界: [{lower1:.2f}, {upper1:.2f}]")

# 检测feature2的异常值
outliers_feature2, lower2, upper2 = detect_outliers_iqr(df, 'feature2')
print(f"\nfeature2异常值数量: {len(outliers_feature2)}")
print(f"feature2异常值边界: [{lower2:.2f}, {upper2:.2f}]")

# 3.2 Z-score方法
print("\n3.2 Z-score方法")

def detect_outliers_zscore(data, column, threshold=3):
    """使用Z-score方法检测异常值"""
    z_scores = np.abs(stats.zscore(data[column]))
    outliers = data[z_scores > threshold]
    return outliers

# 检测feature1的异常值
outliers_zscore1 = detect_outliers_zscore(df, 'feature1')
print(f"feature1 Z-score异常值数量: {len(outliers_zscore1)}")

# 检测feature2的异常值
outliers_zscore2 = detect_outliers_zscore(df, 'feature2')
print(f"feature2 Z-score异常值数量: {len(outliers_zscore2)}")

# 3.3 Modified Z-score方法
print("\n3.3 Modified Z-score方法")

def detect_outliers_modified_zscore(data, column, threshold=3.5):
    """使用Modified Z-score方法检测异常值"""
    median = data[column].median()
    mad = np.median(np.abs(data[column] - median))
    modified_z_scores = 0.6745 * (data[column] - median) / mad
    outliers = data[np.abs(modified_z_scores) > threshold]
    return outliers

# 检测feature1的异常值
outliers_modified1 = detect_outliers_modified_zscore(df, 'feature1')
print(f"feature1 Modified Z-score异常值数量: {len(outliers_modified1)}")

# 检测feature2的异常值
outliers_modified2 = detect_outliers_modified_zscore(df, 'feature2')
print(f"feature2 Modified Z-score异常值数量: {len(outliers_modified2)}")

# 4. 机器学习方法检测异常值
print("\n=== 4. 机器学习方法检测异常值 ===")

# 4.1 隔离森林
print("\n4.1 隔离森林")
isolation_forest = IsolationForest(contamination=0.1, random_state=42)
outliers_if = isolation_forest.fit_predict(X)
df['outlier_if'] = outliers_if
print(f"隔离森林检测到的异常值数量: {len(df[df['outlier_if'] == -1])}")

# 4.2 局部异常因子
print("\n4.2 局部异常因子")
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
outliers_lof = lof.fit_predict(X)
df['outlier_lof'] = outliers_lof
print(f"局部异常因子检测到的异常值数量: {len(df[df['outlier_lof'] == -1])}")

# 4.3 椭圆包络
print("\n4.3 椭圆包络")
eliptic = EllipticEnvelope(contamination=0.1, random_state=42)
outliers_ee = eliptic.fit_predict(X)
df['outlier_ee'] = outliers_ee
print(f"椭圆包络检测到的异常值数量: {len(df[df['outlier_ee'] == -1])}")

# 4.4 单类SVM
print("\n4.4 单类SVM")
onesvm = OneClassSVM(nu=0.1, kernel='rbf', gamma=0.1)
outliers_svm = onesvm.fit_predict(X)
df['outlier_svm'] = outliers_svm
print(f"单类SVM检测到的异常值数量: {len(df[df['outlier_svm'] == -1])}")

# 5. 异常值可视化
print("\n=== 5. 异常值可视化 ===")

# 5.1 IQR方法可视化
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='feature1', data=df)
plt.axhline(y=lower1, color='r', linestyle='--')
plt.axhline(y=upper1, color='r', linestyle='--')
plt.title('feature1 IQR异常值检测')

plt.subplot(1, 2, 2)
sns.boxplot(x='feature2', data=df)
plt.axhline(y=lower2, color='r', linestyle='--')
plt.axhline(y=upper2, color='r', linestyle='--')
plt.title('feature2 IQR异常值检测')

plt.tight_layout()
plt.savefig('iqr_outliers.png')
plt.show()
print("IQR异常值检测图已保存为 iqr_outliers.png")

# 5.2 隔离森林可视化
plt.figure(figsize=(10, 6))
sns.scatterplot(x='feature1', y='feature2', data=df, hue='outlier_if', palette='viridis')
plt.title('隔离森林异常值检测')
plt.savefig('isolation_forest_outliers.png')
plt.show()
print("隔离森林异常值检测图已保存为 isolation_forest_outliers.png")

# 6. 异常值处理
print("\n=== 6. 异常值处理 ===")

# 6.1 删除异常值
print("\n6.1 删除异常值")
df_no_outliers = df[df['outlier_if'] == 1]
print(f"删除异常值前形状: {df.shape}")
print(f"删除异常值后形状: {df_no_outliers.shape}")

# 6.2 替换异常值
print("\n6.2 替换异常值")

# 方法1: 用中位数替换
df_replace_median = df.copy()
for col in ['feature1', 'feature2']:
    median = df[col].median()
    df_replace_median.loc[df['outlier_if'] == -1, col] = median

# 方法2: 用上下边界替换
df_replace_bound = df.copy()
df_replace_bound.loc[df['feature1'] < lower1, 'feature1'] = lower1
df_replace_bound.loc[df['feature1'] > upper1, 'feature1'] = upper1
df_replace_bound.loc[df['feature2'] < lower2, 'feature2'] = lower2
df_replace_bound.loc[df['feature2'] > upper2, 'feature2'] = upper2

print("异常值处理完成")

# 7. 实际应用示例
print("\n=== 7. 实际应用示例 ===")

# 7.1 销售数据异常值检测
print("\n7.1 销售数据异常值检测")

# 创建销售数据
np.random.seed(42)
sales_data = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=100, freq='D'),
    'sales': np.random.normal(1000, 100, 100)
})

# 添加异常值
sales_data.loc[np.random.choice(sales_data.index, 5), 'sales'] = sales_data['sales'] * 3
sales_data.loc[np.random.choice(sales_data.index, 3), 'sales'] = sales_data['sales'] * 0.1

# 检测异常值
outliers_sales, lower_sales, upper_sales = detect_outliers_iqr(sales_data, 'sales')
print(f"销售数据异常值数量: {len(outliers_sales)}")
print(f"销售数据异常值边界: [{lower_sales:.2f}, {upper_sales:.2f}]")

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(sales_data['date'], sales_data['sales'], 'b-', label='销售数据')
plt.scatter(outliers_sales['date'], outliers_sales['sales'], color='r', label='异常值')
plt.axhline(y=lower_sales, color='g', linestyle='--', label='下界')
plt.axhline(y=upper_sales, color='g', linestyle='--', label='上界')
plt.title('销售数据异常值检测')
plt.xlabel('日期')
plt.ylabel('销售额')
plt.legend()
plt.savefig('sales_outliers.png')
plt.show()
print("销售数据异常值检测图已保存为 sales_outliers.png")

# 7.2 客户数据异常值检测
print("\n7.2 客户数据异常值检测")

# 创建客户数据
customer_data = pd.DataFrame({
    'age': np.random.randint(18, 70, 200),
    'income': np.random.normal(50000, 10000, 200),
    'spending': np.random.normal(5000, 1000, 200)
})

# 添加异常值
customer_data.loc[np.random.choice(customer_data.index, 10), 'income'] = customer_data['income'] * 2
customer_data.loc[np.random.choice(customer_data.index, 5), 'spending'] = customer_data['spending'] * 3

# 使用隔离森林检测异常值
X_customer = customer_data[['age', 'income', 'spending']]
isolation_forest = IsolationForest(contamination=0.05, random_state=42)
outliers_customer = isolation_forest.fit_predict(X_customer)
customer_data['outlier'] = outliers_customer

print(f"客户数据异常值数量: {len(customer_data[customer_data['outlier'] == -1])}")

# 可视化
plt.figure(figsize=(12, 8))
ax = plt.axes(projection='3d')
ax.scatter3D(customer_data[customer_data['outlier'] == 1]['age'], 
             customer_data[customer_data['outlier'] == 1]['income'], 
             customer_data[customer_data['outlier'] == 1]['spending'], 
             c='blue', label='正常数据')
ax.scatter3D(customer_data[customer_data['outlier'] == -1]['age'], 
             customer_data[customer_data['outlier'] == -1]['income'], 
             customer_data[customer_data['outlier'] == -1]['spending'], 
             c='red', label='异常值')
ax.set_xlabel('年龄')
ax.set_ylabel('收入')
ax.set_zlabel('支出')
ax.set_title('客户数据异常值检测')
plt.legend()
plt.savefig('customer_outliers.png')
plt.show()
print("客户数据异常值检测图已保存为 customer_outliers.png")

# 8. 最佳实践
print("\n=== 8. 最佳实践 ===")
print("1. 首先可视化数据，了解数据分布")
print("2. 结合多种方法检测异常值")
print("3. 根据业务场景选择合适的异常值处理方法")
print("4. 记录异常值检测和处理的过程")
print("5. 评估异常值处理对模型性能的影响")

# 9. 清理文件
print("\n=== 9. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['data_with_outliers.png', 'iqr_outliers.png', 'isolation_forest_outliers.png', 
                   'sales_outliers.png', 'customer_outliers.png']
for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n异常值检测练习完成！")
