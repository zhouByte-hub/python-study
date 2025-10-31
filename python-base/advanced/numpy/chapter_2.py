
import numpy as np

# ndarray的基本属性
a = np.array(np.arange(10))
print(a.ndim) ## ndim 数组的维度
print(a.shape) ## shape 数组的形状
print(a.size) ## size 数组的元素个数
print(a.dtype) ## dtype 数组的元素类型

## 通过 zeros 创建数组
a1 = np.zeros((2, 3))
print(a1)

a2 = np.zeros(shape=(10), dtype=int)
print(a2)

a3 = np.zeros_like(a2)
print(a3)


## 通过 ones 创建数组
a4 = np.ones((2, 3))
a4 = np.ones(shape=(2, 3), dtype=int)
a5 = np.ones_like(a4).reshape((3, 2))
print(a4)
print(a5)

## 通过 empty 创建数组
## empty只是创建一个未初始化的数组，数组中的元素是随机的
a6 = np.empty(10, dtype=int)
a7 = np.arange(0, 5)
np.add(2, a7, out=a6[:5]) ## 承载数据的数组一定要比被承载的数组大
print(a6)

## 使用 full 创建指定值的数组
a8 = np.full(shape=(2, 3), fill_value=2)
print(a8)
print(np.full_like(a8.reshape(6), 5, dtype=int))


## 单位矩阵：从左上角到右下角的对角线上的元素均为 1，除此之外全部都是 0，任何矩阵与单位矩阵相乘都等于本身，而且单位矩阵因此特性在高等数学中广泛应用。
eye = np.eye(3)
print(eye)
identity = np.identity(3, dtype=int)
print(identity)


## 利用lispace创建等差数列(一维数组)
# linspace(start, stop, num, endpoint, retstep, dtype)
# start: 起始值
# stop: 结束值（包含）
# num: 样本数量(几个数)
# endpoint: 是否包含结束值
# retstep: 是否返回步长
# dtype: 数据类型
a9 = np.linspace(0, 10, 5)
print(a9)

## 利用logspace创建等比数列(一维数组)（指数）
# logspace(start, stop, num, endpoint, base, dtype)
# start: 起始值
# stop: 结束值（包含）
# num: 样本数量(几个数)
# endpoint: 是否包含结束值
# base: 底数
# dtype: 数据类型
a10 = np.logspace(0, 10, 5)
print(a10)


# 切片
print(a9[0], a9[1:5], a9[::-1])

print(a8[0][0], a8[0, 0]) ## 行，列
print(a8[0]) ## 整行
print(a8[:, 0]) ## 整列
print(a8[0:2, :]) ## 0-1行的所有数据
print(a8[0:2, 0:2]) ## 0-1行的0-1列的所有数据
print(a8[:, 1:2]) ## 所有行的1列的所有数据