#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""


from flask import Flask, render_template, Response, redirect, jsonify
from flask_socketio import SocketIO, send, emit
import base64, cv2, io, numpy as np
from PIL import Image
import pandas as pd
import json
import BestandFreek as fr
import WebcamBarcodeReader as wbr

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/") # Startpagina
def welcome_message():
    return "<p><h1>The Python Endpoint is up and running...</h1><b>Routes:</b><br>Zoeken op product: /nameLookup/{productnaam}<br>Zoeken op ID: /idLookup/{id}<br>Zoeken op barcode: /bcodeLookup/{barcode}</p>"


@app.route("/nameLookup/<name>", methods = ['GET']) # Zoeken op productnaam
def name_lookup(name):
    prodList = fr.prod_lookup(name)
    
    if len(prodList) == 0:
        return "No results"
    else:
        for p in prodList:
            result = pd.DataFrame(p)
            print(result)
            return result.to_json()


@app.route("/idLookup/<id>", methods = ['GET']) # Zoeken op ID
def id_lookup(id):
    product = fr.id_lookup(int(id))
    
    if product == None:
        return "No results"
    else:
        return jsonify(product)


@app.route("/bcodeLookup/<bcode>", methods = ['GET']) # Zoeken op barcode
def bcode_lookup(bcode):
   product = fr.bcode_lookup(int(bcode))
   
   if product == None:
       return "No results"
   else:
       return jsonify(product)

















# START Barcode Webcam Scanner

@app.route("/cam")  # Barcode webcam scanner landing page
def cam():
    return render_template("cam.html")


@app.route("/video_feed", methods=["POST", "GET"])  # Video feed, as Response html page, non-visitable
def video_feed():
    return Response(wbr.gen(),
        mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/scanner", methods=["POST", "GET"])  # Scanner landing page
def scanner():
  return render_template("client.html")


@app.route("/restart", methods=["POST", "GET"])  # Restart and reset global variables
def restart():
  wbr.code = 0
  return redirect("/cam")


# Upon submit, check if code was scanned
# If true: show scanned product details
# If false: reload scanner page
@app.route("/result", methods=["POST", "GET"])
def result():
  if wbr.code:
    product = fr.bcode_lookup(int(wbr.code))
    product_keys = list(product.keys())
    return render_template("result.html", barcode=wbr.code, product=product, keys=product_keys)
  else:
    return redirect("scanner")

@socketio.on('catch-frame')
def catch_frame(data):
    emit('response_back', data)

def readb64(base64_string):
    idx = base64_string.find('base64,')
    base64_string  = base64_string[idx+7:]

    sbuf = io.BytesIO()

    sbuf.write(base64.b64decode(base64_string, ' /'))
    pimg = Image.open(sbuf)


    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

@socketio.on('image')
def image(data_image):
    feed = (readb64(data_image))
    frame = wbr.gen(feed)[0]
    theCode = wbr.gen(feed)[1]
    if theCode == 0:
        theCode = "Scan a barcode!"
    imgencode = cv2.imencode('.jpeg', frame, [cv2.IMWRITE_JPEG_QUALITY, 40])[1]

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpeg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', [stringData, theCode])

# END Barcode Webcam Scanner

socketio.run(app)
