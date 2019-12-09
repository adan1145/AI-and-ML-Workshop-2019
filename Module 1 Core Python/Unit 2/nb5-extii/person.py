# -*- coding: utf-8 -*-
"""

@author: MASTER
"""
import datetime

class Person(object):
    
    def __init__(self, name):
        """Create a person"""
        name =name.lower()
        self.name = name.split(' ')# Set name property
        self.Lastname = self.name[-1]
        self.name = ' '.join(self.name[0:-1])
        
        '''
        if there is a blank somewhere in the name, then consider it a 
        Firstname Lastname combination. Then extract lastname 
        in a property lastName and First name in name.
        Use rindex string method to detect last blank in the string
        '''
        self.lastblank = name.rindex(' ')
        self.lastname = name[self.lastblank+1:]
        self.Name = name[:self.lastblank-1]
    def getName(self):
        """Return's self's name
        """
        return self.name
    
    def getLastName(self):
        """Returns self's last name"""
        return self.Lastname
		
    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate
		
    def getAge(self):
        """Returns self's current age in years
           USe datetime.date.today() method and see what attributes
           it has to extract current year
        """
        self.age = datetime.date.today().year-self.birthday.year
        return self.age
		
    def __lt__(self, other):
        if self.Lastname == other.Lastname:
            return self.name < other.name
        else:
            return self.Lastname < other.Lastname
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""

    def __str__(self):
        """
           Returns self's name. if last name present then concantenate
           first and last names with a ' ' in between, otherwise just return the name
        """
        if self.Lastname =='':
            return self.name
        else:
            return self.name+' '+self.Lastname
		