#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 16: 项目实践5 - 文件处理工具

本文件实现一个文件处理工具，支持文件合并、分割、统计等功能
"""

import os
import argparse
import shutil

class FileProcessor:
    """文件处理工具类"""
    
    def merge_files(self, input_files, output_file):
        """
        合并多个文件
        
        Args:
            input_files: 输入文件列表
            output_file: 输出文件路径
        """
        print(f"正在合并 {len(input_files)} 个文件到 {output_file}")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as out_f:
                for i, input_file in enumerate(input_files, 1):
                    print(f"处理文件 {i}/{len(input_files)}: {input_file}")
                    try:
                        with open(input_file, 'r', encoding='utf-8') as in_f:
                            content = in_f.read()
                            out_f.write(content)
                            out_f.write('\n')  # 在文件之间添加换行
                    except Exception as e:
                        print(f"读取文件 {input_file} 失败: {e}")
            print(f"文件合并完成: {output_file}")
        except Exception as e:
            print(f"合并文件失败: {e}")
    
    def split_file(self, input_file, output_dir, chunk_size=1024*1024):
        """
        分割文件
        
        Args:
            input_file: 输入文件路径
            output_dir: 输出目录
            chunk_size: 每个块的大小（字节）
        """
        print(f"正在分割文件 {input_file} 到 {output_dir}")
        
        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        try:
            with open(input_file, 'rb') as f:
                chunk_num = 1
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    
                    output_file = os.path.join(output_dir, f"{os.path.basename(input_file)}.part{chunk_num}")
                    with open(output_file, 'wb') as out_f:
                        out_f.write(chunk)
                    
                    print(f"创建块 {chunk_num}: {output_file}")
                    chunk_num += 1
            
            print(f"文件分割完成，共创建 {chunk_num-1} 个块")
        except Exception as e:
            print(f"分割文件失败: {e}")
    
    def count_lines(self, input_file):
        """
        统计文件行数
        
        Args:
            input_file: 输入文件路径
            
        Returns:
            行数
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                line_count = sum(1 for line in f)
            print(f"文件 {input_file} 共有 {line_count} 行")
            return line_count
        except Exception as e:
            print(f"统计行数失败: {e}")
            return 0
    
    def count_words(self, input_file):
        """
        统计文件单词数
        
        Args:
            input_file: 输入文件路径
            
        Returns:
            单词数
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
                word_count = len(content.split())
            print(f"文件 {input_file} 共有 {word_count} 个单词")
            return word_count
        except Exception as e:
            print(f"统计单词数失败: {e}")
            return 0
    
    def copy_file(self, source, destination):
        """
        复制文件
        
        Args:
            source: 源文件路径
            destination: 目标文件路径
        """
        try:
            shutil.copy2(source, destination)
            print(f"文件已复制: {source} -> {destination}")
        except Exception as e:
            print(f"复制文件失败: {e}")
    
    def move_file(self, source, destination):
        """
        移动文件
        
        Args:
            source: 源文件路径
            destination: 目标文件路径
        """
        try:
            shutil.move(source, destination)
            print(f"文件已移动: {source} -> {destination}")
        except Exception as e:
            print(f"移动文件失败: {e}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='文件处理工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 合并文件命令
    merge_parser = subparsers.add_parser('merge', help='合并多个文件')
    merge_parser.add_argument('output', help='输出文件')
    merge_parser.add_argument('inputs', nargs='+', help='输入文件列表')
    
    # 分割文件命令
    split_parser = subparsers.add_parser('split', help='分割文件')
    split_parser.add_argument('input', help='输入文件')
    split_parser.add_argument('output_dir', help='输出目录')
    split_parser.add_argument('--size', type=int, default=1024*1024, help='每个块的大小（字节）')
    
    # 统计行数命令
    count_lines_parser = subparsers.add_parser('count-lines', help='统计文件行数')
    count_lines_parser.add_argument('input', help='输入文件')
    
    # 统计单词数命令
    count_words_parser = subparsers.add_parser('count-words', help='统计文件单词数')
    count_words_parser.add_argument('input', help='输入文件')
    
    # 复制文件命令
    copy_parser = subparsers.add_parser('copy', help='复制文件')
    copy_parser.add_argument('source', help='源文件')
    copy_parser.add_argument('destination', help='目标文件')
    
    # 移动文件命令
    move_parser = subparsers.add_parser('move', help='移动文件')
    move_parser.add_argument('source', help='源文件')
    move_parser.add_argument('destination', help='目标文件')
    
    args = parser.parse_args()
    
    processor = FileProcessor()
    
    if args.command == 'merge':
        processor.merge_files(args.inputs, args.output)
    elif args.command == 'split':
        processor.split_file(args.input, args.output_dir, args.size)
    elif args.command == 'count-lines':
        processor.count_lines(args.input)
    elif args.command == 'count-words':
        processor.count_words(args.input)
    elif args.command == 'copy':
        processor.copy_file(args.source, args.destination)
    elif args.command == 'move':
        processor.move_file(args.source, args.destination)

if __name__ == "__main__":
    main()
