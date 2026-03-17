import pandas as pd

def load_data(filepath):
    """
    读入数据文件，支持CSV和Excel。
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("不支持的文件格式，请使用CSV或Excel文件。")
    return df

def basic_info(df):
    """
    返回数据集的基本信息：行数、列数、列名、数据类型。
    """
    info = {
        "行数": df.shape[0],
        "列数": df.shape[1],
        "列名": list(df.columns),
        "数据类型": df.dtypes.to_dict()
    }
    return info
def descriptive_stats(df):
    """
    返回数值列的描述性统计信息。
    """
    return df.describe().to_dict()

def missing_values_analysis(df):
    """
    计算每列的缺失值数量和占比。
    """
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100
    return {
        "缺失数量": missing_count.to_dict(),
        "缺失占比": missing_percent.to_dict()
    }
def correlation_analysis(df):
    """
    计算数值列之间的相关系数矩阵。
    """
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr().to_dict()