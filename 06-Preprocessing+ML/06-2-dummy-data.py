#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import pandas as pd
import numpy.random as np

np.seed(111)

# 연습용 데이터셋 생성 함수
def CreateDataSet(Number=1):
    
    Output = []
    
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        data = np.randint(low=25,high=1000,size=len(rng))
        states = ['GA','FL','fl','NY','NJ','TX']
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]    
        Output.extend(zip(random_states, data, rng))
        
    return Output


# 연습용 데이터셋 생성
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','CustomerCount','StatusDate'])
df.info()
df.head()

# Dataframe feature 전처리
df['State'] = df.State.apply(lambda x: x.upper())

# State 변수 더미변수로 만들기
df_one_hot_encoded = pd.get_dummies(df.State)
type(df_one_hot_encoded)
result = pd.concat([df, df_one_hot_encoded], axis=1)

# one-hot encoding 예제
import keras
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation

# 훈련셋과 시험셋 로딩
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 데이터셋 전처리
X_train = X_train.reshape(60000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0

# one-hot encoding
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

# 모델링 구성
model = Sequential()
model.add(Dense(units=64, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, epochs=3, batch_size=32)

# 샘플 테스트
from numpy import argmax

xhat_idx = np.random.choice(X_test.shape[0], 5)
xhat = X_test[xhat_idx]
yhat = model.predict_classes(xhat)

for i in range(5):
    print('True : ' + str(argmax(Y_test[xhat_idx[i]])) + ', Predict : ' + str(yhat[i]))
    

## 참고용 실행 코드
argmax(Y_test[xhat_idx[0]])
Y_test[xhat_idx[0]]