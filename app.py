#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:14:22 2022

@author: tom
"""

from flask import Flask
import endpointTest
import BestandFreek as fr
import tomsFile as tf
import bestandFelix as bf

app = Flask(__name__)

@app.route("/")
def end_point_test():
    message = endpointTest.readFile()
    return message

@app.route("/mijnfunctie")
def end_point_test_mijnfunctie():
    fr.Freek()
    return "functie van Freek"

@app.route("/functietom")
def end_point_functietom():
    tf.toms_functie()
    return "functie van Tom"

@app.route("/functiefelix")
def end_point_functiefelix():
    return bf.felixProbeert()



