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

    '''
    tso = TwitterSearchOrder() 
    tso.set_language('en')
    tso.set_include_entities(False) # and don't give us all those entity information

    ts = TwitterSearch(
        consumer_key = '***REMOVED***',
        consumer_secret = '***REMOVED***',
        access_token = '***REMOVED***',
        access_token_secret = '***REMOVED***'
     )

    def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
            time.sleep(60) # sleep for 60 seconds

    results = []
    skips = 0
    for keyword_list in get_keywords():
        tso.set_keywords(keyword_list)
        print 'searching for', keyword_list, '...',
        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
            if tweet['truncated']:
                skips += 1
                continue
            results.append(tweet)
            tweet['target'] = keyword_list[0] # Save target and cause in the result
            tweet['cause'] = keyword_list[1]
        print len(results), 'tweets total,', skips, 'skipped'''

    consumer_key = '***REMOVED***'
    consumer_secret = '***REMOVED***'
    access_token = '***REMOVED***'
    access_token_secret = '***REMOVED***'

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

