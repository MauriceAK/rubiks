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
    cornerWRB = [botColor, theCube.get()[FMM], theCube.get()[RMM]]
    print (*cornerWRB)
    
    if theCube.get()[DTL] == theCube.get()[DBL] == theCube.get()[DTR] == theCube.get()[DBR] == botColor and \
         theCube.get()[FBL] == theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[RBL] == theCube.get()[RBR] == theCube.get()[RMM] and \
         theCube.get()[BBL] == theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LBR] == theCube.get()[LMM]:
        return moves
    
    while theCube.get()[DTR] != botColor:
        #if white and green and blue in white blue green
        if theCube.get()[FTR] in botColor or theCube.get()[FTR] == theCube.get()[FMM] or theCube.get()[FTR] == theCube.get()[LMM] and \
         theCube.get()[RTL] == botColor or theCube.get()[RTL] == theCube.get()[FMM] or theCube.get()[RTL] == theCube.get()[RMM] and \
         theCube.get()[UBR] == botColor or theCube.get()[UBR] == theCube.get()[FMM] or theCube.get()[UBR] == theCube.get()[RMM]:
            return 'x'
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
