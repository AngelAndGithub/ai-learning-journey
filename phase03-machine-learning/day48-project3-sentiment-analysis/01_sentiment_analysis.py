#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 48: 实战项目3 - 情感分类

本文件包含情感分类的实战项目代码
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import os
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 下载NLTK资源
nltk.download('stopwords')
nltk.download('wordnet')

# 1. 数据准备
print("=== 1. 数据准备 ===")

# 创建示例情感分析数据
np.random.seed(42)

# 正面情感文本
positive_texts = [
    "这部电影非常精彩，我很喜欢",
    "服务态度很好，下次还会再来",
    "产品质量不错，性价比高",
    "今天天气很好，心情愉快",
    "这家餐厅的食物味道很棒",
    "这本书写得非常好，推荐大家阅读",
    "演唱会非常精彩，难忘的夜晚",
    "酒店环境舒适，服务周到",
    "新手机性能很好，非常满意",
    "假期过得很愉快，留下了美好的回忆"
]

# 负面情感文本
negative_texts = [
    "这部电影很无聊，浪费时间",
    "服务态度很差，不会再来了",
    "产品质量太差，不值这个价格",
    "今天天气很糟糕，心情很差",
    "这家餐厅的食物很难吃",
    "这本书写得很差，不推荐阅读",
    "演唱会很失望，音响效果不好",
    "酒店环境很差，服务态度恶劣",
    "新手机性能很差，非常不满意",
    "假期过得很糟糕，遇到了很多问题"
]

# 中性情感文本
neutral_texts = [
    "这部电影一般，没有特别的感觉",
    "服务态度一般，中规中矩",
    "产品质量一般，符合预期",
    "今天天气一般，没什么特别的",
    "这家餐厅的食物一般，不难吃也不好吃",
    "这本书写得一般，可看可不看",
    "演唱会一般，没有特别的亮点",
    "酒店环境一般，符合价格",
    "新手机性能一般，符合预期",
    "假期过得一般，平平无奇"
]

# 构建数据集
data = []
labels = []

for text in positive_texts:
    data.append(text)
    labels.append('positive')

for text in negative_texts:
    data.append(text)
    labels.append('negative')

for text in neutral_texts:
    data.append(text)
    labels.append('neutral')

# 转换为DataFrame
df = pd.DataFrame({'text': data, 'label': labels})
print(f"数据集形状: {df.shape}")
print("\n数据前5行:")
print(df.head())

# 标签分布
print("\n标签分布:")
print(df['label'].value_counts())

# 可视化标签分布
plt.figure(figsize=(10, 6))
sns.countplot(x='label', data=df)
plt.title('标签分布')
plt.xlabel('情感')
plt.ylabel('数量')
plt.savefig('label_distribution.png')
plt.show()
print("标签分布图已保存为 label_distribution.png")

# 2. 文本预处理
print("\n=== 2. 文本预处理 ===")

# 文本预处理函数
def preprocess_text(text):
    """预处理文本"""
    # 转为小写
    text = text.lower()
    # 移除标点符号
    text = re.sub(r'[.,;:!?()\[\]{}]', '', text)
    # 分词
    words = text.split()
    # 移除停用词
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # 词形还原
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # 重新组合为文本
    processed_text = ' '.join(words)
    return processed_text

# 应用预处理
print("应用文本预处理...")
df['processed_text'] = df['text'].apply(preprocess_text)
print("预处理完成！")

print("\n预处理前后对比:")
print(f"原始文本: {df['text'][0]}")
print(f"预处理后: {df['processed_text'][0]}")

# 3. 特征提取
print("\n=== 3. 特征提取 ===")

# 使用TF-IDF提取特征
print("使用TF-IDF提取特征...")
tfidf = TfidfVectorizer(max_features=1000)
X = tfidf.fit_transform(df['processed_text'])
y = df['label']

print(f"特征形状: {X.shape}")
print(f"特征数量: {X.shape[1]}")

# 标签编码
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
print(f"标签编码映射: {dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))}")

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
print(f"训练集形状: {X_train.shape}, {y_train.shape}")
print(f"测试集形状: {X_test.shape}, {y_test.shape}")

# 4. 模型训练与评估
print("\n=== 4. 模型训练与评估 ===")

# 定义模型
models = {
    '逻辑回归': LogisticRegression(),
    '决策树': DecisionTreeClassifier(),
    '随机森林': RandomForestClassifier(),
    'SVM': SVC(),
    'K近邻': KNeighborsClassifier(),
    '朴素贝叶斯': MultinomialNB()
}

# 训练和评估模型
results = []
for name, model in models.items():
    # 交叉验证
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    
    # 训练模型
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 计算评估指标
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    
    results.append({
        '模型': name,
        '交叉验证准确率': scores.mean(),
        '测试集准确率': accuracy,
        '测试集精确率': precision,
        '测试集召回率': recall,
        '测试集F1分数': f1
    })
    
    print(f"{name}: 交叉验证准确率 = {scores.mean():.4f}, 测试集准确率 = {accuracy:.4f}, 测试集F1分数 = {f1:.4f}")

# 结果排序
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('测试集F1分数', ascending=False)
print("\n模型性能排序:")
print(results_df)

# 5. 模型调优
print("\n=== 5. 模型调优 ===")

# 选择表现最好的模型进行调优（逻辑回归）
print("调优逻辑回归模型...")

param_grid = {
    'C': [0.1, 1, 10, 100],
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear', 'saga']
}

grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='f1_macro', n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳交叉验证分数: {grid_search.best_score_:.4f}")

# 评估调优后的模型
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
accuracy_best = accuracy_score(y_test, y_pred_best)
f1_best = f1_score(y_test, y_pred_best, average='macro')

print(f"\n调优后模型性能:")
print(f"准确率: {accuracy_best:.4f}")
print(f"F1分数: {f1_best:.4f}")

# 6. 模型评估
print("\n=== 6. 模型评估 ===")

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred_best)
print("混淆矩阵:")
print(cm)

# 可视化混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('混淆矩阵')
plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.savefig('confusion_matrix.png')
plt.show()
print("混淆矩阵已保存为 confusion_matrix.png")

# 分类报告
print("\n分类报告:")
print(classification_report(y_test, y_pred_best, target_names=label_encoder.classes_))

# 7. 特征重要性
print("\n=== 7. 特征重要性 ===")

# 获取特征重要性（逻辑回归系数）
feature_names = tfidf.get_feature_names_out()
feature_coefficients = best_model.coef_[0]

# 排序
indices = np.argsort(np.abs(feature_coefficients))[::-1]

print("前20个重要特征:")
for i, idx in enumerate(indices[:20]):
    print(f"{i+1}. {feature_names[idx]}: {feature_coefficients[idx]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(12, 6))
plt.bar(range(20), feature_coefficients[indices[:20]])
plt.xticks(range(20), [feature_names[i] for i in indices[:20]], rotation=45)
plt.title('前20个重要特征')
plt.savefig('feature_importance.png')
plt.show()
print("特征重要性图已保存为 feature_importance.png")

# 8. 模型测试
print("\n=== 8. 模型测试 ===")

# 测试新文本
new_texts = [
    "这部电影真的很棒，我非常喜欢",
    "服务态度很差，我很不满意",
    "产品质量一般，符合预期"
]

# 预处理新文本
processed_new_texts = [preprocess_text(text) for text in new_texts]

# 提取特征
X_new = tfidf.transform(processed_new_texts)

# 预测
predictions = best_model.predict(X_new)
predicted_labels = label_encoder.inverse_transform(predictions)

print("新文本预测结果:")
for text, label in zip(new_texts, predicted_labels):
    print(f"文本: {text}")
    print(f"预测情感: {label}")
    print()

# 9. 模型部署
print("\n=== 9. 模型部署 ===")

import joblib

# 保存模型
joblib.dump(best_model, 'sentiment_analysis_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
print("模型已保存为 sentiment_analysis_model.pkl")
print("TF-IDF向量化器已保存为 tfidf_vectorizer.pkl")
print("标签编码器已保存为 label_encoder.pkl")

# 加载模型
loaded_model = joblib.load('sentiment_analysis_model.pkl')
loaded_tfidf = joblib.load('tfidf_vectorizer.pkl')
loaded_label_encoder = joblib.load('label_encoder.pkl')

# 测试加载的模型
print("\n测试加载的模型:")
test_text = "这家餐厅的食物非常美味，服务也很周到"
processed_test_text = preprocess_text(test_text)
X_test = loaded_tfidf.transform([processed_test_text])
prediction = loaded_model.predict(X_test)
predicted_label = loaded_label_encoder.inverse_transform(prediction)
print(f"文本: {test_text}")
print(f"预测情感: {predicted_label[0]}")

# 10. 项目总结
print("\n=== 10. 项目总结 ===")
print("1. 数据准备: 创建了包含正面、负面和中性情感的示例数据")
print("2. 文本预处理: 实现了文本清洗、分词、停用词移除和词形还原")
print("3. 特征提取: 使用TF-IDF提取文本特征")
print("4. 模型训练: 比较了多种分类模型的性能")
print("5. 模型调优: 使用网格搜索优化了逻辑回归模型")
print("6. 模型评估: 分析了模型的预测性能和特征重要性")
print("7. 模型部署: 保存了模型和相关组件，可用于实际应用")

# 11. 清理文件
print("\n=== 11. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['label_distribution.png', 'confusion_matrix.png', 'feature_importance.png',
                   'sentiment_analysis_model.pkl', 'tfidf_vectorizer.pkl', 'label_encoder.pkl']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n情感分类项目完成！")
