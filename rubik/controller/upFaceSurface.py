import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube


def swapBackCorners(theCube: Cube) -> str:
    moves = ''
    for x in range(3):
        moves += 'BUbu'
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
    for x in range(3):
        moves += 'ruRU'
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateR()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateR()
        theCube._rotateU()
    moves += 'u'
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU() 
    return moves
    
def swapLeftCorners(theCube: Cube) -> str:
    moves = ''
    for x in range(3):
        moves += 'LUlu'
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateL()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
    for x in range(3):
        moves += 'buBU'
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateB()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateB()
        theCube._rotateU()
    moves += 'u'
    theCube._rotateU()
    theCube._rotateU()
    theCube._rotateU() 
    return moves


def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    
    moves = ''
    return 'x'
    #check if solved
    if theCube.get()[FMM] in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]] and \
        theCube.get()[RMM] in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]] and \
        theCube.get()[RMM] in [theCube.get()[RTR], theCube.get()[BTL], theCube.get()[UTR]] and \
        theCube.get()[BMM] in [theCube.get()[RTR], theCube.get()[BTL], theCube.get()[UTR]] and \
        theCube.get()[BMM] in [theCube.get()[BTR], theCube.get()[LTL], theCube.get()[UTL]] and \
        theCube.get()[LMM] in [theCube.get()[BTR], theCube.get()[LTL], theCube.get()[UTL]] and \
        theCube.get()[FMM] in [theCube.get()[LTR], theCube.get()[FTL], theCube.get()[UBL]] and \
        theCube.get()[LMM] in [theCube.get()[LTR], theCube.get()[FTL], theCube.get()[UBL]]:
        return moves
    
    while theCube.get()[FMM] not in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]] or \
        theCube.get()[RMM] not in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]] or \
        theCube.get()[RMM] not in [theCube.get()[RTR], theCube.get()[BTL], theCube.get()[UTR]] or \
        theCube.get()[BMM] not in [theCube.get()[RTR], theCube.get()[BTL], theCube.get()[UTR]] or \
        theCube.get()[BMM] not in [theCube.get()[BTR], theCube.get()[LTL], theCube.get()[UTL]] or \
        theCube.get()[LMM] not in [theCube.get()[BTR], theCube.get()[LTL], theCube.get()[UTL]] or \
        theCube.get()[FMM] not in [theCube.get()[LTR], theCube.get()[FTL], theCube.get()[UBL]] or \
        theCube.get()[LMM] not in [theCube.get()[LTR], theCube.get()[FTL], theCube.get()[UBL]]:
        
        #rotate top until blue red corner is correct
        while theCube.get()[FMM] not in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]] and \
            theCube.get()[RMM] not in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]]:
            moves += 'U'
            theCube._rotateU()
    
        if theCube.get()[RMM] not in [theCube.get()[RTR], theCube.get()[BTL], theCube.get()[UTR]]:
            if theCube.get()[RMM] in [theCube.get()[BTR], theCube.get()[LTL], theCube.get()[UTL]]:
                moves += swapBackCorners(theCube) 
            else: 
                moves += swapLeftCorners(theCube)
                moves += swapBackCorners(theCube)    
        
        if theCube.get()[FMM] not in [theCube.get()[FTL], theCube.get()[LTR], theCube.get()[UBL]]:
            moves += swapLeftCorners(theCube)
                    
    return moves      #TODO:  remove this stubbed value
