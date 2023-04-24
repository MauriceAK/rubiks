'''
    Created on 4/18/23
    
    @author: Maurice Kenon
'''

from unittest import TestCase
from rubik.view.solve import solve
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *
from rubik.controller.upFaceCross import *
from rubik.controller.upFaceSurface import *
from rubik.controller.upperLayer import *

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
        
    def test460_frontRightEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        frontTop = theCube.get()[FTM]
        topBottom = theCube.get()[UBM]
        frontRightEdge(theCube)
        self.assertEqual(frontTop + topBottom, theCube.get()[FMR] + theCube.get()[RML])
    
    def test470_rightRightEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        rightTop = theCube.get()[RTM]
        topRight = theCube.get()[UMR]
        rightRightEdge(theCube)
        self.assertEqual(rightTop + topRight, theCube.get()[RMR] + theCube.get()[BML])
        
    def test480_backRightEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        backTop = theCube.get()[BTM]
        topTop = theCube.get()[UTM]
        backRightEdge(theCube)
        self.assertEqual(backTop + topTop, theCube.get()[BMR] + theCube.get()[LML])
        
    def test490_backLeftEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        backTop = theCube.get()[BTM]
        topTop = theCube.get()[UTM]
        backLeftEdge(theCube)
        self.assertEqual(backTop + topTop, theCube.get()[BML] + theCube.get()[RMR])
        
    def test411_leftRightEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        leftTop = theCube.get()[LTM]
        topLeft = theCube.get()[UML]
        leftRightEdge(theCube)
        self.assertEqual(leftTop + topLeft, theCube.get()[LMR] + theCube.get()[FML])
        
    def test411_leftLeftEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        leftTop = theCube.get()[LTM]
        topLeft = theCube.get()[UML]
        leftLeftEdge(theCube)
        self.assertEqual(leftTop + topLeft, theCube.get()[LML] + theCube.get()[BMR])
        
    def test413_frontLeftEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        frontTop = theCube.get()[FTM]
        topBottom = theCube.get()[UBM]
        frontLeftEdge(theCube)
        self.assertEqual(frontTop + topBottom, theCube.get()[FML] + theCube.get()[LMR])
        
    def test470_rightLeftEdge(self):
        parms = {}
        parms['cube'] = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        cubeMidLayer = 'ooyobrbbbbbobryrrrbogggggggyygroyooorbyryyygrwwwwwwwww'
        theCube = cube.Cube(cubeMidLayer)
        rightTop = theCube.get()[RTM]
        topRight = theCube.get()[UMR]
        rightLeftEdge(theCube)
        self.assertEqual(rightTop + topRight, theCube.get()[RML] + theCube.get()[FMR])
    '''
    def test500_checkIntegrity(self):
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
        self.assertIn(result['integrity'],'d1fb44852b3724cb340f1d228a17b3b74473f7270bc914dd01582d582900078b')
    '''   
    def test510_solve_topCross(self):
        parms = {}
        parms['cube'] = 'oyobbbbbbyyrrrrrrrgobggggggrryooooooyyyyybbggwwwwwwwww'
        cubeTopCross = 'oyobbbbbbyyrrrrrrrgobggggggrryooooooyyyyybbggwwwwwwwww'
        theCube = cube.Cube(cubeTopCross)
        result = solve(parms)
        topCross = solveUpCross(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('FURurf', topCross)
        
    def test520_solve_topCross(self):
        parms = {}
        parms['cube'] = 'orgbbbbbbyyrrrrrrryobggggggyygoooooooybgybyyrwwwwwwwww'
        cubeTopCross = 'orgbbbbbbyyrrrrrrryobggggggyygoooooooybgybyyrwwwwwwwww'
        theCube = cube.Cube(cubeTopCross)
        result = solve(parms)
        topCross = solveUpCross(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('LFUful', topCross)
        
     
    def test530_solve_upSurfaceSolved(self):
        parms = {}
        parms['cube'] = 'yoybbbbbbbbrrrrrrrgggggggggorbooooooyyyyyyoyrwwwwwwwww'
        cubeTopFace = 'yoybbbbbbbbrrrrrrrgggggggggorbooooooyyyyyyoyrwwwwwwwww'
        theCube = cube.Cube(cubeTopFace)
        result = solve(parms)
        topFace = solveUpSurface(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('URUrURUUrURUrURUUrUUURUrURUUr', topFace)
    '''  
    def test540_solve_upSurface(self):
        parms = {}
        parms['cube'] = 'gbybbbbbbbrorrrrrrbyyggggggryyooooooggyoyyoyrwwwwwwwww'
        cubeTopFace = 'gbybbbbbbbrorrrrrrbyyggggggryyooooooggyoyyoyrwwwwwwwww'
        theCube = cube.Cube(cubeTopFace)
        result = solve(parms)
        topFace = solveUpSurface(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('BUbuBUbuBUburuRUruRUruRUuLUluLUluLUlubuBUbuBUbuBUu', topFace)
    '''
    def test550_fishAlg(self):
        parms = {}
        parms['cube'] = 'ogbbbbbbbrrgrrrrrryogggggggobyooooooyyryyybyywwwwwwwww'
        cubeTopCross = 'ogbbbbbbbrrgrrrrrryogggggggobyooooooyyryyybyywwwwwwwww'
        theCube = cube.Cube(cubeTopCross)
        result = solve(parms)
        topCross = fishAlg(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(theCube.get()[UBL], 'g')   
        
    def test560_makeFish(self):
        parms = {}
        parms['cube'] = 'rgobbbbbbybyrrrrrrorrggggggyoyoooooobybyyygygwwwwwwwww'
        cubeTopCross = 'rgobbbbbbybyrrrrrrorrggggggyoyoooooobybyyygygwwwwwwwww'
        theCube = cube.Cube(cubeTopCross)
        result = solve(parms)
        topCross = makeFish(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual(theCube.get()[UBL], theCube.get()[UMM])   
        
    def test610_solveUpperLayer(self):
        parms = {}
        parms['cube'] = 'orobbbbbbbgbrrrrrrrorgggggggbgooooooyyyyyyyyywwwwwwwww'
        cubeTopLayer = 'orobbbbbbbgbrrrrrrrorgggggggbgooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeTopLayer)
        result = solve(parms)
        topLayer = solveUpperLayer(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('URUruluLURUruRUruRUruRUruRUruluLUluLUluLUluLUluLUBUbufuFUBUbuBUbuBUbuBUbuBUbufuFUfuFUfuFUfuFUfuFU', topLayer)

def test610_solveUpperLayer(self):
        parms = {}
        parms['cube'] = 'orobbbbbbbgbrrrrrrrorgggggggbgooooooyyyyyyyyywwwwwwwww'
        cubeTopLayer = 'orobbbbbbbgbrrrrrrrorgggggggbgooooooyyyyyyyyywwwwwwwww'
        theCube = cube.Cube(cubeTopLayer)
        result = solve(parms)
        topLayer = switchCorners(theCube)
        print(topLayer)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('', topLayer)  
    
    
        