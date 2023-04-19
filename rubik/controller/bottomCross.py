import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def checkDaisy(theCube):
    botColor = theCube.get()[DMM]
    if theCube.get()[UTM] == theCube.get()[UML] == theCube.get()[UMR] == theCube.get()[UBM] == botColor:
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
    #return 'X' 
    
    if botColor == theCube.get()[RML] or botColor == theCube.get()[DTM] or botColor == theCube.get()[LMR]:
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
        
    #right top edge      
    if botColor in {theCube.get()[BML], theCube.get()[DMR], theCube.get()[FMR]}:
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
        
    #back top edge     
    if botColor in {theCube.get()[RMR], theCube.get()[DBM], theCube.get()[LML]}:   
        while theCube.get()[UTM] != botColor:
            moves += 'B'
            theCube._rotateB()
    elif botColor in {theCube.get()[FTM], theCube.get()[FMR], theCube.get()[FML], theCube.get()[FBM]}:
        while theCube.get()[BMR] != botColor:
            moves += 'B'
            theCube._rotateB()
        moves += 'uLU'
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateL()
        theCube._rotateU()  
            
    #left top edge  
    if botColor in {theCube.get()[FML], theCube.get()[DML], theCube.get()[BMR]}:      
        while theCube.get()[UML] != botColor:
            moves += 'L'
            theCube._rotateL()
    elif botColor in {theCube.get()[FTM], theCube.get()[FMR], theCube.get()[FML], theCube.get()[FBM]}:
        while theCube.get()[LMR] != botColor:
            moves += 'L' 
            theCube._rotateL()
        moves += 'uFU'
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateU()
        theCube._rotateF()
        theCube._rotateU()  
     
    
    if checkDaisy(theCube) is True:
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