import numpy as np
import pandas as pd
import json
# 数据展示设置
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列


# 读取数据
__file_path = 'data.json'

with open(__file_path, 'r', encoding='utf-8') as file:
    __data_json = json.load(file)

# 数据清洗
__data_df = pd.DataFrame()
for item in __data_json:
    # 取出数据
    data_item = item.get('data').get('diff')
    # 合并所有数据并重置索引
    __data_df = pd.concat([__data_df, pd.DataFrame(data_item)], axis=0).reset_index(drop=True)

# 处理重复值与缺失值
__data_df.dropna(how='all').drop_duplicates(inplace=True)
__data_df = __data_df.apply(lambda x: x.replace('-', None), axis=0)

# 删除无意义列
__data_df.drop(columns=['f1', 'f13', 'f124', 'f265'], inplace=True)

# 列标签重命名
rename_dict = {
    'f2': '最新价',
    'f3': '涨跌_今日',
    'f12': '股票代码',
    'f14': '公司名称',
    'f62': '今日主力流入_元',
    'f100': '所属模块',
    'f109': '涨跌_5日',
    'f160': '涨跌_10日',
    'f165': '主力净占比_5日',
    'f175': '主力净占比_10日',
    'f184': '主力净占比_今日',
    'f225': '排名_今日',
    'f263': '排名_5日',
    'f264': '排名_10日'
}
__data_df.rename(columns=rename_dict, inplace=True)

# 数据处理
# 默认数据
def query_default():
    return __data_df
# st公司查询
def query_st():
    return __data_df[__data_df['公司名称'].str.contains('ST')]

# 停牌公司查询
def query_suspend():
    return __data_df[__data_df['最新价'].isna()]

# 行业分类数量
def query_class(df):
    return df.value_counts(['所属模块'])

# 涨跌排序
def sort_change(df, period, ascending=True):
    return df.sort_values(by=f'涨跌_{period}', ascending=not ascending)

# 排名排序
def sort_ranking(df, period, ascending=True):
    return df.sort_values(by=f'排名_{period}', ascending=ascending)

# 主力流入排序
def sort_main_inflow(df, period, ascending=True):
    return df.sort_values(by=f'主力净占比_{period}', ascending=not ascending)

# 筛选'涨跌' change为1取涨，0取无涨跌，-1取跌
def query_change(df, period, change):
    if change == 1:
        return df[df[f'涨跌_{period}'] > 0]
    elif change == 0:
        return df[df[f'涨跌_{period}'] == 0]
    elif change == -1:
        return df[df[f'涨跌_{period}'] < 0]
    else:
        return df

# 行业分析
data_class = __data_df['所属模块'].value_counts().sort_values(ascending=False)
def analysis_company_class_info():
    return pd.Series({
        # 过滤空值
        'class': list(filter(lambda x: x is not None, __data_df['所属模块'].unique().tolist())),
        'mean': round(data_class.mean(), 2),
        'max': round(data_class.max(), 2),
        'min': round(data_class.min(), 2),
    })

# 行业整体数据
def analysis_company_class_data():
    return data_class.sort_values(ascending=False)

# 大于平均值行业
def analysis_company_class_above_mean():
    return data_class[data_class > data_class.mean()].sort_values(ascending=False)

# 小于平均值行业
def analysis_company_class_below_mean():
    return data_class[data_class < data_class.mean()].sort_values(ascending=False)

def get_company_class_index(start, end):
    return data_class[start:end]
# 导出数据为cvs
# __data_df.to_csv('data.csv', index=True)
# __data_df.to_excel('data.xlsx', index=True)
# print(sort_change(query_suspend(), '今日'))
# print(query_change(__data_df, '今日', 0))
# print(analysis_company_class_above_mean())
