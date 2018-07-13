#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

import os
import numpy as np

# 리뷰데이터
train_data = pd.read_csv('rating_train.csv')
test_data = pd.read_csv('rating_test.csv')
train_data = train_data.dropna()
test_data = test_data.dropna()

# tf-idf 임베딩
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

vect = TfidfVectorizer()
review_column = np.array([row['review'] for index, row in train_data.iterrows()])
y_train = np.array([row['like'] for index, row in train_data.iterrows()])

# fit_transform : vect object에게 transform을 학습시킴
X_train = vect.fit_transform(review_column)

# 로지스틱 분류기 학습 : 약 81% 정확도
from sklearn.linear_model import LogisticRegression
lrm = LogisticRegression()
lrm.fit(X_train, y_train)

review_column = np.array([row['review'] for index, row in test_data.iterrows()])
y_test = np.array([row['like'] for index, row in test_data.iterrows()])

# transform : test 데이터를 학습된 vect object로 임베딩시킴
X_test = vect.transform(review_column)
lrm.score(X_test, y_test)

# 실제 텍스트로 테스트
test_data1 = ["그저그럼.. 재미없음"] # label : 0
test_data2 = ["꿀잼 최고의 영화"] # label : 1
test_tfidf1 = vect.transform(test_data1)
test_tfidf2 = vect.transform(test_data2)
print(lrm.predict(test_tfidf1))
print(lrm.predict(test_tfidf2))

# 응용 어플리케이션 임베딩을 위한 모델 관련 파일 저장
import pickle
import os

pickle.dump(vect, open(os.path.join('vectorizer.pkl'), 'wb'))
vect_read = pickle.load(open(os.path.join('vectorizer.pkl'), 'rb'))

pickle.dump(lrm, open(os.path.join('classification_model.pkl'), 'wb'))
lrm_read = pickle.load(open(os.path.join('classification_model.pkl'), 'rb'))









