#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 44: 大模型基础

本文件包含大模型基础概念的练习代码
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Attention, Input
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import requests

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1. 大模型概述
print("=== 1. 大模型概述 ===")

print("大语言模型（LLM）是指参数量巨大、能够理解和生成人类语言的人工智能模型。")
print("主要特点：")
print("1. 参数量大：通常在数十亿到数万亿参数之间")
print("2. 预训练：在海量文本数据上进行预训练")
print("3. 微调：通过少量数据进行微调以适应特定任务")
print("4. 涌现能力：随着模型规模增大，出现的新能力")
print("5. 上下文理解：能够理解长上下文的语义")

# 2. 大模型的发展历程
print("\n=== 2. 大模型的发展历程 ===")

print("大模型的发展主要经历了以下几个阶段：")
print("1. 早期语言模型：n-gram模型、RNN")
print("2.  transformer架构的出现：2017年Google发表Attention is All You Need")
print("3. BERT和GPT系列：2018年BERT，2018年GPT-1，2019年GPT-2")
print("4. 大模型时代：2020年GPT-3（175B参数）")
print("5. 多模态大模型：GPT-4V、Claude 3等")
print("6. 开源大模型：Llama、Falcon、GPT-J等")

# 3. 大模型的核心技术
print("\n=== 3. 大模型的核心技术 ===")

print("大模型的核心技术包括：")
print("1. Transformer架构：自注意力机制")
print("2. 预训练-微调范式：在海量数据上预训练，然后微调")
print("3. 规模化训练：分布式训练、混合精度训练")
print("4. 高效推理：模型压缩、量化、蒸馏")
print("5. 提示工程：通过提示引导模型生成期望的输出")
print("6. 上下文学习：few-shot、one-shot、zero-shot学习")

# 4. 简单的Transformer模型实现
print("\n=== 4. 简单的Transformer模型实现 ===")

# 简化版的自注意力机制
def scaled_dot_product_attention(q, k, v, mask=None):
    """缩放点积注意力"""
    matmul_qk = tf.matmul(q, k, transpose_b=True)
    dk = tf.cast(tf.shape(k)[-1], tf.float32)
    scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
    
    if mask is not None:
        scaled_attention_logits += (mask * -1e9)
    
    attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
    output = tf.matmul(attention_weights, v)
    
    return output, attention_weights

# 测试自注意力机制
q = tf.random.normal((1, 3, 64))
k = tf.random.normal((1, 3, 64))
v = tf.random.normal((1, 3, 64))

output, weights = scaled_dot_product_attention(q, k, v)
print(f"自注意力输出形状: {output.shape}")
print(f"注意力权重形状: {weights.shape}")

# 5. 大模型的应用场景
print("\n=== 5. 大模型的应用场景 ===")

print("大模型的主要应用场景：")
print("1. 自然语言处理：文本分类、情感分析、命名实体识别")
print("2. 问答系统：知识库问答、对话系统")
print("3. 文本生成：文章写作、代码生成、创意内容生成")
print("4. 机器翻译：多语言翻译")
print("5. 语音识别：语音转文本")
print("6. 图像处理：图像描述、图像分类")
print("7. 多模态任务：图文生成、视频理解")
print("8. 教育领域：智能辅导、个性化学习")
print("9. 医疗领域：医疗咨询、病历分析")
print("10. 金融领域：风险评估、市场分析")

# 6. 大模型的评估指标
print("\n=== 6. 大模型的评估指标 ===")

print("大模型的评估指标包括：")
print("1. 困惑度（Perplexity）：衡量模型预测的不确定性")
print("2. 准确率（Accuracy）：分类任务的正确率")
print("3. F1分数：综合精确率和召回率")
print("4. BLEU分数：机器翻译的评估指标")
print("5. ROUGE分数：文本摘要的评估指标")
print("6. MMLU：大规模多任务语言理解")
print("7. GSM8K：数学问题求解能力")
print("8. HumanEval：代码生成能力")
print("9. 人工评估：人类对模型输出的评价")

# 7. 大模型的挑战
print("\n=== 7. 大模型的挑战 ===")

print("大模型面临的主要挑战：")
print("1. 计算资源需求：训练和推理需要大量GPU/TPU")
print("2. 数据质量和偏见：模型可能学习到数据中的偏见")
print("3. 模型可解释性：难以理解模型的决策过程")
print("4. 安全性：可能生成有害内容")
print("5. 版权问题：使用受版权保护的数据进行训练")
print("6. 能耗：训练过程能耗高，对环境有影响")
print("7. 推理延迟：在边缘设备上部署困难")

# 8. 大模型的部署策略
print("\n=== 8. 大模型的部署策略 ===")

print("大模型的部署策略包括：")
print("1. 云端部署：使用云服务提供API")
print("2. 边缘部署：在本地设备上部署小型模型")
print("3. 混合部署：结合云端和边缘的优势")
print("4. 模型压缩：剪枝、量化、蒸馏")
print("5. 服务架构：负载均衡、缓存、批处理")

# 9. 实际应用示例
print("\n=== 9. 实际应用示例 ===")

# 9.1 文本生成
print("\n9.1 文本生成")

# 简单的文本生成示例
def generate_text(prompt, model, tokenizer, max_length=100):
    """生成文本"""
    input_ids = tokenizer.encode(prompt, return_tensors='tf')
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# 9.2 问答系统
print("\n9.2 问答系统")

# 简单的问答示例
def answer_question(question, context, model, tokenizer):
    """回答问题"""
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    input_ids = tokenizer.encode(prompt, return_tensors='tf')
    output = model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=1
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# 10. 大模型的未来发展
print("\n=== 10. 大模型的未来发展 ===")

print("大模型的未来发展方向：")
print("1. 更大规模：参数量继续增长")
print("2. 多模态融合：整合文本、图像、音频、视频等")
print("3. 更高效的训练和推理：新的模型架构和算法")
print("4. 更强的推理能力：逻辑推理、数学推理")
print("5. 更好的可解释性：理解模型的决策过程")
print("6. 更安全、更可控：减少有害输出")
print("7. 领域专用模型：针对特定领域优化")
print("8. 联邦学习：保护隐私的分布式训练")

# 11. 大模型工具和框架
print("\n=== 11. 大模型工具和框架 ===")

print("常用的大模型工具和框架：")
print("1. Hugging Face Transformers：提供预训练模型和工具")
print("2. PyTorch：深度学习框架")
print("3. TensorFlow：深度学习框架")
print("4. GPT-NeoX：开源大模型训练框架")
print("5. DeepSpeed：微软的分布式训练库")
print("6. Megatron-LM：NVIDIA的大模型训练框架")
print("7. vLLM：高效的大模型推理库")
print("8. LangChain：大模型应用开发框架")
print("9. LlamaIndex：大模型知识索引框架")

# 12. 大模型的伦理考虑
print("\n=== 12. 大模型的伦理考虑 ===")

print("大模型的伦理考虑包括：")
print("1. 公平性：避免模型歧视特定群体")
print("2. 透明度：公开模型的训练数据和过程")
print("3. 隐私保护：保护用户数据隐私")
print("4. 安全性：防止模型被滥用")
print("5. 责任归属：明确模型决策的责任")
print("6. 环境影响：减少训练和推理的能耗")

# 13. 实践练习
print("\n=== 13. 实践练习 ===")

# 13.1 文本预处理
print("\n13.1 文本预处理")

# 简单的文本预处理函数
def preprocess_text(text):
    """预处理文本"""
    # 转为小写
    text = text.lower()
    # 移除标点符号
    text = re.sub(r'[.,;:!?()\[\]{}]', '', text)
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 测试文本预处理
test_text = "Hello, World! This is a test."
print(f"原始文本: {test_text}")
print(f"预处理后: {preprocess_text(test_text)}")

# 13.2 简单的语言模型
print("\n13.2 简单的语言模型")

# 准备示例数据
texts = [
    "I love machine learning",
    "Machine learning is fascinating",
    "I am learning about neural networks",
    "Neural networks are powerful",
    "I enjoy working with AI"
]

# 文本预处理
processed_texts = [preprocess_text(text) for text in texts]

# 标记化
tokenizer = Tokenizer()
tokenizer.fit_on_texts(processed_texts)
vocab_size = len(tokenizer.word_index) + 1

# 准备训练数据
sequences = []
for text in processed_texts:
    tokens = tokenizer.texts_to_sequences([text])[0]
    for i in range(1, len(tokens)):
        sequence = tokens[:i+1]
        sequences.append(sequence)

# 填充序列
max_length = max(len(seq) for seq in sequences)
sequences = pad_sequences(sequences, maxlen=max_length, padding='pre')

# 拆分输入和目标
X = sequences[:, :-1]
y = sequences[:, -1]

# 构建简单的语言模型
model = Sequential([
    Embedding(vocab_size, 10, input_length=max_length-1),
    LSTM(50),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print("简单语言模型结构:")
model.summary()

# 训练模型
model.fit(X, y, epochs=50, verbose=0)
print("模型训练完成")

# 生成文本
def generate_text_simple(prompt, model, tokenizer, max_length=10):
    """生成文本"""
    input_text = preprocess_text(prompt)
    input_sequence = tokenizer.texts_to_sequences([input_text])[0]
    input_sequence = pad_sequences([input_sequence], maxlen=max_length-1, padding='pre')
    
    output = []
    for _ in range(5):
        prediction = model.predict(input_sequence, verbose=0)
        predicted_id = np.argmax(prediction[0])
        predicted_word = tokenizer.index_word[predicted_id]
        output.append(predicted_word)
        
        # 更新输入序列
        input_sequence = np.roll(input_sequence, -1, axis=1)
        input_sequence[0, -1] = predicted_id
    
    return ' '.join(output)

# 测试文本生成
prompt = "I love"
generated_text = generate_text_simple(prompt, model, tokenizer)
print(f"输入: {prompt}")
print(f"生成: {generated_text}")

# 14. 清理文件
print("\n=== 14. 清理文件 ===")
print("大模型基础练习完成！")
