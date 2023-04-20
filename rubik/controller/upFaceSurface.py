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
    
    if ['b','r'] in [theCube.get()[FTR], theCube.get()[RTL], theCube.get()[UBR]]:
        return 'x'
    
    
    
    
    
    return moves      #TODO:  remove this stubbed value
