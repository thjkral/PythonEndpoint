#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""

from flask import Flask
#import pandas as pd
import BestandFreek as fr

app = Flask(__name__)

@app.route("/prodLookup")
def prod_lookup_ep():
    '''
    End point voor terug geven van voedingswaarden van een product naar keuze.
    '''    
    return fr.prod_lookup("butter,with")








