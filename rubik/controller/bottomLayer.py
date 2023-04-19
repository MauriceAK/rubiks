import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    
    moves = ''
    
    botColor = theCube.get()[DMM]
    
    if theCube.get()[DTL] == theCube.get()[DBL] == theCube.get()[DTR] == theCube.get()[DBR] == botColor and \
         theCube.get()[FBL] == theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[RBL] == theCube.get()[RBR] == theCube.get()[RMM] and \
         theCube.get()[BBL] == theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LBR] == theCube.get()[LMM]:
        return moves
    
    while theCube.get()[DTR] != botColor:
        #if white and green and blue in white blue green
        if theCube.get()[FTR] and theCube.get()[LTL] and theCube.get()[UBR] in {botColor, theCube.get()[FMM], theCube.get()[RMM]}:
            moves += 'RUru'
            theCube._rotateR()
            theCube._rotateU()
            theCube._rotateR()
            theCube._rotateR()
            theCube._rotateR()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
        else:
            moves += 'U'
            theCube._rotateU()
        
    
    
    
    return moves      #TODO:  remove this stubbed value
