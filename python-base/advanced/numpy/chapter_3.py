# 数学函数

import numpy as np

a = np.arange(1, 10)

# 计算个元素的倒数
print(np.reciprocal(a))

# 每个元素的平方
print(np.square(a))

## 常见函数如下：
# np.abs(),  # 绝对值
# np.sqrt(),  # 平方根
# np.square(),  # 平方
# np.power(),  # 指数
# np.log(),  # 自然对数
# np.log2(),  # 以2为底的对数
# np.log10(),  # 以10为底的对数
# np.exp(),  # 指数函数
# np.sign()  # 符号函数
# np.floor()  # 向下取整
# np.ceil()  # 向上取整
# np.round()  # 四舍五入
# np.modf()  # 分别返回整数部分和小数部分
# np.cos()  # 余弦函数
# np.sin()  # 正弦函数
# np.tan()  # 正切函数
# np.add()/np.subtract()  # 数组元素相加/相减/
# np.multiply()/np.divide()  # 数组元素相乘/相除

# 指数函数
print(np.exp(a))

# 自然对数
print(np.log(a))

# 以2为底的对数
print(np.log2(a))

# 以10为底的对数
print(np.log10(a))


# 统计操作
print(np.sum(a, dtype=int))  # 数组元素的和
print(np.mean(a, dtype=int))  # 数组元素的平均值
print(np.median(a))  # 数组元素的中位数
print(np.std(a))  # 数组元素的标准差
print(np.var(a))  # 数组元素的方差

# 其他操作
print(np.repeat(a, 2))  # 每个元素重复2次
print(np.savetxt('array.txt', a))  # 保存数组
print(np.loadtxt('array.txt'))  # 加载数组
print(np.any(a))  # 数组中是否存在任意一个元素为True
print(np.all(a))  # 数组中是否所有元素都为True
print(np.where(len(a) / 2, a, 0))  # 满足条件的元素返回a，不满足的返回0
print(np.sort(a))  # 数组排序, 默认为升序，返回一个新数组，原数组不变
print(np.argsort(a))  # 数组排序后的索引


b = np.arange(1, 21).reshape(4, 5)
print(b > 10)