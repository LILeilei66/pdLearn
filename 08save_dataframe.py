from pandas import DataFrame
from pandas import read_csv
import numpy as np

save_path = './data/df.csv'

value = np.arange(9).reshape(3,3)
df = DataFrame(data=value)
print(df)
"""
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
"""
df.to_csv(save_path)

df2 = read_csv(save_path)
print(df2)
"""
   Unnamed: 0  0  1  2
0           0  0  1  2
1           1  3  4  5
2           2  6  7  8
"""
