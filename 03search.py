"""
loc 和 [] 的作用一致, 除了切片.
    s[0:2] -> s[[0,1]]
    s.loc[0:2] -> s[[0,1,2]]
iloc 切片方式与 [] 一致,
    s.iloc[0:2] -> s[[0,1]]

.iloc 根据标签的所在位置，从 0 开始计数, 选取列.
.loc 根据 DataFrame 的具体标签选取列.

"""
import numpy as np
import pandas as pd
data= [[[1,2],[3,4]],
       [[2,3],[4,5]],
       [[1,3],[2,4]]]
s = pd.Series(data=data)
# ================================================================
# 1. 序数索引
# ================================================================
print(s[1]) # [[2, 3], [4, 5]]
print(s[0:2])
"""
0    [[1, 2], [3, 4]]
1    [[2, 3], [4, 5]]
dtype: object"""
print(s[[0,2]])
"""
0    [[1, 2], [3, 4]]
2    [[1, 3], [2, 4]]
dtype: object"""
mask = [False, True, False]
print(s[mask])
"""
1    [[2, 3], [4, 5]]
dtype: object"""

# ================================================================
# 2. loc 索引
# ================================================================
print(s.loc[1]) # [[2, 3], [4, 5]]
print(s.loc[0:2])
"""
0    [[1, 2], [3, 4]]
1    [[2, 3], [4, 5]]
2    [[1, 3], [2, 4]]
dtype: object"""
print(s.loc[[0,2]])
"""
0    [[1, 2], [3, 4]]
2    [[1, 3], [2, 4]]
dtype: object"""
mask = [False, True, False]
print(s.loc[mask])
"""
1    [[2, 3], [4, 5]]
dtype: object"""

# ================================================================
# 2. iloc 索引
# ================================================================
index = ['A', 'B', 'C']
s = pd.Series(data=data, index=index)
# print(s)
# print(s.loc['A']) # [[1, 2], [3, 4]]
# print(s.loc[1]) # Error
print(s.iloc[1]) # [[1, 2], [3, 4]]
print(s.iloc[0:2])
"""
A    [[1, 2], [3, 4]]
B    [[2, 3], [4, 5]]
dtype: object"""
print(s.iloc[[0,1]])
"""
A    [[1, 2], [3, 4]]
B    [[2, 3], [4, 5]]
dtype: object"""
mask = [False, True, False]
print(s[mask])
"""
B    [[2, 3], [4, 5]]
dtype: object
"""
