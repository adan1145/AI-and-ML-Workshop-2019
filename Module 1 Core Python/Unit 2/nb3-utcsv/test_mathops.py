# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:38:16 2019

@author: MASTER
"""

import mathops
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the mathops library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mathops.add(1, 2)
        self.assertEqual(result, 3)
        
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mathops.add(10.5, 2)
        self.assertEqual(result, 12.5)
        
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mathops.add('abc', 'def')
        self.assertEqual(result, 'abcdef')
        
        