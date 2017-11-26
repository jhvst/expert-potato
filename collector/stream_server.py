# -*- coding: utf-8 -*-

import pickle
import re
import sys
import numpy as np
from sklearn.externals import joblib
import tweepy
import json #as json
import time
import csv
from generating_reviews_discovering_sentiment.encoder import Model

reg = joblib.load('regressor.joblib')
m = Model()

threats = []

def save_threats():
	with open('../front/public/threats.json', 'w') as f:
		json.dump(f, threats)

def find_tweet_locations(status, destinations):
		locations = []
		
		user_location = ''
		user_time_zone = ''
		text = status._json['text'].lower()
		
		if status._json['user']['location'] is not None:
			user_location = status._json['user']['location'].lower()
		if status._json['user']['time_zone'] is not None:
			user_time_zone = status._json['user']['time_zone'].lower()
		
		for a, t, c in destinations:
			if text.find(t.lower()) >= 0 or user_location.find(t.lower()) >= 0 or user_time_zone.find(t.lower()) >= 0:
				locations.append((a, t, c))
				break
		
		for a, t, c in destinations:
			if text.find(c.lower()) >= 0 or user_location.find(c.lower()) >= 0:
				locations.append((a, t, c))
			
		print(locations)
		print(text)
		
		print(status._json['user']['location'])
		print(status._json['user']['time_zone'])
		print(status._json['user']['geo_enabled'])
		print(status._json['geo'])
		print(status._json['coordinates'])
		print(status._json['place'])
		print('')
		#print(status._json)
		#user = get_user(status._json[])
		#print('')
		return locations

		
def get_destinations(filename):
	names = []
	
	with open(filename, 'r', encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in reader:
			names.append((row[0], row[2], row[3]))
		
	return names
		

# load predictor model...
from create_model import word_tokenize
reg = joblib.load('regressor.joblib')
with open('words.json') as f:
	g_words = json.load(f)
	g_words_set = set(g_words)
def text_to_prob(text):
	x = np.zeros((1, len(g_words)))
	for word in word_tokenize(text):
		word = word.lower()
		if word in g_words_set:
			x[0, g_words.index(word)] = 1.0
	prob = reg.predict_proba(x)[0, 1]
	return prob

def text_to_category(text):
	categories = {
    	'weather':[
      	  'hail',
      	  'storm',
      	  'wind',
      	  'hurricane',
      	  'tornado',
      	  'snow',
      	  'sleet'
    	],
    	'airspace':[
      	  'closed airspace',
      	  'radiation'
    	],
    	'strikes':[
      	  'strike',
      	  'labour strike',
      	  'labor strike',
      	  'strike action'
    	],
    	'environmental':[
      	  'mudslide',
      	  'tsunami',
      	  'earthquake',
      	  'dust',
      	  'volcano',
      	  'forest fire',
      	  'dust bowl',
      	  'dust storm'
    	],
    	'airport closure':[
      	  'airfield closed'
    	],
    	'national':[
      	  'christmas',
      	  'xmas',
      	  'national',
      	  'holiday', #overbooking
      	  'thanksgiving',
      	  'national holiday'
    	],
    	'large events':[
      	  'olympics',
      	  'festival',
      	  'parade',
      	  'carneval',
      	  'carnival'
    	],
    	'political conflicts':[
      	  'rally',
      	  'demonstration',
      	  'protest',
      	  'picket',
      	  'manifestation',
      	  'political conflict'
    	],
    	'military operations':[
      	  'war',
      	  'conflict',
      	  'military operations'
    	],
    	'terror threat':[
      	  'terrorism',
      	  'bomb',
      	  'terror',
      	  'attack',
      	  'terrorist',
      	  'terror threat'
    	]
	}
	for category in categories.keys():
		for keyword in categories[category]:
			if text.lower().find(keyword) != -1:
				return category
	return 'other'

g_destinations = get_destinations('finnair_airports.csv')
def tweet_to_threat(status):
	if status.text.find('RT ') != -1:
		return None

	prob = text_to_prob(status.text)
	
	locations = find_tweet_locations(status, g_destinations)

	if prob < 0.500142755657:
		print('prob', prob, 'below threshold')
		return None
	return {
		probability: prob,
		source: 'twitter',
		airport: 'HEL',
		twitter_message: status.text,
		category: text_to_category(status.text)
	}

class MyListener(tweepy.StreamListener):
	def on_status(self, status):
		t = tweet_to_threat(status)
		if t is not None:
			threats.append(t)
			save_threats()
			print('new threat:', threats[-1])

	def on_error(self, status_code):
		print('error',status_code)

def get_keywords():

	# list of keyword permutations to search for
	targets = ['heathrow', 'helsinki-vantaa', 'finnair', 'airport']
	problems = ['storm', 'rain', 'ice', 'strike', 'closed', 'fire', 'military',
			'lakko', 'myrsky']
	get_destinations('finnair_airports.csv')

	from itertools import product
	conditions = list(product(targets, problems))
	#conditions = [a + ' AND ' + b for a, b in conditions]
	conditions = [b for a, b in conditions]
	return conditions

def main():
	consumer_key = '***REMOVED***'
	consumer_secret = '***REMOVED***'
	access_token = '***REMOVED***'
	access_token_secret = '***REMOVED***'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	myListener = MyListener()
	listener = tweepy.Stream(auth=auth, listener=myListener)
	listener.filter(track=get_keywords())

if __name__ == '__main__':
	main()
