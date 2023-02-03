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
    for char in string:
        if char.isalnum() != False:
            return False
        return True;
    
def rotate(parms):
    """Return rotated cube""" 
    
    
    result = {}
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    directions = parms.get('dir')
    theCube.rotate(directions)
    result['cube'] = theCube.get()
    
    if check_length(encodedCube) == False: 
        result['status'] = 'Error: Invalid cube length'
    elif check_middles(encodedCube) == False:
        result['status'] = 'Error: Cube middles are not unique'
    elif check_alphanum(encodedCube) == True:
        result['status'] = 'Error: Invalid characters present'
    else:
        result['status'] = 'ok'
    
                         
    return result