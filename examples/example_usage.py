#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据探索工具包使用示例
======================
这个脚本演示了如何使用 data_explorer 包来自动分析一个 CSV 数据集，
并生成包含统计信息和交互式图表的 HTML 报告。
"""

import os
import sys

# 为了能够导入项目根目录下的 data_explorer 包（如果没有安装该包）
# 将项目根目录添加到 Python 的模块搜索路径中
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from data_explorer import generate_report

def main():
    # 1. 定义文件路径
    # 假设 sample_data.csv 与当前脚本在同一目录下
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, 'sample_data.csv')
    output_file = os.path.join(current_dir, 'report.html')

    # 2. 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"❌ 错误：找不到示例数据文件 {input_file}")
        print("请确保 sample_data.csv 文件位于 examples/ 目录下。")
        sys.exit(1)

    # 3. 生成报告
    print(f"🔍 开始分析数据：{input_file}")
    try:
        generate_report(input_file, output_path=output_file)
        print(f"✅ 成功！报告已生成：{output_file}")
        print("请用浏览器打开该 HTML 文件查看交互式分析结果。")
    except Exception as e:
        print(f"⚠️ 生成报告时出错：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()