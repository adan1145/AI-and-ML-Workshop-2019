# -*- coding: utf-8 -*-
"""

@author: MASTER
"""

class Course(object):
    
    def __init__(self,subject):
        """Create empty grade book
        Set subject property
        Create an empty student names list
        Create an empty grades dictionary
        set a boolean property that identifies if the student list is sorted
        (Default is True)
        """
        self.gradebook =[]
        self.Subject=subject
        self.students=[]
        self.gradesdict={}
        self.issorted=True
        
    def addStudent(self, student):
        """
        Assumes: student is of type Student
        Add student to the list
        Raise Value Error if student already in the list
        Create an entry in the grades dict with value an empty list 
        for the student's semester grades
        set the boolean flag for sorted to False
        """
        try:
            self.students.append(student)
        except:
            raise ValueError('Student {} is already in the list'.format(student))
        self.gradesdict[student] = []
        self.issorted=False
        
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student
        Raise value error is student's key not found in grades dict
        """
        try:
            self.gradesdict[student].append(grade)
        except:
            raise ValueError('Student key not found in the grades dict'.format(student))
       
    def getGrades(self, student):
        """Return a copy of the list of grades for student
           Raise value error is student's key not found in grades dict
        """
        try:
            return self.gradesdict[student]
        except:
            raise ValueError('Student key not found in the grades dict'.format(student))
            
    def getStudents_list(self):
        """Return a sorted copy of list of the students in the grade book
           Set sorted boolean flag accordingly
        """
        self.issorted = True
        
        return sorted(self.students)
        
    def getStudents_gen(self):
        """Return the students in the grade book one at a time
           in alphabetical order (generator)
        """
        li = sorted(self.students)
        for stu in li:
            yield stu