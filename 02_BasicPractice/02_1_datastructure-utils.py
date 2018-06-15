#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

list, map, lambda 등 유용한 자료구조, 객체구조 활용법

'''


# 리스트 요소들에 2 곱하기
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)


# map 함수 이용
def two_times(x): 
    return x*2

list(map(two_times, [1, 2, 3, 4]))


# map + lambda 함수 이용
list(map(lambda a: a*2, [1, 2, 3, 4]))


# 리스트 요소들에 조건 걸어서 필터링하기
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))


# filter 함수 이용
def positive(x): return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


# filter + lambda 함수 이용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))


# 연습!
x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))

for i in y:
    print(i)
    
print(list(filter(lambda u : u % 2, x)))
print(list(filter(lambda u : u < 4, x)))


# dictionary 자료구조
my_dict = {'first': 1, 'second': '2'}
for key, val in my_dict.items():
    print(key)
    print(val)