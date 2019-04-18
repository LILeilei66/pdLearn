"""
提取 最大, 前 n 个最大值, 最小, 前 n 个最小值.

"""

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

csv_fp ='E:\pdLearn\data\df.csv'
with open(csv_fp, 'r') as f:
    df = pd.read_csv(f, index_col=0, encoding='GBK')
    print(df)

    print(df['0'].argmax()) # 'test2'
    print(df['0'].max()) # 6
    print(df['0'].nlargest(n=3))
        # test2    6
        # test1    3
        # 3        1
    print(df['0'].nsmallest(n=3))
        # 0        0
        # 3        1
        # test4    1

"""
       0  1  2
0      0  1  2
test1  3  4  5
test2  6  7  8
3      1  2  3
test4  1  2  3
5      1  2  3
6      1  2  3
08     1  2  3
7      1  2  3
"""