from data_explorer.report import generate_report
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python run.py <数据文件路径>")
    else:
        generate_report(sys.argv[1])