import requests
import ujson as json

def get_keywords():
    # list of keyword permutations to search for
    # read airports
    with open('finnair_airports.csv') as f:
        airports = [a.split(',')[2].strip() for a in f.readlines()]
        airports = [a.replace('"','') for a in airports]
    
    targets = airports
    problems = ['storm', 'rain', 'strike', 'fire', 'military', 'lakko',
            'myrsky', 'bomb', 'threat', 'security', 'delay', 'delayed',
            'cancelled']
    #problems = ['delay', 'delayed', 'storm', 'rain', 'ice', 'strike', 'closed', 'fire',
    #'military']
    from itertools import product
    return product(targets, problems)

def main():
    apikey = open('newsapi_token.txt','r').read().strip()
    results = []
    for keywords in get_keywords():
        print('searching for', keywords)
        page = 1
        while True:
            r = requests.get('https://newsapi.org/v2/everything',
                {
                    'q': ' AND '.join(keywords),
                    'sortBy': 'popularity',
                    'apiKey': apikey,
                    'page': page
                }
            )
            obj = r.json()
            if not 'articles' in obj:
                break
            for a in obj['articles']:
                results.append(a)
            print('have', len(results), 'articles')
            if len(obj['articles']) == 20:
                page += 1
                continue
            break
    with open('newsapi_results.json', 'w') as f:
        json.dump(results, f)
    print('done')

if __name__ == '__main__':
    main()
