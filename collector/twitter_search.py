#from TwitterSearch import *
import tweepy
import json #ujson as json
import time

def get_keywords():
    # list of keyword permutations to search for
    # read airports
    with open('finnair_airports.csv') as f:
        airports = [a.split(',')[2].strip() for a in f.readlines()]
        airports = [a.replace('"','') for a in airports]
    
    targets = airports
    problems = ['storm', 'rain', 'strike', 'fire', 'military', 'lakko',
            'myrsky', 'bomb', 'threat', 'security']

    from itertools import product
    return product(targets, problems)

#print json.dumps(get_keywords(), indent=4)
#exit(0)

def get_tweets():

    results = []
    skips = 0

    keys = open('twitter_token.txt','r').readlines()
    consumer_key = keys[0].strip()
    consumer_secret = keys[1].strip()
    access_token = keys[2].strip()
    access_token_secret = keys[3].strip()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
    
    print('api created')
    results = []
    skips = 0
    for keyword_list in get_keywords():
        print('searching for', keyword_list[0], keyword_list[1], '...')
        #for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
        query = ' AND '.join(keyword_list)
        max_items = 500
        for tweet in tweepy.Cursor(api.search, q=query, count=100,
                tweet_mode='extended').items(max_items):
            tweet = tweet._json
            if tweet['truncated']:
                skips += 1
                continue
            results.append(tweet)
            tweet['target'] = keyword_list[0] # Save target and cause in the result
            tweet['cause'] = keyword_list[1]
        print(len(results), 'tweets total,', skips, 'skipped')
    
    with open('tweet_results.json', 'w') as f:
        json.dump(results, f)
    print('done')

if __name__ == '__main__':
    get_tweets()

