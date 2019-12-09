# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 02:41:46 2019

@author: MASTER
"""

class IntSet():
    """An intSet is a set of integers"""
        #Value of the set is represented by a list of ints, self.vals.
        #Each int in the set occurs in self.vals exactly once.
        
    def __init__(self):
        """Create an empty set of integers"""
        self.vals =set([])
    def insert(self, e):
        """Assumes e is an integer and inserts e into self if e is not already inserted"""
        self.vals.add(e)
    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError("{} not found".format(e))
        
    def getMembers(self):
        """Returns a list containing the elements of self.
        Nothing can be assumed about the order of the elements"""
        return list(self.vals)[:]
    
    def __str__(self):
        """Returns a string representation of self in sorted (ascending) order
           for example: {5,10,12}
        """
        return str(sorted(list(self.vals)))
        
    def __len__(self):
        '''
        return the length od the current set
        '''
        return len(list(self.vals))
        
        
        
        
        
        
        