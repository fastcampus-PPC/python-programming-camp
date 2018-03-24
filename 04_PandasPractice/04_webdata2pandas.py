#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


req = requests.get('https://music.bugs.co.kr/chart')
html = req.content
soup = BeautifulSoup(html, 'lxml') # pip install lxml
list_song = soup.find_all(name="p", attrs={"class":"title"})
list_artist = soup.find_all(name="p", attrs={"class":"artist"})

# 크롤링된 데이터를 df로 만들기
df = pd.DataFrame(columns=['rank', 'title', 'artist'])
for index in range(0, len(list_song)):
    title = list_song[index].find('a').text
    title = title.split("(")[0] # 피처링 제거
    artist = list_artist[index].find('a').text
    df.loc[index] = [index+1, title, artist]
    if index == 100:
        break

# column의 순서를 바꾸고 싶을때
df.loc[ : , ['artist', 'title']] = df[['title', 'artist']].values

# 응용 : 차트에 가장 많은 곡을 올린 가수
df['artist'].value_counts()

# Dataframe을 파일로 저장(csv)
df.to_csv('bugs_chart.csv', encoding='utf-8')

# 저장된 파일 읽기 // https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
newdf = pd.read_csv('bugs_chart.csv')
newdf = pd.read_csv('bugs_chart.csv', index_col = 0)

# json type (str fake)
df.to_json(orient='index')
df.to_json(orient='records')
df.to_json(orient='table')

df.to_json(orient='index', force_ascii=False)
df.loc[1].to_json(orient='index', force_ascii=False)
df.to_json(orient='records', force_ascii=False)
df.loc[1].to_json(orient='records', force_ascii=False)
df.to_json(orient='table', force_ascii=False)
df.loc[1].to_json(orient='table', force_ascii=False)

# json object shape as dictionary in python
import json

json_data = df.loc[1].to_json(orient='table', force_ascii=False)
data = json.loads(json_data)['data']
data[0]['index']






