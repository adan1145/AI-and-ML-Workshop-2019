# -*- coding: utf-8 -*-
"""
@author: MASTER
"""
from person import Person

class NUCES_Person(Person):
    id = 0
    def __init__(self, name):
        super().__init__(name)
        '''
        Set the idNum of the student to the next available Id
        then increment the next available Id
        '''
        self.idNum = NUCES_Person.id
        NUCES_Person.id +=1
        
    def getIdNum(self):
        '''
        return this student's id
        '''
        return self.idNum
    
    def __lt__(self, other):
        '''
        compare student ids and return if self is less than the other
        '''
        return self.idNum<other.idNum
    
    def isStudent(self):
        return self.__class__ is Student or self.__class__ is UG or self.__class__ is Grad

class Student(NUCES_Person):
    '''
    Abstract Class
    '''
    pass
class UG(Student):
    def __init__(self, name, classYear):
        '''
        Call parent's constructor and set the class Year property
        '''
        super().__init__(name)
        self.class_Year = classYear

        
    def getClass(self):
        '''
        Return the class year
        '''
        return self.class_Year


class Grad(Student):
    pass

class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        '''
         Call parent's constructor and set the from school property
        '''
        super().__init__(name)
        self.fromschool = fromSchool

    def getOldSchool(self):
        
        return self.fromschool
        
        
