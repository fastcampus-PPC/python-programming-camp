#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import os
import pandas as pd

# 리뷰데이터 다운로드 - https://github.com/e9t/nsmc
train_data = pd.read_csv('rating_train.csv')
test_data = pd.read_csv('rating_test.csv')
train_data = train_data.dropna()
test_data = test_data.dropna()

# 사전 생성을 위한 형태소 추출
from konlpy.tag import Twitter
pos_tagger = Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

# (형태소 뭉치, label) 을 element로 하는 list 생성
train_docs = [(tokenize(row['review']), row['like']) for index, row in train_data.iterrows()]
test_docs = [(tokenize(row['review']), row['like']) for index, row in test_data.iterrows()]

# 생성된 리스트에서 말뭉치 추출
token = [t for d in train_docs for t in d[0]]

# 자연어 처리 모듈 nltk로, 말뭉치에서 빈도수 상위 n개 단어 추출
import nltk
text = nltk.Text(token, name="NMSC") # text.vocab().most_common(n)

# 상위 2000개 빈도수의 단어를 추출한 뒤, BoW(Bag of Words)기법으로 워드임베딩
selected_words = [f[0] for f in text.vocab().most_common(2000)]

# nltk 라이브러리가 원하는 형태로 input formatting
def term_exists(doc):
    return {'exists({})'.format(word): (word in set(doc)) for word in selected_words}

train_docs = train_docs[:10000]
test_docs = test_docs[:10000]
train_xy = [(term_exists(d), c) for d,c in train_docs]
test_xy = [(term_exists(d), c) for d,c in test_docs]

# 약 80%의 정확도
classifier = nltk.NaiveBayesClassifier.train(train_xy)
print(nltk.classify.accuracy(classifier, test_xy))