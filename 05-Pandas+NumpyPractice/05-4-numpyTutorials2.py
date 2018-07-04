#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import numpy as np

arr_data1 = np.arange(1,10)
arr_data1

# 제곱근, 로그 : Data Scaling에 활용 가능
np.sqrt(arr_data1)
np.log10(arr_data1)

# 두 ndarray중 최대값으로 통합
x=np.random.randn(8)
y=np.random.randn(8)
np.maximum(x,y)

# series 데이터처럼 연산하기
arr_data2=np.random.randn(5,4)
arr_data2.sum()
arr_data2.mean()
arr_data2.sum(axis=0)
arr_data2.sum(axis=1)
arr_data2>0
arr_data2[arr_data2[:, 3]>0, :]
(arr_data2>0).sum()

# 정렬하기
arr_data3 = np.random.randn(8)
np.sort(arr_data3)
np.sort(arr_data3)[::-1]

arr_data4 = np.random.rand(5,3)
np.sort(arr_data4,axis=0)
np.sort(arr_data4,axis=1)

large_arr=np.random.rand(150)
np.sort(large_arr)[::-1]

# 150개의 랜덤값 중, 상위 5%에 위치하는 값을 출력하기
np.sort(large_arr)[::-1][int(len(large_arr) * 0.05)]

# unique 함수 사용
names=np.array(["Charles","Kilho","Hayoung","Charles","Hayoung","Kilho","Kilho"])
ints=np.array([3,3,3,2,2,1,1,4,4])
np.unique(names)
np.unique(ints)

#### 모델링 활용 예제

# 훈련셋과 시험셋 로딩
import keras
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation

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