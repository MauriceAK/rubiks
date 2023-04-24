import rubik.model.constants
from rubik.model.constants import *
from rubik.model.cube import Cube


def fishAlg(theCube: Cube) -> str:
    moves = ''
    moves += 'RUrURUUr'
    theCube._rotateR()
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

def makeFish(theCube: Cube) -> str:
    moves = ''
    
    if theCube.get()[UMM] != theCube.get()[UTR] and \
     theCube.get()[UMM] != theCube.get()[UTL] and \
     theCube.get()[UMM] != theCube.get()[UBR] and \
     theCube.get()[UMM] != theCube.get()[UBL]:
        while theCube.get()[UMM] != theCube.get()[LTR]:
            moves += 'U'
            theCube._rotateU()
        
        moves += fishAlg(theCube)
        while theCube.get()[UMM] != theCube.get()[UBL]:
            moves += 'U'
            theCube._rotateU()    
    
    else: 
        
        while theCube.get()[UMM] == theCube.get()[UTR] or \
         theCube.get()[UMM] == theCube.get()[UTL] or \
         theCube.get()[UMM] == theCube.get()[UBR] or \
         theCube.get()[UMM] == theCube.get()[UBL]:
            
            
            while theCube.get()[UMM] != theCube.get()[FTR] and \
             theCube.get()[UMM] != theCube.get()[RTR] and \
             theCube.get()[UMM] != theCube.get()[LTR] and \
             theCube.get()[UMM] != theCube.get()[BTR]:
                moves += fishAlg(theCube)  
             
        
            while theCube.get()[UMM] != theCube.get()[LTR]:
                moves += 'U'
                theCube._rotateU()
        
            moves += fishAlg(theCube)
        
        
        while theCube.get()[UMM] != theCube.get()[LTR]:
                moves += 'U'
                theCube._rotateU()
        moves += fishAlg(theCube)
        
        while theCube.get()[UMM] != theCube.get()[UBL]:
            moves += 'U'
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
    while (theCube.get()[UMM] == theCube.get()[UTR] == theCube.get()[UTM] == \
     theCube.get()[UTL] == theCube.get()[UML] == theCube.get()[UMR] == \
     theCube.get()[UBR] == theCube.get()[UBM] == theCube.get()[UBL]) is False:
        
        moves += makeFish(theCube)
        
        
        moves += fishAlg(theCube) 
        

    
    return moves      #TODO:  remove this stubbed value
