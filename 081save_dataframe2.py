"""
df.to_csv(fp) 会多空行, 当添加 newline 参数, 可以修复此问题.
"""
import pandas as pd

fp = 'E:\pdLearn\data\df.csv'
# <editor-fold desc="append to csv 1">
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