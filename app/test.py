from PIL import Image
from io import BytesIO
import numpy
import json
import requests
im = Image.open("img.jpg")
#img = numpy.asarray(im)

fp = BytesIO()
im.save(fp,format = 'JPEG')
fp.seek(0)

files = {'pict': ('img.jpg', fp, 'image/jpg')}
#data = json.dumps(data)

ans = requests.post('http://127.0.0.1:5000/api',files = files)
print(ans)
