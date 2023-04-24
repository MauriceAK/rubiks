'''
    Created on 4/18/23
    
    @author: Maurice Kenon
'''


import rubik.model.constants
from rubik.model.cube import Cube
from rubik.model.constants import *


def switchCorners(theCube: Cube) -> str:
    moves = ''
    moves += 'lURuLUUrURUUr'
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateU()          
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateU()
    
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateR()
    
    return moves


def solveFinal(theCube: Cube) -> str:
    
    moves = ''
    moves += 'RUruluLU'
    theCube._rotateR()
    theCube._rotateU()
    theCube._rotateR()
    theCube._rotateR()
    theCube._rotateR()
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
    
    for x in range(5):
        moves += 'RUru'
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        
    for x in range(5):
        moves += 'luLU'
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateU()
        
    
    return moves
    
def solveFinalFromBack(theCube: Cube) -> str:
    
    moves = ''
    moves += 'LUluruRU'
    theCube._rotateL()
    theCube._rotateU()
    theCube._rotateL()
    theCube._rotateL()
    theCube._rotateL()
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
    
    for x in range(5):
        moves += 'LUlu'
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        
    for x in range(5):
        moves += 'ruRU'
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateU()
        
    
    return moves 
  
def solveFinalFromRight(theCube: Cube) -> str:
    
    moves = ''
    moves += 'BUbufuFU'
    theCube._rotateB()
    theCube._rotateU()
    theCube._rotateB()
    theCube._rotateB()
    theCube._rotateB()
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
    
    for x in range(5):
        moves += 'BUbu'
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        
    for x in range(5):
        moves += 'fuFU'
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateU()
        
    
    return moves 

def solveFinalFromLeft(theCube: Cube) -> str:
    
    moves = ''
    moves += 'FUfubuBU'
    theCube._rotateF()
    theCube._rotateU()
    theCube._rotateF()
    theCube._rotateF()
    theCube._rotateF()
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
    
    for x in range(5):
        moves += 'FUfu'
        theCube._rotateF()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateF()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        
    for x in range(5):
        moves += 'buBU'
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateU()        
    
    return moves 
    
def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    moves = ''
    while theCube.get()[FMM] != theCube.get()[FTR]:
        moves += 'U' 
        theCube._rotateU()
        
    if theCube.get()[FMM] != theCube.get()[FTL]:
         
        if theCube.get()[LMM] == theCube.get()[BTR]:
            moves += 'UU' 
            theCube._rotateU()
            theCube._rotateU()
            moves += switchCorners(theCube)
            moves += 'UU' 
            theCube._rotateU()
            theCube._rotateU()
        
        elif theCube.get()[LMM] == theCube.get()[RTR]:
            moves += 'U' 
            theCube._rotateU()
            moves += switchCorners(theCube)  
            moves += 'U' 
            theCube._rotateU()
            moves += switchCorners(theCube) 
            moves += 'UU' 
            theCube._rotateU()
            theCube._rotateU()
        
    if theCube.get()[RMM] != theCube.get()[RTR]:
        moves += 'U' 
        theCube._rotateU()    
        moves += switchCorners(theCube) 
        
    while theCube.get()[FMM] != theCube.get()[FTR]:
        moves += 'U' 
        theCube._rotateU()
        
    #CORNERS SHOULD BE ALIGNED NOW
    
    while theCube.get()[FMM] != theCube.get()[FTM] or \
     theCube.get()[RMM] != theCube.get()[RTM] or \
     theCube.get()[LMM] != theCube.get()[LTM] or \
     theCube.get()[BMM] != theCube.get()[BTM]:
        
        if theCube.get()[LMM] == theCube.get()[LTM]: 
            moves += solveFinalFromLeft(theCube)
        
        elif theCube.get()[BMM] == theCube.get()[BTM]: 
            moves += solveFinalFromBack(theCube)
            
        elif theCube.get()[RMM] == theCube.get()[RTM]: 
            moves += solveFinalFromRight(theCube)
            
        else:
           
            moves += solveFinal(theCube)
    
            
    return moves      #TODO:  remove this stubbed value
