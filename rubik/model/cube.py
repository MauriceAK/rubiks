from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
    
    def get(self):
        return self.cube
  
    def rotate(self, directions):
        try:
            if directions == '':
                self._rotateF()
            else:    
                for direction in directions:
                        
                    if direction == 'F':
                        self._rotateF()
                    
                    if direction == 'f':
                        self._rotateF()
                        self._rotateF()
                        self._rotateF()
                    
                    if direction == 'R':
                        self._rotateR()
                    
                    if direction == 'r':
                        self._rotateR()
                        self._rotateR()
                        self._rotateR()
                    
                    if direction == 'B':
                        self._rotateB()
                    
                    if direction == 'b':
                        self._rotateB()
                        self._rotateB()
                        self._rotateB()
                    
                    if direction == 'L':
                        self._rotateL()
                    
                    if direction == 'l':
                        self._rotateL()
                        self._rotateL()
                        self._rotateL()
                    
                    if direction == 'U':
                        self._rotateU()
                    
                    if direction == 'u':
                        self._rotateU()
                        self._rotateU()
                        self._rotateU()
        except: 
            print("Invalid Direction Input: Cannot Rotate Cube")      
     
        return self._cube
    
   
    def _rotateF(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        #rotate front
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]
        #rotate right to bottom
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
        #rotate bottom to left
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]
        #rotate left to up
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self._cube = "".join(rotatedCubeList)

    def _rotateB(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        #rotate back
        rotatedCubeList[BTR] = cubeList[BTL]
        rotatedCubeList[BMR] = cubeList[BTM]
        rotatedCubeList[BBR] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BBR]
        #rotate right to up
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
        #rotate up to left
        rotatedCubeList[LTL] = cubeList[UTR]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LBL] = cubeList[UTL]
        #rotate left to down
        rotatedCubeList[DBR] = cubeList[LBL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBL] = cubeList[LTL]
        #rotate down to right
        rotatedCubeList[RTR] = cubeList[DBR]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RBR] = cubeList[DBL]
        self._cube = "".join(rotatedCubeList)
        
    def _rotateR(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        #rotate right
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBR] = cubeList[RTR]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RBL] = cubeList[RBR]
        #rotate up to back
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        #rotate back to bottom
        rotatedCubeList[DBR] = cubeList[BTL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DTR] = cubeList[BBL]
        #rotate bottom to front
        rotatedCubeList[FBR] = cubeList[DBR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FTR] = cubeList[DTR]
        #rotate front to up
        rotatedCubeList[UBR] = cubeList[FBR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UTR] = cubeList[FTR]
        self._cube = "".join(rotatedCubeList) 
        
    def _rotateL(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        #rotate left
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
        #rotate up to front
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
        #rotate front to down
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
        #rotate down to back
        rotatedCubeList[BBR] = cubeList[DTL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BTR] = cubeList[DBL]
        #rotate back to up
        rotatedCubeList[UTL] = cubeList[BBR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UBL] = cubeList[BTR]
        self._cube = "".join(rotatedCubeList) 
        
    def _rotateU(self):
        cubeList = list(self._cube)
        rotatedCubeList = cubeList[:]
        #rotate up
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBR] = cubeList[UTR]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UBL] = cubeList[UBR]
        #rotate front to left
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
        #rotate left to back
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
        #rotate back to right
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
        #rotate right to front
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
        self._cube = "".join(rotatedCubeList) 
