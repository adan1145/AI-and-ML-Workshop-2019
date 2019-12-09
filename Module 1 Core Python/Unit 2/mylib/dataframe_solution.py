# -*- coding: utf-8 -*-
"""

@author: MASTER
"""
import statistics
import my_utils
import copy

class DataFrame():
    def __init__(self,data):
        '''
        First we need to store rows and dict_ of the dataframe
        Store column names in a property (first row of data)
        '''
        self.columns = data[0][:]
        '''

        Store data without column names (excluding the first row)
        '''
        self.excluding_the_first_row = data[1:][:]
        '''
        
        create a data list property to store all the data rows
        We will create tuples with first value of each tuple as the row number (index)
        and the second value as the row data (list)
        '''
        self.data = []
        self.dict_ =dict()

        '''
        
        go through each row in data enumerating it
            create a list for values
            go through each column within the row
                if it is a float, insert in the list of values by typecasting to float
                if it is an int, insert in the list of values by typercasting to int
                if it is neither float nor int, just add it as is in the list
            
            add a tuple to the data list property with enumerated index of this row 
            along with the row (list) itself
            
        '''
        for row in self.excluding_the_first_row:
            values=[]
            for col in row:
                if my_utils.is_float(col):
                    values.append(float(col))
                else:
                    values.append(col)
            self.data.append(values)
        self.data = list(enumerate(self.data))
        
        self.__set_dict__from_rows()
          # self.__set_rows_from_dict_()        
        self.info()
        
            
        # Now create a dictionary of dict_ with keys as column names and values as lists
        #self.__set_dict__from_rows()
        
    
    def __set_dict__from_rows(self):
        '''
        create a dict_ dictionary property
        '''
        self.dict_ =dict()
        col_list = self.columns
        row_data = self.data
        '''
        for each column in the dict_ list
            create a list for values
            for each row of data
               access this column's value and append to the list
            add the list to the dictionary
        finally replace the previous dict_ dictionary property
        '''
        for col_no,col in list(enumerate(col_list)):
            values=[]
            for row in row_data:
                values.append(row[1][col_no])
            self.dict_[col]=values
        
    def __set_rows_from_dict_(self):
      #  col_list = self.dict_.keys()
        col_data = self.dict_.values()
        '''
        create a rows list
        '''
        rows = []
        '''
        for each row in the data
            create a list for values
            for each column in dict_ list
               access this row's value and append to the list
            add the list to the rows list
        finally replace the previous data list property
        '''
        for row in range(len(self.data)):
            values=[]
            for col in col_data:
                values.append(col[row])
            rows.append(values)
        self.data = list(enumerate(rows))
                
                
            
    def display(self,row_range=(0,5),col_range=(0,5)):
        col_no,col_list = zip(*list(enumerate(self.columns)))
        row_data = self.data
        '''
        first diplay all column names in the given range
        Then for each row in the given range 
           go through each row's data for only the dict_ range given and display it
        '''
        print(col_list[col_range[0]:col_range[1]])
        print(row_data[row_range[0]:row_range[1]][col_range[0]:col_range[1]])
            
    def info(self):
        '''
        Create a dictionary for types of each column in the constructor
        Use a new private method __set_types for that
        for each column construct a dictionary with key as column name and
        value as a tuple containing length of the column and the data type
        Detect ype of the column by getting the first row of data and go through 
        each column using isinstance to infer type
        '''
        self.inf_ = dict()
        col_list = self.columns
        first_row = self.data[0][1]
        for col_no,col in list(enumerate(col_list)):
            length = len(self.dict_[col])
            self.inf_[col] = (length,type(first_row[col_no]))
            
        print(self.inf_)
    
    def __set_types(self,row):
        pass    
        
    def describe(self):
        '''
        create a stats dictionary
        for each column calculate stats if the column type is int or float
          Use statistics.mean, median and std and Python's own max min 
        return the dictonary
        '''
        
        cols = self.dict_
        self.stats = dict()
        for col,col_d in cols.items():
            if self.inf_[col][1] == type(0.0):
                mean = statistics.mean(col_d)
                median = statistics.median(col_d)
                std = statistics.stdev(col_d)
                maxx = max(col_d)
                minn = min(col_d)
                self.stats[col] = {'mean':mean,'median':median,'std':std,'max':maxx,'min':minn}
        print(self.stats)
        
    def count_missing(self):
        '''
        create a missing dictionary
        '''
        missing = dict()
        '''
        for each column if the type of column is either int or float
           for each row of the given column collect all values in a list that 
           are not int or float (i.e.) strings (assuming msising values 
           contain strings)
           insert the length of the missing values list in the dictionary
        return the dictonary
        '''
        col_list = self.columns
        for col in col_list:
            count_m = 0
            if self.inf_[col][1] == type(0.0):
                for row in self.dict_[col]:
                    count_m += not(isinstance(row,float))
                missing[col] = count_m
        print(missing)
    
    def replace_missing(self,replace_with=0.0):
        '''
        for each column if the type of column is either int or float
           for each row of the given column if the value is neither int nor float
           (i.e.) strings (assuming msising values contain strings) replace that value
           with the replace_with value
        call __set_rows_from_dict_ to update the data as well
           
        '''
        col_list = self.columns
        for col in col_list:
            if self.inf_[col][1] == type(0.0):
                for row_no,row in list(enumerate(self.dict_[col])):
                    if not(isinstance(row,float)):
                        self.dict_[col][row_no] = replace_with
        self.__set_rows_from_dict_()
    
    def value_counts(self):
        '''
        create a counts dictionary
        for each column 
            if the length of the unique values in that column < 100
                 for each row in that column update the counts with the value as key 
                     and adding 1 to the count of that key every time that value is 
                     encountered
                
        return counts   
        '''
        col_list = self.columns

        self.counts = dict()
        for col in col_list:
            self.counts[col] = dict()
            for row in self.dict_[col]:
                if row not in self.counts[col]:
                    self.counts[col][row] = 1
                else:
                    self.counts[col][row] +=1
            if len(self.counts[col]) >= 100:
                del(self.counts[col])
        print(self.counts)
                
    def add_one_hot_columns_(self,cols):
        '''
        for each column 
           obtain the unique values of the column as a list
           for each value in the list of unique values
               create a new list for one-hot values
               for each value in the column values (look up the dict_ dictionary)
                  if value is present in the dictionary append 1 to the one-hot-values list
                  otherwise append a 0 to the one-hot-values list
               add a new column to the dict_ dictionary as well as dict_ list with that 
               unique value as the name of the column
           Remove the column from the dict_ list as well as del the key
           for that column from the column dictionary. 
           If the column has already been removed catch that error and silently discsard it
         
         call __set_rows_from_dict_ to update the data as well
         call __set_types to update the types so that info method still works with new dict_
        '''
        
        for col in cols:
            unique_v = list(self.counts[col])
            for val in unique_v:
                one_hot_v = []
                try:
                    for v in self.dict_[col]:
                        if v == val:
                            one_hot_v.append(1)
                        else:
                            one_hot_v.append(0)
                    self.dict_[col+val] = one_hot_v 
                    self.columns.append(col+val)
                except KeyError:
                    print(col + 'not in the df.dict_')
            try:
                del self.dict_[col]
                self.columns.remove(col)
            except ValueError:
                pass
        self.__set_rows_from_dict_()
        #self.__set_types()
        self.info()
        
    def __len__(self):
        '''
        return the length of the data rows
        '''
        return len(self.data)
    def get_rows_slice(self,row_range=None):
        '''
        return the range of rows from data rows
        but return fll length if row_range is None
        '''
        return copy.deepcopy(self.data[row_range[0]:row_range[1]])
                