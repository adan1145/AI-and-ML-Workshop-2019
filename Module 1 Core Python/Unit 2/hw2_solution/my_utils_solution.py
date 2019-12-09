# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:03:21 2019

@author: MASTER
"""

import math
import statistics

def cosine_similarity(a,b):
    if len(a) == 0 or len(b) == 0:
        return 'lengths of vectors must be > 0'
    if len(a) != len(b):
        return 'lengths of vectors must be equal'
    
    numerator = sum([a[i]*b[i] for i in range(len(a))])
    denom1 = math.sqrt(sum([a[i]**2 for i in range(len(a))]))
    denom2 = math.sqrt(sum([b[i]**2 for i in range(len(b))]))
    return numerator/(denom1*denom2)
    

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def rmse(predictions,targets):
    if len(predictions) == 0 or len(targets) == 0:
        return 'lengths of vectors must be > 0'
    if len(predictions) != len(targets):
        return 'lengths of vectors must be equal'
    
    return math.sqrt(statistics.mean([(predictions[i] - targets[i])**2 for i in range(len(targets))]))
