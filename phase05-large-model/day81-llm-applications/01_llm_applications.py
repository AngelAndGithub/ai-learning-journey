#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 81: 大模型应用开发

本文件包含大模型应用开发的练习代码，包括Prompt工程、RAG检索增强和向量数据库的使用
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import faiss
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. Prompt工程
print("=== 1. Prompt工程 ===")

# 1.1 基础Prompt
print("\n1.1 基础Prompt")

# 示例1: 简单问题
print("示例1: 简单问题")
prompt1 = "什么是人工智能？"
print(f"Prompt: {prompt1}")

# 示例2: 指令型Prompt
print("\n示例2: 指令型Prompt")
prompt2 = "请解释什么是机器学习，并用简单的例子说明。"
print(f"Prompt: {prompt2}")

# 示例3: 情境型Prompt
print("\n示例3: 情境型Prompt")
prompt3 = "你是一位专业的软件工程师，请解释什么是面向对象编程。"
print(f"Prompt: {prompt3}")

# 1.2 Prompt优化技巧
print("\n1.2 Prompt优化技巧")

# 技巧1: 明确任务
print("技巧1: 明确任务")
bad_prompt = "写一篇关于人工智能的文章"
good_prompt = "写一篇关于人工智能在医疗领域应用的文章，重点介绍诊断辅助和药物研发，长度约500字。"
print(f"不好的Prompt: {bad_prompt}")
print(f"好的Prompt: {good_prompt}")

# 技巧2: 提供示例
print("\n技巧2: 提供示例")
prompt_with_example = "请将以下句子转换为被动语态：\n\n主动语态: 科学家发现了新的行星。\n被动语态: 新的行星被科学家发现了。\n\n主动语态: 学生们完成了作业。\n被动语态:"
print(f"带示例的Prompt: {prompt_with_example}")

# 技巧3: 设定角色
print("\n技巧3: 设定角色")
prompt_with_role = "你是一位专业的财务顾问，请为一位刚毕业的大学生提供理财建议。"
print(f"设定角色的Prompt: {prompt_with_role}")

# 技巧4: 详细说明
print("\n技巧4: 详细说明")
detailed_prompt = "请分析以下股票市场数据，预测未来一个月的走势。\n\n数据：\n- 过去三个月的收盘价：[100, 105, 110, 108, 115, 120, 118, 125, 130, 128, 135, 140]\n- 交易量：[1000, 1200, 1500, 1300, 1600, 1800, 1700, 2000, 2200, 2100, 2400, 2500]\n- 市场情绪：中性偏乐观\n\n请提供详细的分析过程和预测结果。"
print(f"详细说明的Prompt: {detailed_prompt}")

# 2. RAG检索增强
print("\n=== 2. RAG检索增强 ===")

# 2.1 文档处理
print("\n2.1 文档处理")

# 创建示例文档
documents = [
    "人工智能（AI）是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。",
    "机器学习是人工智能的一个分支，它使计算机系统能够从数据中学习并改进性能，而不需要明确的编程。",
    "深度学习是机器学习的一个分支，它使用多层神经网络来模拟人脑的学习过程。",
    "自然语言处理（NLP）是人工智能的一个领域，它使计算机能够理解、解释和生成人类语言。",
    "计算机视觉是人工智能的一个领域，它使计算机能够理解和解释图像和视频。",
    "强化学习是机器学习的一种方法，它通过与环境交互并接收反馈来学习最佳行为。",
    "监督学习是机器学习的一种方法，它使用标记数据来训练模型。",
    "无监督学习是机器学习的一种方法，它使用未标记数据来发现数据中的模式。"
]

print(f"文档数量: {len(documents)}")
print("\n示例文档:")
for i, doc in enumerate(documents[:3]):
    print(f"文档{i+1}: {doc}")

# 2.2 向量嵌入
print("\n2.2 向量嵌入")

# 使用TF-IDF作为简单的向量嵌入
vectorizer = TfidfVectorizer()
document_embeddings = vectorizer.fit_transform(documents)
print(f"文档嵌入形状: {document_embeddings.shape}")

# 2.3 向量存储
print("\n2.3 向量存储")

# 使用FAISS创建向量索引
dimension = document_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# 将文档嵌入添加到索引
index.add(document_embeddings.toarray().astype('float32'))
print(f"索引中的向量数量: {index.ntotal}")

# 2.4 检索过程
print("\n2.4 检索过程")

# 示例查询
query = "什么是深度学习？"
print(f"查询: {query}")

# 将查询转换为向量
query_embedding = vectorizer.transform([query]).toarray().astype('float32')

# 检索最相似的文档
k = 3  # 检索前3个最相似的文档
distances, indices = index.search(query_embedding, k)

print("\n检索结果:")
for i in range(k):
    print(f"相似度: {1 - distances[0][i]:.4f}, 文档: {documents[indices[0][i]]}")

# 2.5 生成回答
print("\n2.5 生成回答")

# 构建上下文
context = " ".join([documents[idx] for idx in indices[0]])
print(f"上下文: {context}")

# 构建Prompt
rag_prompt = f"基于以下上下文，回答问题：\n\n上下文: {context}\n\n问题: {query}\n\n回答:"
print(f"\nRAG Prompt: {rag_prompt}")

# 3. 向量数据库
print("\n=== 3. 向量数据库 ===")

# 3.1 向量数据库简介
print("\n3.1 向量数据库简介")
print("向量数据库是专门用于存储和检索向量嵌入的数据库，它支持高效的相似性搜索。")
print("常见的向量数据库包括：")
print("1. Pinecone")
print("2. Milvus")
print("3. FAISS (Facebook AI Similarity Search)")
print("4. Weaviate")
print("5. Qdrant")
print("6. Chroma")

# 3.2 向量数据库使用示例
print("\n3.2 向量数据库使用示例")

# 使用FAISS作为向量数据库
print("使用FAISS作为向量数据库:")

# 创建索引
dimension = 128  # 向量维度
index = faiss.IndexFlatL2(dimension)

# 生成随机向量
n_vectors = 1000
vectors = np.random.random((n_vectors, dimension)).astype('float32')

# 添加向量到索引
index.add(vectors)
print(f"添加了 {n_vectors} 个向量到索引")
print(f"索引中的向量数量: {index.ntotal}")

# 生成查询向量
query_vector = np.random.random((1, dimension)).astype('float32')

# 搜索相似向量
k = 5  # 检索前5个最相似的向量
distances, indices = index.search(query_vector, k)

print("\n搜索结果:")
print(f"查询向量与前5个最相似向量的距离: {distances[0]}")
print(f"前5个最相似向量的索引: {indices[0]}")

# 4. 实际应用示例
print("\n=== 4. 实际应用示例 ===")

# 4.1 知识库问答系统
print("\n4.1 知识库问答系统")

# 创建知识库
knowledge_base = [
    "Python是一种高级编程语言，它具有简单易学、可读性强的特点。",
    "Python的主要应用领域包括Web开发、数据科学、人工智能、自动化等。",
    "Python的主要库包括NumPy、Pandas、Matplotlib、Scikit-learn等。",
    "NumPy是Python中用于科学计算的核心库，它提供了高效的多维数组操作。",
    "Pandas是Python中用于数据分析的库，它提供了DataFrame等数据结构。",
    "Matplotlib是Python中用于数据可视化的库，它提供了各种绘图功能。",
    "Scikit-learn是Python中用于机器学习的库，它提供了各种机器学习算法。",
    "TensorFlow是Google开发的深度学习框架，它用于构建和训练神经网络。",
    "PyTorch是Facebook开发的深度学习框架，它提供了动态计算图。",
    "Keras是一个高级深度学习API，它可以运行在TensorFlow、Theano或CNTK上。"
]

# 向量嵌入
vectorizer = TfidfVectorizer()
kb_embeddings = vectorizer.fit_transform(knowledge_base)

# 创建FAISS索引
dimension = kb_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(kb_embeddings.toarray().astype('float32'))

# 定义问答函数
def answer_question(question, knowledge_base, vectorizer, index, k=3):
    """回答问题"""
    # 转换查询为向量
    query_embedding = vectorizer.transform([question]).toarray().astype('float32')
    
    # 检索相关文档
    distances, indices = index.search(query_embedding, k)
    
    # 构建上下文
    context = " ".join([knowledge_base[idx] for idx in indices[0]])
    
    # 构建Prompt
    prompt = f"基于以下上下文，回答问题：\n\n上下文: {context}\n\n问题: {question}\n\n回答:"
    
    # 这里可以调用大模型生成回答
    # 为了演示，我们使用简单的规则生成回答
    answer = f"根据知识库，{question} 的答案是：{context}"
    
    return answer, context

# 测试问答系统
questions = [
    "Python有哪些主要应用领域？",
    "NumPy库的作用是什么？",
    "什么是TensorFlow？"
]

for question in questions:
    print(f"\n问题: {question}")
    answer, context = answer_question(question, knowledge_base, vectorizer, index)
    print(f"回答: {answer}")

# 4.2 文档摘要
print("\n4.2 文档摘要")

# 示例文档
document = "Python是一种高级编程语言，它具有简单易学、可读性强的特点。Python的主要应用领域包括Web开发、数据科学、人工智能、自动化等。Python的主要库包括NumPy、Pandas、Matplotlib、Scikit-learn等。NumPy是Python中用于科学计算的核心库，它提供了高效的多维数组操作。Pandas是Python中用于数据分析的库，它提供了DataFrame等数据结构。Matplotlib是Python中用于数据可视化的库，它提供了各种绘图功能。Scikit-learn是Python中用于机器学习的库，它提供了各种机器学习算法。"

# 文档摘要Prompt
summary_prompt = f"请为以下文档生成一个简洁的摘要，长度不超过100字：\n\n文档: {document}\n\n摘要:"
print(f"摘要Prompt: {summary_prompt}")

# 4.3 文本分类
print("\n4.3 文本分类")

# 示例文本
texts = [
    "Python是一种很好的编程语言，我很喜欢使用它",
    "这个产品质量很差，我非常不满意",
    "今天天气很好，心情愉快",
    "服务态度很差，下次不会再来了"
]

# 文本分类Prompt
for text in texts:
    classification_prompt = f"请将以下文本分类为正面、负面或中性：\n\n文本: {text}\n\n分类:"
    print(f"\n分类Prompt: {classification_prompt}")

# 5. 大模型接口调用
print("\n=== 5. 大模型接口调用 ===")

# 5.1 模拟大模型接口
print("\n5.1 模拟大模型接口")

def mock_llm_api(prompt, model="gpt-3.5-turbo", temperature=0.7):
    """模拟大模型接口"""
    # 简单的模拟回复
    responses = {
        "什么是人工智能？": "人工智能（AI）是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。",
        "什么是机器学习？": "机器学习是人工智能的一个分支，它使计算机系统能够从数据中学习并改进性能，而不需要明确的编程。",
        "什么是深度学习？": "深度学习是机器学习的一个分支，它使用多层神经网络来模拟人脑的学习过程。"
    }
    
    return responses.get(prompt, "抱歉，我无法回答这个问题。")

# 测试模拟接口
print("测试模拟大模型接口:")
test_prompts = ["什么是人工智能？", "什么是机器学习？", "什么是深度学习？"]
for prompt in test_prompts:
    response = mock_llm_api(prompt)
    print(f"\nPrompt: {prompt}")
    print(f"Response: {response}")

# 5.2 实际接口调用（注释掉，需要实际API密钥）
print("\n5.2 实际接口调用")
print("以下是调用OpenAI API的示例代码（需要API密钥）:")
print("""
import openai

openai.api_key = "YOUR_API_KEY"

def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个专业的AI助手。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
""")

# 6. 项目实践
print("\n=== 6. 项目实践 ===")

# 6.1 构建简单的RAG系统
print("\n6.1 构建简单的RAG系统")

# 1. 准备知识库
knowledge_base = [
    "Python是一种高级编程语言，它具有简单易学、可读性强的特点。",
    "Python的主要应用领域包括Web开发、数据科学、人工智能、自动化等。",
    "Python的主要库包括NumPy、Pandas、Matplotlib、Scikit-learn等。",
    "NumPy是Python中用于科学计算的核心库，它提供了高效的多维数组操作。",
    "Pandas是Python中用于数据分析的库，它提供了DataFrame等数据结构。",
    "Matplotlib是Python中用于数据可视化的库，它提供了各种绘图功能。",
    "Scikit-learn是Python中用于机器学习的库，它提供了各种机器学习算法。",
    "TensorFlow是Google开发的深度学习框架，它用于构建和训练神经网络。",
    "PyTorch是Facebook开发的深度学习框架，它提供了动态计算图。",
    "Keras是一个高级深度学习API，它可以运行在TensorFlow、Theano或CNTK上。"
]

# 2. 向量嵌入和索引
vectorizer = TfidfVectorizer()
kb_embeddings = vectorizer.fit_transform(knowledge_base)
dimension = kb_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(kb_embeddings.toarray().astype('float32'))

# 3. 定义RAG系统
def rag_system(question):
    """RAG系统"""
    # 检索相关文档
    query_embedding = vectorizer.transform([question]).toarray().astype('float32')
    distances, indices = index.search(query_embedding, 3)
    context = " ".join([knowledge_base[idx] for idx in indices[0]])
    
    # 构建Prompt
    prompt = f"基于以下上下文，回答问题：\n\n上下文: {context}\n\n问题: {question}\n\n回答:"
    
    # 调用大模型
    answer = mock_llm_api(prompt)
    
    return answer

# 4. 测试RAG系统
print("测试RAG系统:")
test_questions = [
    "Python有哪些主要库？",
    "TensorFlow是什么？",
    "Pandas库的作用是什么？"
]

for question in test_questions:
    answer = rag_system(question)
    print(f"\n问题: {question}")
    print(f"回答: {answer}")

# 7. 总结
print("\n=== 7. 总结 ===")
print("1. Prompt工程: 学习了基础Prompt、指令型Prompt、情境型Prompt和Prompt优化技巧")
print("2. RAG检索增强: 学习了文档处理、向量嵌入、向量存储、检索过程和生成回答")
print("3. 向量数据库: 学习了向量数据库的基本概念和使用示例")
print("4. 实际应用: 实现了知识库问答系统、文档摘要和文本分类的示例")
print("5. 大模型接口: 学习了模拟大模型接口和实际接口调用的方法")
print("6. 项目实践: 构建了一个简单的RAG系统")

print("\n大模型应用开发练习完成！")
