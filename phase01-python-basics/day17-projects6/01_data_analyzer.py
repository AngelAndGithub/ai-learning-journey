#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 17: 项目实践6 - 数据统计工具

本文件实现一个数据统计工具，支持基本的统计分析功能
"""

import csv
import json
import argparse
import statistics
from collections import Counter

class DataAnalyzer:
    """数据统计分析工具类"""
    
    def load_csv(self, file_path):
        """
        加载CSV文件
        
        Args:
            file_path: CSV文件路径
            
        Returns:
            数据列表
        """
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
            print(f"成功加载CSV文件: {file_path}")
            print(f"共 {len(data)} 条记录")
        except Exception as e:
            print(f"加载CSV文件失败: {e}")
        return data
    
    def load_json(self, file_path):
        """
        加载JSON文件
        
        Args:
            file_path: JSON文件路径
            
        Returns:
            数据
        """
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"成功加载JSON文件: {file_path}")
            if isinstance(data, list):
                print(f"共 {len(data)} 条记录")
        except Exception as e:
            print(f"加载JSON文件失败: {e}")
        return data
    
    def get_column_data(self, data, column):
        """
        获取指定列的数据
        
        Args:
            data: 数据列表
            column: 列名
            
        Returns:
            列数据列表
        """
        column_data = []
        for row in data:
            if column in row:
                value = row[column]
                # 尝试转换为数值
                try:
                    value = float(value)
                except ValueError:
                    pass
                column_data.append(value)
        return column_data
    
    def calculate_statistics(self, data):
        """
        计算基本统计量
        
        Args:
            data: 数值列表
            
        Returns:
            统计结果字典
        """
        # 过滤非数值数据
        numeric_data = [x for x in data if isinstance(x, (int, float))]
        
        if not numeric_data:
            return {"error": "No numeric data found"}
        
        stats = {
            "count": len(numeric_data),
            "mean": statistics.mean(numeric_data),
            "median": statistics.median(numeric_data),
            "min": min(numeric_data),
            "max": max(numeric_data),
            "sum": sum(numeric_data)
        }
        
        try:
            stats["mode"] = statistics.mode(numeric_data)
        except statistics.StatisticsError:
            stats["mode"] = "No unique mode"
        
        try:
            stats["std"] = statistics.stdev(numeric_data)
        except statistics.StatisticsError:
            stats["std"] = 0
        
        return stats
    
    def count_frequency(self, data):
        """
        计算频率分布
        
        Args:
            data: 数据列表
            
        Returns:
            频率分布字典
        """
        counter = Counter(data)
        return dict(counter)
    
    def analyze_column(self, data, column):
        """
        分析指定列
        
        Args:
            data: 数据列表
            column: 列名
        """
        print(f"\n分析列: {column}")
        column_data = self.get_column_data(data, column)
        
        if not column_data:
            print(f"列 {column} 不存在或无数据")
            return
        
        # 计算统计量
        stats = self.calculate_statistics(column_data)
        if "error" not in stats:
            print("基本统计量:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
        
        # 计算频率分布
        frequency = self.count_frequency(column_data)
        print("\n频率分布:")
        for item, count in frequency.items():
            print(f"  {item}: {count}")
    
    def analyze_file(self, file_path, columns=None):
        """
        分析文件
        
        Args:
            file_path: 文件路径
            columns: 要分析的列列表
        """
        # 根据文件扩展名选择加载方法
        if file_path.endswith('.csv'):
            data = self.load_csv(file_path)
        elif file_path.endswith('.json'):
            data = self.load_json(file_path)
        else:
            print(f"不支持的文件格式: {file_path}")
            return
        
        if not data:
            return
        
        # 获取所有列名
        if isinstance(data, list) and data:
            if isinstance(data[0], dict):
                all_columns = list(data[0].keys())
                print(f"\n文件包含以下列: {', '.join(all_columns)}")
                
                # 分析指定列或所有列
                if columns:
                    for column in columns:
                        self.analyze_column(data, column)
                else:
                    for column in all_columns:
                        self.analyze_column(data, column)
    
    def generate_report(self, file_path, output_file):
        """
        生成分析报告
        
        Args:
            file_path: 输入文件路径
            output_file: 输出报告文件路径
        """
        # 加载数据
        if file_path.endswith('.csv'):
            data = self.load_csv(file_path)
        elif file_path.endswith('.json'):
            data = self.load_json(file_path)
        else:
            print(f"不支持的文件格式: {file_path}")
            return
        
        if not data:
            return
        
        # 生成报告
        report = f"# 数据统计分析报告\n\n"
        report += f"## 基本信息\n"
        report += f"- 数据文件: {file_path}\n"
        report += f"- 记录数: {len(data)}\n\n"
        
        if isinstance(data, list) and data and isinstance(data[0], dict):
            all_columns = list(data[0].keys())
            report += f"## 列信息\n"
            report += f"- 列数: {len(all_columns)}\n"
            report += f"- 列名: {', '.join(all_columns)}\n\n"
            
            # 分析每一列
            for column in all_columns:
                column_data = self.get_column_data(data, column)
                stats = self.calculate_statistics(column_data)
                frequency = self.count_frequency(column_data)
                
                report += f"## 列: {column}\n"
                
                if "error" not in stats:
                    report += "### 基本统计量\n"
                    for key, value in stats.items():
                        report += f"- {key}: {value}\n"
                
                report += "### 频率分布\n"
                for item, count in frequency.items():
                    report += f"- {item}: {count}\n"
                
                report += "\n"
        
        # 保存报告
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"报告已生成: {output_file}")
        except Exception as e:
            print(f"生成报告失败: {e}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='数据统计分析工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 分析命令
    analyze_parser = subparsers.add_parser('analyze', help='分析文件')
    analyze_parser.add_argument('file', help='输入文件路径')
    analyze_parser.add_argument('--columns', nargs='+', help='要分析的列列表')
    
    # 生成报告命令
    report_parser = subparsers.add_parser('report', help='生成分析报告')
    report_parser.add_argument('file', help='输入文件路径')
    report_parser.add_argument('output', help='输出报告文件路径')
    
    args = parser.parse_args()
    
    analyzer = DataAnalyzer()
    
    if args.command == 'analyze':
        analyzer.analyze_file(args.file, args.columns)
    elif args.command == 'report':
        analyzer.generate_report(args.file, args.output)

if __name__ == "__main__":
    main()
