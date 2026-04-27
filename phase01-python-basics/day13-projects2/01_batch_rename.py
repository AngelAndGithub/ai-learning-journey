#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 13: 项目实践2 - 批量重命名工具

本文件实现一个批量重命名文件的工具
"""

import os
import argparse
import re

def batch_rename(directory, pattern, replacement, file_extension=None, recursive=False, dry_run=False):
    """
    批量重命名文件
    
    Args:
        directory: 要重命名文件的目录
        pattern: 要匹配的正则表达式模式
        replacement: 替换字符串
        file_extension: 只处理特定扩展名的文件
        recursive: 是否递归处理子目录
        dry_run: 是否只显示将要执行的操作而不实际执行
    """
    renamed_count = 0
    
    def process_directory(current_dir):
        nonlocal renamed_count
        
        print(f"处理目录: {current_dir}")
        
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            
            if os.path.isdir(item_path) and recursive:
                process_directory(item_path)
            elif os.path.isfile(item_path):
                # 检查文件扩展名
                if file_extension:
                    ext = os.path.splitext(item)[1].lower()
                    if ext != f".{file_extension.lower()}":
                        continue
                
                # 应用正则表达式替换
                new_name = re.sub(pattern, replacement, item)
                
                if new_name != item:
                    new_path = os.path.join(current_dir, new_name)
                    
                    # 检查新文件名是否已存在
                    counter = 1
                    base_name, ext = os.path.splitext(new_name)
                    while os.path.exists(new_path):
                        new_name = f"{base_name}_{counter}{ext}"
                        new_path = os.path.join(current_dir, new_name)
                        counter += 1
                    
                    print(f"{item} -> {new_name}")
                    
                    if not dry_run:
                        try:
                            os.rename(item_path, new_path)
                            renamed_count += 1
                        except Exception as e:
                            print(f"重命名失败: {e}")
    
    # 处理指定目录
    process_directory(directory)
    
    print(f"\n处理完成，共重命名 {renamed_count} 个文件")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='批量重命名文件工具')
    parser.add_argument('directory', help='要处理的目录')
    parser.add_argument('pattern', help='要匹配的正则表达式模式')
    parser.add_argument('replacement', help='替换字符串')
    parser.add_argument('-e', '--extension', help='只处理特定扩展名的文件')
    parser.add_argument('-r', '--recursive', action='store_true', help='递归处理子目录')
    parser.add_argument('-d', '--dry-run', action='store_true', help='只显示将要执行的操作而不实际执行')
    
    args = parser.parse_args()
    
    # 检查目录是否存在
    if not os.path.exists(args.directory):
        print(f"错误: 目录 {args.directory} 不存在")
        return
    
    if not os.path.isdir(args.directory):
        print(f"错误: {args.directory} 不是一个目录")
        return
    
    # 执行批量重命名
    batch_rename(
        directory=args.directory,
        pattern=args.pattern,
        replacement=args.replacement,
        file_extension=args.extension,
        recursive=args.recursive,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()
