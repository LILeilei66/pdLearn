import pandas as pd

csv_fp = 'E:\pdLearn\data\df.csv'

with open(csv_fp, 'r') as f:
    pd_read = pd.read_csv(f, index_col=0, encoding='gbk')
    col0 = pd_read['0'].values
    print(pd_read)
    print(col0) # [0 3 6 1 1 1 1 1 1]

    col01 = pd_read[['0','1']]
    print(col01)

    """
           0  1
    0      0  1
    test1  3  4
    test2  6  7
    3      1  2
    test4  1  2
    5      1  2
    6      1  2
    08     1  2
    7      1  2
    """

    col01_sorted = col01.sort_values()