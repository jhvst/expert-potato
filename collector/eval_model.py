# -*- coding: utf-8 -*-

import pickle
import ujson as json
import re
import sys
import numpy as np
from sklearn.externals import joblib
from create_model import word_tokenize
    
if __name__ == '__main__':
    reg = joblib.load('regressor.joblib')
    from generating_reviews_discovering_sentiment.encoder import Model
    m = Model()
    with open('words.json') as f:
        words = json.load(f)
        words_set = set(words)
    while True:
        text = input('>')

        x = np.zeros((1, len(words)))
        for word in word_tokenize(text):
            word = word.lower()
            if word in words_set:
                x[0, words.index(word)] = 1.0
        #feat = m.transform([text])
        prob = reg.predict_proba(x)[0, 1]
        print(prob, prob > 0.50064)
        

        
