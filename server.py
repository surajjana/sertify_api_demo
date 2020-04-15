from bottle import *
from pymongo import MongoClient
from bson.json_util import dumps
import json
import time
import os

app = Bottle(__name__)

# client = MongoClient('mongodb://cas:cas@54/cas')
# db = client.db

@app.route('/')
def root():
	print(os.environ('mongo_uri'))
	return "Centa API Demo Server"

# @app.route('/home')
# def home():
# 	return static_file('home.html',  root='templates/')

# @app.route('/badge')
# def badge():
# 	return static_file('badge.html', root='templates/')