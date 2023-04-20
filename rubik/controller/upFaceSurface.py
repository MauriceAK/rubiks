import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    
    moves = ''
    
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
    
    
    
    
    
    return moves      #TODO:  remove this stubbed value
