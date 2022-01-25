#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""


from flask import Flask
import pandas as pd
import BestandFreek as fr
import json

app = Flask(__name__)

@app.route('/')
def welcome_message():
    return '<p>Python Endpoint</p>'


@app.route('/nameLookup/<name>') # Zoeken op productnaam
def name_lookup(name):
    return fr.prod_lookup(name)


@app.route('/idLookup/<id>') # Zoeken op ID
def id_lookup(id):
    pass


@app.route('/bcodeLookup/<bcode>') # Zoeken op barcode
def bcode_lookup(bcode):
    pass






