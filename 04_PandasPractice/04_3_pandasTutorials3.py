#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy.random as np

np.seed(111)

# 연습용 데이터셋 생성 함수
def CreateDataSet(Number=1):
    
    Output = []
    
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        data = np.randint(low=25,high=1000,size=len(rng))
        status = [1,2,3]
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        states = ['GA','FL','fl','NY','NJ','TX']
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]    
        Output.extend(zip(random_states, random_status, data, rng))
        
    return Output


# 연습용 데이터셋 생성
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
df.info()
df.head()


# datetime object를 index로 사용
df.index = df['StatusDate']
df.head()
del df['StatusDate']


# Dataframe feature 전처리
df['State'].unique()
df['State'] = df.State.apply(lambda x: x.upper())


# 조건에 맞는 데이터 선택
mask = (df['Status'] == 1)
df = df[mask]


# 조건에 맞게 데이터 변경
mask = (df['State'] == 'NJ')
df['State'][mask] = 'NY'
df['State'].unique()


# 조건에 맞는 데이터 중, index를 기준으로 정렬
sortdf = df[df['State']=='NY'].sort_index(axis=0)
sortdf.head(10)


# 그룹 연산 적용
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()
Daily.index


# 이상치 계산하여 새로운 feature로 추가 (월 단위로 이상치 측정), transform 함수 : 각 원소는 그대로 유지하되, 원소간의 연산 결과를 새로운 피처로 사용
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Max'] = StateYearMonth['CustomerCount'].transform( lambda x: x.max() )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper']) 

# 참고 : apply는 그룹별 연산값을 리턴해주고, transform은 각 row의 연산값을 리턴한다.

# 이상치 제외
Daily = Daily[Daily['Outlier'] == False]

