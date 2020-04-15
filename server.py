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
	myobj = {'api_key': os.environ.get('api_key', None), 'user_id': os.environ.get('user_id', None)}

	print(os.environ.get('api_key'), os.environ.get('user_id'))

	res = requests.post(url, data = myobj)

	data = json.loads(res.text)
	print(data)
	
	return template('templates/badge.tpl', badge_link=data['badges'][0]['badge_link'])