import ujson as json
import random

def get_label(message):
    #print tweet.keys()
    print()
    #print message
    #print message['description']
    print(message['title'])
    while True:
        result = input('This article will cause delay? 1 = yes, 0 = no: ')
        if result in ['0', '1']:
            return int(result)
    
def main():

    # load existing labels
    try:
        with open('newsapi_labels.json') as f:
            labels = json.load(f)
    except:
        print('empty label file')
        labels = {}

    def save_labels():
        with open('newsapi_labels.json', 'w') as f:
            json.dump(labels, f)

    # load tweets
    with open('newsapi_results.json') as f:
        news = json.load(f)

    random.shuffle(news)
    # find tweets without labels
    for article in news:
        id_str = article['title']
        if id_str not in labels:
            labels[id_str] = get_label(article)
            save_labels()

if __name__ == '__main__':
    main()
