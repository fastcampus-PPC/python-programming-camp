#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:36:47 2018

@author: yoon
"""

import pandas as pd
import numpy as np

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()

# 결측데이터 처리하기 : 기타 대륙으로 통합
drinks.isnull().sum()
drinks.dtypes
drinks['continent'] = drinks['continent'].astype(str)
drinks = drinks.replace('nan', 'OT', regex=True)

# 전체 평균보다 많은 알코올을 섭취하는 대륙 구하기
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_over_mean = continent_mean[continent_mean >= total_mean]

# 평균 beer_servings이 가장 높은 대륙 구하기
beer_continent = drinks.groupby('continent').beer_servings.mean().idxmax()

# 대륙별 spirit_servings의 평균, 최소, 최대, 합계 구하기
result = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])

# 대륙별 평균 wine_servings 칼럼 만들어서 병합하기
result = drinks.groupby('continent').mean()['wine_servings']
df = result.to_frame().reset_index()
df = df.rename(columns={'wine_servings': 'wine_servings_contavg'})
drinks = pd.merge(drinks, df, on='continent', how='outer')

# 같은 방법
drinks['wine_servings_contavg'] = drinks.groupby('continent')['wine_servings'].transform(np.mean)

# 국가별 total_servings 칼럼 만들어서 병합하기
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit을 가장 많이 마시는 국가 구하기
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_under_mean = continent_mean[continent_mean <= total_mean].index.tolist()
df_continent_under_mean = drinks.loc[drinks.continent.isin(continent_under_mean)]

most_spirit_under_mean = df_continent_under_mean.loc[df_continent_under_mean['spirit_servings'].idxmax()]

# 술 소비량 대비 알콜 비율에 대한 칼럼 만들어서 병합하기 -> 독하게 술을 마시는 나라
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

# 전체 순위 중 한국의 순위 구하기
drinks['alcohol_rate_rank'] = drinks['alcohol_rate'].rank(ascending=False)
drinks['alcohol_rate_rank'] = drinks['alcohol_rate_rank'].apply(np.floor)
drinks.loc[drinks['country'] == 'South Korea'].alcohol_rate_rank

# 대륙별 술 소비량 대비 알콜 비율 구하기
continent_sum = drinks.groupby('continent').sum()
continent_sum['alcohol_rate_continent'] = continent_sum['total_litres_of_pure_alcohol'] / continent_sum['total_servings']
continent_sum = continent_sum.reset_index()
continent_sum = continent_sum[['continent', 'alcohol_rate_continent']]

drinks = pd.merge(drinks, continent_sum, on='continent', how='outer')

# 아프리카와 유럽간의 술 소비량 대비 알콜 비율의 차이 검정하기
africa = drinks.loc[drinks['continent']=='AF']
europe = drinks.loc[drinks['continent']=='EU']

from scipy import stats
tTestResult = stats.ttest_ind(africa['alcohol_rate'], europe['alcohol_rate'])
tTestResultDiffVar = stats.ttest_ind(africa['alcohol_rate'], europe['alcohol_rate'], equal_var=False)

print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f" % tTestResultDiffVar)

