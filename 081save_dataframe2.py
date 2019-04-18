"""
df.to_csv(fp) 会多空行, 当添加 newline 参数, 可以修复此问题.

read_csv 得到的文件有时会多一列:
  Unnamed: 0  col1  col2  col3
0       test     1     2   3.0
其实是read的时候的问题, read_csv 函数增加参数 index_col=0 可以解决此问题.

不建议用 Serie 来 to_csv, 因为源码表现为转为 DataFrame 再 save.
"""
import pandas as pd

fp = 'E:\pdLearn\data\df.csv'
# <editor-fold desc="df append to csv 1">
df_read = pd.read_csv(fp)
print(df_read)
header = df_read.columns
print(header)
item = pd.DataFrame([range(len(header))], columns=header)
with open(fp, 'a') as f:
    item.to_csv(f, header=False, index=False)

df_read = pd.read_csv(fp)

print(len(df_read))
print(df_read)
"""并无空格
   Unnamed: 0  0  1  2
0           0  0  1  2
1           1  3  4  5
2           2  6  7  8
3           0  1  2  3
4           0  1  2  3
5           0  1  2  3
"""
# </editor-fold>

# <editor-fold desc="create csv file and append item to csv">
columns = ['col1', 'col2', 'col3']
fp = 'E:\pdLearn\data\\test.csv'
df = pd.DataFrame(columns=columns)
with open(fp, 'a') as f:
    df.to_csv(f)
df_read = pd.read_csv(fp)
print(df_read)
"""
Empty DataFrame
Columns: [Unnamed: 0, col1, col2, col3]
Index: []
"""
item = pd.DataFrame(data=[[1,2,3]], columns=columns, index=['test'])
with open(fp, 'a') as f:
    item.to_csv(f, header=False)
    item.to_csv(f, header=False)
    item.to_csv(f, header=False)
    item.to_csv(f, header=False)
df_read = pd.read_csv(fp)
print(df_read)
"""
  Unnamed: 0  col1  col2  col3
0       test     1     2     3
1       test     1     2     3
2       test     1     2     3
3       test     1     2     3
"""
# </editor-fold>

# <editor-fold desc="read csv with index">
df_read = pd.read_csv(fp, index_col=0)
print(df_read)
"""
       col1  col2  col3
test1     1     2     3
test2     1     2     3
test3     1     2     3
test4     1     2     3
NaN    col1  col2  col3
test      1     2     3
test      1     2     3
test      1     2     3
test      1     2     3
"""
# </editor-fold>

serie = pd.Series(data=['s1','s2','s3'], index=columns,name='test serie')
with open(fp, 'a') as f:
    serie.to_csv(f)
df_read = pd.read_csv(fp, index_col=0)
print(df_read)