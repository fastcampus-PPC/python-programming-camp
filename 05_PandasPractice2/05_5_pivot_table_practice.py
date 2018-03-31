#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:34:59 2018

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

# FL만 보고싶은 경우
florida_df = df[df['State'] == 'FL']

# pivot을 활용한 data reshaping (error)
reshaped_df = df.pivot(index='StatusDate', columns='State', values='CustomerCount')

# pivot을 활용한 data reshaping (중복 처리) -> 결측값 문제 발생
reshaped_df = df.pivot_table(index='StatusDate', columns='State', values='CustomerCount', aggfunc='mean')












