#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

class preprocess_df():
    
    def __init__(self,df,target_col,df_test,one_hot=False,scaler=None):
        self.df = df
        #handle target column
        self.df.dropna(axis=0, subset=[target_col],inplace=True)
        self.y = df[target_col]
        df.drop([target_col], axis=1, inplace=True)
        len_X = len(df)
        combined = pd.concat([df,df_test])
        print(len(combined.columns))
        #handle combined
        self.split_num_and_cat(combined)
        self.impute_num_cols()
        self.impute_cat_cols()
        self.labelEncode()
        
        if one_hot:
            self.OneHotEncode() 
        if scaler is not None:
            self.scale_num_columns(scaler)
      
        print(len(self.cat_df.columns))
        print(len(self.num_df.columns))
        self.combined = pd.concat([self.cat_df,self.num_df],axis=1).reset_index()
        if 'index' in self.combined.columns:
            self.combined.drop('index',axis=1,inplace=True)
        print(len(self.combined.columns))
        self.X = self.combined[:len_X]
        self.X_test = self.combined[len_X:]
        print(len(self.X.columns))
        
        
        
        
    def split_num_and_cat(self,df,cat_keep_threshold=10):
        self.cat_cols = [col for col in df.columns if df[col].dtype == "object"]
        self.low_count_cols = [col for col in self.cat_cols if df[col].nunique() < cat_keep_threshold]
        self.high_count_cols = list(set(self.cat_cols)-set(self.low_count_cols))
        self.cat_df = df[self.cat_cols]
        self.num_df = df.drop(self.cat_cols,axis=1)
        
        
    
    def impute_num_cols(self,strategy='median'):
        my_imputer = SimpleImputer(strategy=strategy)
        columns = self.num_df.columns
        self.num_df = pd.DataFrame(my_imputer.fit_transform(self.num_df))
        self.num_df.columns = columns
        
        
    def impute_cat_cols(self,strategy='most_frequent'):
        my_imputer_cat = SimpleImputer(strategy=strategy)
        columns = self.cat_df.columns
        self.cat_df = pd.DataFrame(my_imputer_cat.fit_transform(self.cat_df))
        self.cat_df.columns = columns
        
    def labelEncode(self):
        label_encoder = LabelEncoder()
        for col in self.cat_cols:
            self.cat_df[col] = label_encoder.fit_transform(self.cat_df[col])
            
    def split_df(self,train_size=0.8,test_size=0.2,stratify=None):
        ret_dict = {}
        
        ret_dict['X_train'],ret_dict['X_test'],ret_dict['y_train'],ret_dict['y_test'] = train_test_split(self.X,
                                                            self.y,train_size=train_size,random_state=0,
                                                            stratify=stratify)
            
        if test_size is not None:
            ret_dict['X_valid'] = ret_dict['X_test']
            ret_dict['y_valid'] = ret_dict['y_test']
            ret_dict['X_train'],ret_dict['X_test'],ret_dict['y_train'],ret_dict['y_test'] = train_test_split(ret_dict['X_train'],ret_dict['y_train'],
                                                   test_size=test_size,random_state=100,stratify=stratify)
        return ret_dict
    
    def OneHotEncode(self):
        high_count_df = self.cat_df[self.high_count_cols]
        dummy = pd.get_dummies(self.cat_df,columns=self.low_count_cols)
        self.cat_df = pd.concat([high_count_df,dummy],axis=1)
        
    def scale_num_columns(self,scaler):
        num_scaler = scaler()
        num_scaler.fit(self.num_df)
        self.num_df = pd.DataFrame(num_scaler.transform(self.num_df),columns=self.num_df.columns)
        
            
            
        

