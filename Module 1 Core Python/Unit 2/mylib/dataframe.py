# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:02:31 2019

@author: MASTER
"""
import statistics
import my_utils

class DataFrame():
    def __init__(self,data):
        pass
            
    def display(self,row_range=(0,5),col_range=(0,5)):
        '''
        displays the slice of the dataframe in the range of the given 
        rows and columns
        '''
        pass
            
    def info(self):
        '''
        returns a dictionary containing information about dataframe columns,
        their count and data type
        '''
        pass
        
    def describe(self):
        '''
        returns a dictionary containing statistics of each column 
        including mean,median,sd,max and min values
        '''
        pass
        
    def count_missing(self):
        '''
        returns the counts of missing values in each column
        '''
        pass
    
    def replace_missing(self,replace_with=0):
        '''
        replaces missing values in int of float column types 
        with the passed value in each column
        '''
        pass
        
    def value_counts(self):
        '''
        returns the count of unique values of all int of float type columns whose 
        number of unique value counts are less than 100
        '''
        pass
    
    def add_one_hot_columns(self,cols):
        '''
        for each column-name in the list given, calculate the unique values
        and then create that many additional columns in the dataframe,
        naming each new column with original_column_name_1, original_column_name_2 etc.
        Also removfe the oriiginal column from the dataframe
        '''
        pass
        
    def __len__(self):
        '''
        return the length of the dataframe in number of rows
        '''
        pass
        
    def get_rows_slice(self,row_range=None):
        '''
        returns a slice of dtaaframe rows in the given range.
        If given range is None it returns all the rows
        '''
        pass
                