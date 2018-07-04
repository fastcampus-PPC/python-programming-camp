#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:49:24 2018

@author: yoon
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', 
                 header=None, sep='\s+')

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 
              'NOX', 'RM', 'AGE', 'DIS', 'RAD', 
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

X = df[['RM']].values
X.shape
y = df['MEDV'].values
y.shape

# 훈련 데이터와 테스트 데이터로 나누기
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 훈련데이터로 학습시키기
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

# 테스트 데이터로 결과값 예측
y_pred = regr.predict(X_test)

# 회귀 계수 출력
print('Coefficients: \n', regr.coef_)

# MSE 출력
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))

# r-score 출력
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()

###################################################
###################################################
# 다항 회귀모델 학습하기
X = df.iloc[:, :-1].values
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

mlr = linear_model.LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)

print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
print('Variance score: %.2f' % r2_score(y_test, y_pred))





