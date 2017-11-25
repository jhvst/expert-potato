# -*- coding: utf-8 -*-

import pickle
import ujson as json
import re
import sys
import numpy as np
from sklearn.externals import joblib
import tweepy
import ujson as json
import time
from generating_reviews_discovering_sentiment.encoder import Model

reg = joblib.load('regressor.joblib')
m = Model()

threats = []

def save_threats():
    with open('../front/public/threats.json', 'w') as f:
        json.dump(f, threats)

class MyListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.text.find('RT ') != -1:
            return
        feat = m.transform([status.text])
        prob = reg.predict_proba(feat)[0, 1]
        if prob < 0.56:
            return
        # TODO: find airport
        
        threats.append({
            probability: prob,
            airport: 'HEL',
            reason: 'weather'
        })
        save_threats()
        print('new threat:', prob, status.text)

    def on_error(self, status_code):
        print('error',status_code)

def get_keywords():

    # list of keyword permutations to search for
    targets = ['heathrow', 'helsinki-vantaa', 'finnair', 'airport']
    problems = ['storm', 'rain', 'ice', 'strike', 'closed', 'fire', 'military',
            'lakko', 'myrsky']

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
    exit(0)
    text = ' '.join(sys.argv[1:]).strip()
    reg = joblib.load('regressor.joblib')
    m = Model()
    print('input:', text)
    feat = m.transform([text])
    print(feat)
    prob = reg.predict_proba(feat)[0, 1]
    print(prob)
    

    
