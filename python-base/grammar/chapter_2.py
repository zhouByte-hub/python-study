## 选择结构
a = 10
if a > 0:
    print('a 是一个正数')
elif a == 10: 
    print('a 等于 10')
elif a < 0 and a != -10:
    print('a 是一个负数')
elif a == -10 or a == -20:
    print('a 等于 -10 或 -20')
else:
    print('a 不是一个正数')


match a:
    case 10:
        print('a 等于 10')
    case -10 | -20:
        print('a 等于 -10 或 -20')
    case _:
        print('a 不是 10 或 -10 或 -20')


## 循环结构
number = 5
while number > 0:
    print(number)
    number -= 1

for i in range(5):
    print(i)

## 使用for遍历列表
list1 = [1, 2, 3, 4, 5]
for item in list1:
    if item == 3:
        continue
    if item == 4:
        break
    print(item)
## 使用 for 遍历元组
tuple1 = (1, 2, 3, 4, 5)
for item in tuple1:
    print(item)
## 使用 for 遍历集合
set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(item)
## 使用 for 遍历字典
dict1 = {"name": "张三", "age": 18}
for key, value in dict1.items():
    print(key, value)

for key in dict1.keys():
    pass

for i in range(1, 10):
    for k in range(1, i + 1):
        print(f"{k}*{i}={i*k}", end=" ")
    print()