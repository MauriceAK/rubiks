'''
    Created on 4/18/23
    
    @author: Maurice Kenon
'''

import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def makeDaisy(theCube: Cube) -> str:
    moves = ''
    cubeList = theCube.get()
    botColor = cubeList[DMM]
    #loop for making daisy on top 
    while botColor != theCube.get()[UTM] or botColor != theCube.get()[UML] or botColor != theCube.get()[UMR] or botColor != theCube.get()[UBM]:
        
        #front top edge
        if botColor == theCube.get()[RML] or botColor == theCube.get()[DTM] or botColor == theCube.get()[LMR] or botColor == theCube.get()[UBM]:
            while theCube.get()[UBM] != botColor:
                moves += 'F'
                theCube._rotateF()
        elif botColor == theCube.get()[FTM] or botColor == theCube.get()[FMR] or botColor == theCube.get()[FML] or botColor == theCube.get()[FBM]:
            while theCube.get()[FMR] != botColor:
                moves += 'F'
                theCube._rotateF()
            moves += 'uRU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateR()
            theCube._rotateU()
        else:
            moves += 'U'
            theCube._rotateU()   
           
        #right top edge      
        if botColor in {theCube.get()[BML], theCube.get()[DMR], theCube.get()[FMR], theCube.get()[UMR]}:
            while theCube.get()[UMR] != botColor:       
                moves +='R'
                theCube._rotateR()
        elif botColor in {theCube.get()[RTM], theCube.get()[RMR], theCube.get()[RML], theCube.get()[RBM]}:
            while theCube.get()[RMR] != botColor:
                moves +='R'
                theCube._rotateR()
            moves += 'uBU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateB()
            theCube._rotateU()           
        else:
            moves += 'U'
            theCube._rotateU()   
           
        #back top edge     
        if botColor in {theCube.get()[RMR], theCube.get()[DBM], theCube.get()[LML], theCube.get()[UTM]}:   
            while theCube.get()[UTM] != botColor:
                moves += 'B'
                theCube._rotateB()
        elif botColor in {theCube.get()[BTM], theCube.get()[BMR], theCube.get()[BML], theCube.get()[BBM]}:
            while theCube.get()[BMR] != botColor:
                moves += 'B'
                theCube._rotateB()
            moves += 'uLU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateL()
            theCube._rotateU()  
        else:
            moves += 'U'
            theCube._rotateU()   
               
        #left top edge  
        if botColor in {theCube.get()[FML], theCube.get()[DML], theCube.get()[BMR], theCube.get()[UML]}:      
            while theCube.get()[UML] != botColor:
                moves += 'L'
                theCube._rotateL()
        elif botColor in {theCube.get()[LTM], theCube.get()[LMR], theCube.get()[LML], theCube.get()[LBM]}:
            while theCube.get()[LMR] != botColor:
                moves += 'L' 
                theCube._rotateL()
            moves += 'uFU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateF()
            theCube._rotateU()  
        else:
            moves += 'U'
            theCube._rotateU() 
            
    return moves        
def     solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    moves = ''
    cubeList = theCube.get()
    botColor = cubeList[DMM]
    
    #return cubeList
    # checks completion
    if cubeList[DTM] == cubeList[DBM] == cubeList[DML] == cubeList[DMR] == botColor and \
         cubeList[FBM] == cubeList[FMM] and \
         cubeList[RBM] == cubeList[RMM] and \
         cubeList[BBM] == cubeList[BMM] and \
         cubeList[LBM] == cubeList[LMM]:
        return moves
    moves += makeDaisy(theCube)
    '''
    #loop for making daisy on top 
    while botColor != theCube.get()[UTM] or botColor != theCube.get()[UML] or botColor != theCube.get()[UMR] or botColor != theCube.get()[UBM]:
        
        #front top edge
        if botColor == theCube.get()[RML] or botColor == theCube.get()[DTM] or botColor == theCube.get()[LMR] or botColor == theCube.get()[UBM]:
            while theCube.get()[UBM] != botColor:
                moves += 'F'
                theCube._rotateF()
        elif botColor == theCube.get()[FTM] or botColor == theCube.get()[FMR] or botColor == theCube.get()[FML] or botColor == theCube.get()[FBM]:
            while theCube.get()[FMR] != botColor:
                moves += 'F'
                theCube._rotateF()
            moves += 'uRU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateR()
            theCube._rotateU()
        else:
            moves += 'U'
            theCube._rotateU()   
           
        #right top edge      
        if botColor in {theCube.get()[BML], theCube.get()[DMR], theCube.get()[FMR], theCube.get()[UMR]}:
            while theCube.get()[UMR] != botColor:       
                moves +='R'
                theCube._rotateR()
        elif botColor in {theCube.get()[RTM], theCube.get()[RMR], theCube.get()[RML], theCube.get()[RBM]}:
            while theCube.get()[RMR] != botColor:
                moves +='R'
                theCube._rotateR()
            moves += 'uBU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateB()
            theCube._rotateU()           
        else:
            moves += 'U'
            theCube._rotateU()   
           
        #back top edge     
        if botColor in {theCube.get()[RMR], theCube.get()[DBM], theCube.get()[LML], theCube.get()[UTM]}:   
            while theCube.get()[UTM] != botColor:
                moves += 'B'
                theCube._rotateB()
        elif botColor in {theCube.get()[BTM], theCube.get()[BMR], theCube.get()[BML], theCube.get()[BBM]}:
            while theCube.get()[BMR] != botColor:
                moves += 'B'
                theCube._rotateB()
            moves += 'uLU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateL()
            theCube._rotateU()  
        else:
            moves += 'U'
            theCube._rotateU()   
               
        #left top edge  
        if botColor in {theCube.get()[FML], theCube.get()[DML], theCube.get()[BMR], theCube.get()[UML]}:      
            while theCube.get()[UML] != botColor:
                moves += 'L'
                theCube._rotateL()
        elif botColor in {theCube.get()[LTM], theCube.get()[LMR], theCube.get()[LML], theCube.get()[LBM]}:
            while theCube.get()[LMR] != botColor:
                moves += 'L' 
                theCube._rotateL()
            moves += 'uFU'
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateF()
            theCube._rotateU()  
        else:
            moves += 'U'
            theCube._rotateU()    
    '''
    #flips top edges to bottom after aligning center squares with edge to make proper white cross
    if theCube.get()[UTM] == theCube.get()[UML] == theCube.get()[UMR] == theCube.get()[UBM] == botColor:
        
        while theCube.get()[FTM] != theCube.get()[FMM] or theCube.get()[UBM] != botColor:
            moves += 'U'
            theCube._rotateU()
        moves += 'FF'
        theCube._rotateF()
        theCube._rotateF()
         
        while theCube.get()[RTM] != theCube.get()[RMM] or theCube.get()[UMR] != botColor:
            moves += 'U'
            theCube._rotateU()
        moves +='RR'
        theCube._rotateR()
        theCube._rotateR()
         
        while theCube.get()[BTM] != theCube.get()[BMM] or theCube.get()[UTM] != botColor:
            moves += 'U'
            theCube._rotateU()
        moves += 'BB'
        theCube._rotateB()
        theCube._rotateB()
        
        while theCube.get()[LTM] != theCube.get()[LMM] or theCube.get()[UML] != botColor:
            moves += 'U'
            theCube._rotateU()
        moves += 'LL'
        theCube._rotateL()
        theCube._rotateL()
        
    return moves