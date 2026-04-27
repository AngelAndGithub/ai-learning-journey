#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 32: 特征工程

本文件包含特征工程的练习代码
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.feature_selection import SelectKBest, f_regression, f_classif
from sklearn.feature_selection import RFE, SelectFromModel
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

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
    'age': np.random.randint(18, 70, 100),
    'gender': np.random.choice(['Male', 'Female'], 100),
    'income': np.random.randint(20000, 100000, 100),
    'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 100),
    'work_experience': np.random.randint(0, 30, 100),
    'distance_from_home': np.random.uniform(1, 50, 100),
    'satisfaction_score': np.random.uniform(1, 10, 100),
    'salary': np.random.randint(30000, 120000, 100),
    'department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 100),
    'job_level': np.random.choice(['Entry', 'Mid', 'Senior', 'Executive'], 100)
}

# 转换为DataFrame
df = pd.DataFrame(data)
print(f"原始数据形状: {df.shape}")
print(f"原始数据前5行:\n{df.head()}")

# 2. 特征创建
print("\n=== 2. 特征创建 ===")

# 2.1 数值特征创建
print("\n2.1 数值特征创建")

# 年龄分组
df['age_group'] = pd.cut(df['age'], bins=[18, 30, 45, 60, 70], 
                         labels=['18-30', '31-45', '46-60', '61-70'])

# 收入分组
df['income_group'] = pd.cut(df['income'], bins=[20000, 40000, 60000, 80000, 100000], 
                           labels=['Low', 'Medium', 'High', 'Very High'])

# 经验年限分组
df['experience_level'] = pd.cut(df['work_experience'], bins=[0, 5, 10, 15, 30], 
                               labels=['Junior', 'Mid', 'Senior', 'Expert'])

# 计算收入与经验的比值
df['income_per_experience'] = df['income'] / (df['work_experience'] + 1)  # +1避免除零

# 计算满意度与距离的关系
df['satisfaction_distance_ratio'] = df['satisfaction_score'] / (df['distance_from_home'] + 1)

print(f"添加新特征后的数据形状: {df.shape}")
print(f"添加新特征后的数据前5行:\n{df.head()}")

# 2.2 交互特征创建
print("\n2.2 交互特征创建")

# 性别与教育水平的交互
df['gender_education'] = df['gender'] + '_' + df['education']

# 部门与职位级别的交互
df['department_level'] = df['department'] + '_' + df['job_level']

# 收入与经验的交互
df['income_experience_interaction'] = df['income'] * df['work_experience']

print(f"添加交互特征后的数据形状: {df.shape}")
print(f"添加交互特征后的数据前5行:\n{df.head()}")

# 3. 特征转换
print("\n=== 3. 特征转换 ===")

# 3.1 数值特征转换
print("\n3.1 数值特征转换")

# 标准化
scaler_standard = StandardScaler()
df['income_standardized'] = scaler_standard.fit_transform(df[['income']])

# 最小-最大归一化
scaler_minmax = MinMaxScaler()
df['income_normalized'] = scaler_minmax.fit_transform(df[['income']])

# 鲁棒归一化
scaler_robust = RobustScaler()
df['income_robust'] = scaler_robust.fit_transform(df[['income']])

# 对数转换
df['income_log'] = np.log(df['income'] + 1)  # +1避免log(0)

# 平方根转换
df['income_sqrt'] = np.sqrt(df['income'])

print(f"数值特征转换后的数据前5行:\n{df[['income', 'income_standardized', 'income_normalized', 'income_robust', 'income_log', 'income_sqrt']].head()}")

# 3.2 类别特征编码
print("\n3.2 类别特征编码")

# 标签编码
label_encoder = LabelEncoder()
df['gender_encoded'] = label_encoder.fit_transform(df['gender'])
df['department_encoded'] = label_encoder.fit_transform(df['department'])

# 序数编码
ordinal_encoder = OrdinalEncoder(categories=[['Entry', 'Mid', 'Senior', 'Executive']])
df['job_level_encoded'] = ordinal_encoder.fit_transform(df[['job_level']]).flatten()

# 独热编码
onehot_encoder = OneHotEncoder(sparse=False, drop='first')
onehot_encoded = onehot_encoder.fit_transform(df[['education']])
onehot_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['education']))
df = pd.concat([df, onehot_df], axis=1)

print(f"类别特征编码后的数据形状: {df.shape}")
print(f"类别特征编码后的数据前5行:\n{df.head()}")

# 4. 特征选择
print("\n=== 4. 特征选择 ===")

# 4.1 基于统计测试的特征选择
print("\n4.1 基于统计测试的特征选择")

# 准备特征和目标变量
X = df.select_dtypes(include=['float64', 'int64'])
y = df['salary']

# 使用SelectKBest选择最好的5个特征
selector = SelectKBest(score_func=f_regression, k=5)
X_selected = selector.fit_transform(X, y)
selected_features = X.columns[selector.get_support()]
print(f"基于统计测试选择的特征: {selected_features.tolist()}")
print(f"特征得分:\n{pd.DataFrame({'Feature': X.columns, 'Score': selector.scores_}).sort_values('Score', ascending=False)")

# 4.2 基于模型的特征选择
print("\n4.2 基于模型的特征选择")

# 使用随机森林选择特征
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# 特征重要性
feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': rf.feature_importances_})
feature_importances = feature_importances.sort_values('Importance', ascending=False)
print(f"基于随机森林的特征重要性:\n{feature_importances}")

# 使用SelectFromModel选择特征
selector = SelectFromModel(rf, threshold='median')
X_selected_model = selector.fit_transform(X, y)
selected_features_model = X.columns[selector.get_support()]
print(f"基于模型选择的特征: {selected_features_model.tolist()}")

# 4.3 递归特征消除
print("\n4.3 递归特征消除")

# 使用RFE选择特征
estimator = LinearRegression()
rfe = RFE(estimator, n_features_to_select=5, step=1)
rfe.fit(X, y)

selected_features_rfe = X.columns[rfe.support_]
print(f"基于RFE选择的特征: {selected_features_rfe.tolist()}")
print(f"RFE特征排名:\n{pd.DataFrame({'Feature': X.columns, 'Rank': rfe.ranking_}).sort_values('Rank')}")

# 5. 特征降维
print("\n=== 5. 特征降维 ===")

# 5.1 主成分分析
print("\n5.1 主成分分析")

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_result = pca.fit_transform(X)
df['pca1'] = pca_result[:, 0]
df['pca2'] = pca_result[:, 1]

print(f"PCA解释方差比: {pca.explained_variance_ratio_}")
print(f"累计解释方差比: {sum(pca.explained_variance_ratio_)}")

# 可视化PCA结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pca1', y='pca2', data=df)
plt.title('PCA降维结果')
plt.savefig('pca_result.png')
plt.show()
print("PCA降维结果图已保存为 pca_result.png")

# 5.2 t-SNE降维
print("\n5.2 t-SNE降维")

from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(X)
df['tsne1'] = tsne_result[:, 0]
df['tsne2'] = tsne_result[:, 1]

# 可视化t-SNE结果
plt.figure(figsize=(10, 6))
sns.scatterplot(x='tsne1', y='tsne2', data=df)
plt.title('t-SNE降维结果')
plt.savefig('tsne_result.png')
plt.show()
print("t-SNE降维结果图已保存为 tsne_result.png")

# 6. 实际应用示例
print("\n=== 6. 实际应用示例 ===")

# 6.1 完整的特征工程流程
print("\n6.1 完整的特征工程流程")

# 步骤1: 数据准备
print("步骤1: 数据准备")
# 我们已经创建了示例数据

# 步骤2: 特征创建
print("\n步骤2: 特征创建")
# 我们已经创建了多个新特征

# 步骤3: 特征转换
print("\n步骤3: 特征转换")
# 我们已经对数值特征进行了标准化和归一化
# 我们已经对类别特征进行了编码

# 步骤4: 特征选择
print("\n步骤4: 特征选择")
# 我们已经使用多种方法选择了重要特征

# 步骤5: 模型训练
print("\n步骤5: 模型训练")

from sklearn.model_selection import train_test_split

# 选择特征
selected_features = ['income', 'work_experience', 'satisfaction_score', 'income_per_experience', 'department_encoded']
X_final = df[selected_features]
y_final = df['salary']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.2, random_state=42)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 评估模型
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"模型性能 - MSE: {mse:.2f}, R²: {r2:.2f}")

# 6.2 特征工程对模型性能的影响
print("\n6.2 特征工程对模型性能的影响")

# 不使用特征工程的模型
X_basic = df[['age', 'income', 'work_experience', 'distance_from_home', 'satisfaction_score']]
y_basic = df['salary']

X_train_basic, X_test_basic, y_train_basic, y_test_basic = train_test_split(X_basic, y_basic, test_size=0.2, random_state=42)

model_basic = LinearRegression()
model_basic.fit(X_train_basic, y_train_basic)
y_pred_basic = model_basic.predict(X_test_basic)
mse_basic = mean_squared_error(y_test_basic, y_pred_basic)
r2_basic = r2_score(y_test_basic, y_pred_basic)

print(f"不使用特征工程的模型性能 - MSE: {mse_basic:.2f}, R²: {r2_basic:.2f}")
print(f"使用特征工程的模型性能 - MSE: {mse:.2f}, R²: {r2:.2f}")
print(f"性能提升 - MSE降低: {((mse_basic - mse) / mse_basic * 100):.2f}%, R²提升: {((r2 - r2_basic) / r2_basic * 100):.2f}%")

# 7. 最佳实践
print("\n=== 7. 最佳实践 ===")
print("1. 了解业务背景，根据业务知识创建有意义的特征")
print("2. 结合多种特征创建方法，如分箱、交互特征等")
print("3. 对不同类型的特征使用合适的转换方法")
print("4. 使用多种特征选择方法，综合考虑特征重要性")
print("5. 评估特征工程对模型性能的影响")
print("6. 记录特征工程的过程和方法")

# 8. 清理文件
print("\n=== 8. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['pca_result.png', 'tsne_result.png']
for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n特征工程练习完成！")
