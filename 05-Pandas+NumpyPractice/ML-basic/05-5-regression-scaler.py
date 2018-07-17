#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from math import sqrt

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', 
                 header=None, sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
              'NOX', 'RM', 'AGE', 'DIS', 'RAD', 
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

X = df.iloc[:, :-1].values
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

mlr = linear_model.LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)

print('Coefficients: \n', regr.coef_)
print("root mean squared error: %.2f"% sqrt(mean_squared_error(y_test, y_pred)))
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# 데이터 스케일링 : 표준화 (결과는 동일, linear_model 안에 자체구현 되어있기 때문)
from sklearn.preprocessing import StandardScaler
y = df[['MEDV']].values

sc_x = StandardScaler()
X_std = sc_x.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.3, random_state=0)

mlr = linear_model.LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)

print('Coefficients: \n', mlr.coef_)
print("root mean squared error: %.2f"% sqrt(mean_squared_error(y_test, y_pred)))
print('Variance score: %.2f' % r2_score(y_test, y_pred))