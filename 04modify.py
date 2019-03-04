"""
改变值:
法一: 直接s[] = value
法二: s.replace(to_replace, value, inplace)
    效果1. 改变所有此数值.
    问题1. list时出现问题.
改变索引:
法一: 直接s.index = new_index
法二: s.rename({old_name: new_name}, inplace)
"""
import pandas as pd
data = [[[1,2],[2,3]],
        [[2,3],[4,5]],
        [[1,2],[2,3]]]
s = pd.Series(data=data)
print(s)
"""
0     [[1, 2], [2, 3]]
1     [[2, 3], [4, 5]]
2    [[1,2],[2,3]]
dtype: object"""

# ================================================================
# 1. 改变数值
# ================================================================
# s.loc[1] = [[123,234],[456,654]]
# print(s)
"""
0            [[1, 2], [2, 3]]
1    [[123, 234], [456, 654]]
2           [[1,2],[2,3]]
dtype: object"""
s2 = s.replace(to_replace=1, value=100, inplace=False)
print(s2) # ?!
"""
0    [[1, 2], [2, 3]]
1    [[2, 3], [4, 5]]
2    [[1, 2], [2, 3]]
dtype: object"""

data2 = [1,2,3]
s = pd.Series(data=data2)
s2 = s.replace(to_replace=1, value=100, inplace=False)
print(s2)
"""
0    100
1      2
2      3
dtype: int64"""

# ================================================================
# 2. 改变索引
# ================================================================
print(s.index) # RangeIndex(start=0, stop=3, step=1)
# s.index = ['a', 'b', 'c']
# print(s.index) # Index(['a', 'b', 'c'], dtype='object')

s.rename(index={0:'a'}, inplace=True)
print(s.index) # Index(['a', 1, 2], dtype='object')
