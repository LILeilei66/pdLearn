
# https://github.com/hangsz/pandas-tutorial/blob/master/2.%20Series%E5%92%8CDataFrame%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%9F%A5%E3%80%81%E6%94%B9%E3%80%81%E5%A2%9E%E3%80%81%E5%88%A0.ipynb

import pandas as pd
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