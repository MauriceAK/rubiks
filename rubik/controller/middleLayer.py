'''
    Created on 4/21/23
    
    @author: Maurice Kenon
'''

import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

#front right edge piece
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

#right right edge piece
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

#back right edge piece
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

#back left edge piece
def backLeftEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'uruRUBUbu'
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
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()

    return moves

#left right edge piece
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

#left left edge piece
def leftLeftEdge(theCube: Cube) -> str:
    moves = ''
    moves += 'ubuBULUlu'
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
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU() 

    return moves

#front left edge piece
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

#right left edge
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
    
    #checks if solved
    if theCube.get()[FMM] == theCube.get()[FMR] == theCube.get()[FML] and \
        theCube.get()[RMM] == theCube.get()[RMR] == theCube.get()[RML] and \
        theCube.get()[LMM] == theCube.get()[LMR] == theCube.get()[LML] and \
        theCube.get()[BMM] == theCube.get()[BMR] == theCube.get()[BML]:
        return moves
    
    
    topColor = theCube.get()[UMM]
    middleEdges = [theCube.get()[FTM], theCube.get()[UBM], theCube.get()[RTM], theCube.get()[UMR],
                   theCube.get()[BTM], theCube.get()[UTM], theCube.get()[LTM], theCube.get()[UML]]
    
    #removes top color from middle layer edges
    while topColor in middleEdges:
        
        if topColor in [theCube.get()[FTM], theCube.get()[UBM]]:
            moves += frontRightEdge(theCube)
            
        if topColor in [theCube.get()[RTM], theCube.get()[UMR]]:
            moves +=rightRightEdge(theCube)
        
        if topColor in [theCube.get()[BTM], theCube.get()[UTM]]:
            moves += backRightEdge(theCube)
        
        if topColor in [theCube.get()[LTM], theCube.get()[UML]]:
            moves += leftRightEdge(theCube)
    
        middleEdges = [theCube.get()[FTM], theCube.get()[UBM], theCube.get()[RTM], theCube.get()[UMR],
                   theCube.get()[BTM], theCube.get()[UTM], theCube.get()[LTM], theCube.get()[UML]]
    
     
    #moves += 'x'   
    
    #solves for front left and right edge
    while theCube.get()[FMM] != theCube.get()[FML] or theCube.get()[FMM] != theCube.get()[FMR] or \
        theCube.get()[LMR] != theCube.get()[LMM] or \
        theCube.get()[RML] != theCube.get()[RMM]:
        
        while theCube.get()[FMM] not in [theCube.get()[FTM], theCube.get()[UBM]] or \
         (topColor == theCube.get()[FTM] and theCube.get()[FMM] == theCube.get()[UBM]) or \
         (topColor == theCube.get()[UBM] and theCube.get()[FMM] == theCube.get()[FTM]):
            moves += 'U'
            theCube._rotateU()
           
        if theCube.get()[FMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[RMM]:
            moves += frontRightEdge(theCube)
        elif theCube.get()[RMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[FMM]: 
            moves += 'u' 
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            moves += rightLeftEdge(theCube)
            
        elif theCube.get()[FMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[LMM]: 
            moves += frontLeftEdge(theCube)
            
        elif theCube.get()[LMM] == theCube.get()[FTM] and theCube.get()[UBM] == theCube.get()[FMM]: 
            moves += 'U' 
            theCube._rotateU()
            moves += leftRightEdge(theCube)
    

               
    #moves += 'x'
    
    #solves for back left and right edge 
    while theCube.get()[BMM] != theCube.get()[BML] or theCube.get()[BMM] != theCube.get()[BMR] or \
        theCube.get()[LML] != theCube.get()[LMM] or \
        theCube.get()[RMR] != theCube.get()[RMM]:
        
        while theCube.get()[BMM] not in [theCube.get()[BTM], theCube.get()[UTM]] or \
         (topColor == theCube.get()[BTM] and theCube.get()[BMM] == theCube.get()[UTM]) or \
         (topColor == theCube.get()[UTM] and theCube.get()[BMM] == theCube.get()[BTM]):
            moves += 'U'
            theCube._rotateU()
            
        if theCube.get()[BMM] == theCube.get()[BTM] and theCube.get()[UTM] == theCube.get()[LMM]:
            moves += backRightEdge(theCube)
            
        elif theCube.get()[LMM] == theCube.get()[BTM] and theCube.get()[UTM] == theCube.get()[BMM]: 
            moves += 'u' 
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            moves += leftLeftEdge(theCube)
            
        elif theCube.get()[BMM] == theCube.get()[BTM] and theCube.get()[UTM] == theCube.get()[RMM]: 
            moves += backLeftEdge(theCube)
            
        elif theCube.get()[RMM] == theCube.get()[BTM] and theCube.get()[UTM] == theCube.get()[BMM]: 
            moves += 'U' 
            theCube._rotateU()
            moves += rightRightEdge(theCube)
            
        #moves += 'x'
        #return moves + 'x' 
    return moves      
