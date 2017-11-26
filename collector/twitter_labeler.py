import ujson as json

def get_label(tweet):
    #print tweet.keys()
    print()
    print(tweet['full_text'])
    while True:
        result = input('This tweet will cause delay? 1 = yes, 0 = no: ')
        if result in ['0', '1']:
            return int(result)
    
def main():

    # load existing labels
    try:
        with open('tweet_labels.json') as f:
            labels = json.load(f)
    except:
        print('empty label file')
        labels = {}

    def save_labels():
        with open('tweet_labels.json', 'w') as f:
            json.dump(labels, f)
    # load tweets
    with open('tweet_results.json') as f:
        tweets = json.load(f)
    import random
    random.shuffle(tweets)

    # find tweets without labels
    for tweet in tweets:
        if tweet['retweeted']:
            continue
        if tweet['full_text'].startswith('RT '):
            continue
        id_str = str(tweet['id'])
        if id_str not in labels:
            labels[id_str] = get_label(tweet)
            save_labels()

if __name__ == '__main__':
    main()
