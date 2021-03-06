"""
在自己用的时候通常会建立这样形式的df:
============================================
fn  |  calculate1 | calculate2 | calculate3
============================================
"""

import numpy as np
import pandas as pd

columns = ['cal1', 'cal2', 'cal3']
# <editor-fold desc="利用series添加方式1">
df = pd.DataFrame(columns=columns)
serie = pd.Series([1,2,3], name='fn_serie', index=columns)
df = df.append(serie)
print(df)
"""
         cal1 cal2 cal3
fn_serie    1    2    3
"""
# </editor-fold>

# <editor-fold desc="利用series添加方式2">
df = pd.DataFrame(columns=columns)
assert len(df) == 0
serie = pd.Series([1,2,3], name='fn_serie', index=columns)
df.loc['fn_serir'] = serie
print(df)
"""
         cal1 cal2 cal3
fn_serir    1    2    3
"""
# </editor-fold>

# <editor-fold desc="利用df添加方式1">
df = pd.DataFrame(columns=columns)
assert len(df) == 0
item = pd.DataFrame(data=[[4, 3, 1]], index=['test2'], columns=columns)
df = df.append(item)
print(df)
"""
      cal1 cal2 cal3
test2    4    3    1
"""
# </editor-fold>