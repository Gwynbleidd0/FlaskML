import requests
import json
import cv2
import datetime

print(datetime.datetime.now())
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('img.jpg')
# encode image as jpeg'

_, img_encoded = cv2.imencode('.jpg', img)


print(datetime.datetime.now())
response = requests.post('http://127.0.0.1:5000/api', data=img_encoded.tostring(), headers=headers)
#print(json.loads(response.text))
print(datetime.datetime.now())
