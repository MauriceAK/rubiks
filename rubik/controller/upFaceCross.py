import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def horizLineCross(theCube: Cube) -> str:
    moves = ''
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
    return moves
    

def vertLineCross(theCube: Cube) -> str:
    moves = ''
    moves += 'LFUful'
    theCube._rotateL()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL() 
    return moves
    

def angleCross(theCube: Cube) -> str:
    moves = ''
    
    #front
    if theCube.get()[UMM] == theCube.get()[UBM] == theCube.get()[UMR]:
        moves += 'BULulb'
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB() 
        return moves
    #left
    elif theCube.get()[UMM] == theCube.get()[UML] == theCube.get()[UBM]:
        moves += 'RUBubr'
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR() 
        return moves
    #back
    elif theCube.get()[UMM] == theCube.get()[UML] == theCube.get()[UTM]:
        moves += 'FURurf'
        theCube._rotateF()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateF() 
        return moves
    #right  
    elif theCube.get()[UMM] == theCube.get()[UTM] == theCube.get()[UMR]:
        moves += 'LUFufl'
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateL() 
        return moves
    return moves 

def middleOnlyCross(theCube: Cube) -> str:
    moves = ''
    horizLineCross(theCube)
    angleCross(theCube)
    return moves
    
    
    
def makeTopCross(theCube: Cube) -> str:
    moves = ''
    while theCube.get()[UMM] != theCube.get()[UTM] or \
     theCube.get()[UMM] != theCube.get()[UBM] or \
     theCube.get()[UMM] != theCube.get()[UML] or \
     theCube.get()[UMM] != theCube.get()[UMR]:
        #horizontal
        if theCube.get()[UMM] == theCube.get()[UMR] == theCube.get()[UML]:
            moves += horizLineCross(theCube) 
            return moves
        #vertical
        elif theCube.get()[UMM] == theCube.get()[UTM] == theCube.get()[UBM]:
            moves += vertLineCross(theCube)
            return moves
        #front
        elif theCube.get()[UMM] == theCube.get()[UMR] == theCube.get()[UBM]:
            moves += angleCross(theCube)
            return moves
        #left
        elif theCube.get()[UMM] == theCube.get()[UBM] == theCube.get()[UML]:
            moves += angleCross(theCube)
            return moves
        #back
        elif theCube.get()[UMM] == theCube.get()[UML] == theCube.get()[UTM]:
            moves += angleCross(theCube)
            return moves
        #right
        elif theCube.get()[UMM] == theCube.get()[UTM] == theCube.get()[UMR]:
            moves += angleCross(theCube)
            return moves
        #middle
        else: 
            moves += middleOnlyCross(theCube)
            return moves
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
    
    
    moves += makeTopCross(theCube)
    
    
    
    
    return moves      #TODO:  remove this stubbed value
