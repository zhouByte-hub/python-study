## 序列：成员是有序排列的，并且可以通过下标访问成员，下标从0开始，-1表示最后一个成员
## 序列通用操作：len、del、max、min 等函数，支持切片操作，常见的有数组
## 常见的序列有：列表、元组、字符串


## 列表：列表是一种有序的序列，列表的成员可以是不同类型的对象
my_list = [1,2,3,4,5,6]
for i in my_list:
    print(i)
my_list = [1, False, 2.0, "hello"]
print(my_list[0])
a = [1,2]
print(my_list + a) ## 列表拼接
print(a * 2)    ## 列表重复
print(my_list[1:3]) ## 列表切片
print(len(my_list)) ## 列表长度

for index, value in enumerate(my_list):
    print(index, value)    # 输出列表的下标和成员


## 元组：元组是一种不可变的序列，元组的成员不能被修改，元组的成员可以是不同类型的对象
tuple1 = (1, True, 3.0, "abc", 5)
for item in tuple1:
    print(item)

tuple2 = tuple([1,2,3,4,5, "hello"])
print(tuple2)
## list --> tuple
tuple2 = tuple([1,2,3,4,5])
## str --> tuple
tuple2 = tuple("hello")
print(tuple2)
## tuple --> list
list2 = list(tuple2)
print(list2)
## str --> tuple
tuple2 = tuple("hello")
print(tuple2)

for item in tuple2:
    print(item)

for index, value in enumerate(tuple2):
    print(index, value)


## range：range()函数可以用来生成一个整数序列，常用的有range(start, end, step)
## start：可选参数，默认值为0，序列的起始值
## end：必填参数，序列的结束值，不包含在序列中
## step：可选参数，默认值为1，序列的步长

for i in range(10):
    print(i)

my_list = list(range(10)) ## 将 range() 函数生成的整数序列转换为列表
print(my_list)
my_list = list(range(1, 10, 2)) ## 将 range() 函数生成的整数序列转换为列表
print(my_list)


## 字典类型：字典是一种无序的序列，字典的成员是键值对，每个键值对之间用逗号隔开，每个键值对的键和值之间用冒号隔开，字典的成员可以是不同类型的对象
dict1 = {"name": "张三", "age": 18}
for key, value in dict1.items():
    print(key, value)

dict2 = dict(name="张三", age=18)
print(dict2)
dict2 = dict([("name", "张三"), ("age", 18)])
print(dict2)
dict2 = dict({"name": "张三", "age": 18})
print(dict2)

## 字典key的遍历
for key in dict2.keys():
    print(key)

## 字典值的遍历
for value in dict2.values():
    print(value)

dict2.pop("age")      ## 删除字典中的键值对
print(dict2)

print(dict2.get('name')) ## 获取字典中指定键的值
print(dict2.popitem()) ## 删除并返回字典中的最后一个键值对，得到元组

dict2.clear()      ## 清空字典
print(dict2)

dict2.update({"name": "张三", "age": 18}) ## 更新字典中的键值对
print(dict2)



## 集合（set）：集合是一种无序的序列，集合的成员不能重复，如果添加重复元素则会自动过滤，可以进行集合的交、并、差、对称差等操作，
# 集合的成员可以是不同类型的对象
set1 = {1, 2, 3, 4, 5}
print(set1)

set2 = set([1,2,3,4,5])
print(set2)

set3 = set("hello")
print(set3)

set3 = set((1,2,3,4,5))
set3 = set({"name": "张三", "age": 12})

for item in set3:
    print(item)


set4 = {1,2,3,4,5}
set5 = {5,6,7,8,9}
print(set4 & set5)  # 交集: {5}
print(set4 | set5)  # 并集: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set4 - set5)  # 差集: {1, 2, 3, 4}
print(set4 ^ set5)  # 对称差集: {1, 2, 3, 4, 6, 7, 8, 9}
