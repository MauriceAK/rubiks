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
    cubeList = theCube.get()
    
    moves = []
    
    
    botColor = cubeList[DMM]
    botEdges = [DTM, DML, DMR, DBM]
    f_edges = [FTM, FML, FMR, FBM]
    r_edges = [RTM, RML, RMR, RBM]
    b_edges = [BTM, BML, BMR, BBM]
    l_edges = [LTM, LML, LMR, LBM]
    d_edges = [DTM, DML, DMR, DBM]
    
    
    # checks completion
    if cubeList[DTM] == cubeList[DBM] == cubeList[DML] == cubeList[DMR] == botColor and \
         cubeList[FBM] == cubeList[FMM] and \
         cubeList[RBM] == cubeList[RMM] and \
         cubeList[BBM] == cubeList[BMM] and \
         cubeList[LBM] == cubeList[LMM]:
        return moves
    return cubeList
    botcolor_edges = [i for i in range(len(cubeList)) if cubeList[i] == botColor]
    
    #front top edge
    while cubeList[UBM] != botColor:
        if botColor in {cubeList[RML], cubeList[DTM], cubeList[LMR]}:
            moves.append('F')
            theCube._rotateF()
        elif botColor in {cubeList[FTM], cubeList[FMR], cubeList[FML], cubeList[FBM]}:
            while cubeList[FMR] != botColor:
                moves.append('F')
                theCube._rotateF()
            moves.append('uRU')
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateR()
            theCube._rotateU()
            
    #right top edge        
    while cubeList[UMR] != botColor:
        if botColor in {cubeList[BML], cubeList[DMR], cubeList[FMR]}:
            moves.append('R')
            theCube._rotateR()
        elif botColor in {cubeList[RTM], cubeList[RMR], cubeList[RML], cubeList[RBM]}:
            while cubeList[RMR] != botColor:
                moves.append('R')
                theCube._rotateR()
            moves.append('uBU')
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateB()
            theCube._rotateU()           
        
    #back top edge        
    while cubeList[UTM] != botColor:
        if botColor in {cubeList[RML], cubeList[DTM], cubeList[LMR]}:
            moves.append('B')
            theCube._rotateB()
        elif botColor in {cubeList[FTM], cubeList[FMR], cubeList[FML], cubeList[FBM]}:
            while cubeList[BMR] != botColor:
                moves.append('B')
                theCube._rotateB()
            moves.append('uLU')
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateL()
            theCube._rotateU()  
            
    #left top edge        
    while cubeList[UML] != botColor:
        if botColor in {cubeList[RML], cubeList[DTM], cubeList[LMR]}:
            moves.append('L')
            theCube._rotateL()
        elif botColor in {cubeList[FTM], cubeList[FMR], cubeList[FML], cubeList[FBM]}:
            while cubeList[LMR] != botColor:
                moves.append('L')
                theCube._rotateL()
            moves.append('uFU')
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateU()
            theCube._rotateF()
            theCube._rotateU()  
     
    
    if checkDaisy(cubeList) is True:
        while cubeList[FTM] != cubeList[FMM] or cubeList[UBM] != botColor:
            moves.append('U')
            theCube._rotateU()
        moves.append('FF')
        theCube._rotateF()
        theCube._rotateF()
        
        while cubeList[RTM] != cubeList[RMM] or cubeList[UMR] != botColor:
            moves.append('U')
            theCube._rotateU()
        moves.append('RR')
        theCube._rotateR()
        theCube._rotateR()
        
        while cubeList[BTM] != cubeList[BMM] or cubeList[UTM] != botColor:
            moves.append('U')
            theCube._rotateU()
        moves.append('BB')
        theCube._rotateB()
        theCube._rotateB()
        
        while cubeList[LTM] != cubeList[LMM] or cubeList[UML] != botColor:
            moves.append('U')
            theCube._rotateU()
        moves.append('LL')
        theCube._rotateL()
        theCube._rotateL()
    
    return moves    #TODO:  remove this stubbed value
