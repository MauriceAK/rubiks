import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def checkDaisy(cubeList):
    botColor = cubeList[DMM]
    if cubeList[UTM] == cubeList[UML] == cubeList[UMR] == cubeList[UBM] == botColor:
        return True

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
    botEdges = [DTM, DML, DMR, DBM]
    f_edges = [FTM, FML, FMR, FBM]
    r_edges = [RTM, RML, RMR, RBM]
    b_edges = [BTM, BML, BMR, BBM]
    l_edges = [LTM, LML, LMR, LBM]
    d_edges = [DTM, DML, DMR, DBM]
    
    #return cubeList
    # checks completion
    if cubeList[DTM] == cubeList[DBM] == cubeList[DML] == cubeList[DMR] == botColor and \
         cubeList[FBM] == cubeList[FMM] and \
         cubeList[RBM] == cubeList[RMM] and \
         cubeList[BBM] == cubeList[BMM] and \
         cubeList[LBM] == cubeList[LMM]:
        return moves
   
    #botcolor_edges = [i for i in range(len(cubeList)) if cubeList[i] == botColor]
    return 'X'
    #if botColor == (cubeList[RML] or cubeList[DTM] or cubeList[LMR]):
        