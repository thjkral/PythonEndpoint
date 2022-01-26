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
    return "<p><h1>The Python Endpoint is up and running...</h1><b>Routes:</b><br>Zoeken op product: /nameLookup/{productnaam}<br>Zoeken op ID: /idLookup/{id}<br>Zoeken op barcode: /bcodeLookup/{barcode}</p>"


@app.route("/nameLookup/<name>") # Zoeken op productnaam
def name_lookup(name):
    prodList = fr.prod_lookup(name)
    
    if len(prodList) == 0:
        return "No results"
    else:
        for p in prodList:
            return str(p)


@app.route("/idLookup/<id>") # Zoeken op ID
def id_lookup(id):
    product = fr.id_lookup(int(id))
    
    if product == None:
        return "No results"
    else:
        return product


@app.route("/bcodeLookup/<bcode>") # Zoeken op barcode
def bcode_lookup(bcode):
   product = fr.bcode_lookup(bcode)
   
   if product == None:
       return "No results"
   else:
       return product










