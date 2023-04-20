from unittest import TestCase
from rubik.view.solve import solve
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *


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

    
    def test200_solve_returnEmptyForSolvedCross(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', result.get('solution'))
        
        
    def test210_solve_bottomCrossIfValid(self):
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
     
    
    def test220_solve_bottomCrossIfValid(self):
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
       
    def test300_removeWhiteCorners(self): 
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
      
    def test310_frontRightCorner(self):
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
    
    def test320_backRightCorner(self):
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
       
    def test330_backLeftCorner(self):
        parms = {}
        parms['cube'] = 'rrrrbggbbwbgorywrrwyooggwggbbbyogyoyyboryoyygrwowwwowb'
        cubeBackLeft = 'rrrrbggbbwbgorywrrwyooggwggbbbyogyoyyboryoyygrwowwwowb' 
        theCube = cube.Cube(cubeBackLeft)
        backLeftCorner(theCube)
        x = False
        if theCube.get()[DBL] == theCube.get()[DMM] and theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LMM]:
            x = True
        self.assertEqual(True, x) 
      
    def test340_frontLeftCorner(self):
        parms = {}
        parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
        cubeFrontLeft = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo' 
        theCube = cube.Cube(cubeFrontLeft)
        frontLeftCorner(theCube)
        x = False
        if theCube.get()[DTL] == theCube.get()[DMM] and theCube.get()[LBR] == theCube.get()[LMM] and \
         theCube.get()[FBL] == theCube.get()[FMM]:
            x = True
        self.assertEqual(True, x) 
            
       
    def test350_solve_returnEmptyForSolvedBottom(self):
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
    
    def test360_solve_bottomCornersIfValid(self):
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
        
    def test370_solve_bottomCornersIfValid(self):
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
    
    def test400_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'robybobbbrrbbrrrrryogbgygggoyyrogoooyyobygggywwwwwwwww'
        cubeMidLayer = 'robybobbbrrbbrrrrryogbgygggoyyrogoooyyobygggywwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('ULUlubuBUUFUfuluLUURUrufuFUUFUfuluLUURUrufuFUUBUburuRUUUURUrufuFUUUUuluLUFUfuUUULUlubuBUUUUuruRUBUbu', midLayer)
    
    def test410_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'bbygbybbbryobrrrrrbyybgrgggggygooooooryyyorogwwwwwwwww'
        cubeMidLayer = 'bbygbybbbryobrrrrrbyybgrgggggygooooooryyyorogwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('UBUburuRUUFUfuluLUULUlubuBUUuufuFURUruUUUFUfuluLUULUlubuBUUUBUburuRU', midLayer)
        
    def test420_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'byrybbbbbgborrgrrryyorgbgggbgyyogoooyogoyorrywwwwwwwww'
        cubeMidLayer = 'byrybbbbbgborrgrrryyorgbgggbgyyogoooyogoyorrywwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('URUrufuFUULUlubuBUUFUfuluLUURUrufuFUUBUburuRUUuufuFURUruUUUuluLUFUfuuruRUBUbuUuubuBULUlu', midLayer)
        
    def test430_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('UBUburuRUULUlubuBUUBUburuRUULUlubuBUUFUfuluLUURUrufuFUUUFUfuluLUUUURUrufuFUUuruRUBUbuuubuBULUlu', midLayer)
        
    def test440_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'yoyobrbbbbyryrbrrrgygrgogggorbgoboooygygyboyrwwwwwwwww'
        cubeMidLayer = 'yoyobrbbbbyryrbrrrgygrgogggorbgoboooygygyboyrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('URUrufuFUUBUburuRUUFUfuluLUULUlubuBUUUFUfuluLUUUURUrufuFUUuubuBULUluUuruRUBUbu', midLayer)
        
    def test450_solve_middleEdgesIfValid(self):
        parms = {}
        parms['cube'] = 'rrgybybbbyoogrbrrrbryygoggggbbgoooooogyrybyyrwwwwwwwww'
        cubeMidLayer = 'rrgybybbbyoogrbrrrbryygoggggbbgoooooogyrybyyrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        midLayer = solveMiddleLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('URUrufuFUUBUburuRUULUlubuBUUUUFUfuluLUUUuufuFURUruULUlubuBUuruRUBUbu', midLayer)
        
    def test450_frontRightEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        result = solve(parms)
        frontTop = theCube.get()[FTM]
        topBottom = theCube.get()[UBM]
        frontRightEdge(theCube)
        self.assertEqual('w' + topBottom, theCube.get()[FMR] + theCube.get()[RML])
        
    