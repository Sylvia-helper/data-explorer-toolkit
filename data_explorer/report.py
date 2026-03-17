from jinja2 import Template
from .core import load_data, basic_info, descriptive_stats, missing_values_analysis, correlation_analysis
from .visualization import plot_distribution, plot_correlation_heatmap, plot_missing_heatmap

# 修改后的HTML模板，添加了meta编码声明和样式
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>数据分析报告</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', 'SimHei', 'PingFang SC', 'STHeiti', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 3px solid #3498db;
            margin-bottom: 30px;
        }
        h2 {
            color: #34495e;
            background-color: #ecf0f1;
            padding: 10px 15px;
            border-left: 5px solid #3498db;
            border-radius: 0 5px 5px 0;
            margin-top: 30px;
        }
        h3 {
            color: #7f8c8d;
            margin: 20px 0 10px 0;
            padding-left: 10px;
            border-left: 3px solid #bdc3c7;
        }
        .section {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        pre {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
        }
        .plot-container {
            margin: 20px 0;
            padding: 15px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .info-box {
            background-color: #e8f4f8;
            border: 1px solid #b8e0f0;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        p {
            margin: 10px 0;
        }
        .stats-table {
            border-collapse: collapse;
            width: 100%;
        }
        .stats-table td, .stats-table th {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        .stats-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .stats-table th {
            background-color: #3498db;
            color: white;
        }
    </style>
</head>
<body>
    <h1>📊 数据集探索性分析报告</h1>

    <div class="section">
        <h2>📋 1. 数据集概览</h2>
        <div class="info-box">
            <p><strong>📏 行数:</strong> {{ basic_info.行数 }}, <strong>📐 列数:</strong> {{ basic_info.列数 }}</p>
            <p><strong>📑 列名:</strong> {{ basic_info.列名 | join(', ') }}</p>
            <p><strong>🔤 数据类型:</strong></p>
            <ul>
            {% for col, dtype in basic_info.数据类型.items() %}
                <li><strong>{{ col }}:</strong> {{ dtype }}</li>
            {% endfor %}
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>📈 2. 描述性统计</h2>
        <div class="plot-container">
            <pre>{{ descriptive_stats }}</pre>
        </div>
    </div>

    <div class="section">
        <h2>❓ 3. 缺失值分析</h2>
        <div class="plot-container">
            <pre>{{ missing_values }}</pre>
        </div>
        {% if missing_heatmap %}
        <div class="plot-container">
            <h3>缺失值热力图</h3>
            {{ missing_heatmap }}
        </div>
        {% endif %}
    </div>

    <div class="section">
        <h2>🔄 4. 相关性分析</h2>
        {% if correlation_heatmap %}
        <div class="plot-container">
            {{ correlation_heatmap }}
        </div>
        {% endif %}
    </div>

    <div class="section">
        <h2>📊 5. 单变量分布</h2>
        {% for col in distributions %}
        <div class="plot-container">
            <h3>{{ col }}</h3>
            {{ distributions[col] }}
        </div>
        {% endfor %}
    </div>

    <div style="text-align: center; margin-top: 40px; color: #7f8c8d; font-size: 0.9em;">
        <p>报告生成时间: {{ generation_time }}</p>
    </div>
</body>
</html>
"""


def generate_report(filepath, output_path="report.html"):
    # 1. 读入数据
    df = load_data(filepath)

    # 2. 计算各种分析结果
    info = basic_info(df)
    stats = descriptive_stats(df)
    missing = missing_values_analysis(df)
    corr = correlation_analysis(df)

    # 3. 生成各种图
    missing_heatmap = plot_missing_heatmap(df)
    corr_heatmap = plot_correlation_heatmap(corr)

    # 4. 生成所有数值列的分布图
    distributions = {}
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        distributions[col] = plot_distribution(df, col)

    # 5. 添加生成时间
    from datetime import datetime
    generation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 6. 把所有内容塞进模板，生成最终的HTML
    template = Template(HTML_TEMPLATE)
    html_content = template.render(
        basic_info=info,
        descriptive_stats=stats,
        missing_values=missing,
        missing_heatmap=missing_heatmap,
        correlation_heatmap=corr_heatmap,
        distributions=distributions,
        generation_time=generation_time
    )

    # 7. 写入文件（使用UTF-8编码）
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f" 报告已生成: {output_path}")