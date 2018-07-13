#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import pandas as pd
import numpy as np

# 랜덤한 데이터 프레임 생성
# 데이터가 없거나, numpy의 nan 타입은 모두 결측으로 인식
df = pd.DataFrame(np.random.randint(5, size=(3, 4)), columns=['A', 'B', 'C', 'D'])
df.iloc[1, 2] = None
df.iloc[2, 3] = np.nan

# 결측데이터 확인
df.isnull()
df.isnull().sum()
df.isnull().sum(axis=0)
df.isnull().sum(axis=1)

# values attributes의 속성 = numpy
df.values
type(df.values)

# 결측데이터 제거
df.dropna()
df.dropna(axis=0)
df.dropna(axis=1)
df.dropna(how='all', axis=1)
df.dropna(how='any', axis=1)
df.dropna(thresh=4)
df.dropna(thresh=3)
df.dropna(subset=['C'])

# 결측데이터 보정
from sklearn.preprocessing import Imputer

imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
imputed_data

# 텍스트 결측값의 보정
df = pd.DataFrame(np.random.randint(5, size=(3, 4)), columns=['A', 'B', 'C', 'D'])
df.iloc[1, 2] = None
df.iloc[2, 3] = np.nan

import numpy as np
df1 = df.replace(np.nan, 'text')
df1 = df1.astype(str)



