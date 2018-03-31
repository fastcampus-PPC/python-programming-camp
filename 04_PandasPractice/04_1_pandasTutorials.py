#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys

# 데이터 생성
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

BabyDataSet = list(zip(names,births))
BabyDataSet

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])

# 데이터 I/O
df.to_csv('births.csv', index=True, header=True)
df.to_csv('births.csv', index=False, header=True)
newdf = pd.read_csv('births.csv')
newdf = pd.read_csv('births.csv', names=['Names','Births'])

# 파일 삭제
import os
os.remove('births.csv')

# 데이터 타입 체크
df.dtypes
df.Births.dtype
df['Births'].dtype

# 데이터 살펴보기
df.info()
df.head(3)
df.tail(1)
df['Names'].describe()
df['Names'].unique()
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)
df['Births'].max()

# 데이터 조작(병합)
df_row = pd.DataFrame([["Donald", 111]], columns=['Names', 'Births'])
newdf = df.append(df_row)
newdf.loc[0]
newdf = newdf.reset_index(drop=True)

# 무작위 수 이용하기
import random
names = ['Bob','Jessica','Mary','John','Mel']
random.seed(500)
random_names = [random.choice(names) for i in range(10)]
random_births = [random.choice(births) for i in range(10)]
random_custom = [random.choice(custom) for i in range(10)]
BabyDataSet = list(zip(random_names, random_births, custom))
df = pd.DataFrame(data = BabyDataSet, 
                  columns=['Names', 'Births', 'Custom'])
df['Names'].unique()

# 범주형 데이터 그룹 연산
name = df.groupby('Names')
df2 = name.sum()
df2
df2['Births'].value_counts()





