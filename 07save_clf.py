from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.datasets import make_classification

save_path = './data/clf_model.m'

# 1. 创建数据集
X1, Y1 = make_classification()
X2, Y2 = make_classification()

# 2. 创建clf
clf = RandomForestClassifier()
clf2 = RandomForestClassifier()

# 3. 训练clf
clf.fit(X1, Y1)
clf2.fit(X2, Y2)
joblib.dump(clf, save_path)

# 4. 验证存储
diff = []
for i in range(100):
    predict1 = clf.predict(X1[i].reshape(1,-1))
    predict2 = clf2.predict(X1[i].reshape(1,-1))
    if predict1 != predict2:
        diff.append(i)
        print('At {:} : predict1: {:}, predict2: {:}'.format(i, predict1, predict2))

clf2 = joblib.load(save_path)
diff2 = []
print('loaded')
for i in range(100):
    predict1 = clf.predict(X1[i].reshape(1,-1))
    predict2 = clf2.predict(X1[i].reshape(1,-1))
    if predict1 != predict2:
        diff2.append(i)
        print('At {:} : predict1: {:}, predict2: {:}'.format(i, predict1, predict2))
