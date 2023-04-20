import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def frontRightEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'URUrufuFU'
    theCube._rotateU()
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
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateU()

    return moves

def rightRightEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'UBUburuRU'
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateU()

    return moves

def backRightEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'ULUlubuBU'
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateU()

    return moves

def leftRightEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'UFUfuluLU'
    theCube._rotateU()
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
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateU()

    return moves

def frontLeftEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'uluLUFUfu'
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()

    return moves

def rightLeftEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'ufuFURUru'
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()

    return moves

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    
    moves = ''
    topColor = theCube.get()[UMM]
    middleEdges = [theCube.get()[FTM], theCube.get()[UBM], theCube.get()[RTM], theCube.get()[UMR],
                   theCube.get()[BTM], theCube.get()[UTM], theCube.get()[LTM], theCube.get()[UML]]
    #return moves + 'x'
    while topColor in middleEdges:
        if topColor in [theCube.get()[FTM], theCube.get()[UBM]]:
            frontRightEdge(theCube)
            
        if topColor in [theCube.get()[RTM], theCube.get()[UMR]]:
            rightRightEdge(theCube)
        
        if topColor in [theCube.get()[BTM], theCube.get()[UTM]]:
            backRightEdge(theCube)
        
        if topColor in [theCube.get()[LTM], theCube.get()[UML]]:
            leftRightEdge(theCube)
    
        middleEdges = [theCube.get()[FTM], theCube.get()[UBM], theCube.get()[RTM], theCube.get()[UMR],
                   theCube.get()[BTM], theCube.get()[UTM], theCube.get()[LTM], theCube.get()[UML]]
    
    
    
    while theCube.get()[FMM] != theCube.get()[FML] or theCube.get()[FMM] != theCube.get()[FMR] or \
        theCube.get()[LMR] != theCube.get()[LMM] or \
        theCube.get()[RMR] != theCube.get()[RMM]:
        
        while theCube.get()[FMM] not in [theCube.get()[FTM], theCube.get()[UBM]]:
            moves += 'U'
            theCube._rotateU()
        
        if theCube.get()[FMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[RMM]:
            frontRightEdge(theCube)
        elif theCube.get()[RMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[FMM]: 
            moves += 'u' 
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            rightLeftEdge(theCube)
            
        elif theCube.get()[FMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[LMM]: 
            frontLeftEdge(theCube)
        elif theCube.get()[LMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[FMM]: 
            moves += 'U' 
            theCube._rotateU()
            leftRightEdge(theCube)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return moves      #TODO:  remove this stubbed value
