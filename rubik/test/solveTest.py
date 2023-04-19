from unittest import TestCase
from rubik.view.solve import solve
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import *


class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    def test100_solve_returnStubbedSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))

    
    def test110_solve_returnEmptyForSolvedCross(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
        
        
    def test120_solve_bottomCrossIfValid(self):
        parms = {}
        parms['cube'] = 'ywwobwwyybbwgrybyyrbgoggowoyorrogwrgrobwyrbborboywggrg'
        cubeBotCross = 'ywwobwwyybbwgrybyyrbgoggowoyorrogwrgrobwyrbborboywggrg'
        theCube = cube.Cube(cubeBotCross)
        result = solve(parms)
        botCross = solveBottomCross(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('uRUuBUBBuLUUFFRRUBBUULL', botCross)
     
    
    def test130_solve_bottomCrossIfValid(self):
        parms = {}
        parms['cube'] = 'ywwobwwyybbwgrybyyrbgoggowoyorrogwrgrobwyrbborboywggrg'
        cubeBotCross = 'ywwobwwyybbwgrybyyrbgoggowoyorrogwrgrobwyrbborboywggrg'
        theCube = cube.Cube(cubeBotCross)
        result = solve(parms)
        botCross = solveBottomCross(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('uRUuBUBBuLUUFFRRUBBUULL', botCross)  
        
    def test170_removeWhiteCorners(self): 
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeWhiteCorners = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        theCube = cube.Cube(cubeWhiteCorners)
        removeWhiteCorners(theCube)
        cornerWhites = [theCube.get()[DTR], theCube.get()[FBR], theCube.get()[RBL], theCube.get()[RBR], 
                    theCube.get()[BBL], theCube.get()[DBR], theCube.get()[DBL], theCube.get()[BBR], 
                    theCube.get()[LBL], theCube.get()[FBL], theCube.get()[LBR], theCube.get()[DTL]]
        x = False
        if 'w' not in cornerWhites:
            x = True
        self.assertEqual(True, x)  
        
    def test180_frontRightCorner(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeFrontRight = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo' 
        theCube = cube.Cube(cubeFrontRight)
        frontRightCorner(theCube)
        x = False
        if theCube.get()[DTR] == theCube.get()[DMM] and theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[RBL] == theCube.get()[RMM]:
            x = True
        self.assertEqual(True, x) 
    
    def test190_backRightCorner(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeBackRight = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo' 
        theCube = cube.Cube(cubeBackRight)
        backRightCorner(theCube)
        x = False
        if theCube.get()[DBR] == theCube.get()[DMM] and theCube.get()[RBR] == theCube.get()[RMM] and \
         theCube.get()[BBL] == theCube.get()[BMM]:
            x = True
        self.assertEqual(True, x) 
        
    def test200_backLeftCorner(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeBackLeft = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo' 
        theCube = cube.Cube(cubeBackLeft)
        backLeftCorner(theCube)
        x = False
        if theCube.get()[DBL] == theCube.get()[DMM] and theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LMM]:
            x = True
        self.assertEqual(True, x) 
        
    def test210_frontLeftCorner(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeFrontRight = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo' 
        theCube = cube.Cube(cubeFrontRight)
        frontRightCorner(theCube)
        x = False
        if theCube.get()[DTR] == theCube.get()[DMM] and theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[FBL] == theCube.get()[FMM]:
            x = True
        self.assertEqual(True, x) 
            
        
        
    
    def test140_solve_returnEmptyForSolvedBottom(self):
        parms = {}
        parms['cube'] = 'rrbbbobbbyyyyrrrrrgrrbgggggggbyoooooyyooybygowwwwwwwww'
        cubeBotLayer = 'rrbbbobbbyyyyrrrrrgrrbgggggggbyoooooyyooybygowwwwwwwww'
        theCube = cube.Cube(cubeBotLayer)
        result = solve(parms)
        botLayer = solveBottomLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', botLayer)   
    
    def test150_solve_bottomCornersIfValid(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeBotLayer = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        theCube = cube.Cube(cubeBotLayer)
        result = solve(parms)
        botLayer = solveBottomLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('BUbUBUbUURUruRUruRUruUUBubULUluLUluLUluUUFuf', botLayer)
        
    def test160_solve_bottomCornersIfValid(self):
        parms = {}
        parms['cube'] = 'yrrrbggbbwbrorbwrobbbyggwggrobyogyoyyrwyyooygrwowwwowg'
        cubeBotLayer = 'yrrrbggbbwbrorbwrobbbyggwggrobyogyoyyrwyyooygrwowwwowg'
        theCube = cube.Cube(cubeBotLayer)
        result = solve(parms)
        botLayer = solveBottomLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('RUrBUbURUrBUbURUrURUrURUrURUrUUUURurUUBUbuUUULulUFuf', botLayer)
    
    