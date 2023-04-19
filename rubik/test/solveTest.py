from unittest import TestCase
from rubik.view.solve import solve
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross


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
        result = solveBottomCross(theCube)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('uRUuBUBBuLUUFFRRUBBUULL', result.get('solution'))
        
    #def test120_solve_bottomCornersIfValid(self):
    #    parms = {}
    #    parms['cube'] = 'wyrbbybbgbooorrrrwwrgygyggbogrgoryoyygboybgbwowywwwrwo'
    #    result = solve(parms)
    #    self.assertIn('status', result)
    #    self.assertEqual('ok', result['status'])
    #    self.assertIn('integrity', result)
    #    self.assertEqual('uRUuBUBBuLUUFFRRUBBUULL', result.get('solution'))