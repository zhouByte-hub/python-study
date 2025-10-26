import math

# name = input("请输入您的名字：")
# print("您的名字是：" + name)
# print(type(name)) ## 查看变量的类型

# 变量
# 在 python 中，如果变量名，需要由两个或多个单词组成，可以使用下划线 _ 连接


a = 10
num1 = num2 = num3 = 10
x, y = 100, 200
x = "abcdef"

print(type(x))  ## 获取变量的类型
print(isinstance(x, str)) ## 判断变量是否是指定的类型

# python中的数据类型
integer = 100                               ## 整型
float_num = 3.14                            ## 浮点型
boolean = True                              ## 布尔型(True/False)
string = "hello world"                      ## 字符串型
tupleType = (1, 2, 3, 4, 5)                 ## 元组型
listType = [1, 2, 3, 4, 5]                  ## 列表型
setType = {1, 2, 3, 4, 5}                   ## 集合型
dictType = {"name": "张三", "age": 18}       ## 字典型       


print(round(3.0 + 0.5, 2)) # 3.5 四舍五入保留两位小数
print(math.ceil(3.0 + 0.5)) # 4 向上取整

# 多行字符串
content = """
    这是一个多行字符串
    可以包含多个段落
    每个段落之间用空行隔开
"""

content = "---->" + content # 字符串拼接
print(content * 5)  # 重复输出5次

## 字符串的索引和切片
## 字符串的索引从0开始，-1表示最后一个字符
print(content[0], content[-1], content[1:5], content[::-1])


# 类型转换
a = int("100")
b = float("3.14")
c = str(100)
d = bool(100)
print(a, b, c, d)
print(id(a))

# Python 中的小整数，通常是-5～256之间的整数，当你在 python 中创建一个整数对象时，Python 会根据该整数的值
# 动态的为他分配内容空间，对于小整数，Python 会使用一种称为“小整数换成”的机制来优化内存使用，这个缓存池中的整数对象
# 会被重复利用，而不是为每个新创建的小整数分配新的内容空间，这样可以减少内容分配和释放，提高程序的性能。

# 如果需要跟踪 Python 中对象的内存地址，可以使用内置的 id()来火毒对象的唯一标志服，这个标识符通常可以用来近似地表示近似的
# 表示对象的内存地址；但并不是真真的内存地址。





## python 算数运算符
print(1 + 2)    ## 加法
print(1 - 2)    ## 减法
print(1 * 2)    ## 乘法
print(1 / 2)    ## 除法
print(1 // 2)   ## 整除
print(1 % 2)    ## 取余
print(1 ** 2)   ## 指数

## python 赋值运算符
a = 10
a += 2  ## 加法赋值
print(a)

a -= 2  ## 减法赋值
print(a)

a *= 2  ## 乘法赋值
print(a)

a /= 2  ## 除法赋值
print(a)

a //= 2  ## 整除赋值
print(a)

a %= 2  ## 取余赋值
print(a)

a **= 2  ## 指数赋值
print(a)


## python 关系运算符
print(1 == 2)  ## 等于
print(1 != 2)  ## 不等于
print(1 > 2)   ## 大于
print(1 < 2)   ## 小于
print(1 >= 2)  ## 大于等于
print(1 <= 2)  ## 小于等于

## python 逻辑运算符
print(True and False)  ## 与
print(True or False)   ## 或
print(not True)        ## 非

## python 位运算符
a = 0b1010  ## 10
b = 0b1100  ## 12

print(a & b)  ## 与
print(a | b)  ## 或
print(a ^ b)  ## 异或
print(~a)     ## 非
print(a << 2) ## 左移
print(a >> 2) ## 右移


## python 成员运算符
a = [1, 2, 3, 4, 5]
print(1 in a)  ## 成员运算符
print(1 not in a)  ## 非成员运算符
print(a[0] is 1)  ## is 运算符，判断两个对象是否引用自同一个内存地址
print(a[0] is not 2)  ## is not 运算符，判断两个对象是否引用自不同的内存地址

