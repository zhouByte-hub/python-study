## 错误与异常
from functools import reduce

list1 = [1, 2, 3, 4, 5]

try:
    temp = list1[10]
except IndexError as e:
    print("索引超出范围", e)
finally:
    print("程序结束")

# 自定义异常
if len(list1) < 10:
    raise Exception("列表长度不足 10")


## 函数：使用关键字 def 定义函数，python 中的函数需要满足先定义后调用，否则会报错
def function(args):
    pass

## 位置参数：形参与实参位置需要一一对应，因为形参没有默认值，所以需要实参一一传递值
def add(a, b):
    return a + b
print(add(1, 2))

## 缺省参数：缺省参数需要卸载位置参数后面
def show(name, age = 18, address = "中国"):
    print(f"{name} 是一个 {age} 岁的人，来自 {address}")

show("张三", address="中国") ## 可以只传递 name 参数，其他参数使用默认值

## 可变参数：可变参数需要在位置参数后面，且只能有一个可变参数
def show_info(name, age = 18, address = "中国", *args):  ## *args表示可以接受一个列表，**args表示可以接受一个列表，实参也需要加*号
    print(f"{name} 是一个 {age} 岁的人，来自 {address}")

show_info("张三", 18, "中国", "北京", "上海")


## 匿名函数：一种快速定义单行的最小函数，可以用在任何需要函数的地方，让代码更加精简。
add = lambda a, b: a + b
print(add(1, 2))

## 隐射
a = [1,2,3,4,5]
result = map(lambda x: x**2, a)
print(reuslt)

## reduce累计
result = reduce(lambda x, y: x + y, a)
print(result)

# 递归
def factorial(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return factorial(n - 1) + factorial(n - 2)

print(factorial(5))
