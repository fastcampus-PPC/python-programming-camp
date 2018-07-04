#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import numpy as np

# float type의 ndarray 생성
arr_data = [6, 7.5, 8, 0,1]
n_arr = np.array(arr_data)
print(n_arr)
n_str_arr = np.array(["a", "dfd", "33"])

# ndarray의 shape 확인
print(n_arr.shape)

# n차원 데이터 생성
arr_data2 = [
    [1,2,3,4],
    [5,6,7,8]
]
n_arr2 = np.array(arr_data2)
print(n_arr2)
print(n_arr2.shape)

# 모든 원소가 0으로 구성된 array생성
print(np.zeros((3,6)))

# 모든 원소가 1로 구성된 array생성
print(np.ones(10))

# 0~14까지의 수로 구성된 array생성
print(np.arange(15))

# 데이터 타입 확인
print(n_arr.dtype)
print(n_arr2.dtype)

##### Numpy 배열과 일반 배열의 속도 비교

# 10의 7승 데이터 생성
arr_data3 = np.arange(10e7)
arr_list = arr_data3.tolist()

# python list timecheck 함수
def list_timecheck(list, num):
    for idx,val in enumerate(list):
        list[idx] = val * num
    return list

# 시간 측정
import time
start_time = time.time()
list_timecheck(arr_list, 2)
print("--- %s seconds ---" % (time.time() - start_time))

start_time2 = time.time()
arr_data3 * 2
print("--- %s seconds ---" % (time.time() - start_time2))

###################################

# 데이터 타입 설정
arr_data4 = np.array([1,2,3,4,5], dtype = np.int64)
print("Type of arr : ",arr_data4.dtype)

float_arr = arr_data4.astype(np.float64)
print("\nAbout float_arr : ", float_arr, ", ", float_arr.dtype)

###################################

# array 연산
arr1 = np.array([
    [1,2,3],
    [4,5,6]
], dtype = np.float64)

arr2 = np.array([[7,8,9],[10,11,12]], dtype = np.float64)
arr3 = np.array([[5,6,7],[10,8]], dtype = np.float64) # error

# 사칙연산
print("arr1 + arr2 = ")
print(arr1 + arr2,"\n")
print("arr1 - arr2 = ")
print(arr1 - arr2,"\n")
print("arr1 * arr2 = ")
print(arr1 * arr2,"\n")
print("arr1 / arr2 = ")
print(arr1 / arr2,"\n")

# --> 사칙연산은 모두 같은 위치의 성분끼리 연산해줌. shape이 반드시 맞아야 가능.

# 상수배, 제곱근, 역수
print("2 x arr1 = ")
print(2 * arr1)
print("\n arr^0.5 = ")
print(arr1 ** 0.5)
print("\n 1/arr1 = ")
print(1 / arr1)

# array 인덱싱.
arr = np.arange(10)
print("arr[5] : ", arr[5])
print("arr[5:8] = ",arr[5:8])
arr[5:8] = 12
print("\n",arr)

# 2d array 접근법
arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

arr2d[2,1:3]
arr2d[1:3,:]
arr2d[:2,1:3] = 0

# 3d array 접근법
arr3d = np.zeros((4,4,3))
arr3d[1,1,1]
arr3d[1:2,1:3,1]
arr3d[1:3,1:3,1]
arr3d[1:3,1:3,1:3]

# 마스킹 기법
names = np.array(["YKT","YSJ","HJS","YKT","HJS","YSJ","YSJ"])
data = np.random.randn(7,4)

print("names")
print(names)
print("data")
print(data)

names == "YKT" # 마스킹을 논리값으로 반환

print("YKT: ", data[names=="YKT",:])
print("YSJ: ", data[names=="YSJ",:])
print("YKT or YSJ : ", data[(names=="YKT")|(names=="YSJ"),:])

print(data[:,3])
print(data[:,3]<0)

data[data[:,3]<0,:]=0
print(data)












