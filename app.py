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

# @app.route("/cam")  # Barcode webcam scanner
# def cam():
#   return render_template("cam.html")

# END Barcode Webcam Scanner