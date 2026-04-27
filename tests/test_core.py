import pytest
import pandas as pd
from data_explorer.core import load_data, basic_info, descriptive_stats


def test_load_data(tmp_path):
    # 创建临时 CSV 文件
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
    csv_path = tmp_path / "test.csv"
    df.to_csv(csv_path, index=False)

    loaded = load_data(str(csv_path))
    pd.testing.assert_frame_equal(df, loaded)


def test_basic_info():
    df = pd.DataFrame({'A': [1, 2], 'B': [3.0, 4.0]})
    info = basic_info(df)
    assert info['行数'] == 2
    assert info['列数'] == 2
    assert 'A' in info['列名']


def test_descriptive_stats():
    df = pd.DataFrame({'num': [1, 2, 3, 4]})
    stats = descriptive_stats(df)
    assert stats.loc['mean', 'num'] == 2.5