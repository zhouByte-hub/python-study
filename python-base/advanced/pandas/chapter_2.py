import pandas as pd
import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 构建Excel文件的完整路径
txt_path = os.path.join(current_dir, 'files', 'pandas.txt')

df = pd.read_table(txt_path, encoding='utf-8', sep='\s+')  # 使用正则表达式匹配任意空白字符作为分隔符
# print(df)

print("------------------------------读取前两行")
print(df.head(2)) ## 读取前两行
print("------------------------------读取后两行")
print(df.tail(2)) ## 读取后两行
print("------------------------------数据信息")
print(df.info()) ## 数据信息
print("------------------------------读取第一行")
print(df.loc[0], type(df.loc[0]), df.iloc[0]) ## 读取第一行, 类型为 Series, loc 会算是标题行，iloc 则不会算上标题行



print(df.columns)
df.columns = list(['方案 1', '设备投资 1', '单件成本1', '年销售量1', '销售单价1'])
df.rename(columns={'方案 1': '方案'}, inplace=True) ## inplace: 是否直接修改原数据
print("------------------------------修改列名")
print(df)

print("------------------------------筛选列")
print(df.方案)  # 获取单列，返回的类型为 Series
print(df['方案'])
print(df[['方案', '设备投资 1']]) # 获取多列，返回的类型为 DataFrame



## df.drop(index/columns=['列名'/行号], inplace=True) ## 删除行或列
df.drop(columns=['设备投资 1'], inplace=True)
print("------------------------------删除列")
print(df)

## df[column] = pd.Series([val, val, val], index = [c1, c2, c3])
df['设备投资'] = pd.Series([1000, 1000, 1000])
print("------------------------------添加列")
print(df)

## 指定列作为索引， 默认的索引是没有名字的并且索引从 0 开始
df.set_index(keys = ['方案', '设备投资'], inplace=True, drop=False) # drop=False 表示不删除原列
print("------------------------------指定索引")
print(df)

df.reset_index(inplace=True, drop=True)
print("------------------------------重置索引")
print(df)

df.index = ['方案1', '方案2', '方案3']
print("------------------------------修改索引")
print(df)
