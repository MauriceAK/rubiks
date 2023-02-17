from rubik.model.cube import Cube

def check_length(string): 
    if len(string) != 54:
        return False    
    return True

def check_middles(string):
    middles = {string[4],string[13],string[22],string[31],string[40],string[49]}
    if len(middles) < 6:
            return False
    return True    

def check_alphanum(string):
    if string.isalnum() != True:
        return False;
    return True;

def check_validamount(string):
    for letter in string:
        if string.count(letter) != 9:
            return False;
    return True;
    
def rotate(parms):
    """Return rotated cube""" 
    
    
    result = {}
    
    if parms.get('cube') == None:
        result['status'] = 'Error: Missing cube'
        return result
    encodedCube = parms.get('cube')
    
    theCube = Cube(encodedCube)
    
    if check_length(encodedCube) == False: 
        result['status'] = 'Error: Invalid cube length'
        return result
    
    directions = parms.get('dir')
    rotatedCube = theCube.rotate(directions)
    
    if rotatedCube == 'DirException':
        result['status'] = 'Error: Invalid rotation'
        return result
    
    if check_alphanum(encodedCube) == False:
        result['status'] = 'Error: Invalid characters present'
        return result
    elif check_validamount(encodedCube) == False:
        result['status'] = 'Error: Invalid amount of valid colors'
        return result
    elif check_middles(encodedCube) == False:
        result['status'] = 'Error: Cube middles are not unique'
        return result
    
    else:
        result['status'] = 'ok'
    
    result['cube'] = rotatedCube
                         
    return result