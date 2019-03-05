"""
只能 append 同类型, 如: pd.Series 或是 pd.DataFrame

append 多维, 需要指名这多维的 list 是在同一个 index 中的, 否则会建立多个index.
ex.:
item = pd.DataFrame(data=[], columns=columns)
item.loc[0] = value
print(item)
                        ft1                       ft2
0  [[123, 234], [156, 314]]  [[523, 635], [261, 543]]
df2 = df.append(item, ignore_index=True)

"""

# https://github.com/hangsz/pandas-tutorial/blob/master/2.%20Series%E5%92%8CDataFrame%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%9F%A5%E3%80%81%E6%94%B9%E3%80%81%E5%A2%9E%E3%80%81%E5%88%A0.ipynb

import pandas as pd
from numpy import array as nparray

# ================================================================
# 0. Series 数值 (label)
# ================================================================
s = pd.Series(data=[])
for i in range(3):
    item = pd.Series(data=i)
    s = s.append(item, ignore_index=True)
print(s)
"""
0    0
1    1
2    2
dtype: int64
"""
# ================================================================
# 1. Series 多维
# ================================================================
data = [[[1,2],[3,4]],
        [[3,4],[1,7]],
        [[4,7],[2,9]]]
s = pd.Series(data=data)
print(s)
"""
0    [[1, 2], [3, 4]]
1    [[3, 4], [1, 7]]
2    [[4, 7], [2, 9]]
dtype: object"""
item = pd.Series([[[123,234],[456,862]]])
s2 = s.append(item, ignore_index=True)
print(s2)
"""
0            [[1, 2], [3, 4]]
1            [[3, 4], [1, 7]]
2            [[4, 7], [2, 9]]
3    [[123, 234], [456, 862]]
dtype: object"""


# ================================================================
# 2. DataFrame
# ================================================================
columns = ['ft1', 'ft2']
df = pd.DataFrame(data=data, columns=columns)
print(df)
a = [[123,234],[156,314]]
b = [[523,635],[261,543]]
value = [a, b]
item = pd.DataFrame(data=value)
print(item)
"""  0           1
0  [123, 234]  [156, 314]
1  [523, 635]  [261, 543]"""
item = pd.DataFrame(data=[], columns=columns)
item.loc[0] = value
print(item)
"""
                        ft1                       ft2
0  [[123, 234], [156, 314]]  [[523, 635], [261, 543]]"""
item.append(value)
print(item)
"""
                        ft1                       ft2
0  [[123, 234], [156, 314]]  [[523, 635], [261, 543]]"""

df2 = df.append(value, ignore_index=True)
print(df2)
"""
      ft1     ft2           0           1
0  [1, 2]  [3, 4]         NaN         NaN
1  [3, 4]  [1, 7]         NaN         NaN
2  [4, 7]  [2, 9]         NaN         NaN
3     NaN     NaN  [123, 234]  [156, 314]
4     NaN     NaN  [523, 635]  [261, 543]"""
df2 = df.append(item, ignore_index=True)
print(df2)
"""
                        ft1                       ft2
0                    [1, 2]                    [3, 4]
1                    [3, 4]                    [1, 7]
2                    [4, 7]                    [2, 9]
3  [[123, 234], [156, 314]]  [[523, 635], [261, 543]]"""
print('--------------')
print(nparray(df2.loc[3, 'ft1']).shape)