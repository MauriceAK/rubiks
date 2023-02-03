'''
Created on Feb 3, 2023

@author: Maurice
'''
import unittest
import rubik.model.cube as cube


class CubeTest(unittest.TestCase):

    def test_rotate_010_ShouldRotateCubeInFDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('F')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_020_ShouldRotateCubeInfDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('f')
        self.assertEqual(rotatedCube, 'rgggbgywyyoboryorwobrggrgwywywyowbbbgwwbyybrrrrgowbooo')
       
    #def test_rotate_030_ShouldRotateCubeInRDirection(self):
    #    cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
    #    theCube = cube.Cube(cubeToRotate)
    #    rotatedCube = theCube.rotate('R')
    #    self.assertEqual(rotatedCube, 'ygywbbygorrbrrowybwbrygrwwywyryorbbggwrbygbwgoogowgooo')
     
    #def test_rotate_040_ShouldRotateCubeInrDirection(self):
    #    cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
    #    theCube = cube.Cube(cubeToRotate)
    #    rotatedCube = theCube.rotate('r')
    #    self.assertEqual(rotatedCube, 'ygwwbyygwbyworrbrrobrbgrywywyryorbbggwgbygbwooorowgoog')
    
    def test_rotate_050_ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'ygrwbgbbgbobrryyggobrggrrrwwyryorgwygwwbyybwwoooowooby')
    
    def test_rotate_060_ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'ygwwbyygwbyworrbrrobrbgrywywyryorbbggwgbygbwooorowgoog')
    