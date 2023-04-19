import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''  
    
    moves = ''
    
    botColor = theCube.get()[DMM]
    cornerWRB = [botColor, theCube.get()[FMM], theCube.get()[RMM]]
    cornerWhites = [theCube.get()[DTR], theCube.get()[FBR], theCube.get()[RBL], theCube.get()[RBR], 
                    theCube.get()[BBL], theCube.get()[DBR], theCube.get()[DBL], theCube.get()[BBR], 
                    theCube.get()[LBL], theCube.get()[FBL], theCube.get()[LBR], theCube.get()[DTL]]

    
    if theCube.get()[DTL] == theCube.get()[DBL] == theCube.get()[DTR] == theCube.get()[DBR] == botColor and \
         theCube.get()[FBL] == theCube.get()[FBR] == theCube.get()[FMM] and \
         theCube.get()[RBL] == theCube.get()[RBR] == theCube.get()[RMM] and \
         theCube.get()[BBL] == theCube.get()[BBR] == theCube.get()[BMM] and \
         theCube.get()[LBL] == theCube.get()[LBR] == theCube.get()[LMM]:
        return moves
    
    
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
        #return moves + 'x'
    
    
    while theCube.get()[DTR] != botColor or theCube.get()[FBR] != theCube.get()[FMM] or \
     theCube.get()[RBL] != theCube.get()[RMM]:
           
        if theCube.get()[FTR] in ['w', 'r', 'b'] and \
                 theCube.get()[RTL] in ['w', 'r', 'b'] and \
                 theCube.get()[UBR] in ['w', 'r', 'b']:

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
    
    
    while theCube.get()[DBR] != botColor or theCube.get()[RBR] != theCube.get()[RMM] or \
     theCube.get()[BBL] != theCube.get()[BMM]:
        
        if theCube.get()[BTL] in ['w', 'r', 'g'] and \
                 theCube.get()[RTR] in ['w', 'r', 'g'] and \
                 theCube.get()[UTR] in ['w', 'r', 'g']:
                
               
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
                
            
    while theCube.get()[DBL] != botColor or theCube.get()[BBR] != theCube.get()[BMM] or \
     theCube.get()[LBL] != theCube.get()[LMM]:
        
        if theCube.get()[BTR] in ['w', 'o', 'g'] and \
                 theCube.get()[LTL] in ['w', 'o', 'g'] and \
                 theCube.get()[UTL] in ['w', 'o', 'g']:
                
               
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
        
    
    
    while theCube.get()[DTR] != botColor or theCube.get()[LBR] != theCube.get()[LMM] or \
     theCube.get()[FBL] != theCube.get()[FMM]:
        
        if theCube.get()[LTR] in ['w', 'o', 'b'] and \
                 theCube.get()[FTL] in ['w', 'o', 'b'] and \
                 theCube.get()[UTL] in ['w', 'o', 'b']:
                
               
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
        
    
            
    return moves      #TODO:  remove this stubbed value
