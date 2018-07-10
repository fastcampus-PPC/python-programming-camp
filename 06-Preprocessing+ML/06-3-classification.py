#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())

X = dataset.iloc[:, :-1].values
y = dataset['class'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# 로지스틱 분류기 학습
from sklearn.linear_model import LogisticRegression
lrm = LogisticRegression()
lrm.fit(X_train, y_train)

lrm.score(X_test, y_test)


# Decision Tree 분류기 학습
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

clf.score(X_test, y_test)


# Decision Tree 시각화 (필요한 모듈 설치시에만 보임)
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

dot_data = export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


# knn 분류기 학습 : 최근접 이웃을 찾아가는 분류 알고리즘. 지도학습의 일종.
from sklearn import neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf = clf.fit(X_train, y_train)

clf.score(X_test, y_test)