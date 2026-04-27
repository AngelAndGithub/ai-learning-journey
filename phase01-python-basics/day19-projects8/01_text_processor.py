#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 19: 项目实践8 - 文本处理工具

本文件实现一个文本处理工具，支持文本的各种操作
"""

import re
import argparse
import os

class TextProcessor:
    """文本处理工具类"""
    
    def read_file(self, file_path):
        """
        读取文件内容
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"成功读取文件: {file_path}")
            return content
        except Exception as e:
            print(f"读取文件失败: {e}")
            return ""
    
    def write_file(self, file_path, content):
        """
        写入文件
        
        Args:
            file_path: 文件路径
            content: 内容
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"成功写入文件: {file_path}")
        except Exception as e:
            print(f"写入文件失败: {e}")
    
    def count_words(self, text):
        """
        统计单词数
        
        Args:
            text: 文本
            
        Returns:
            单词数
        """
        words = re.findall(r'\b\w+\b', text)
        return len(words)
    
    def count_lines(self, text):
        """
        统计行数
        
        Args:
            text: 文本
            
        Returns:
            行数
        """
        lines = text.split('\n')
        return len(lines)
    
    def count_characters(self, text):
        """
        统计字符数
        
        Args:
            text: 文本
            
        Returns:
            字符数
        """
        return len(text)
    
    def count_sentences(self, text):
        """
        统计句子数
        
        Args:
            text: 文本
            
        Returns:
            句子数
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
    
    def to_uppercase(self, text):
        """
        转换为大写
        
        Args:
            text: 文本
            
        Returns:
            大写文本
        """
        return text.upper()
    
    def to_lowercase(self, text):
        """
        转换为小写
        
        Args:
            text: 文本
            
        Returns:
            小写文本
        """
        return text.lower()
    
    def capitalize(self, text):
        """
        首字母大写
        
        Args:
            text: 文本
            
        Returns:
            首字母大写的文本
        """
        return text.capitalize()
    
    def title_case(self, text):
        """
        标题大小写
        
        Args:
            text: 文本
            
        Returns:
            标题大小写的文本
        """
        return text.title()
    
    def remove_whitespace(self, text):
        """
        移除多余空白
        
        Args:
            text: 文本
            
        Returns:
            移除多余空白的文本
        """
        # 移除行首行尾空白
        text = text.strip()
        # 移除多余的空格
        text = re.sub(r'\s+', ' ', text)
        return text
    
    def remove_punctuation(self, text):
        """
        移除标点符号
        
        Args:
            text: 文本
            
        Returns:
            移除标点符号的文本
        """
        return re.sub(r'[\p{P}\p{S}]', '', text)
    
    def replace_text(self, text, old, new):
        """
        替换文本
        
        Args:
            text: 文本
            old: 要替换的内容
            new: 替换为的内容
            
        Returns:
            替换后的文本
        """
        return text.replace(old, new)
    
    def search_text(self, text, pattern):
        """
        搜索文本
        
        Args:
            text: 文本
            pattern: 搜索模式
            
        Returns:
            匹配结果列表
        """
        matches = re.findall(pattern, text)
        return matches
    
    def extract_emails(self, text):
        """
        提取邮箱
        
        Args:
            text: 文本
            
        Returns:
            邮箱列表
        """
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)
    
    def extract_phone_numbers(self, text):
        """
        提取电话号码
        
        Args:
            text: 文本
            
        Returns:
            电话号码列表
        """
        pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        return re.findall(pattern, text)
    
    def summarize(self, text, max_sentences=3):
        """
        文本摘要
        
        Args:
            text: 文本
            max_sentences: 最大句子数
            
        Returns:
            摘要
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        summary = '. '.join(sentences[:max_sentences]) + '.'
        return summary

def main():
    """
    主函数
    """
    parser = argparse.ArgumentParser(description='文本处理工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 统计命令
    stats_parser = subparsers.add_parser('stats', help='统计文本信息')
    stats_parser.add_argument('file', help='输入文件')
    
    # 转换命令
    convert_parser = subparsers.add_parser('convert', help='转换文本')
    convert_parser.add_argument('file', help='输入文件')
    convert_parser.add_argument('output', help='输出文件')
    convert_parser.add_argument('--uppercase', action='store_true', help='转换为大写')
    convert_parser.add_argument('--lowercase', action='store_true', help='转换为小写')
    convert_parser.add_argument('--capitalize', action='store_true', help='首字母大写')
    convert_parser.add_argument('--title', action='store_true', help='标题大小写')
    
    # 清理命令
    clean_parser = subparsers.add_parser('clean', help='清理文本')
    clean_parser.add_argument('file', help='输入文件')
    clean_parser.add_argument('output', help='输出文件')
    clean_parser.add_argument('--whitespace', action='store_true', help='移除多余空白')
    clean_parser.add_argument('--punctuation', action='store_true', help='移除标点符号')
    
    # 替换命令
    replace_parser = subparsers.add_parser('replace', help='替换文本')
    replace_parser.add_argument('file', help='输入文件')
    replace_parser.add_argument('output', help='输出文件')
    replace_parser.add_argument('old', help='要替换的内容')
    replace_parser.add_argument('new', help='替换为的内容')
    
    # 搜索命令
    search_parser = subparsers.add_parser('search', help='搜索文本')
    search_parser.add_argument('file', help='输入文件')
    search_parser.add_argument('pattern', help='搜索模式')
    
    # 提取命令
    extract_parser = subparsers.add_parser('extract', help='提取信息')
    extract_parser.add_argument('file', help='输入文件')
    extract_parser.add_argument('type', choices=['emails', 'phones'], help='提取类型')
    
    # 摘要命令
    summarize_parser = subparsers.add_parser('summarize', help='生成文本摘要')
    summarize_parser.add_argument('file', help='输入文件')
    summarize_parser.add_argument('--sentences', type=int, default=3, help='摘要句子数')
    
    args = parser.parse_args()
    
    processor = TextProcessor()
    
    if args.command == 'stats':
        content = processor.read_file(args.file)
        if content:
            print(f"单词数: {processor.count_words(content)}")
            print(f"行数: {processor.count_lines(content)}")
            print(f"字符数: {processor.count_characters(content)}")
            print(f"句子数: {processor.count_sentences(content)}")
    
    elif args.command == 'convert':
        content = processor.read_file(args.file)
        if content:
            if args.uppercase:
                content = processor.to_uppercase(content)
            elif args.lowercase:
                content = processor.to_lowercase(content)
            elif args.capitalize:
                content = processor.capitalize(content)
            elif args.title:
                content = processor.title_case(content)
            processor.write_file(args.output, content)
    
    elif args.command == 'clean':
        content = processor.read_file(args.file)
        if content:
            if args.whitespace:
                content = processor.remove_whitespace(content)
            elif args.punctuation:
                content = processor.remove_punctuation(content)
            processor.write_file(args.output, content)
    
    elif args.command == 'replace':
        content = processor.read_file(args.file)
        if content:
            content = processor.replace_text(content, args.old, args.new)
            processor.write_file(args.output, content)
    
    elif args.command == 'search':
        content = processor.read_file(args.file)
        if content:
            matches = processor.search_text(content, args.pattern)
            print(f"找到 {len(matches)} 个匹配:")
            for match in matches:
                print(f"- {match}")
    
    elif args.command == 'extract':
        content = processor.read_file(args.file)
        if content:
            if args.type == 'emails':
                emails = processor.extract_emails(content)
                print(f"找到 {len(emails)} 个邮箱:")
                for email in emails:
                    print(f"- {email}")
            elif args.type == 'phones':
                phones = processor.extract_phone_numbers(content)
                print(f"找到 {len(phones)} 个电话号码:")
                for phone in phones:
                    print(f"- {phone}")
    
    elif args.command == 'summarize':
        content = processor.read_file(args.file)
        if content:
            summary = processor.summarize(content, args.sentences)
            print("摘要:")
            print(summary)

if __name__ == "__main__":
    main()
