#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 18: 项目实践7 - 密码生成器

本文件实现一个密码生成器工具
"""

import random
import string
import argparse

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_symbols=True, exclude_chars=''):
    """
    生成密码
    
    Args:
        length: 密码长度
        include_uppercase: 是否包含大写字母
        include_lowercase: 是否包含小写字母
        include_digits: 是否包含数字
        include_symbols: 是否包含符号
        exclude_chars: 要排除的字符
        
    Returns:
        生成的密码
    """
    # 构建字符集
    char_set = ''
    
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_lowercase:
        char_set += string.ascii_lowercase
    if include_digits:
        char_set += string.digits
    if include_symbols:
        char_set += string.punctuation
    
    # 排除指定字符
    if exclude_chars:
        char_set = ''.join([c for c in char_set if c not in exclude_chars])
    
    # 检查字符集是否为空
    if not char_set:
        raise ValueError("字符集为空，请至少选择一种字符类型")
    
    # 生成密码
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def generate_multiple_passwords(count=5, length=12, include_uppercase=True, 
                             include_lowercase=True, include_digits=True, 
                             include_symbols=True, exclude_chars=''):
    """
    生成多个密码
    
    Args:
        count: 密码数量
        length: 密码长度
        include_uppercase: 是否包含大写字母
        include_lowercase: 是否包含小写字母
        include_digits: 是否包含数字
        include_symbols: 是否包含符号
        exclude_chars: 要排除的字符
        
    Returns:
        密码列表
    """
    passwords = []
    for _ in range(count):
        password = generate_password(length, include_uppercase, include_lowercase, 
                                   include_digits, include_symbols, exclude_chars)
        passwords.append(password)
    return passwords

def check_password_strength(password):
    """
    检查密码强度
    
    Args:
        password: 密码
        
    Returns:
        强度评分和建议
    """
    score = 0
    suggestions = []
    
    # 长度检查
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("密码长度至少为8个字符")
    
    # 大写字母检查
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("添加大写字母")
    
    # 小写字母检查
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("添加小写字母")
    
    # 数字检查
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("添加数字")
    
    # 符号检查
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("添加符号")
    
    # 强度等级
    if score >= 6:
        strength = "强"
    elif score >= 4:
        strength = "中等"
    else:
        strength = "弱"
    
    return score, strength, suggestions

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='密码生成器')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 生成密码命令
    generate_parser = subparsers.add_parser('generate', help='生成密码')
    generate_parser.add_argument('-l', '--length', type=int, default=12, help='密码长度')
    generate_parser.add_argument('-c', '--count', type=int, default=1, help='生成密码数量')
    generate_parser.add_argument('--no-uppercase', action='store_true', help='不包含大写字母')
    generate_parser.add_argument('--no-lowercase', action='store_true', help='不包含小写字母')
    generate_parser.add_argument('--no-digits', action='store_true', help='不包含数字')
    generate_parser.add_argument('--no-symbols', action='store_true', help='不包含符号')
    generate_parser.add_argument('--exclude', default='', help='要排除的字符')
    
    # 检查密码强度命令
    check_parser = subparsers.add_parser('check', help='检查密码强度')
    check_parser.add_argument('password', help='要检查的密码')
    
    args = parser.parse_args()
    
    if args.command == 'generate':
        # 生成密码
        passwords = generate_multiple_passwords(
            count=args.count,
            length=args.length,
            include_uppercase=not args.no_uppercase,
            include_lowercase=not args.no_lowercase,
            include_digits=not args.no_digits,
            include_symbols=not args.no_symbols,
            exclude_chars=args.exclude
        )
        
        print("生成的密码:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")
            # 检查强度
            score, strength, suggestions = check_password_strength(password)
            print(f"   强度: {strength} (评分: {score}/6)")
            if suggestions:
                print(f"   建议: {', '.join(suggestions)}")
    
    elif args.command == 'check':
        # 检查密码强度
        score, strength, suggestions = check_password_strength(args.password)
        print(f"密码: {args.password}")
        print(f"强度: {strength} (评分: {score}/6)")
        if suggestions:
            print("建议:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

if __name__ == "__main__":
    main()
