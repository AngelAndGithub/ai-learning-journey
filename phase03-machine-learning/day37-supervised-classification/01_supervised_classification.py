#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 37: 监督学习-分类

本文件包含监督学习分类算法的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, make_classification, load_wine, load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 数据准备
print("=== 1. 数据准备 ===")

# 1.1 加载数据集
print("\n1.1 加载数据集")

# 加载鸢尾花数据集
iris = load_iris()
X_iris, y_iris = iris.data, iris.target
print(f"鸢尾花数据集: X={X_iris.shape}, y={y_iris.shape}")
print(f"类别: {iris.target_names}")

# 加载葡萄酒数据集
wine = load_wine()
X_wine, y_wine = wine.data, wine.target
print(f"\n葡萄酒数据集: X={X_wine.shape}, y={y_wine.shape}")
print(f"类别: {wine.target_names}")

# 加载手写数字数据集
digits = load_digits()
X_digits, y_digits = digits.data, digits.target
print(f"\n手写数字数据集: X={X_digits.shape}, y={y_digits.shape}")
print(f"类别: 0-9")

# 创建二分类数据集
X_binary, y_binary = make_classification(n_samples=1000, n_features=20, n_classes=2, n_informative=10, random_state=42)
print(f"\n二分类数据集: X={X_binary.shape}, y={y_binary.shape}")

# 1.2 数据预处理
print("\n1.2 数据预处理")

# 标准化数据
scaler = StandardScaler()
X_iris_scaled = scaler.fit_transform(X_iris)
X_wine_scaled = scaler.fit_transform(X_wine)
X_digits_scaled = scaler.fit_transform(X_digits)
X_binary_scaled = scaler.fit_transform(X_binary)

# 分割数据
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris_scaled, y_iris, test_size=0.2, random_state=42)
X_train_binary, X_test_binary, y_train_binary, y_test_binary = train_test_split(X_binary_scaled, y_binary, test_size=0.2, random_state=42)

print(f"鸢尾花训练集: {X_train_iris.shape}, 测试集: {X_test_iris.shape}")
print(f"二分类训练集: {X_train_binary.shape}, 测试集: {X_test_binary.shape}")

# 2. 分类算法
print("\n=== 2. 分类算法 ===")

# 2.1 逻辑回归
print("\n2.1 逻辑回归")

lr = LogisticRegression()
lr.fit(X_train_iris, y_train_iris)
y_pred_lr = lr.predict(X_test_iris)

print(f"逻辑回归准确率: {accuracy_score(y_test_iris, y_pred_lr):.4f}")
print(f"逻辑回归F1分数: {f1_score(y_test_iris, y_pred_lr, average='macro'):.4f}")

# 2.2 K近邻
print("\n2.2 K近邻")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_iris, y_train_iris)
y_pred_knn = knn.predict(X_test_iris)

print(f"K近邻准确率: {accuracy_score(y_test_iris, y_pred_knn):.4f}")
print(f"K近邻F1分数: {f1_score(y_test_iris, y_pred_knn, average='macro'):.4f}")

# 2.3 支持向量机
print("\n2.3 支持向量机")

svm = SVC(kernel='rbf', C=1.0, gamma='scale')
svm.fit(X_train_iris, y_train_iris)
y_pred_svm = svm.predict(X_test_iris)

print(f"SVM准确率: {accuracy_score(y_test_iris, y_pred_svm):.4f}")
print(f"SVM F1分数: {f1_score(y_test_iris, y_pred_svm, average='macro'):.4f}")

# 2.4 决策树
print("\n2.4 决策树")

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train_iris, y_train_iris)
y_pred_dt = dt.predict(X_test_iris)

print(f"决策树准确率: {accuracy_score(y_test_iris, y_pred_dt):.4f}")
print(f"决策树F1分数: {f1_score(y_test_iris, y_pred_dt, average='macro'):.4f}")

# 2.5 随机森林
print("\n2.5 随机森林")

rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
rf.fit(X_train_iris, y_train_iris)
y_pred_rf = rf.predict(X_test_iris)

print(f"随机森林准确率: {accuracy_score(y_test_iris, y_pred_rf):.4f}")
print(f"随机森林F1分数: {f1_score(y_test_iris, y_pred_rf, average='macro'):.4f}")

# 2.6 梯度提升
print("\n2.6 梯度提升")

gb = GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=42)
gb.fit(X_train_iris, y_train_iris)
y_pred_gb = gb.predict(X_test_iris)

print(f"梯度提升准确率: {accuracy_score(y_test_iris, y_pred_gb):.4f}")
print(f"梯度提升F1分数: {f1_score(y_test_iris, y_pred_gb, average='macro'):.4f}")

# 2.7 朴素贝叶斯
print("\n2.7 朴素贝叶斯")

gnb = GaussianNB()
gnb.fit(X_train_iris, y_train_iris)
y_pred_gnb = gnb.predict(X_test_iris)

print(f"朴素贝叶斯准确率: {accuracy_score(y_test_iris, y_pred_gnb):.4f}")
print(f"朴素贝叶斯F1分数: {f1_score(y_test_iris, y_pred_gnb, average='macro'):.4f}")

# 2.8 线性判别分析
print("\n2.8 线性判别分析")

lda = LinearDiscriminantAnalysis()
lda.fit(X_train_iris, y_train_iris)
y_pred_lda = lda.predict(X_test_iris)

print(f"LDA准确率: {accuracy_score(y_test_iris, y_pred_lda):.4f}")
print(f"LDA F1分数: {f1_score(y_test_iris, y_pred_lda, average='macro'):.4f}")

# 2.9 二次判别分析
print("\n2.9 二次判别分析")

qda = QuadraticDiscriminantAnalysis()
qda.fit(X_train_iris, y_train_iris)
y_pred_qda = qda.predict(X_test_iris)

print(f"QDA准确率: {accuracy_score(y_test_iris, y_pred_qda):.4f}")
print(f"QDA F1分数: {f1_score(y_test_iris, y_pred_qda, average='macro'):.4f}")

# 3. 模型评估
print("\n=== 3. 模型评估 ===")

# 3.1 详细评估报告
print("\n3.1 详细评估报告")

# 选择最佳模型（以随机森林为例）
best_model = rf
y_pred = y_pred_rf

print("分类报告:")
print(classification_report(y_test_iris, y_pred, target_names=iris.target_names))

# 3.2 混淆矩阵
print("\n3.2 混淆矩阵")

cm = confusion_matrix(y_test_iris, y_pred)
print("混淆矩阵:")
print(cm)

# 可视化混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title('混淆矩阵')
plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.savefig('confusion_matrix.png')
plt.show()
print("混淆矩阵已保存为 confusion_matrix.png")

# 3.3 交叉验证
print("\n3.3 交叉验证")

from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 对所有模型进行交叉验证
models = {
    '逻辑回归': LogisticRegression(),
    'K近邻': KNeighborsClassifier(n_neighbors=5),
    'SVM': SVC(kernel='rbf', C=1.0, gamma='scale'),
    '决策树': DecisionTreeClassifier(max_depth=3, random_state=42),
    '随机森林': RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42),
    '梯度提升': GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=42),
    '朴素贝叶斯': GaussianNB(),
    'LDA': LinearDiscriminantAnalysis(),
    'QDA': QuadraticDiscriminantAnalysis()
}

print("5折交叉验证结果:")
for name, model in models.items():
    scores = cross_val_score(model, X_iris_scaled, y_iris, cv=kf, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")

# 4. 超参数调优
print("\n=== 4. 超参数调优 ===")

from sklearn.model_selection import GridSearchCV

# 以SVM为例进行网格搜索
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1],
    'kernel': ['linear', 'rbf', 'poly']
}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_iris, y_train_iris)

print("SVM最佳参数:")
print(grid_search.best_params_)
print(f"最佳准确率: {grid_search.best_score_:.4f}")

# 5. 特征重要性
print("\n=== 5. 特征重要性 ===")

# 随机森林特征重要性
feature_importance = rf.feature_importances_
feature_names = iris.feature_names

# 排序
indices = np.argsort(feature_importance)[::-1]

print("特征重要性排序:")
for i, idx in enumerate(indices):
    print(f"{i+1}. {feature_names[idx]}: {feature_importance[idx]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importance)), feature_importance[indices])
plt.xticks(range(len(feature_importance)), [feature_names[i] for i in indices], rotation=45)
plt.title('特征重要性')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 6. 二分类示例
print("\n=== 6. 二分类示例 ===")

# 训练模型
models_binary = {
    '逻辑回归': LogisticRegression(),
    'K近邻': KNeighborsClassifier(n_neighbors=5),
    'SVM': SVC(kernel='rbf', C=1.0, gamma='scale'),
    '随机森林': RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
}

print("二分类模型评估:")
for name, model in models_binary.items():
    model.fit(X_train_binary, y_train_binary)
    y_pred = model.predict(X_test_binary)
    accuracy = accuracy_score(y_test_binary, y_pred)
    precision = precision_score(y_test_binary, y_pred)
    recall = recall_score(y_test_binary, y_pred)
    f1 = f1_score(y_test_binary, y_pred)
    print(f"{name}: 准确率={accuracy:.4f}, 精确率={precision:.4f}, 召回率={recall:.4f}, F1={f1:.4f}")

# 7. 多分类示例
print("\n=== 7. 多分类示例 ===")

# 分割手写数字数据集
X_train_digits, X_test_digits, y_train_digits, y_test_digits = train_test_split(X_digits_scaled, y_digits, test_size=0.2, random_state=42)

# 训练模型
model_digits = RandomForestClassifier(n_estimators=100, random_state=42)
model_digits.fit(X_train_digits, y_train_digits)
y_pred_digits = model_digits.predict(X_test_digits)

print(f"手写数字分类准确率: {accuracy_score(y_test_digits, y_pred_digits):.4f}")

# 可视化混淆矩阵
cm_digits = confusion_matrix(y_test_digits, y_pred_digits)
plt.figure(figsize=(10, 8))
sns.heatmap(cm_digits, annot=True, cmap='Blues', fmt='d')
plt.title('手写数字分类混淆矩阵')
plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.savefig('confusion_matrix_digits.png')
plt.show()
print("手写数字混淆矩阵已保存为 confusion_matrix_digits.png")

# 8. 实际应用示例
print("\n=== 8. 实际应用示例 ===")

# 8.1 葡萄酒分类
print("\n8.1 葡萄酒分类")

# 分割葡萄酒数据集
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine_scaled, y_wine, test_size=0.2, random_state=42)

# 训练模型
model_wine = GradientBoostingClassifier(n_estimators=100, random_state=42)
model_wine.fit(X_train_wine, y_train_wine)
y_pred_wine = model_wine.predict(X_test_wine)

print(f"葡萄酒分类准确率: {accuracy_score(y_test_wine, y_pred_wine):.4f}")
print("分类报告:")
print(classification_report(y_test_wine, y_pred_wine, target_names=wine.target_names))

# 9. 分类算法选择指南
print("\n=== 9. 分类算法选择指南 ===")
print("1. 逻辑回归: 适用于线性可分的二分类问题，计算效率高")
print("2. K近邻: 适用于小数据集，对异常值敏感")
print("3. SVM: 适用于高维数据，分类效果好，但参数调优复杂")
print("4. 决策树: 易于理解和解释，可处理非线性关系")
print("5. 随机森林: 适用于大多数问题，鲁棒性强，不易过拟合")
print("6. 梯度提升: 精度高，但训练时间长")
print("7. 朴素贝叶斯: 适用于文本分类，计算效率高")
print("8. LDA/QDA: 适用于线性/非线性可分的问题")

# 10. 清理文件
print("\n=== 10. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['confusion_matrix.png', 'feature_importance.png', 'confusion_matrix_digits.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n监督学习-分类练习完成！")
