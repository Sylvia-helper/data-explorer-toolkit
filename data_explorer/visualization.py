import plotly.express as px
import plotly.io as pio
import pandas as pd

def plot_distribution(df, column):
    """
    绘制指定列的直方图。
    """
    fig = px.histogram(df, x=column, title=f'{column} 分布')
    return pio.to_html(fig, full_html=False)

def plot_correlation_heatmap(corr_matrix):
    """
    绘制相关性热力图。
    """
    fig = px.imshow(pd.DataFrame(corr_matrix), title='相关性矩阵热力图')
    return pio.to_html(fig, full_html=False)

def plot_missing_heatmap(df):
    """
    绘制缺失值热力图。
    """
    fig = px.imshow(df.isnull(), title='缺失值热力图')
    return pio.to_html(fig, full_html=False)