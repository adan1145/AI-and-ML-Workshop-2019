# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 04:42:20 2019

@author: MASTER
"""
from person import Person
class NUCES_Person(Person):
    nextIdNum = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self.idNum = NUCES_Person.nextIdNum
        NUCES_Person.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def isStudent(self):
        return isinstance(self, Student)
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def __str__(self):
        return self.name

class Student(NUCES_Person):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        super().__init__(name)
        self.year = classYear
        
    def getClass(self):
        return self.year


class Grad(Student):
    pass

class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        super().__init__(name)
        self.fromSchool = fromSchool
        
    def getOldSchool(self):
            return self.fromSchool
