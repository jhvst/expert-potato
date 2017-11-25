# -*- coding: utf-8 -*-

import keras
import cPickle as pickle
import ujson as json
import re

def get_data():
    # return list of (string, label)
    
    results = []

    with open('newsapi_results.pkl') as f:
        newsapi_results = pickle.load(f)
    with open('newsapi_labels.json') as f:
        newsapi_labels = json.load(f)

    for article in newsapi_results:
        if article['title'] not in newsapi_labels:
            continue
        label = newsapi_labels[article['title']]
        text = str(article['title'].encode('utf-8')) + ' ' +\
            str((article['description'] or '').encode('utf-8'))
        results.append((text, label))

    with open('tweet_results.pkl') as f:
        twitter_results = pickle.load(f)
    with open('tweet_labels.json') as f:
        twitter_labels = json.load(f)

    for tweet in twitter_results:
        if str(tweet['id']) not in twitter_labels:
            continue
        label = newsapi_labels[article['title']]
        text = tweet['full_text'].encode('utf-8')
        results.append((text, label))

    return results


def sent_tokenize(text, language='english'):
    from nltk.data import load
    tokenizer = load('tokenizers/punkt/{0}.pickle'.format(language))
    return tokenizer.tokenize(text)

from nltk.tokenize.treebank import TreebankWordTokenizer

_treebank_word_tokenizer = TreebankWordTokenizer()

improved_open_quote_regex = re.compile(u'([«“‘])', re.U)
improved_close_quote_regex = re.compile(u'([»”’])', re.U)
improved_punct_regex = re.compile(r'([^\.])(\.)([\]\)}>"\'' u'»”’ ' r']*)\s*$', re.U)
_treebank_word_tokenizer.STARTING_QUOTES.insert(0, (improved_open_quote_regex, r' \1 '))
_treebank_word_tokenizer.ENDING_QUOTES.insert(0, (improved_close_quote_regex, r' \1 '))
_treebank_word_tokenizer.PUNCTUATION.insert(0, (improved_punct_regex, r'\1 \2 \3 '))

def word_tokenize(text, language='english', preserve_line=False):

    """:param text: text to split into words
    :param text: str
    :param language: the model name in the Punkt corpus
    :type language: str
    :param preserve_line: An option to keep the preserve the sentence and not sentence tokenize it.
    :type preserver_line: bool
    """
    sentences = [text] if preserve_line else sent_tokenize(text, language)
    return [token for sent in sentences
            for token in _treebank_word_tokenizer.tokenize(sent)]

def tokenize():
    data = get_data()
    X = []
    for msg, label in data:
        X.append(model.transform(msg))
        Y.append(float(label))

if __name__ == '__main__':
    tokenize()
