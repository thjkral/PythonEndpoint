#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""


from flask import Flask, render_template, Response, redirect, jsonify
import pandas as pd
import json
import BestandFreek as fr
import WebcamBarcodeReader as wbr

app = Flask(__name__)

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

@app.route("/cam")  # Barcode webcam scanner
def cam():
  return render_template("cam.html")


@app.route("/video_feed", methods = ["POST", "GET"])  # Video feed, as Response html page, non-visitable
def video_feed():
    return Response(wbr.gen(),
        mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/scanner", methods = ["POST", "GET"])  # Scanner landing page
def scanner():
  return render_template("scanner.html")


@app.route("/restart", methods = ["POST", "GET"])  #
def restart():
  wbr.code = 0
  return redirect("/cam")


@app.route("/result", methods = ["POST", "GET"])
def result():
  if wbr.code:
    return render_template("result.html", barcode=wbr.code)
  else:
    return redirect("scanner")

# END Barcode Webcam Scanner

if __name__ == '__main__':
  app.run(debug=True, port=5001)
