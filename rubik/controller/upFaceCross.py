import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube


def makeTopCross(theCube: Cube) -> str:
    moves = ''
    while theCube.get()[UMM] != theCube.get()[UTM] or \
     theCube.get()[UMM] != theCube.get()[UBM] or \
     theCube.get()[UMM] != theCube.get()[UML] or \
     theCube.get()[UMM] != theCube.get()[UMR]:
        moves += 'FRUruf'
        theCube._rotateF()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateF()
        return 'x'
    return moves
def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    
    moves = ''
    
    #check if top cross is present
    if theCube.get()[UMM] == theCube.get()[UTM] == theCube.get()[UBM] == \
    theCube.get()[UMR] == theCube.get()[UML]:
        return moves
    
    makeTopCross(theCube)
    
    
    
    
    return moves      #TODO:  remove this stubbed value
