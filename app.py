#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""

from flask import Flask
import endpointTest

app = Flask(__name__)

@app.route("/")
def end_point_test():
    message = endpointTest.readFile()
    return message







