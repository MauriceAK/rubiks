from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
    
    def get(self):
        return self.cube
  
    def rotate(self, directions='F'):
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
        