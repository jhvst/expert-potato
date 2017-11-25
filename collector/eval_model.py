# -*- coding: utf-8 -*-

import pickle
import ujson as json
import re
import sys
import numpy as np
from sklearn.externals import joblib
    
if __name__ == '__main__':

    text = ' '.join(sys.argv[1:]).strip()
    reg = joblib.load('regressor.joblib')
    from generating_reviews_discovering_sentiment.encoder import Model
    m = Model()
    print('input:', text)
    feat = m.transform([text])
    print(feat)
    prob = reg.predict_proba(feat)[0, 1]
    print(prob)
    

    
