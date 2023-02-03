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
       
    def test_rotate_030_ShouldRotateCubeInRDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('R')
        self.assertEqual(rotatedCube, 'ygywbbygorrbrrowybwbrygrwwywyryorbbggwrbygbwgoogowgooo')
     
    def test_rotate_040_ShouldRotateCubeInrDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('r')
        self.assertEqual(rotatedCube, 'ygwwbyygwbyworrbrrobrbgrywywyryorbbggwgbygbwooorowgoog')
    
    def test_rotate_050_ShouldRotateCubeInBDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('B')
        self.assertEqual(rotatedCube, 'ygrwbgyggboorrorroggowgbyrrwyrworgbgbywbyybwwooyowbwyb')
    
    def test_rotate_060_ShouldRotateCubeInbDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('b')
        self.assertEqual(rotatedCube, 'ygrwbgyggbogrrwrrwrrybgwoggoyroorobgbywbyybwwooyowbwyb')
    
    def test_rotate_070_ShouldRotateCubeInLDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('L')
        self.assertEqual(rotatedCube, 'ggrbbgbggbobrryrrwoboggogwobywboygrrywwryyrwwyoywwbyoo')
        
    
    def test_rotate_080_ShouldRotateCubeInlDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('l')
        self.assertEqual(rotatedCube, 'ogrobgoggbobrryrrwobbggbgwgrrgyobwybywwwyyywwyoyrwbroo')
        
    def test_rotate_090_ShouldRotateCubeInUDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('U')
        self.assertEqual(rotatedCube, 'bobwbgyggobrrryrrwwyrggrgwyygryorbbgbbgwywwywooyowbooo')
        
    def test_rotate_100_ShouldRotateCubeInuDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('u')
        self.assertEqual(rotatedCube, 'wyrwbgyggygrrryrrwbobggrgwyobryorbbgwywwywgbbooyowbooo')
        
    def test_rotate_110_MissingDirectionRotation(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('')
        self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
        
    def test_rotate_120_MultistringRotation(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('FR')
        self.assertEqual(rotatedCube, 'ywbgbbggowwbrrowybrbrygrwwywyoyoobbygwybyggrrrrgowgooo')
        
    def test_rotate_910_InvalidDirection(self):
        cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        theCube = cube.Cube(cubeToRotate)
        rotatedCube = theCube.rotate('Q')
        self.assertEqual(rotatedCube, 'DirException occurred: Invalid Direction')
        #self.assertRaises(DirException, theCube.rotate('Z'))
    