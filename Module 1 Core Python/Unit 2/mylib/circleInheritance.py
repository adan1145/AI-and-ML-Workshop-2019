# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:47:47 2019

@author: MASTER
"""
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        
class Circle(Shape):
    """Circle class"""
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1,x=0,y=0):
        """Create a Circle with the given radius"""
        self.radius = r
        self.all_circles.append(self)
        
    @staticmethod    
    def circle_area(radius):
        """determine the area of the Circle"""
        return Circle.pi * radius * radius
    
    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.circle_area(c.radius)
        return total
    

