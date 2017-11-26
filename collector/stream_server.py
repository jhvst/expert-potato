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

reg = joblib.load('regressor.joblib')
threats = []

def save_threats():
    with open('../front/public/threats.json', 'w') as f:
        json.dump(f, threats)

def find_locations(status, destinations):
        locations = []
            
        if isinstance(status, str):
            for a, t, c in destinations:
                if status.find(t.lower()) >= 0:
                    locations.append(a)
            
            if len(locations) == 0:
                for a, t, c in destinations:
                    if status.find(c.lower()) >= 0:
                        locations.append(a)
            
        else:       
            user_location = ''
            user_time_zone = ''
            if 'title' in status:
                text = (status['title'] or '') + ' - ' + (status['description'] or '')
                text = text.lower()
            else:
                text = status['full_text'] if 'full_text' in status else status['text']
                text = text.lower()
                if status['user']['location'] is not None:
                    user_location = status['user']['location'].lower()
                if status['user']['time_zone'] is not None:
                    user_time_zone = status['user']['time_zone'].lower()

                if 'place' in status['user']:
                    if status['user']['place']['city'] is not None:
                        user_location = user_location + ' ' + status['user']['place']['city']
                    if status['user']['place']['country'] is not None:
                        user_location = user_location + ' ' + status['user']['place']['country']
                
            for a, t, c in destinations:
                if text.find(t.lower()) >= 0 or user_location.find(t.lower()) >= 0 or user_time_zone.find(t.lower()) >= 0:
                    locations.append(a)
            
            if len(locations) == 0:
                for a, t, c in destinations:
                    if text.find(c.lower()) >= 0 or user_location.find(c.lower()) >= 0:
                        locations.append(a)
                    
            print(locations)
            print(text)
            '''
            print(status['user']['location'])
            print(status['user']['time_zone'])
            print(status['user']['geo_enabled'])
            print(status['geo'])
            print(status['coordinates'])
            print(status['place'])
            print('')'''
            #print(status)
            #user = get_user(status[])
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
    text = status['full_text'] if 'full_text' in status else status['text']

    if text.find('RT ') != -1:
            return None

    prob = text_to_prob(text)
    
    locations = find_locations(status, g_destinations)

    if prob < 0.500142755657:
        print('prob', prob, 'below threshold')
        return None
    return {
        'probability': prob,
        'source': 'twitter',
        'airport': locations,
        'twitter_message': text,
        'category': text_to_category(text),
        'created_at': tweet['created_at']
    }

def article_to_threat(article):
    text = (article['title'] or '') + ' - ' + (article['description'] or '')
    prob = text_to_prob(text)
    locations = find_locations(article, g_destinations)
    if prob < 0.500142755657:
        print('prob', prob, 'below threshold')
        return None
    return {
        'probability': prob,
        'source': 'newsapi.org',
        'airport': locations,
        'article_title': article['title'],
        'article_description': article['description'],
        'article_urlToImage': article['urlToImage'],
        'article_url': article['url'],
        'article_source': article['source'],
        'article_author': article['author'],
        'category': text_to_category(text),
        'created_at': article['publishedAt']
    }

class MyListener(tweepy.StreamListener):
    def on_status(self, status):
        status = status._json
        t = tweet_to_threat(status)
        if t is not None:
            threats.append(t)
            save_threats()
            print('new threat:', threats[-1])

    def on_error(self, status_code):
        print('error',status_code)

def get_keywords():

    # list of keyword permutations to search for
    targets = [t[1] for t in get_destinations('finnair_airports.csv')]
    problems = ['storm', 'rain', 'hail', 'flood', 'strike', 'closed', 'firefight', 'security',
            'military', 'shoot', 'shot', 'police', 'kill'
            'lakko', 'myrsky']
    
    return problems

    #from itertools import product
    #conditions = list(product(targets, problems))
    #conditions = [a + ' AND ' + b for a, b in conditions]
    #conditions = [b for a, b in conditions]
    #return conditions

def main():
    keys = open('twitter_token.txt','r').readlines()
    consumer_key = keys[0].strip()
    consumer_secret = keys[1].strip()
    access_token = keys[2].strip()
    access_token_secret = keys[3].strip()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    myListener = MyListener()
    while True:
        try:
            listener = tweepy.Stream(auth=auth, listener=myListener)
            listener.filter(track=get_keywords())
        except Exception:
            pass  # or you could use 'continue'

if __name__ == '__main__':
    #main()
    #exit(0)
    threats = []
    def save_model():
        with open('threats.json', 'w') as f:
            json.dump(threats, f)
    if True:
        with open('tweet_results.json') as f:
            tweets = json.load(f)
            for i, tweet in enumerate(tweets):
                #print(tweet.keys())
                t = tweet_to_threat(tweet)
                print(i, 'num threats', len(threats))
                if t:
                    threats.append(t)
                    print(threats[-1])
                    save_model()
    if True:
        with open('newsapi_results.json') as f:
            news = json.load(f)
            for i, article in enumerate(news):
                t = article_to_threat(article)
                print(i, 'num threats', len(threats))
                if t:
                    threats.append(t)
                    print(threats[-1])
                    save_model()
    save_model()
