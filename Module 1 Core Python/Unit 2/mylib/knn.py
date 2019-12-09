# -*- coding: utf-8 -*-
"""

@author: MASTER
"""
import my_utils
import statistics

class KNN():
    def __init__(self,k=5,method='cosine'):
        '''
        set k as a property
        set the similarity function as a property based on method. This means set a function
        pointer to one of the similarity functions in my_utils
        set data to None for now
        
        '''
        self.k = k
        if(method == 'cosine'):
            self.func = my_utils.cosine_similarity
        else:
            self.func = my_utils.rmse
        self.data = [] 
        
    def fit(self,data,target_column):
        '''
        copy only the lists representing data (without the index)
        into a list. Thus the data property shall be a list of lists
        Set the target property as another empty list first
        Then for each row in the data access only the target column's index
        and append the value of that column to the target list and 
        also remove that value from the data property
        So at the end all lists representing rows would have the target column
        values removed and they should be shorter in size by one column
        '''
        
        for _,d in data:
            self.data.append(d)
        self.target = []
        for row in self.data:
            self.target.append(row[target_column])
            del row[target_column]
    
    def predict(self,input_data):
        '''
        if data is not set (is still None) then return error saying that
        the KNN model mut be fitted before prediction
        for each row in data call the similarity function with that row and
        the input_data as arguments. collect the similarity scores in a list of 
        tuples with each tuple containing the similarity score, row number and 
        the target value
        Update the similarity scores list of tuples by sorting in descending order
        (highes similarity in the front of the list) and pick only first k tuples
        from the list discarding others.
        
        Take the mean of all the similarity scores (first member of each tuple 
        in the list). This is the final prediction
        Return one tuple containing the first k-tuples used to find the mean 
        and the final prediction
        
        '''
        
        if self.data == []:
            return print('Error: KNN model must be fitted before prediction')
        scores = []
        r_no = 0
        for row in self.data:
           scores.append((self.func(input_data,row),r_no,self.target[r_no]))
           r_no += 1
        scores.sort(reverse=True)
        scores = scores[0:self.k]
        mean = statistics.mean(list(zip(*scores))[2])
        return (scores,mean) 