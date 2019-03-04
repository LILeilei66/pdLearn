"""
若要包含 columns 使用 DataFrame
"""

import pandas as pd
# ================================================================
# 1. data 无索引
# ================================================================
data = [1, 2, 3]
index = ['a', 'b', 'c']
s = pd.Series(data, index, name='name')
# print(s)
"""
a    1
b    2
c    3
Name: name, dtype: int64
"""
# print(s.index) # Index(['a', 'b', 'c'], dtype='object')
# print(s.keys()) # Index(['a', 'b', 'c'], dtype='object')
# print(s.values) # [1 2 3]
# print(s.dtype) # int64

# ================================================================
# 2. data 为 dict
# ================================================================
data = {'a':1, 'b':2, 'c':3}
index = ['a', 'b', 'd']
s = pd.Series(data, index)
# print(s)
"""
a    1.0
b    2.0
d    NaN
dtype: float64
"""

# ================================================================
# 3. data 为 2D
# ================================================================
data = [[1,2,3],
        [4,5,6]]
index = ['a', 'b']
s = pd.Series(data=data, index=index)
print(s)
"""
a    [1, 2, 3]
b    [4, 5, 6]
dtype: object
"""