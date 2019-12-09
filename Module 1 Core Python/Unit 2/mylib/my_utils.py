# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:03:21 2019

@author: MASTER
"""

from math import sqrt

def is_float(s):
    '''
    in a try catch clause,try to typecast s as float.
    catch ValueError and return False otherwise return True (in the try)
    '''    
    try:
            float(s)
            return True
    except ValueError:
            return False
    
def rmse(predictions,targets):
    '''
    check for lengths to be equal and non-zero
    create a list containing the squares of differences between corresponding elements
    of predictions and target
    Take the mean of the list and then take square root of the mean
    return the final result
    '''
    if len(predictions)==len(targets) and len(predictions)!=0:
        sq = [(i-j)*(i-j) for i,j in zip(predictions,targets)]
        mean= sum(sq)/len(sq)
        return sqrt(mean)
    else:
        return "Lengths of predictions and targets are not equal or zero"

def cosine_similarity(a,b):
    '''
    check for lengths to be equal and non-zero
    calculate numerator
    calculate denominator 1
    calculate denominator 2
    return final result of numerator/(denominator1*denominator2)
    '''
    xy=[]
    lX=0
    lY=0
    
    # X = (input("Enter X sequence of floating point numbers(e.g 12.3,45.23,11.98): "))
    # Y = (input("Enter Y sequence of floating point numbers(e.g 12.3,45.23,11.98): "))

    #  X=a.split(',')
    # Y=b.split(',')
    X=a
    Y=b
    if len(X)==len(Y) and len(X)!=0:
        for z in range(0,len(X)):
            xy.append(float(X[z])*float(Y[z]))
            lX += float(X[z])*float(X[z])
            lY += float(Y[z])*float(Y[z])
    
        lX = sqrt(lX)
        lY = sqrt(lY)
        xy =sum(xy)
        return xy/(lX*lY)
        
    else:
        return "Lengths of a and b are not equal or zero"
    
    

        

