import pandas as pd
import numpy as np
import math

# Series 索引与切片
data = pd.Series(np.arange(10), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print("------------------------------Series 索引与切片")
print(data['a']) ## 如果索引不存在就会抛出异常
print("------------------------------Series 索引与切片")
print(data[['a', 'b']]) ## 可以同时获取多个索引对应的值
print("------------------------------Series 索引与切片")
print(data['a': 'd'])  ## 可以使用切片的方式获取数据，包含起始索引
print("------------------------------Series 索引与切片")
print(data[1:3]) ## 可以使用切片的方式获取数据



## DataFrame 索引与切片
data = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])

print("------------------------------DataFrame 索引与切片")
print(data)
print("------------------------------DataFrame 索引与切片")
print(data['A']) ## 获取单列
print("------------------------------DataFrame 索引与切片")
print(data[['A', 'B']]) ## 获取多列
print("------------------------------DataFrame 索引与切片")
print(data['a': 'c']) ## 获取多行
print("------------------------------DataFrame 索引与切片")
print(data[1:3]) ## 获取多行

# loc[普通行索引操作，普通列索引操作]
# iloc[位置行索引，位置列索引]，位置索引就是最左侧从 0 开始的索引，也就是笛卡尔坐标系的索引
print("------------------------------DataFrame 索引与切片")
print(data.loc[:,'A'])
print("------------------------------DataFrame 索引与切片")
print(data.iloc[0])

print("------------------------------DataFrame 索引与切片")
print(data.loc['a':'c', 'A':'C'])

print("------------------------------DataFrame 索引与切片")
print(data.iloc[0:2, 0:2])


# isin返回结果为相应的位置是否匹配给出的 values
print("------------------------------DataFrame 索引与切片")
print(data.isin([15, 16]))  ## 返回的是一个 DataFrame，每个元素都表示是否匹配
print("------------------------------DataFrame 索引与切片")
print(data.loc['a'].isin([1, 4]))

print("------------------------------DataFrame 索引与切片")
print(data)
print(data.isin({
    'A': [1,4],  ## 这里的 1, 4 是在 A 列中查找的
    'B': [5, 6]
}))


## query使用Boolean值表达式进行筛选
# df.query(expr, inplace=False)，在表达式中使用@符合可以引用变量
print(data[data['A'] >= 5]) # 老方式进行过滤

print("------------------------------DataFrame 筛选")
print(data.query('A >= 5'))  ## 新方式进行过滤
print("------------------------------DataFrame 筛选")
minAge = 5
maxAge = 10
print(data.query('A >= @minAge and B < @maxAge'))  ## 可以使用 and, or, not 等运算符
print(data.query('A >= @minAge and B < @maxAge and C == 7').index) # 筛选出 A >= 5 且 B < 10 且 C == 7 的行索引


# 排序

# 按照索引排序：df.sort_index(level, ascending, inplace, na_position)
# level：要排序的索引层级，默认0，指定使用哪个索引进行排序
# ascending：True升序，False降序，默认True
# inplace：True在原数据上操作，False返回新的DataFrame
# na_position：{‘first’，‘last’}，缺失值位置，默认‘last’

# 使用变量值进行排序： df.sort_values(by, ascending, inplace, na_position)
# by：要排序的列索引
# ascending：True升序，False降序，默认True
# inplace：True在原数据上操作，False返回新的DataFrame
# na_position：{‘first’，‘last’}，缺失值位置，默认‘last’

seriesData = pd.Series([5,1,3,4,2], index=['e', 'd', 'c', 'b', 'a'])
print("------------------------------DataFrame 排序")
print(seriesData.sort_index())

print("------------------------------DataFrame 排序")
print(seriesData.sort_values())

print(data)
data['sum'] = data['A'].apply(lambda x: math.sqrt(x)) # apply: 对每一个元素进行操作
print("------------------------------DataFrame 排序")
print(data)

data['A'] = 1
print(data['A'].replace(1, 10))
print("------------------------------DataFrame 排序")
print(data)

data['B'].replace({6: 60, 11: 110}, inplace=True)
print("------------------------------DataFrame 排序")
print(data)

data['C'].replace([2, 7], [20, 70], inplace=True)
print("------------------------------DataFrame 排序")
print(data)


data = pd.DataFrame(np.arange(20).reshape(4,5), columns=['A', 'B', 'C', 'D', 'E'], index=['a', 'b', 'c', 'd'])

# 使用data['A'] > 0生成的布尔 Series 作为索引，从原始 DataFrame 中选择所有对应位置为 True 的行
temp = data[data['A'] > 0]
print(temp)
