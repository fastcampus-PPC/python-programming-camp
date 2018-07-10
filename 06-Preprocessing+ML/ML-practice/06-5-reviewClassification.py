#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 탭 구분 txt 읽는 함수
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

# 리뷰데이터 다운로드 - https://github.com/e9t/nsmc
train_data = read_data('/Users/yoon/Downloads/nsmc-master/ratings_train.txt')
test_data = read_data('/Users/yoon/Downloads/nsmc-master/ratings_test.txt')

# 사전 생성을 위한 형태소 추출
from konlpy.tag import Twitter
pos_tagger = Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
token = [t for d in train_docs for t in d[0]]

# 자연어 처리 모듈 nltk로 빈도수 상위 n개 단어 추출
import nltk
text = nltk.Text(token, name="NMSC")
text.vocab().most_common(10)

# 상위 2000개 빈도수의 단어를 추출한 뒤, BoW(Bag of Words)기법으로 워드임베딩
selected_words = [f[0] for f in text.vocab().most_common(2000)]

def term_exists(doc):
    return {'exists({})'.format(word): (word in set(doc)) for word in selected_words}

train_docs = train_docs[:10000]
test_docs = test_docs[:10000]
train_xy = [(term_exists(d), c) for d,c in train_docs]
test_xy = [(term_exists(d), c) for d,c in test_docs]

# 약 80%의 정확도
classifier = nltk.NaiveBayesClassifier.train(train_xy)
print(nltk.classify.accuracy(classifier, test_xy))

