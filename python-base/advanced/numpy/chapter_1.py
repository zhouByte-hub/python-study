## 使用 array 创建多维数组
import numpy as np

# 使用 array 创建一维数组
a1 = np.array([1,2,3,4,5])
print(a1)


# 使用 array 创建二维数组
a2 = np.array([[1,2,3],[4,5,6]])
print(a2)


# 使用 array 创建三维数组
a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3)

## 使用arange创建数组
# arange(start, stop, step, dtype) 
# start: 起始值
# stop: 结束值（不包含）
# step: 步长
# dtype: 数据类型，
a4 = np.arange(0,10) # 创建一个包含0到9的数组
print(a4)

a5 = np.array([np.arange(0, 10), np.arange(10, 20)])
print(a5)


## random随机数
print(np.random.random()) ## 生成0到1之间的随机浮点数
a6 = np.random.random(size = 5)
print(a6, a6.shape)

a7 = np.random.random(size = (2, 3)) ## 生成2行3列的随机浮点数数组
print(a7, a7.shape)

print(np.random.randint(0, 10)) ## 生成0到9之间的随机整数
print(np.random.randint(0, 10, size = (2, 3))) ## 生成2行3列的0到9之间的随机整数数组

## 正态分布
print(np.random.randn()) ## 生成标准正态分布的随机数
print(np.random.randn(2, 3)) ## 生成2行3列的标准正态分布的随机数数组

print(np.random.normal()) ## 生成标准正态分布的随机数
# numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc: 均值
# scale: 标准差
# size: 输出数组的形状
print(np.random.normal(0, 1, size = (2, 3))) ## 生成2行3列的标准正态分布的随机数数组