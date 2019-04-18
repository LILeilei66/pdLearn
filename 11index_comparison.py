import pandas as pd
import operator

data1 = [[1,2],[3,4]]

df1 = pd.DataFrame(data=data1 , index=['test1', 'test2'])
df2 = pd.DataFrame(data=data1 , index=['test1', 'test2'])
df3 = pd.DataFrame(data=data1 , index=['test1', 'test3'])

index0 = df1.index.values # of type ndarray Σ(っ °Д °;)っ
index1 = list(df1.index.values)
index2 = list(df2.index.values)

print(index1 == index2) # True
print(operator.eq(index1, index2)) # True

# 对于 ndarray 判断是否相等需要考虑 .all() 与 .any()
index0 = df1.index.values
index3 = df3.index.values

print(index0 == index3) # [ True False]
print((index0 == index3).any()) # True
print((index0 == index3).all()) # False