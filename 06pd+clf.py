"""
df.astype(np.float64) 的适用情况:
1.  df = DataFrame(data=[], columns=['ft1', 'ft2'])
    value1 = nparray([1])
    value2 = nparray([14])
    value3 = nparray([1346])
    value4 = nparray([17])

2. df = DataFrame(data=[], columns=range(2))
    将 features 全部拆开

3. prediction:
    reshape(1,-1) 以表现为一个sample.
    ex: df.loc[0].values.reshape(1,-1)

"""

from pandas import DataFrame, Series
from sklearn.ensemble import RandomForestClassifier as skrandomforest
from numpy import array as nparray
import numpy as np

# ====================================================================
# 1. 多特征, 每个特征为一个数 [Pass]
# ====================================================================

value1 = nparray([1])
value2 = nparray([14])
value3 = nparray([1346])
value4 = nparray([17])

df = DataFrame(data=[], columns=['ft1', 'ft2'])
df.loc[0, 'ft1'] = value1
df.loc[0, 'ft2'] = value2
df.loc[1, 'ft1'] = value3
df.loc[1, 'ft2'] = value4

df.astype(np.float64)


# ====================================================================
# 2. 多特征, 每个特征为一个array [Fail]
# ValueError: setting an array element with a sequence.
# ====================================================================

value1 = nparray([1,2])
value2 = nparray([14,25])
value3 = nparray([1346,1])
value4 = nparray([17,156])

df = DataFrame(data=[], columns=['ft1', 'ft2'])
df.loc[0, 'ft1'] = value1
df.loc[0, 'ft2'] = value2
df.loc[1, 'ft1'] = value3
df.loc[1, 'ft2'] = value4

# df.astype(np.float64)


# ====================================================================
# 3. 单特征, 每个特征为一个array [Fail]
# ValueError: setting an array element with a sequence.
# ====================================================================

value1 = nparray([1,2])
value2 = nparray([14,25])

s = Series(data=[])
s.loc[0] = value1
s.loc[1] = value2

# s.astype(np.float64)

# ====================================================================
# 4. 将 features 全部拆开
# ====================================================================
value1 = nparray([1,2])
value2 = nparray([14,25])
df = DataFrame(data=[], columns=range(2))
df.loc[0] = value1
df.loc[1] = value2

# print(df)
"""
    0   1
0   1   2
1  14  25
"""

print(type(df))
label = [1,0]
y = Series(data=label)


clf = skrandomforest(n_estimators=1, max_depth=2)
clf.fit(df, y)


predict1 = clf.predict(df.loc[0].values.reshape(1,-1))
predict2 = clf.predict(df.loc[1].values.reshape(1,-1))
print('prediction: ', predict1, predict2)

# print(clf)
"""
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=2, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)"""

