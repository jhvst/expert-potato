import requests
import ujson as json

def get_keywords():
    # list of keyword permutations to search for
    
    targets = ['heathrow', 'helsinki-vantaa', 'finnair']
    problems = ['storm', 'rain', 'strike', 'fire', 'military',
            'lakko', 'myrsky', 'extreme', 'cancelled', 'delay', 'delayed',
            'cancellation']
    #problems = ['delay', 'delayed', 'storm', 'rain', 'ice', 'strike', 'closed', 'fire',
    #'military']
    from itertools import product
    return product(targets, problems)

def main():
    apikey = '141d03e1166245eba71c3d00d7d316a4'
    '''curl https://newsapi.org/v2/everything -G \
        -d q=Apple \
        -d from=2017-11-25 \
        -d sortBy=popularity \
        -d apiKey=141d03e1166245eba71c3d00d7d316a4'''

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
