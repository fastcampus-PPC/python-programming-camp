#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# 데이터셋의 전체적인 구조 살펴보기
chipo.shape
chipo.info()
chipo.head(10)


# 데이터셋의 모든 feature, index 형태 출력하기
chipo.columns
chipo.index


# 가장 많이 주문한 item 출력하기
a = chipo['item_name'].value_counts()
chipo['item_name'].value_counts().index.tolist()[0]


# 얼마나 많은 종류의 item이 주문되었는지 출력하기
len(chipo['item_name'].value_counts())


# item당 주문 총량 출력하기
chipo_all = chipo.groupby('item_name').sum()
del chipo_all['order_id']
chipo_all.sort_values(['quantity'], ascending=False)


# 달러 타입 변환하기
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))


# 주문당 평균 계산금액 출력하기
chipo.groupby('order_id').sum().mean()['item_price']


















