#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 29: 数据分析流程

本文件包含完整数据分析流程的练习代码，涵盖从数据获取到结果报告的全流程

数据分析流程包括：
1. 数据获取 - 从各种来源获取数据
2. 数据探索 - 了解数据的基本特征
3. 数据清洗 - 处理缺失值和异常值
4. 特征工程 - 创建和转换特征
5. 数据分析 - 进行统计分析和可视化
6. 数据建模 - 构建预测模型
7. 结果可视化 - 展示分析结果
8. 报告生成 - 生成分析报告
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据获取
print("=== 1. 数据获取 ===")

# 1.1 从CSV文件读取数据
print("\n1.1 从CSV文件读取数据")
# 创建示例数据
np.random.seed(42)  # 设置随机种子，保证结果可重现
data = pd.DataFrame({
    'customer_id': range(1, 101),  # 客户ID
    'age': np.random.randint(18, 70, 100),  # 年龄，18-70岁
    'gender': np.random.choice(['Male', 'Female'], 100),  # 性别
    'income': np.random.randint(20000, 100000, 100),  # 收入，20000-100000
    'spending_score': np.random.randint(1, 100, 100),  # 支出得分，1-100
    'purchase_frequency': np.random.randint(1, 20, 100),  # 购买频率，1-20次
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], 100),  # 产品类别
    'region': np.random.choice(['North', 'South', 'East', 'West'], 100)  # 地区
})

# 保存为CSV文件
csv_path = os.path.join(current_dir, 'customer_data.csv')
data.to_csv(csv_path, index=False)  # index=False 不保存索引列
print(f"数据已保存为 {csv_path}")

# 读取CSV文件
df = pd.read_csv(csv_path)
print(f"\n数据形状: {df.shape}")  # 输出数据的行数和列数
print(f"数据前5行:\n{df.head()}")  # 查看数据的前5行

# 2. 数据探索
print("\n=== 2. 数据探索 ===")

# 2.1 基本信息
print("\n2.1 基本信息")
print(f"数据类型:\n{df.dtypes}")  # 查看各列的数据类型
print(f"\n数据描述性统计:\n{df.describe()}")  # 查看数值型数据的统计信息
print(f"\n缺失值情况:\n{df.isnull().sum()}")  # 检查各列的缺失值数量

# 2.2 数据分布
print("\n2.2 数据分布")
# 数值型变量分布
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns  # 选择数值型列
for col in numeric_cols:
    plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
    sns.histplot(df[col], kde=True)  # 绘制直方图，kde=True 添加核密度估计
    plt.title(f'{col} 分布')  # 设置图表标题
    plot_path = os.path.join(current_dir, f'{col}_distribution.png')  # 保存路径
    plt.savefig(plot_path)  # 保存图表
    plt.close()  # 关闭图表，避免内存占用
print("数值型变量分布图已保存")

# 分类型变量分布
categorical_cols = df.select_dtypes(include=['object']).columns  # 选择分类型列
for col in categorical_cols:
    plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
    sns.countplot(x=col, data=df)  # 绘制计数图
    plt.title(f'{col} 分布')  # 设置图表标题
    plt.xticks(rotation=45)  # 旋转x轴标签，避免重叠
    plot_path = os.path.join(current_dir, f'{col}_distribution.png')  # 保存路径
    plt.savefig(plot_path)  # 保存图表
    plt.close()  # 关闭图表
print("分类型变量分布图已保存")

# 2.3 相关性分析
print("\n2.3 相关性分析")
corr_matrix = df[numeric_cols].corr()  # 计算数值型变量的相关系数矩阵
plt.figure(figsize=(10, 8))  # 创建10x8英寸的图表
# 绘制热力图，annot=True 显示相关系数值，cmap='coolwarm' 使用红蓝渐变颜色
# cmap颜色说明：红色表示正相关，蓝色表示负相关，颜色深浅表示相关程度
# 数值范围：-1（完全负相关）到 1（完全正相关）
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('相关性矩阵')  # 设置图表标题
plot_path = os.path.join(current_dir, 'correlation_matrix.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表
print("相关性矩阵图已保存")

# 3. 数据清洗
print("\n=== 3. 数据清洗 ===")

# 3.1 处理缺失值
print("\n3.1 处理缺失值")
# 模拟添加缺失值
df_with_missing = df.copy()  # 创建数据副本
# 随机选择10行，将income列设为NaN
# np.nan 表示缺失值，在pandas中用于表示缺失数据
df_with_missing.loc[np.random.choice(df.index, 10), 'income'] = np.nan
# 随机选择5行，将spending_score列设为NaN
df_with_missing.loc[np.random.choice(df.index, 5), 'spending_score'] = np.nan
print(f"添加缺失值后:\n{df_with_missing.isnull().sum()}")  # 查看各列的缺失值数量

# 填充缺失值
df_clean = df_with_missing.copy()  # 创建数据副本
# 使用中位数填充income列的缺失值（中位数对异常值不敏感）
df_clean['income'] = df_clean['income'].fillna(df_clean['income'].median())
# 使用均值填充spending_score列的缺失值
df_clean['spending_score'] = df_clean['spending_score'].fillna(df_clean['spending_score'].mean())
print(f"\n填充缺失值后:\n{df_clean.isnull().sum()}")  # 再次检查缺失值

# 3.2 处理异常值
print("\n3.2 处理异常值")
# 模拟添加异常值
df_with_outliers = df_clean.copy()  # 创建数据副本
# 随机选择5行，将income值乘以3，模拟异常值
df_with_outliers.loc[np.random.choice(df.index, 5), 'income'] = df_with_outliers['income'] * 3

# 使用IQR方法检测异常值
# IQR (Interquartile Range) 四分位距方法：
# Q1 = 25%分位数，Q3 = 75%分位数
# 异常值定义为：小于 Q1 - 1.5*IQR 或 大于 Q3 + 1.5*IQR
Q1 = df_with_outliers['income'].quantile(0.25)  # 第一四分位数
Q3 = df_with_outliers['income'].quantile(0.75)  # 第三四分位数
IQR = Q3 - Q1  # 四分位距
lower_bound = Q1 - 1.5 * IQR  # 异常值下界
upper_bound = Q3 + 1.5 * IQR  # 异常值上界

# 筛选出异常值
outliers = df_with_outliers[(df_with_outliers['income'] < lower_bound) | (df_with_outliers['income'] > upper_bound)]
print(f"异常值数量: {len(outliers)}")  # 异常值数量
print(f"异常值:\n{outliers}")  # 显示异常值

# 处理异常值（替换为中位数）
# 使用np.where函数：如果income是异常值，则替换为中位数，否则保持原值
df_clean['income'] = np.where((df_with_outliers['income'] < lower_bound) | (df_with_outliers['income'] > upper_bound), 
                             df_with_outliers['income'].median(), 
                             df_with_outliers['income'])

# 3.3 数据类型转换
print("\n3.3 数据类型转换")
# 将分类型变量转换为category类型，节省内存并提高性能
df_clean['gender'] = df_clean['gender'].astype('category')
df_clean['product_category'] = df_clean['product_category'].astype('category')
df_clean['region'] = df_clean['region'].astype('category')
print(f"转换后的数据类型:\n{df_clean.dtypes}")  # 查看转换后的数据类型

# 4. 特征工程
print("\n=== 4. 特征工程 ===")

# 4.1 特征创建
print("\n4.1 特征创建")
# 创建新特征
# 收入与年龄的比值，反映收入水平相对于年龄的情况
df_clean['income_per_age'] = df_clean['income'] / df_clean['age']
# 支出得分与购买频率的比值，反映每次购买的平均支出水平
df_clean['spending_per_frequency'] = df_clean['spending_score'] / df_clean['purchase_frequency']

# 创建年龄分组
# pd.cut() 用于将连续变量分割为离散的区间
# bins: 分割点，labels: 每个区间的标签
df_clean['age_group'] = pd.cut(df_clean['age'], bins=[18, 30, 45, 60, 70], 
                               labels=['18-30', '31-45', '46-60', '61-70'])

# 创建收入分组
df_clean['income_group'] = pd.cut(df_clean['income'], bins=[20000, 40000, 60000, 80000, 100000], 
                                 labels=['Low', 'Medium', 'High', 'Very High'])

print(f"\n添加新特征后:\n{df_clean.head()}")  # 查看添加新特征后的数据

# 4.2 特征编码
print("\n4.2 特征编码")
# 独热编码（One-Hot Encoding）
# 将分类型变量转换为数值型变量，每个类别创建一个二进制列
# columns: 需要编码的列名
encoded_df = pd.get_dummies(df_clean, columns=['gender', 'product_category', 'region', 'age_group', 'income_group'])
print(f"\n独热编码后的数据形状: {encoded_df.shape}")  # 查看编码后的数据形状
print(f"独热编码后的数据前5行:\n{encoded_df.head()}")  # 查看编码后的数据

# 5. 数据分析
print("\n=== 5. 数据分析 ===")

# 5.1 描述性分析
print("\n5.1 描述性分析")
# 按性别分析
# groupby('gender'): 按性别分组
# agg(): 聚合函数，计算每个分组的均值
# 字典中的键是要聚合的列，值是聚合函数
gender_analysis = df_clean.groupby('gender').agg({
    'income': 'mean',  # 平均收入
    'spending_score': 'mean',  # 平均支出得分
    'purchase_frequency': 'mean'  # 平均购买频率
})
print(f"按性别分析:\n{gender_analysis}")  # 显示分析结果

# 按地区分析
region_analysis = df_clean.groupby('region').agg({
    'income': 'mean',  # 平均收入
    'spending_score': 'mean',  # 平均支出得分
    'purchase_frequency': 'mean'  # 平均购买频率
})
print(f"\n按地区分析:\n{region_analysis}")  # 显示分析结果

# 按产品类别分析
category_analysis = df_clean.groupby('product_category').agg({
    'income': 'mean',  # 平均收入
    'spending_score': 'mean',  # 平均支出得分
    'purchase_frequency': 'mean'  # 平均购买频率
})
print(f"\n按产品类别分析:\n{category_analysis}")  # 显示分析结果

# 5.2 可视化分析
print("\n5.2 可视化分析")
# 性别与支出关系
plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
# 箱线图：展示数据的分布情况，包括中位数、四分位数、异常值等
sns.boxplot(x='gender', y='spending_score', data=df_clean)
plt.title('性别与支出关系')  # 设置图表标题
plot_path = os.path.join(current_dir, 'gender_spending.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 地区与收入关系
plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
# 柱状图：展示不同类别的数值大小
sns.barplot(x='region', y='income', data=df_clean)
plt.title('地区与收入关系')  # 设置图表标题
plot_path = os.path.join(current_dir, 'region_income.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 年龄与支出关系
plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
# 散点图：展示两个变量之间的关系
sns.scatterplot(x='age', y='spending_score', data=df_clean, hue='gender')  # hue='gender' 按性别着色
plt.title('年龄与支出关系')  # 设置图表标题
plot_path = os.path.join(current_dir, 'age_spending.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 产品类别与购买频率关系
plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
# 柱状图：展示不同产品类别的购买频率
sns.barplot(x='product_category', y='purchase_frequency', data=df_clean)
plt.title('产品类别与购买频率关系')  # 设置图表标题
plot_path = os.path.join(current_dir, 'category_frequency.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 6. 数据建模
print("\n=== 6. 数据建模 ===")

# 6.1 准备建模数据
print("\n6.1 准备建模数据")
from sklearn.model_selection import train_test_split  # 用于划分训练集和测试集
from sklearn.preprocessing import StandardScaler  # 用于特征标准化

# 选择特征和目标变量
# X: 特征变量，包含除了customer_id和spending_score之外的所有列
# y: 目标变量，即spending_score（支出得分）
X = encoded_df.drop(['customer_id', 'spending_score'], axis=1)
y = encoded_df['spending_score']

# 划分训练集和测试集
# test_size=0.2: 测试集占20%，训练集占80%
# random_state=42: 设置随机种子，保证结果可重现
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"训练集大小: {X_train.shape}")  # 训练集的形状
print(f"测试集大小: {X_test.shape}")  # 测试集的形状

# 特征标准化
# StandardScaler: 将特征转换为均值为0，标准差为1的分布
# fit_transform: 拟合并转换训练集
# transform: 使用训练集的参数转换测试集
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6.2 模型训练
print("\n6.2 模型训练")
from sklearn.linear_model import LinearRegression  # 线性回归模型
from sklearn.ensemble import RandomForestRegressor  # 随机森林回归模型
from sklearn.metrics import mean_squared_error, r2_score  # 评估指标

# 线性回归模型
lr_model = LinearRegression()  # 创建线性回归模型实例
lr_model.fit(X_train_scaled, y_train)  # 训练模型
y_pred_lr = lr_model.predict(X_test_scaled)  # 预测测试集
lr_mse = mean_squared_error(y_test, y_pred_lr)  # 计算均方误差（MSE）
lr_r2 = r2_score(y_test, y_pred_lr)  # 计算R²评分
print(f"线性回归模型 - MSE: {lr_mse:.2f}, R2: {lr_r2:.2f}")  # 显示模型性能

# 随机森林模型
# n_estimators=100: 使用100棵决策树
# random_state=42: 设置随机种子，保证结果可重现
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)  # 训练模型
y_pred_rf = rf_model.predict(X_test_scaled)  # 预测测试集
rf_mse = mean_squared_error(y_test, y_pred_rf)  # 计算均方误差（MSE）
rf_r2 = r2_score(y_test, y_pred_rf)  # 计算R²评分
print(f"随机森林模型 - MSE: {rf_mse:.2f}, R2: {rf_r2:.2f}")  # 显示模型性能

# 6.3 模型评估
print("\n6.3 模型评估")
# 特征重要性
# 随机森林模型可以计算特征的重要性，帮助理解哪些特征对预测最重要
feature_importances = pd.DataFrame({
    'feature': X.columns,  # 特征名称
    'importance': rf_model.feature_importances_  # 特征重要性得分
}).sort_values('importance', ascending=False)  # 按重要性降序排序

print(f"特征重要性前10名:\n{feature_importances.head(10)}")  # 显示前10个重要特征

# 预测与实际值对比
plt.figure(figsize=(10, 6))  # 创建10x6英寸的图表
plt.scatter(y_test, y_pred_rf)  # 散点图：x轴是实际值，y轴是预测值
# 绘制对角线，表示预测值等于实际值的情况
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('实际值')  # x轴标签
plt.ylabel('预测值')  # y轴标签
plt.title('随机森林模型预测与实际值对比')  # 图表标题
plot_path = os.path.join(current_dir, 'prediction_vs_actual.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 7. 结果可视化
print("\n=== 7. 结果可视化 ===")

# 7.1 客户分群
print("\n7.1 客户分群")
from sklearn.cluster import KMeans  # K-means聚类算法

# 选择用于聚类的特征
# 选择收入、支出得分和购买频率作为聚类特征
cluster_features = df_clean[['income', 'spending_score', 'purchase_frequency']]

# 标准化特征
# 聚类算法对特征的尺度敏感，需要标准化
scaler = StandardScaler()
cluster_features_scaled = scaler.fit_transform(cluster_features)

# K-means聚类
# n_clusters=4: 将数据分为4个聚类
# random_state=42: 设置随机种子，保证结果可重现
kmeans = KMeans(n_clusters=4, random_state=42)
df_clean['cluster'] = kmeans.fit_predict(cluster_features_scaled)  # 预测每个样本的聚类

# 可视化聚类结果
plt.figure(figsize=(12, 8))  # 创建12x8英寸的图表
# 散点图：x轴是收入，y轴是支出得分，hue='cluster' 按聚类着色
sns.scatterplot(x='income', y='spending_score', data=df_clean, hue='cluster', palette='viridis')
plt.title('客户分群结果')  # 图表标题
plot_path = os.path.join(current_dir, 'customer_clusters.png')  # 保存路径
plt.savefig(plot_path)  # 保存图表
plt.close()  # 关闭图表

# 分析每个聚类的特征
# 计算每个聚类的各特征均值
cluster_analysis = df_clean.groupby('cluster').agg({
    'age': 'mean',  # 平均年龄
    'income': 'mean',  # 平均收入
    'spending_score': 'mean',  # 平均支出得分
    'purchase_frequency': 'mean',  # 平均购买频率
    'income_per_age': 'mean',  # 平均收入年龄比
    'spending_per_frequency': 'mean'  # 平均支出频率比
})
print(f"聚类分析:\n{cluster_analysis}")  # 显示聚类分析结果

# 8. 报告生成
print("\n=== 8. 报告生成 ===")

# 8.1 生成HTML报告
print("\n8.1 生成HTML报告")
# 创建HTML报告内容
# 使用f-string格式化字符串，插入分析结果
report_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>客户数据分析报告</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2, h3 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .section {{ margin: 30px 0; }}
        .chart {{ margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>客户数据分析报告</h1>
    
    <div class="section">
        <h2>1. 数据概况</h2>
        <p>数据总量: {df.shape[0]} 条记录</p>
        <p>数据字段: {df.shape[1]} 个字段</p>
    </div>
    
    <div class="section">
        <h2>2. 数据分析结果</h2>
        
        <h3>2.1 性别分析</h3>
        <table>
            <tr>
                <th>性别</th>
                <th>平均收入</th>
                <th>平均支出得分</th>
                <th>平均购买频率</th>
            </tr>
            {''.join([f'<tr><td>{index}</td><td>{row["income"]:.2f}</td><td>{row["spending_score"]:.2f}</td><td>{row["purchase_frequency"]:.2f}</td></tr>' for index, row in gender_analysis.iterrows()])}
        </table>
        
        <h3>2.2 地区分析</h3>
        <table>
            <tr>
                <th>地区</th>
                <th>平均收入</th>
                <th>平均支出得分</th>
                <th>平均购买频率</th>
            </tr>
            {''.join([f'<tr><td>{index}</td><td>{row["income"]:.2f}</td><td>{row["spending_score"]:.2f}</td><td>{row["purchase_frequency"]:.2f}</td></tr>' for index, row in region_analysis.iterrows()])}
        </table>
    </div>
    
    <div class="section">
        <h2>3. 模型性能</h2>
        <table>
            <tr>
                <th>模型</th>
                <th>MSE</th>
                <th>R²</th>
            </tr>
            <tr>
                <td>线性回归</td>
                <td>{lr_mse:.2f}</td>
                <td>{lr_r2:.2f}</td>
            </tr>
            <tr>
                <td>随机森林</td>
                <td>{rf_mse:.2f}</td>
                <td>{rf_r2:.2f}</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <h2>4. 客户分群</h2>
        <table>
            <tr>
                <th>聚类</th>
                <th>平均年龄</th>
                <th>平均收入</th>
                <th>平均支出得分</th>
                <th>平均购买频率</th>
            </tr>
            {''.join([f'<tr><td>{index}</td><td>{row["age"]:.2f}</td><td>{row["income"]:.2f}</td><td>{row["spending_score"]:.2f}</td><td>{row["purchase_frequency"]:.2f}</td></tr>' for index, row in cluster_analysis.iterrows()])}
        </table>
    </div>
    
    <div class="section">
        <h2>5. 结论与建议</h2>
        <ul>
            <li>客户群体可以分为4个不同的聚类，每个聚类具有不同的消费行为特征</li>
            <li>随机森林模型在预测客户支出得分方面表现良好</li>
            <li>收入和购买频率是影响支出得分的重要因素</li>
            <li>建议针对不同聚类的客户制定差异化的营销策略</li>
        </ul>
    </div>
</body>
</html>
"""

# 保存HTML报告
report_path = os.path.join(current_dir, 'customer_analysis_report.html')
with open(report_path, 'w', encoding='utf-8') as f:  # 使用utf-8编码，支持中文
    f.write(report_html)
print(f"HTML报告已生成: {report_path}")

# 9. 清理文件
print("\n=== 9. 清理文件 ===")
# 注意：根据要求，保留生成的文件，所以注释掉清理代码

"""
# 清理生成的文件
files_to_delete = [os.path.join(current_dir, 'customer_data.csv')] + \
                 [os.path.join(current_dir, f'{col}_distribution.png') for col in numeric_cols] + \
                 [os.path.join(current_dir, f'{col}_distribution.png') for col in categorical_cols] + \
                 [os.path.join(current_dir, 'correlation_matrix.png'), \
                  os.path.join(current_dir, 'gender_spending.png'), \
                  os.path.join(current_dir, 'region_income.png'), \
                  os.path.join(current_dir, 'age_spending.png'), \
                  os.path.join(current_dir, 'category_frequency.png'), \
                  os.path.join(current_dir, 'prediction_vs_actual.png'), \
                  os.path.join(current_dir, 'customer_clusters.png')]

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")
"""

print("\n数据分析流程练习完成！")
