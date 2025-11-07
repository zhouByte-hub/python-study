# RFM：会员价值评估模型（评估用户的价值情况），是一种经典的客户价值分析模型，广泛应用于市场营销、客户关系管理（CRM）和用户运营等领域。
# 它的核心思想是通过三个关键指标对客户进行细分，从而识别高价值客户、潜在流失客户等不同群体，帮助企业制定更有针对性的策略。
# R：Recency：最近一次消费时间。
# F：Frequency：消费频率
# M：Monetary：消费金额

# RFM模型的应用步骤：
# 1.数据准备：收集客户的历史交易数据，包括客户ID、交易时间、交易金额等。
# 2.计算 RFM 指标：
#   2.1 计算 Recency：计算客户最近一次交易的时间，与当前时间的差值，单位为天。
#   2.2 计算 Frequency：计算客户在一段时间内的交易次数。
#   2.3 计算 Monetary：计算客户在一段时间内的交易金额总和。
# 3.打分（通常为 1-5 分）对每个指标进行分位数划分（如五分位），给每个客户在 R、F、M 三个指标上分别打分。
# 注意：R是越小越好，所以最近购买的客户 R 分高；F和 M 是越大越好，消费越多分越高。
# 4.客户分类：
#   4.1 高价值客户：R 分高、F 分高、M 分高。
#   4.2 中等价值客户：R 分中等、F 分中等、M 分中等。
#   4.3 低价值客户：R 分低、F 分低、M 分低。


import pandas as pd
import numpy as np
import os

sheet_names = ['2015', '2016', '2017', '2018', '会员等级']
# 1. 加载数据
current_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件所在目录

sales_data = pd.read_excel(os.path.join(current_dir, "files", "sales.xlsx"), sheet_name=sheet_names)

for sheet_name in sheet_names[:-1]:
    # print(sales_data[sheet_name].info()) # 通过info函数查看是否存在缺失值
    # print(sales_data[sheet_name].describe())  # 通过describe函数查看数据是否存在非法数据
    
    # 2. 数据预处理
    sales_data[sheet_name].dropna(inplace=True)
    sales_data[sheet_name] = sales_data[sheet_name][sales_data[sheet_name]['订单金额'] > 1]

    # 固定 Recency，以年为单位，获取该用户在这一年最后一次下单的时间
    sales_data[sheet_name]['max_year_data'] = sales_data[sheet_name]['提交日期'].max()

# 3. 将上述表合并: 将多张表合并时，索引依旧使用各自表中的索引，所以需要忽略索引
df_merge = pd.concat(list(sales_data.values())[:-1], ignore_index=True)

# 4. 添加统计字段
df_merge['year'] = df_merge['提交日期'].dt.year
df_merge['data_interval'] = (df_merge['max_year_data'] - df_merge['提交日期']).dt.days

# 5. 数据统计分析
# 5.1 按会员 ID 和年份进行分区统计 RFM 三项基本数据
rfm_gb = df_merge.groupby(['会员ID', 'year'], as_index=False).agg({
    'data_interval': 'min',  # Recency：最近一次消费时间
    '订单号': 'count',         # Frequency：消费频率
    '订单金额': 'sum'          # Monetary：消费金额
})
rfm_gb.columns = ['会员ID', 'year', 'Recency', 'Frequency', 'Monetary']

# print(rfm_gb.head(10))

# 5.2 划分区间：r：最近一次购买，越小分越高，f：消费频率，越大分越高，m：消费金额，越大分越高
# 思路：由我们给出区间数，由系统自动划分区间范围
print(rfm_gb.iloc[:, 2:].describe().T) # T是行列转置

# 根据 62 行中的 describe 统计结果中的 min、25%、75%、max 四个值划分成三区间[0, 79), [79, 255), [255, 365)
r_bins = [-1, 79, 255, 365]
f_bins = [0, 2, 5, 130]
m_bins = [1, 69, 1199, 206251]

rfm_gb["Recency_Score"] = pd.cut(rfm_gb["Recency"], bins=r_bins, labels=[i for i in range(len(r_bins)- 1, 0, -1)])
rfm_gb["Frequency_Score"] = pd.cut(rfm_gb["Frequency"], bins=f_bins, labels=[i for i in range(1, len(f_bins))])
rfm_gb["Monetary_Score"] = pd.cut(rfm_gb["Monetary"], bins=m_bins, labels=[i for i in range(1, len(m_bins))])

# 6. 客户价值评估
rfm_gb["RFM_Score"] = rfm_gb["Recency_Score"].astype(str) + rfm_gb["Frequency_Score"].astype(str) + rfm_gb["Monetary_Score"].astype(str)

print(rfm_gb.head(10))

# 7. 导出数据
rfm_gb.to_excel(os.path.join(current_dir, "files", "rfm.xlsx"), index=False)
    

