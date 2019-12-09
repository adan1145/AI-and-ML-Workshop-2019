# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:02:31 2019

@author: MASTER
"""
import statistics
import my_utils_solution

class DataFrame():
    def __init__(self,data):
        self.columns = data[0]
        self.types = {}
        self.data = []
        data_rows = data[1:] # local variable
        
        for index,row in enumerate(data_rows):
            l = []
            for col in row:
                if my_utils_solution.is_float(col):
                    l.append(float(col))
                elif col.isdigit():
                    l.append(int(col))
                else:
                    l.append(col)
            self.data.append((index,l))
            
        # Now make the dictionary with each column containing its values    
        self.set_columns_from_data()
        
        self.set_types(self.data[0][1])
            
        
    
    def set_columns_from_data(self):
        self.dict_ = {}
        for colnum in range(len(self.columns)):
            column_values = []
            for i in range(len(self.data)):
                column_values.append(self.data[i][1][colnum])
                
            self.dict_[self.columns[colnum]] = column_values
        
    def set_data_from_columns(self):
        new_data = []
        for i in range(len(self.data)):
            row_data = []
            for col in self.columns:
                row_data.append(self.dict_[col][i])
            new_data.append((i,row_data))
            
        self.data = new_data
        
    def set_types(self,data_row):
        for i in range(len(data_row)):
            value = data_row[i]
            if my_utils_solution.is_float(value):
                self.types[self.columns[i]] = type(float(value))
            elif value.isdigit():
                self.types[self.columns[i]] = type(int(value))
            else:
                self.types[self.columns[i]] = type(str(value))
                
    def display(self,row_range=(0,5),col_range=(0,5)):
        for col_num in range(*col_range):
            print(self.columns[col_num],end='  ')
        print()
        
        for row_num in range(*row_range):
            for col_num in range(*col_range):
                print(self.data[row_num][1][col_num],end='  ')
            print()
            
    def info(self):
        return {col:(len(self.dict_[col]),self.types[col]) for col in self.columns}
        
    def describe(self):
        
        stats = {}
        for col in self.columns:
            if isinstance(self.dict_[col][0], int) or isinstance(self.dict_[col][0], float):
                stats[col] = {}
                stats[col]['mean'] = statistics.mean(self.dict_[col])
                stats[col]['median'] = statistics.median(self.dict_[col])
                stats[col]['std'] = statistics.stdev(self.dict_[col])
                stats[col]['max'] = max(self.dict_[col])
                stats[col]['min'] = min(self.dict_[col])
            
        return stats   
        
    def count_missing(self):
        missing_dict = {}
        for col in self.columns:
            if isinstance(self.dict_[col][0], int) or isinstance(self.dict_[col][0], float):
                missing = [value for value in self.dict_[col] if not isinstance(value, int) and not isinstance(value, float)]
                missing_dict[col] = len(missing)
        return missing_dict
    
    def replace_missing(self,replace_with=0.0):
        for col in self.columns:
            if isinstance(self.dict_[col][0], int) or isinstance(self.dict_[col][0], float):
                for i in range(len(self.dict_[col])):
                    value = self.dict_[col][i]
                    if not isinstance(value, int) and not isinstance(value, float):
                        self.dict_[col][i] = replace_with
                        
        self.set_data_from_columns()
        
        
    def value_counts(self):
        counts = {}
        for col in self.columns:
            if len(set(self.dict_[col])) < 100:
                for value in self.dict_[col]:
                    counts.setdefault(col,{})
                    counts[col].setdefault(value,0)
                    counts[col][value] += 1
        return counts
    
    def add_one_hot_columns(self,cols):
        for col in cols:
            unique_values = list(set(self.dict_[col]))
            for i in range(len(unique_values)):
                new_values = []
                for val in self.dict_[col]:
                    if val == unique_values[i]:
                        new_values.append(1)
                    else:
                        new_values.append(0)
                self.dict_[unique_values[i]] = new_values
                self.columns.append(unique_values[i])
            try:
                self.columns.remove(col)
                del self.dict_[col]
            except ValueError:
                pass
        
        self.set_data_from_columns()
        self.set_types(self.data[0][1])
                
    def __len__(self):
        return len(self.data)
    
    def get_rows_slice(self,row_range=None):
        if row_range == None:
            rows = (0,len(self.data))
        else:
            rows = row_range
            
        return self.data[rows[0]:rows[1]]
        
                