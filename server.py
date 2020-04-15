from bottle import *
from pymongo import MongoClient
from bson.json_util import dumps
import requests
import json
import time
import os

app = Bottle(__name__)

@app.route('/')
def root():
	return "Centa API Demo Server"

@app.route('/badge')
def badge():
	
	url = 'https://centa.sertify.me/api/fetch_badges'
	myobj = {'api_key': 'sAqElnNeC7n5zQkVx9gq9vbG6RyLwt0N4VZbQoSCb3M=', 'user_id': 'kartik_centa_test'}

	res = requests.post(url, data = myobj)

	data = json.loads(res.text)
	
	return template('templates/badge.tpl', badge_link=data['badges'][0]['badge_link'])