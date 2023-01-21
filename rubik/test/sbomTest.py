'''
Created on Jan 20, 2023

@author: Maurice
'''
import unittest
import app

class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'mak0078'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)

