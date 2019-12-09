# -*- coding: utf-8 -*-
"""

@author: MASTER
"""
import my_utils_solution
import statistics

class KNN():
    def __init__(self,k=5,method='cosine'):
        self.k = k
        self.data = None
        if method.lower() == 'cosine':
            self.similarity_func = my_utils_solution.cosine_similarity
        
    def fit(self,data,target_column):
        self.data = [data[i][1].copy() for i in range(len(data))]
        self.target = []
        for row in self.data:
            value = row[target_column]
            self.target.append(value)
            row.remove(value)
            
    
    def predict(self,input_data):
        if self.data is None:
            return 'Error: This KNN instance has not been fitted yet' 
        
        similarity_scores = [(self.similarity_func(self.data[i],input_data),i,self.target[i]) for i in range(len(self.data))]
        similarity_scores.sort(reverse=True)
        similarity_scores = similarity_scores[:self.k]
        predicted_values = [x[0] for x in similarity_scores]
        predicted_value = statistics.mean(predicted_values)
        return (similarity_scores,predicted_value)
        