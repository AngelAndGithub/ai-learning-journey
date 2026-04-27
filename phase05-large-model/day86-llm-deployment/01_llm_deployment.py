#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 86: 大模型部署与微调

本文件包含大模型部署与微调的练习代码，包括本地部署、LoRA轻量化微调和API服务封装
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import gradio as gr
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 设置Seaborn风格
sns.set_style("whitegrid")

# 1. 大模型本地部署
print("=== 1. 大模型本地部署 ===")

# 1.1 模型选择
print("\n1.1 模型选择")
print("常见的开源大模型:")
print("1. Llama 2系列 (Meta)")
print("2. Mistral 7B (Mistral AI)")
print("3. Falcon系列 (TII)")
print("4. Bloom (BigScience)")
print("5. GPT-J (EleutherAI)")
print("6. Cohere Command R (Cohere)")

# 1.2 模型下载
print("\n1.2 模型下载")
print("使用Hugging Face下载模型:")
print("""
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
""")

# 1.3 模型加载
print("\n1.3 模型加载")
print("使用不同精度加载模型:")
print("""
# 全精度加载
model = AutoModelForCausalLM.from_pretrained(model_name)

# 半精度加载
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

# 量化加载
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=quantization_config)
""")

# 1.4 模型推理
print("\n1.4 模型推理")
print("模型推理示例:")
print("""
def generate_text(prompt, model, tokenizer, max_length=512):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.1
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

prompt = "什么是人工智能？"
response = generate_text(prompt, model, tokenizer)
print(response)
""")

# 2. LoRA轻量化微调
print("\n=== 2. LoRA轻量化微调 ===")

# 2.1 LoRA原理
print("\n2.1 LoRA原理")
print("LoRA (Low-Rank Adaptation) 是一种参数高效的微调方法，它通过低秩分解来减少可训练参数的数量。")
print("核心思想:")
print("1. 对于每个权重矩阵 W，添加一个低秩分解矩阵 ΔW = BA")
print("2. 其中 B 和 A 是低秩矩阵，秩 r 远小于原始矩阵的维度")
print("3. 只训练 B 和 A，保持原始权重 W 不变")
print("4. 推理时，将 ΔW 加到原始权重上")

# 2.2 LoRA配置
print("\n2.2 LoRA配置")
print("LoRA配置示例:")
print("""
from peft import LoraConfig

lora_config = LoraConfig(
    r=8,  # 秩
    lora_alpha=16,  # 缩放因子
    target_modules=["q_proj", "v_proj"],  # 目标模块
    lora_dropout=0.1,  # dropout率
    bias="none",  # 偏置处理
    task_type="CAUSAL_LM"  # 任务类型
)
""")

# 2.3 模型准备
print("\n2.3 模型准备")
print("准备模型进行LoRA微调:")
print("""
from peft import prepare_model_for_kbit_training

# 准备模型
model = prepare_model_for_kbit_training(model)

# 创建LoRA模型
from peft import get_peft_model
model = get_peft_model(model, lora_config)

# 打印可训练参数
model.print_trainable_parameters()
""")

# 2.4 数据集准备
print("\n2.4 数据集准备")
print("创建示例数据集:")
print("""
# 示例数据集
dataset = [
    {
        "instruction": "解释什么是机器学习",
        "input": "",
        "output": "机器学习是人工智能的一个分支，它使计算机系统能够从数据中学习并改进性能，而不需要明确的编程。"
    },
    {
        "instruction": "什么是深度学习",
        "input": "",
        "output": "深度学习是机器学习的一个分支，它使用多层神经网络来模拟人脑的学习过程。"
    },
    {
        "instruction": "解释什么是神经网络",
        "input": "",
        "output": "神经网络是一种模仿人脑结构和功能的计算模型，由大量相互连接的节点（神经元）组成。"
    }
]

# 格式化数据集
def format_dataset(example):
    prompt = f"### 指令:\n{example['instruction']}\n\n### 输入:\n{example['input']}\n\n### 输出:\n"
    return {"text": prompt + example['output']}

formatted_dataset = [format_dataset(example) for example in dataset]
""")

# 2.5 训练配置
print("\n2.5 训练配置")
print("训练配置示例:")
print("""
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./lora-finetuned",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    logging_steps=10,
    save_strategy="epoch",
    fp16=True,
    optim="paged_adamw_32bit"
)
""")

# 2.6 训练过程
print("\n2.6 训练过程")
print("训练过程示例:")
print("""
from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=formatted_dataset,
    tokenizer=tokenizer
)

trainer.train()

# 保存模型
model.save_pretrained("./lora-finetuned")
""")

# 3. API服务封装
print("\n=== 3. API服务封装 ===")

# 3.1 Flask API
print("\n3.1 Flask API")
print("Flask API示例:")
print("""
from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

app = Flask(__name__)

# 加载模型
base_model = "meta-llama/Llama-2-7b-hf"
adapter_model = "./lora-finetuned"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(model, adapter_model)
model.eval()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    max_length = data.get("max_length", 512)
    
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
""")

# 3.2 FastAPI
print("\n3.2 FastAPI")
print("FastAPI示例:")
print("""
from fastapi import FastAPI, Body
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

app = FastAPI()

# 加载模型
base_model = "meta-llama/Llama-2-7b-hf"
adapter_model = "./lora-finetuned"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(model, adapter_model)
model.eval()

class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 512

@app.post("/generate")
def generate(request: GenerateRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=request.max_length,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
""")

# 3.3 Gradio界面
print("\n3.3 Gradio界面")
print("Gradio界面示例:")
print("""
import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# 加载模型
base_model = "meta-llama/Llama-2-7b-hf"
adapter_model = "./lora-finetuned"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(model, adapter_model)
model.eval()

def generate_text(prompt, max_length=512):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 创建Gradio界面
interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(label="输入提示", placeholder="请输入您的问题..."),
        gr.Slider(minimum=100, maximum=1024, value=512, label="最大长度")
    ],
    outputs=gr.Textbox(label="生成结果"),
    title="大模型文本生成",
    description="使用微调后的大模型生成文本"
)

# 启动界面
interface.launch()
""")

# 4. 实际应用示例
print("\n=== 4. 实际应用示例 ===")

# 4.1 本地知识库问答系统
print("\n4.1 本地知识库问答系统")
print("本地知识库问答系统示例:")
print("""
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# 加载模型
base_model = "meta-llama/Llama-2-7b-hf"
adapter_model = "./lora-finetuned"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(model, adapter_model)
model.eval()

# 加载知识库
documents = []
for file in os.listdir("./knowledge_base"):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join("./knowledge_base", file))
        documents.extend(loader.load())

# 分割文档
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(documents)

# 创建向量存储
embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)

# 定义问答函数
def answer_question(question):
    # 检索相关文档
    docs = vectorstore.similarity_search(question, k=3)
    context = " ".join([doc.page_content for doc in docs])
    
    # 构建Prompt
    prompt = f"基于以下上下文，回答问题：\n\n上下文: {context}\n\n问题: {question}\n\n回答:"
    
    # 生成回答
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=512,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1
        )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 测试问答系统
question = "什么是机器学习？"
answer = answer_question(question)
print(f"问题: {question}")
print(f"回答: {answer}")
""")

# 4.2 模型量化
print("\n4.2 模型量化")
print("模型量化示例:")
print("""
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# 4位量化配置
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)

# 加载量化模型
model_name = "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto"
)

# 测试量化模型
prompt = "什么是人工智能？"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs["input_ids"],
    max_length=512,
    temperature=0.7,
    top_p=0.95
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
""")

# 5. 模型部署最佳实践
print("\n=== 5. 模型部署最佳实践 ===")

print("1. 模型选择:")
print("   - 根据硬件资源选择合适大小的模型")
print("   - 考虑使用量化版本减少内存使用")
print("   - 对于边缘设备，选择更小的模型如 DistilBERT、TinyBERT 等")

print("\n2. 硬件优化:")
print("   - 使用 GPU 加速推理")
print("   - 对于大型模型，考虑使用多 GPU 或 TPU")
print("   - 合理设置 batch size 和 max_length")

print("\n3. 软件优化:")
print("   - 使用 ONNX 或 TensorRT 加速推理")
print("   - 实现模型缓存机制")
print("   - 使用异步处理提高并发性能")

print("\n4. 监控与维护:")
print("   - 监控模型性能和资源使用")
print("   - 设置合理的超时机制")
print("   - 定期更新模型和依赖")

print("\n5. 安全性:")
print("   - 实现输入验证和过滤")
print("   - 限制生成内容的长度和类型")
print("   - 监控和防止恶意使用")

# 6. 总结
print("\n=== 6. 总结 ===")
print("1. 大模型本地部署: 学习了模型选择、下载、加载和推理的方法")
print("2. LoRA轻量化微调: 学习了LoRA原理、配置、模型准备、数据集准备和训练过程")
print("3. API服务封装: 学习了使用Flask、FastAPI和Gradio封装模型服务")
print("4. 实际应用: 实现了本地知识库问答系统和模型量化的示例")
print("5. 最佳实践: 学习了模型部署的硬件、软件优化和安全性考虑")

print("\n大模型部署与微调练习完成！")
