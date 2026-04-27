#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 42: 循环神经网络

本文件包含循环神经网络的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense, Embedding, Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 循环神经网络基础
print("=== 1. 循环神经网络基础 ===")

print("循环神经网络（RNN）是一种专门用于处理序列数据的深度学习模型。")
print("主要特点：")
print("1. 能够处理变长序列数据")
print("2. 具有记忆功能，能够捕获序列中的长期依赖关系")
print("3. 适合处理时间序列、自然语言等序列数据")
print("4. 常见变体：SimpleRNN, LSTM, GRU")

# 2. 序列数据示例
print("\n=== 2. 序列数据示例 ===")

# 创建简单的时间序列数据
def create_time_series_data():
    # 创建正弦波数据
    t = np.arange(0, 100, 0.1)
    y = np.sin(t) + np.random.normal(0, 0.1, len(t))
    
    # 可视化数据
    plt.figure(figsize=(12, 4))
    plt.plot(t, y)
    plt.title('正弦波时间序列数据')
    plt.xlabel('时间')
    plt.ylabel('值')
    plt.savefig('time_series_data.png')
    plt.show()
    print("时间序列数据可视化已保存为 time_series_data.png")
    
    return t, y

t, y = create_time_series_data()

# 3. 数据预处理
print("\n=== 3. 数据预处理 ===")

# 准备序列数据
def prepare_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)

# 准备训练数据
sequence_length = 10
X, y = prepare_sequences(y, sequence_length)

# 重塑数据形状 (samples, time steps, features)
X = X.reshape(-1, sequence_length, 1)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"训练集形状: {X_train.shape}, {y_train.shape}")
print(f"测试集形状: {X_test.shape}, {y_test.shape}")

# 4. SimpleRNN模型
print("\n=== 4. SimpleRNN模型 ===")

model_simple_rnn = Sequential([
    SimpleRNN(50, input_shape=(sequence_length, 1)),
    Dense(1)
])

model_simple_rnn.compile(optimizer='adam', loss='mean_squared_error')
print("SimpleRNN模型结构:")
model_simple_rnn.summary()

# 训练模型
history_simple_rnn = model_simple_rnn.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss_simple_rnn = model_simple_rnn.evaluate(X_test, y_test, verbose=0)
print(f"SimpleRNN模型测试损失: {loss_simple_rnn:.4f}")

# 5. LSTM模型
print("\n=== 5. LSTM模型 ===")

model_lstm = Sequential([
    LSTM(50, input_shape=(sequence_length, 1)),
    Dense(1)
])

model_lstm.compile(optimizer='adam', loss='mean_squared_error')
print("LSTM模型结构:")
model_lstm.summary()

# 训练模型
history_lstm = model_lstm.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss_lstm = model_lstm.evaluate(X_test, y_test, verbose=0)
print(f"LSTM模型测试损失: {loss_lstm:.4f}")

# 6. GRU模型
print("\n=== 6. GRU模型 ===")

model_gru = Sequential([
    GRU(50, input_shape=(sequence_length, 1)),
    Dense(1)
])

model_gru.compile(optimizer='adam', loss='mean_squared_error')
print("GRU模型结构:")
model_gru.summary()

# 训练模型
history_gru = model_gru.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# 评估模型
loss_gru = model_gru.evaluate(X_test, y_test, verbose=0)
print(f"GRU模型测试损失: {loss_gru:.4f}")

# 7. 模型性能比较
print("\n=== 7. 模型性能比较 ===")

# 可视化训练过程
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(history_simple_rnn.history['loss'], label='训练损失')
plt.plot(history_simple_rnn.history['val_loss'], label='验证损失')
plt.title('SimpleRNN')
plt.xlabel('epoch')
plt.ylabel('损失')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(history_lstm.history['loss'], label='训练损失')
plt.plot(history_lstm.history['val_loss'], label='验证损失')
plt.title('LSTM')
plt.xlabel('epoch')
plt.ylabel('损失')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(history_gru.history['loss'], label='训练损失')
plt.plot(history_gru.history['val_loss'], label='验证损失')
plt.title('GRU')
plt.xlabel('epoch')
plt.ylabel('损失')
plt.legend()

plt.tight_layout()
plt.savefig('rnn_training_curves.png')
plt.show()
print("RNN训练曲线已保存为 rnn_training_curves.png")

# 8. 预测结果可视化
print("\n=== 8. 预测结果可视化 ===")

# 使用LSTM模型进行预测
y_pred = model_lstm.predict(X_test)

# 可视化预测结果
plt.figure(figsize=(12, 6))
plt.plot(y_test, label='真实值')
plt.plot(y_pred, label='预测值')
plt.title('LSTM模型预测结果')
plt.xlabel('样本索引')
plt.ylabel('值')
plt.legend()
plt.savefig('lstm_prediction.png')
plt.show()
print("LSTM预测结果已保存为 lstm_prediction.png")

# 9. 文本分类应用
print("\n=== 9. 文本分类应用 ===")

# 加载IMDB数据集
max_features = 10000  # 只考虑前10000个最常见的单词
maxlen = 500  # 每个评论最多保留500个单词

print("加载IMDB数据集...")
(x_train_imdb, y_train_imdb), (x_test_imdb, y_test_imdb) = imdb.load_data(num_words=max_features)

# 填充序列
x_train_imdb = pad_sequences(x_train_imdb, maxlen=maxlen)
x_test_imdb = pad_sequences(x_test_imdb, maxlen=maxlen)

print(f"IMDB训练集形状: {x_train_imdb.shape}, {y_train_imdb.shape}")
print(f"IMDB测试集形状: {x_test_imdb.shape}, {y_test_imdb.shape}")

# 构建文本分类模型
model_text = Sequential([
    Embedding(max_features, 32, input_length=maxlen),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

model_text.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("文本分类模型结构:")
model_text.summary()

# 训练模型
history_text = model_text.fit(x_train_imdb, y_train_imdb, epochs=5, batch_size=32, validation_split=0.2, verbose=1)

# 评估模型
loss_text, accuracy_text = model_text.evaluate(x_test_imdb, y_test_imdb, verbose=0)
print(f"文本分类模型测试准确率: {accuracy_text:.4f}")

# 10. 双向RNN
print("\n=== 10. 双向RNN ===")

from tensorflow.keras.layers import Bidirectional

model_bidir = Sequential([
    Embedding(max_features, 32, input_length=maxlen),
    Bidirectional(LSTM(32)),
    Dense(1, activation='sigmoid')
])

model_bidir.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("双向LSTM模型结构:")
model_bidir.summary()

# 训练模型
history_bidir = model_bidir.fit(x_train_imdb, y_train_imdb, epochs=5, batch_size=32, validation_split=0.2, verbose=1)

# 评估模型
loss_bidir, accuracy_bidir = model_bidir.evaluate(x_test_imdb, y_test_imdb, verbose=0)
print(f"双向LSTM模型测试准确率: {accuracy_bidir:.4f}")

# 11. 堆叠RNN
print("\n=== 11. 堆叠RNN ===")

model_stack = Sequential([
    Embedding(max_features, 32, input_length=maxlen),
    LSTM(32, return_sequences=True),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

model_stack.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("堆叠LSTM模型结构:")
model_stack.summary()

# 训练模型
history_stack = model_stack.fit(x_train_imdb, y_train_imdb, epochs=5, batch_size=32, validation_split=0.2, verbose=1)

# 评估模型
loss_stack, accuracy_stack = model_stack.evaluate(x_test_imdb, y_test_imdb, verbose=0)
print(f"堆叠LSTM模型测试准确率: {accuracy_stack:.4f}")

# 12. 文本分类模型比较
print("\n=== 12. 文本分类模型比较 ===")

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(history_text.history['accuracy'], label='训练准确率')
plt.plot(history_text.history['val_accuracy'], label='验证准确率')
plt.title('单向LSTM')
plt.xlabel('epoch')
plt.ylabel('准确率')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(history_bidir.history['accuracy'], label='训练准确率')
plt.plot(history_bidir.history['val_accuracy'], label='验证准确率')
plt.title('双向LSTM')
plt.xlabel('epoch')
plt.ylabel('准确率')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(history_stack.history['accuracy'], label='训练准确率')
plt.plot(history_stack.history['val_accuracy'], label='验证准确率')
plt.title('堆叠LSTM')
plt.xlabel('epoch')
plt.ylabel('准确率')
plt.legend()

plt.tight_layout()
plt.savefig('text_classification_curves.png')
plt.show()
print("文本分类模型训练曲线已保存为 text_classification_curves.png")

# 13. 实际应用示例
print("\n=== 13. 实际应用示例 ===")

print("RNN的主要应用场景：")
print("1. 时间序列预测: 股票价格、天气预报、能源消耗")
print("2. 自然语言处理: 文本分类、情感分析、机器翻译")
print("3. 语音识别: 语音转文本、语音命令")
print("4. 视频分析: 动作识别、视频分类")
print("5. 推荐系统: 序列推荐、用户行为预测")

# 14. 清理文件
print("\n=== 14. 清理文件 ===")
import os

# 清理生成的文件
files_to_delete = ['time_series_data.png', 'rnn_training_curves.png', 'lstm_prediction.png', 'text_classification_curves.png']

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"删除文件: {file}")

print("\n循环神经网络练习完成！")
