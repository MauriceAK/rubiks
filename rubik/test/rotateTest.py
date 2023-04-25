'''
Created on Feb 3, 2023

@author: Maurice Kenon
'''

from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    #def test100_rotate_returnStubbedSolution(self):
    #    encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
    #    parms = {}
    #    parms['cube'] = encodedCube
    #    parms['dir'] = 'F'
    #    result = rotate(parms)
    #    self.assertIn('status', result)
    #    self.assertEqual('ok', result['status'])
    #    self.assertEqual(encodedCube, result.get('cube'))

        
    def test010_rotate_shortCubeKey(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], 'Error: Invalid cube length')
        
    def test020_rotate_invalidMiddles(self):
        encodedCube = 'bbbbbbrbbrrrrbrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], 'Error: Cube middles are not unique')
    
    def test030_rotate_notAlphaNum(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwww!'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], 'Error: Invalid characters present')
    
    def test040_rotate_valid(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual(result['status'], 'ok')
