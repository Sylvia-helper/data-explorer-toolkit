"""数据探索工具包 - 自动生成数据分析报告"""

from .report import generate_report
from .core import load_data, basic_info, descriptive_stats

__all__ = ['generate_report', 'load_data', 'basic_info', 'descriptive_stats']