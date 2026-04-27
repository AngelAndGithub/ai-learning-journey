#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 14: 项目实践3 - 日志工具

本文件实现一个灵活的日志工具
"""

import logging
import os
import datetime
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

class Logger:
    """日志工具类"""
    
    def __init__(self, name='app', level=logging.INFO, 
                 log_file=None, console=True, 
                 file_handler='rotating', max_bytes=10485760, 
                 backup_count=5, when='midnight', interval=1):
        """
        初始化日志工具
        
        Args:
            name: 日志名称
            level: 日志级别
            log_file: 日志文件路径
            console: 是否在控制台输出
            file_handler: 文件处理器类型 ('rotating' 或 'timed')
            max_bytes: 单个日志文件最大大小（仅对rotating有效）
            backup_count: 备份文件数量
            when: 日志轮转时间单位（仅对timed有效）
            interval: 日志轮转间隔（仅对timed有效）
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # 避免重复添加处理器
        if not self.logger.handlers:
            # 日志格式
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # 控制台处理器
            if console:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(level)
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)
            
            # 文件处理器
            if log_file:
                # 确保日志目录存在
                log_dir = os.path.dirname(log_file)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir)
                
                if file_handler == 'rotating':
                    # 按大小轮转
                    file_handler = RotatingFileHandler(
                        log_file, maxBytes=max_bytes, backupCount=backup_count
                    )
                else:
                    # 按时间轮转
                    file_handler = TimedRotatingFileHandler(
                        log_file, when=when, interval=interval, 
                        backupCount=backup_count, encoding='utf-8'
                    )
                
                file_handler.setLevel(level)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """调试级别日志"""
        self.logger.debug(message)
    
    def info(self, message):
        """信息级别日志"""
        self.logger.info(message)
    
    def warning(self, message):
        """警告级别日志"""
        self.logger.warning(message)
    
    def error(self, message):
        """错误级别日志"""
        self.logger.error(message)
    
    def critical(self, message):
        """严重错误级别日志"""
        self.logger.critical(message)

# 全局日志实例
_global_logger = None

def get_logger(name='app', **kwargs):
    """
    获取日志实例
    
    Args:
        name: 日志名称
        **kwargs: 其他参数
    
    Returns:
        Logger实例
    """
    global _global_logger
    if _global_logger is None:
        _global_logger = Logger(name, **kwargs)
    return _global_logger

def example():
    """示例用法"""
    print("=== 日志工具示例 ===")
    
    # 基本用法
    logger = Logger('example')
    logger.debug('这是调试信息')
    logger.info('这是信息')
    logger.warning('这是警告')
    logger.error('这是错误')
    logger.critical('这是严重错误')
    
    # 带文件输出
    log_file = f'logs/app_{datetime.datetime.now().strftime("%Y%m%d")}.log'
    file_logger = Logger(
        'file_example',
        log_file=log_file,
        file_handler='rotating',
        max_bytes=1024 * 1024,  # 1MB
        backup_count=3
    )
    file_logger.info('这是写入文件的信息')
    file_logger.error('这是写入文件的错误')
    
    # 使用全局日志
    global_logger = get_logger()
    global_logger.info('使用全局日志实例')

if __name__ == "__main__":
    example()
