# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 02:44:14 2019

@author: MASTER
"""

from intset import IntSet
import unittest
#import sys

class TestIntSet(unittest.TestCase):
    """
    Test the constructor from the IntSet library
    """
    def test_Intset(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = IntSet()
        self.assertEqual(result.vals,[])
        
    def test_IntSet_insert(self):
        """
        Test that insert method
        """
        s = IntSet()
        s.insert(10)
        self.assertEqual(s.vals,[10])
        s.insert(-5)
        self.assertEqual(len(s.vals),2)
        self.assertIn(-5,s.vals)
        self.assertIn(10,s.vals)
        self.assertFalse(12 in s.vals)
        
    #@unittest.skip('Skip this test')
    def test_IntSet_remove(self):
        """
        Test the remove method
        """
        s = IntSet()
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        s.remove(1)
        self.assertFalse(1 in s.vals)
        try:
            s.remove(22)
        except Exception as e:
            self.assertIsInstance(e,ValueError)
            
    def test_IntSet_getMembers(self):
        s = IntSet()
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        result = s.getMembers()
        self.assertTrue(1 in s.vals)
        self.assertTrue(10 in s.vals)
        self.assertTrue(0 in s.vals)
        self.assertTrue(101 in s.vals)
        self.assertTrue(100 not in s.vals)
        
    def test_IntSet_len(self):
        s = IntSet()
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        self.assertEqual(len(s),4)

        