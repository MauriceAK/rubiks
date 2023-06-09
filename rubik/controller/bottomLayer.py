'''
    Created on 4/19/23
    
    @author: Maurice Kenon
'''

import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

#removes whites from any side of bottom corner piece
def removeWhiteCorners(theCube: Cube) -> str:
    moves = ''
    botColor = theCube.get()[DMM]
    cornerWhites = [theCube.get()[DTR], theCube.get()[FBR], theCube.get()[RBL], theCube.get()[RBR], 
                    theCube.get()[BBL], theCube.get()[DBR], theCube.get()[DBL], theCube.get()[BBR], 
                    theCube.get()[LBL], theCube.get()[FBL], theCube.get()[LBR], theCube.get()[DTL]]
    
    while botColor in cornerWhites:
        if botColor in [theCube.get()[DTL], theCube.get()[FBL], theCube.get()[LBR]]:
            moves += 'FUf'
            theCube._rotateF()
            theCube._rotateU()
            theCube._rotateF()
            theCube._rotateF()
            theCube._rotateF()
            
        if botColor in [theCube.get()[DTR], theCube.get()[FBR], theCube.get()[RBL]]:
            moves += 'RUr'
            theCube._rotateR()
            theCube._rotateU()
            theCube._rotateR()
            theCube._rotateR()
            theCube._rotateR()
             
        if botColor in [theCube.get()[DBR], theCube.get()[RBR], theCube.get()[BBL]]:
            moves += 'BUb'
            theCube._rotateB()
            theCube._rotateU()
            theCube._rotateB()
            theCube._rotateB()
            theCube._rotateB()
            
        if botColor in [theCube.get()[DBL], theCube.get()[LBL], theCube.get()[BBR]]:
            moves += 'LUl'
            theCube._rotateL()
            theCube._rotateU()
            theCube._rotateL()
            theCube._rotateL()
            theCube._rotateL()
        
        moves += 'U'   
        theCube._rotateU()
        cornerWhites = [theCube.get()[DTR], theCube.get()[FBR], theCube.get()[RBL], theCube.get()[RBR], 
                    theCube.get()[BBL], theCube.get()[DBR], theCube.get()[DBL], theCube.get()[BBR], 
                    theCube.get()[LBL], theCube.get()[FBL], theCube.get()[LBR], theCube.get()[DTL]]
        
    return moves

#orients front right bottom corner piece properly
def frontRightCorner(theCube:Cube) -> str:
    moves = ''
    botColor = theCube.get()[DMM]
    while theCube.get()[DTR] != botColor or theCube.get()[FBR] != theCube.get()[FMM] or \
     theCube.get()[RBL] != theCube.get()[RMM]:
           
        if theCube.get()[FTR] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[FMM]] and \
                 theCube.get()[RTL] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[FMM]] and \
                 theCube.get()[UBR] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[FMM]]:
                if theCube.get()[FTR] == theCube.get()[FMM]:
                    while theCube.get()[DTR] != botColor:
                        moves += 'URur'
                        theCube._rotateU()
                        theCube._rotateR()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateR()
                        theCube._rotateR()
                        theCube._rotateR()
                else:
                    while theCube.get()[DTR] != botColor:
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
    return moves

#orients back right bottom corner piece properly
def backRightCorner(theCube:Cube) -> str:
    moves = ''
    botColor = theCube.get()[DMM]
    
    while theCube.get()[DBR] != botColor or theCube.get()[RBR] != theCube.get()[RMM] or \
     theCube.get()[BBL] != theCube.get()[BMM]:
        
        if theCube.get()[BTL] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[BMM]] and \
                 theCube.get()[RTR] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[BMM]] and \
                 theCube.get()[UTR] in [theCube.get()[DMM], theCube.get()[RMM], theCube.get()[BMM]]:
                if theCube.get()[RTR] == theCube.get()[DMM]:
                    while theCube.get()[DBR] != botColor:
                        moves += 'UBub'
                        theCube._rotateU()
                        theCube._rotateB()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateB()
                        theCube._rotateB()
                        theCube._rotateB()
                else:
                    while theCube.get()[DBR] != botColor:
                        moves += 'BUbu'
                        theCube._rotateB()
                        theCube._rotateU()
                        theCube._rotateB()
                        theCube._rotateB()
                        theCube._rotateB()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()         
        else:
                moves += 'U'
                theCube._rotateU()
                
    return moves

#orients back left bottom corner piece properly
def backLeftCorner(theCube:Cube) -> str:
    moves = ''
    botColor = theCube.get()[DMM]
    while theCube.get()[DBL] != botColor or theCube.get()[BBR] != theCube.get()[BMM] or \
     theCube.get()[LBL] != theCube.get()[LMM]:
        
        if theCube.get()[BTR] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[BMM]] and \
                 theCube.get()[LTL] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[BMM]] and \
                 theCube.get()[UTL] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[BMM]]:
                
                if theCube.get()[BTR] == theCube.get()[DMM]:
                    while theCube.get()[DBL] != botColor:
                        moves += 'ULul'
                        theCube._rotateU()
                        theCube._rotateL()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateL()
                        theCube._rotateL()
                        theCube._rotateL()
                else:        
                    while theCube.get()[DBL] != botColor:
                        moves += 'LUlu'
                        theCube._rotateL()
                        theCube._rotateU()
                        theCube._rotateL()
                        theCube._rotateL()
                        theCube._rotateL()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()        
        else:
                moves += 'U'
                theCube._rotateU()
    return moves

#orients front left bottom corner piece properly
def frontLeftCorner(theCube:Cube) -> str:
    moves = ''
    botColor = theCube.get()[DMM]
    while theCube.get()[DTL] != botColor or theCube.get()[LBR] != theCube.get()[LMM] or \
     theCube.get()[FBL] != theCube.get()[FMM]:
        
        if theCube.get()[LTR] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[FMM]] and \
                 theCube.get()[FTL] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[FMM]] and \
                 theCube.get()[UBL] in [theCube.get()[DMM], theCube.get()[LMM], theCube.get()[FMM]]:
                
                if theCube.get()[LTR] == theCube.get()[DMM]:
                    while theCube.get()[DTL] != botColor:
                        moves += 'UFuf'
                        theCube._rotateU()
                        theCube._rotateF()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateF()
                        theCube._rotateF()
                        theCube._rotateF()
                else:  
                    while theCube.get()[DTL] != botColor:
                        moves += 'FUfu'
                        theCube._rotateF()
                        theCube._rotateU()
                        theCube._rotateF()
                        theCube._rotateF()
                        theCube._rotateF()
                        theCube._rotateU()
                        theCube._rotateU()
                        theCube._rotateU()
        else:
                moves += 'U'
                theCube._rotateU()     
                
    return moves



def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    
    moves = ''
    botColor = theCube.get()[DMM]
    
    #checks if already solved
    if theCube.get()[DTL] == theCube.get()[DBL] == theCube.get()[DTR] == theCube.get()[DBR] == botColor and \
         theCube.get()[FBL] == theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[RBL] == theCube.get()[RBR] == theCube.get()[RMM] and \
         theCube.get()[BBL] == theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LBR] == theCube.get()[LMM]:
        return moves
    
    #aligns all corners
    moves += removeWhiteCorners(theCube)
    moves += frontRightCorner(theCube)
    moves += backRightCorner(theCube)     
    moves += backLeftCorner(theCube) 
    moves += frontLeftCorner(theCube)   
    
    
    return moves      #TODO:  remove this stubbed value
