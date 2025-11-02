import pandas as pd
import numpy as np

print(pd.__version__) ## 查看pandas版本
pd.options.display.max_rows = 1000 ## 显示更多行
pd.options.display.max_columns = 1000 ## 显示更多列
# print(pd.options.__dict__)


## Series 对象
a = pd.Series([1, 2, 3, 4, 5])  # 没有指定索引，默认索引为0, 1, 2, 3, 4
a = pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e'])  # 指定索引为a, b, c, d, e，index 的个数需要与数据的个数相同
a = pd.Series([1,2,3,4,5], index=list('abcde'))  # 指定索引为a, b, c, d, e
print(a)
print(a.index)  # 获取索引
print(a.values)  # 获取值


# 通过字典创建Series，默认将字典的 key作为 index，value 作为数据
stu = {
    'name': '张三', 
    'age': 18
}
print(pd.Series(stu))
# 使用字段创建 Series 的时候，指定索引，那么索引就需要是字典中的 key，否则就会得到 NaN
# print(pd.Series(stu, index=['n', 'age']))  
# print(pd.Series(stu, index = list("abc")))  # 也是拿到的 NaN



# DataFrame是Pandas中的一个表格型的数据结构，包含一组有序的列，每列可以是不同的值类型，DataFrame即有行索引也有列索引。
# DataFrame 可以被看做由 Series 组成的字典，将两个 Series 对象作为 dict 的 value 传入，就可以创建一个 DataFrame 对象。
population = {
    'bj': 123123,
    'sh': 345345,
    'gz': 567567
}
area_dict = {
    'bj': 89809,
    'sh': 888,
    'gz': 456456
}

## 通过Series 构建DataFrame，这里指明了 area 和 population 为列，所以行索引就为 bj, sh, gz
df = pd.DataFrame({
    'area': area_dict, 
    'population': population
})
## 通过这里没有指明列索引，则会对列表元素进行并集处理生成列索引，这里的列索引为bj,sh,gz，行索引为 0, 1
df = pd.DataFrame([area_dict, population])
## 可以指定行索引
df = pd.DataFrame([area_dict, population], index=['area', 'population'])
print(df)
print(df.index) # 获取行索引
print(df.columns) # 获取列索引
print(df.values) # 获取数据


## 通过二维数组创建 DataFrame
arr = pd.DataFrame(np.arange(0, 20).reshape(4, 5), index=['a', 'b', 'c', 'd'], columns=['1', '2', '3', '4', '5'])
print(arr)


# pandas 中的 index，其实是不可变的一维数组，那么就可以执行所有一维数组可以执行的所有操作
ind = arr.index;
print(ind.shape)




