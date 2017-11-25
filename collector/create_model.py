# -*- coding: utf-8 -*-

#import keras
import pickle
import ujson as json
import re
import numpy as np
from sklearn.externals import joblib

def get_data():
    # return list of (string, label)
    
    results = []

    with open('newsapi_results.json') as f:
        newsapi_results = json.load(f)
    with open('newsapi_labels.json') as f:
        newsapi_labels = json.load(f)

    for article in newsapi_results:
        if article['title'] not in newsapi_labels:
            continue
        label = newsapi_labels[article['title']]
        text = str(article['title'].encode('utf-8')) + ' ' +\
            str((article['description'] or '').encode('utf-8'))
        results.append((text, label))

    with open('tweet_results.json') as f:
        twitter_results = json.load(f)
    with open('tweet_labels.json') as f:
        twitter_labels = json.load(f)

    for tweet in twitter_results:
        if str(tweet['id']) not in twitter_labels:
            continue
        label = newsapi_labels[article['title']]
        text = tweet['full_text']
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

def get_features():
    import os
    if os.path.isfile('X.npy'):
        return np.load('X.npy'), np.load('Y.npy')
    from generating_reviews_discovering_sentiment.encoder import Model
    data = get_data()

    X = []
    Y = []
    model = Model()

    batch_size = 200
    index = 0
    while True:
        end_index = min(index + batch_size, len(data))
        if end_index == index:
            break
        msgs = []
        for i in range(index, end_index):
            msg = data[i][0]
            msgs.append(msg)
            Y.append(float(data[i][1]))
        feats = model.transform(msgs)
        for f in feats:
            X.append(f)
        print(index,'/',len(data))
        index = end_index

    X = np.array(X)
    Y = np.array(Y)
    print(X[0])
    print(X.shape, Y.shape)
    np.save('X.npy', X)
    np.save('Y.npy', Y)
    return X, Y
    
if __name__ == '__main__':

    X, Y = get_features()
    print(X.shape, Y.shape)

    from sklearn.linear_model import LogisticRegression
    from sklearn.cross_validation import cross_val_score
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score, make_scorer, roc_auc_score, average_precision_score

    scoring = make_scorer(roc_auc_score)
    #scoring = make_scorer(average_precision_score)

    coefs = []
    intercepts = []

    skf = StratifiedKFold(3, shuffle=True)
    for train, test in skf.split(X, Y):

        m = LogisticRegression(C=1e-6, class_weight='balanced')
        m.fit(X[train], Y[train])
        #print(m.coef_, m.intercept_)
        coefs.append(m.coef_)
        intercepts.append(m.intercept_)

    m.coef_ = np.mean(coefs, axis=0)
    m.intercept_ = np.mean(intercepts, axis=0)

    # find threshold
    best_t = None
    best_s = 0
    for t in np.linspace(0.0, 1.0, 1000):
        score = accuracy_score(Y, np.greater(m.predict_proba(X)[:,1], t) * 1.0)
        if score > best_s:
            best_s = score
            best_t = t
        #print(t, score)
    print('best threshold:', best_t)
    print('final', accuracy_score(Y, m.predict_proba(X)[:,1] > best_t))
    joblib.dump(m, 'regressor.joblib')
    
