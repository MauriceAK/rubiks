from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.view.rotate import *
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)

    if theCube.get() == '':
        result['status'] = 'Error: Missing cube'
        return result
    if check_alphanum(theCube.get()) == False:
        result['status'] = 'Error: Invalid characters present'
        return result
    elif check_validamount(theCube.get()) == False:
        result['status'] = 'Error: Invalid amount of valid colors'
        return result
    elif check_middles(theCube.get()) == False:
        result['status'] = 'Error: Cube middles are not unique'
        return result
    
    
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    
    hashToken = parms.get('cube')
    hashToken += rotations
    hashToken += 'mak0078'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(hashToken.encode())
    fullToken = sha256Hash.hexdigest()
    hashRand = random.randrange(len(fullToken) - 8)
    integrity = fullToken[hashRand:hashRand + 8]
    result['integrity'] = integrity              #iteration 3
                     
    return result