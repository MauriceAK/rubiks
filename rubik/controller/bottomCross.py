import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''  
    
    moves = []
    cubeList = list(theCube)
    botColor = cubeList[DMM]
    
    
    return theCube      #TODO:  remove this stubbed value
