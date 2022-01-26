#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""


from flask import Flask
import pandas as pd
import json
import BestandFreek as fr

app = Flask(__name__)

@app.route("/") # Startpagina
def welcome_message():
    return "<p>The Python Endpoint is up and running...</p>"


@app.route("/nameLookup/<name>") # Zoeken op productnaam
def name_lookup(name):
    return fr.prod_lookup(name)


@app.route("/idLookup/<id>") # Zoeken op ID
def id_lookup(id):
    return fr.id_lookup(id)


@app.route("/bcodeLookup/<bcode>") # Zoeken op barcode
def bcode_lookup(bcode):
   return bcode.prod_lookup(bcode)






