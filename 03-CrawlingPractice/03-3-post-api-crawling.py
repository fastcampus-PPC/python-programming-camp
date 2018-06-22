#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: yoon

"""

#%matplotlib inline
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from io import BytesIO
import operator

#Ready your subscription key
subscription_key = '5d2bbb09469e4588a2c57b51c9bf7baa'
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

#Set your image_url 
image_url = 'https://pbs.twimg.com/profile_images/910890240851681280/ACwlsXA9_400x400.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
data = {'url': image_url}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()

# Display the original image and overlay it with the face information.
img = Image.open(BytesIO(requests.get(image_url).content))

def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')
    
img.show()
print(faces)