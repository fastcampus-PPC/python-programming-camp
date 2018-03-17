#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:43:13 2017

@author: yoon
"""

import os
import sys
import urllib.request

client_id = "Your Client_ID" # Client_ID 입력
client_secret = "Your_Client_Password" # Client_Password 입력

encText = urllib.parse.quote("이번 내리실 역은 패스트 캠퍼스, 패스트 캠퍼스 역입니다.")
data = "speaker=mijin&speed=0&text=" + encText;

url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('fastcampus.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)