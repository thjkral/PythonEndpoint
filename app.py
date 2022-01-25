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

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/prodLookup")
def prod_lookup(prod_name):

    data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    prod_name = prod_name.upper()

    
    prod_name = prod_name.split()

    for i, product in testdf.iterrows(): 
        if len(prod_name) == 1:
            if prod_name[0] in product["ShortDescrip"]:
                return str(product)
        elif len(prod_name) == 2:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"]:
                return str(product)
        elif len(prod_name) == 3:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"]:
                return str(product)
        elif len(prod_name) == 4:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"] and prod_name[3] in product["ShortDescrip"]:
                return str(product)
    # '''
    # End point voor terug geven van voedingswaarden van een product naar keuze.
    # '''    
    return fr.prod_lookup("butter with salt")








