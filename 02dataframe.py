"""
对于 DataFrame, .
"""

import pandas as pd

# ================================================================
# 1. data 无索引
# ================================================================
data = [[1,2,3],
        [3,4,5]]
index = ['a', 'b']
columns = ['A', 'B', 'C']
df = pd.DataFrame(data=data, index=index, columns=columns)
# print(df)
"""
   A  B  C
a  1  2  3
b  3  4  5
"""
# print(df.keys()) # Index(['A', 'B', 'C'], dtype='object')
# print(df.values)
""" [[1 2 3]
 [3 4 5]]"""
# print(df.index) # Index(['a', 'b'], dtype='object')
# print(df.columns) # Index(['A', 'B', 'C'], dtype='object')
# print(df.dtypes)
"""A    int64
B    int64
C    int64
dtype: object"""

# ================================================================
# 2. data 为 dict
# ================================================================
data = {'a':[1,2,3], 'b':[1,3,4], 'c':[3,4,5]}
index = ['A', 'B', 'D']
columns = ['a', 'b', 'c', 'f']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
""" a  b  c    f
A  1  1  3  NaN
B  2  3  4  NaN
D  3  4  5  NaN"""
df = pd.DataFrame(data=data)
print(df)
"""a  b  c
0  1  1  3
1  2  3  4
2  3  4  5"""