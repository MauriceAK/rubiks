from rubik.model.cube import Cube

def check_valid(string):
    middles = set(string[4],string[13],string[22],string[31],string[40],string[49])
    
    for char in string:
        if char.isalnum() != False:
            return False
        if len(string) != 54:
            return False
        if len(middles) < 6:
            return False
    return True


def rotate(parms):
    """Return rotated cube""" 
    
    
    result = {}
    
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    directions = parms.get('dir')
    theCube.rotate(directions)
    result['cube'] = theCube.get()
    
    if check_valid(encodedCube): 
        result['status'] = 'ok' 
    else:
        result['status'] = 'Error: Invalid cube'
    
                         
    return result