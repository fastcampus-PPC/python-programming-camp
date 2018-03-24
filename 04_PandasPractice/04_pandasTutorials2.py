#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

int_array = [0,1,2,3,4,5,6,7,8,9]

# Dataframe 생성
df = pd.DataFrame(int_array)
df


# Dataframe column 생성
df.columns = ['Rev']
df

df['NewCol'] = 5
df

# Dataframe column 삭제
del df['NewCol']


# Dataframe column 조작
df['NewCol'] = df['NewCol'] + 1
df


# Dataframe column 조작 2
df['test'] = 3
df['col'] = df['Rev']
df


# Dataframe row 조작
i = ['a','z','x','d','e','f','g','h','i','j']
df.index = i
df


# Dataframe row 접근
df.loc['f']
df.loc['a':'d']
df.iloc[0:3]


# Dataframe column 접근
df['Rev']
df['Rev', 'test']
df[['Rev', 'test', 'col']]


# 종합
df.loc[df.index[0:3], 'Rev']
df.loc[df.index[5:], 'col']
df.loc[df.index[:3], ['col', 'test']]

df.head()
df.tail()
df.info()
df['Rev'].value_counts()
df.shape








