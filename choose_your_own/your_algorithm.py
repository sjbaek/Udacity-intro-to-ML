#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier

# random forest 오브젝트를 처음 만듬
clf = RandomForestClassifier(n_estimators = 100)

# 그 오브젝트에 데이터를 입력함. (내부적으로 모델 parameter가 정의되는 듯)

# clf는 원래 빈 껍데기 (그저 어떤 클래시파이어를 쓰겠다는 것만 정의 된) 였으나
# .fit 과 주어진 train 데이터를 통해서 
# 조율되어진 '함수'로 다시 태어난다 이말이지.
clf.fit(features_train,labels_train)

# 위에서 정의된 parameter를 토대로, 새로운 데이터 (feature_test)를 입력하면
# 예측값 (=pred) 가 생성됨. 

# clf가 train 데이터를 통해서 함수로 튜닝이 되었으므로, .predict를 이용해서 써먹는거야
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
print 'accuracy = ',accuracy_score(pred, labels_test)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
