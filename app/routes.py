# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from flask import request, Response
import numpy as np
from PIL import Image
import json
import shelve
import cv2
import jsonpickle
"""
@app.route("/api", methods=['POST'])
def hello():
        r = request
        image = r.files.get('pict')
        
#        with open('get_image.jpg', mode = 'w') as new:
#                new.write(image)
        img = np.array(Image.open(image))
        print(img)
#        ls = np.asarray(r.form)
#        print(ls)

#        response = {'message': r.form['tezt']}
#        response_pickled = json.dumps(response)
#        return Response(response=response_pickled, status=200, mimetype="application/json")
        return Response(status = 200)
"""

@app.route('/api', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
