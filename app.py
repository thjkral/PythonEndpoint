#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""


from flask import Flask, render_template, Response, redirect
import pandas as pd
import json
import BestandFreek as fr
import cv2
import pyzbar.pyzbar as pb

app = Flask(__name__)

@app.route("/") # Startpagina
def welcome_message():
    return "<p><h1>The Python Endpoint is up and running...</h1><b>Routes:</b><br>Zoeken op product: /nameLookup/{productnaam}<br>Zoeken op ID: /idLookup/{id}<br>Zoeken op barcode: /bcodeLookup/{barcode}</p>"


@app.route("/nameLookup/<name>") # Zoeken op productnaam
def name_lookup(name):
    return fr.prod_lookup(name)


@app.route("/idLookup/<id>") # Zoeken op ID
def id_lookup(id):
    return fr.id_lookup(int(id))


@app.route("/bcodeLookup/<bcode>") # Zoeken op barcode
def bcode_lookup(bcode):
   return bcode.prod_lookup(bcode)


# START Barcode Webcam Scanner

@app.route("/cam")  # Barcode webcam scanner
def cam():
  return render_template("cam.html")

font_duplex = cv2.FONT_HERSHEY_DUPLEX
font_simple = cv2.FONT_HERSHEY_PLAIN

def setText(_img, _string, _pos, _font, _scale, _color, _thickness):
  # cv2.putText(img, string, pos, font, scale, color, thickness)
  txt_shadow = cv2.putText(_img, _string, _pos, _font, _scale, (0, 0, 0), _thickness + 1)
  txt = cv2.putText(_img, _string, _pos, _font, _scale, _color, _thickness)


code = 0
def gen():
  camera = cv2.VideoCapture(0)
  while True:
    success, frame = camera.read()
    if not success:
      # todo show picture > no camera found, plug in your webcam and enable it in your browser
      break
    else:
      decoded = pb.decode(frame)
      if decoded != []:
        objects = []
        for decode in decoded:
          name = str(decode.data).replace("b'", "")
          name = name.replace("'", "")
          type = decode.type
          rect = decode.rect
          objects.append({'name': name, 'type': type, 'rect': rect})

        for o in objects:
          setText(frame, f"{o['name']}", (o['rect'].left - 50, o['rect'].top - 50), font_duplex, 1, (255, 255, 255), 2)
          setText(frame, f"{o['type']}", (o['rect'].left - 50, o['rect'].top - 20), font_simple, 2, (255, 255, 255), 2)
          global code
          code = o['name']

      ret, buffer = cv2.imencode(".jpg", frame)
      frame = buffer.tobytes()
      yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
      if decoded != []:
        camera.release()
        return

@app.route("/video_feed", methods = ["POST", "GET"])  # Video feed, as Response html page, non-visitable
def video_feed():
    return Response(gen(),
        mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/scanner", methods = ["POST", "GET"])  # Scanner landing page
def scanner():
  return render_template("scanner.html")


@app.route("/restart", methods = ["POST", "GET"])  # Restart and reset global variables
def restart():
  code = 0
  return redirect("/cam")


@app.route("/result", methods = ["POST", "GET"])
def result():
  if code:
    return render_template("result.html", barcode=code)
  else:
    return redirect("scanner")

# END Barcode Webcam Scanner