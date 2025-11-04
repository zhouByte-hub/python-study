import pandas as pd
import numpy as np

# 虚拟变量变换， 常在回归分析中使用
# get_dummies(data, prefix, prefix_sep, dummy_na, columns, drop_first)
# data: 要进行虚拟变量变换的 DataFrame
# prefix: 虚拟变量的前缀
# prefix_sep: 虚拟变量的分隔符
# dummy_na: 是否将 NaN 也转换为虚拟变量
# columns: 要进行虚拟变量变换的列
# drop_first: 是否删除第一个虚拟变量

data = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
print(data)
print(pd.get_dummies(data['B'], prefix="prefix", prefix_sep="_"))
print("===========================")
print(pd.get_dummies(data, columns=['B'], prefix="prefix", prefix_sep="_"))


# 数值变量分段
# pd.cut(x, bins, right, labels, include_lowest)
# x: 要分段的数值变量
# bins: 分段的边界值
# right: 是否包含右边界
# labels: 分段的标签
# include_lowest: 是否包含最小值
print("-----------------------------")
data['sign'] = pd.qcut(data['A'], q=2)
print(data) # 将每一行的 A 列进行分位数分段，q=2 表示分成 2 组

print("-----------------------------")
# print(pd.cut(data['A'], bins=[0, 5, 10])) # 将 A 列进行分段，分段的边界值为 0, 5, 10

# 数据分组
# groupby(by, level, as_indx, sort)
# by: 分组的依据
# level: 分组的层级
# as_indx: 是否将分组的依据作为索引
# sort: 是否对分组的结果进行排序
group = data.groupby('A') # 对 A 列进行分组
print(group)
print("分组的结果：")
print(group.groups) # 查看分组的结果
print(group.describe()) # 查看分组的统计描述

print("-----------------------------")
# 分组汇总
# agg(func)
# func: 汇总函数， max、count 等
print(group.agg('max')) # 对分组的结果进行最大值汇总

print("-----------------------------")

def get_fun(series) -> int:
    """自定义聚合函数，返回最小值"""
    return series.min()

print(group.agg(get_fun)) # 对分组的结果进行自定义汇总


## 多个 DataFrame 合并
data1 = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
data2 = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
print("--------------------------------纵向合并")
print(pd.concat([data1, data2])) # 合并两个 DataFrame


# 横向合并
print("--------------------------------横向合并")
print(pd.concat([data1, data2], axis=1)) # 合并两个 DataFrame
print("--------------------------------横向合并")
print(pd.merge(data1, data2)) # 合并两个 DataFrame，默认是基于索引进行合并


data = pd.Series([1, 2, None, 4, 5, np.nan])
# print(data.isnull()) # 检查是否为空值
# print(data.isna()) # 检查是否为空值
# print(data.notnull()) # 检查是否不为空值
print(data[data.notna()]) # 输出不为空值的元素

print("-----------------------------")
print(data.isna().all()) # 检查是否所有元素都为空值
print("-----------------------------")
print(data.isna().any()) # 检查是否存在空值
print("-----------------------------")


## 填充缺省值
# data.fillna(0, inplace=True) # 用 0 填充空值
data.fillna(method='ffill', inplace=True) # 用前一个非空值填充空值
print(data)

print(data.dropna()) # 删除空值

print("-----------------------------")

data = pd.Series([1,1,2,3,4,5])
print(data.duplicated()) # 检查是否重复