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
        Test that creation of IntSet results in an empty set
        """
        result = IntSet()
        self.assertEqual(len(list(result.vals)), 0)# Writ the assert statement
        
    def test_IntSet_insert(self):
        """
        Test that insert method
        """
        s= IntSet()
        # insert integer 10 then write the appropriate assert
        # insert integer -5 then write multiple appropriate asserts
        # check for length, presence of 10, -5 and non-presence of something we did not insert
        s.insert(10)
        self.assertIn(10,s.vals)
        s.insert(-5)
        self.assertIn(-5,s.vals)
        s.insert(10)
        self.assertEqual(len(list(s.vals)),2)
        self.assertNotIn(12,s.vals)

    #@unittest.skip('Skip this test')
    def test_IntSet_remove(self):
        """
        Test the remove method
        """
        s = IntSet()
        # insert 10, 1, 0, 101, then remove 1 and assert for 1's presence
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        s.remove(1)
        self.assertNotIn(1,s.vals)
        '''try to remove someting we did not insert and verify that it is not present
           use isinstance with try/except to realize this
        '''
        self.assertNotIn(12,s.vals)
        with self.assertRaises(ValueError) as a:
            s.remove(12)
        self.assertEqual('12 not found', str(a.exception))
        self.assertRaises(ValueError,s.remove,12)
        try:
            s.remove(12)
        except ValueError as ee:
            self.assertIsInstance(ee,ValueError)
            
    def test_IntSet_getMembers(self):
        
        s = IntSet()
        '''
        insert 10, 1, 0, 101 then test getMembers and verify the presence of 
        all inserted in the result of getmembers 
        and also verify a couple of values that you did not insert
        '''
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        result = s.getMembers()
        self.assertTrue(s.member(10))
        self.assertTrue(s.member(1))
        self.assertTrue(s.member(0))
        self.assertTrue(s.member(101))
        self.assertFalse(s.member(12))
        self.assertFalse(s.member(102))
        self.assertIn(10,result)
        self.assertIn(1,result)
        self.assertIn(0,result)
        self.assertIn(101,result)
        self.assertNotIn(12,result)
        self.assertNotIn(102,result)

    def test_IntSet_len(self):
        s = IntSet()
        '''
        insert 10, 1, 0, 101 then test getMembers and verify by calling len(s)
        '''
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        result = s.getMembers()
        self.assertEqual(len(s),len(result))
        
    def test_Intset_str(self):
        s= IntSet()
        s.insert(10)
        s.insert(1)
        s.insert(0)
        s.insert(101)
        uu = str(s)
        self.assertIsInstance(uu,str)
        r = s.getMembers()
        for n in range(0,len(r)-1):
            p = r[n+1]
            self.assertGreater(p,r[n])

        