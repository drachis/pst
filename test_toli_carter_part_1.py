import math 

def stringToMatrix(_string,_width):
    #break string into a filled matrix
    start = 0
    length = len(_string)
    output = []
    while start < length:
        filler = 0
        if length < start+_width:
            filler = (start+_width) - length
        output.append(_string[start:start+_width]+filler*" ")
        start += _width
    return output

def decrypt(_string,_width):
    height = int(math.ceil(len(_string)/float(_width)))
    
    sizeV = height
    sizeH = _width
    
   
    array2d = [["" for s in xrange(_width)] for a in xrange(height)]
    decrypt = ""
    h = 0
    i = 0
    while h < sizeH:
        v = 0
        while v < sizeV:        
            stringpos = _width*h+v+h+i
            if v*_width+h < len(_string):
                array2d[v][h] = _string[stringpos]
            else:
                i -= 1
            v  += 1
        h += 1
    return array2dToString(array2d)

def array2dToString(_list):
    _string = ""
    for line in _list:
        _string += "".join(line).strip()
    return _string

def stringMatrixToCrypt(_list):
    crypt = array2dToString(zip(*_list))
    return crypt
    
def stringToDecrypt(_string, _width):    
    return decrypt(_string,_width)

def stringToCrypt( _string, _width):
    _string = _string.replace(" ","")
    return stringMatrixToCrypt(stringToMatrix(_string,_width))
    
    
if __name__ == "__main__":
    _input = "thank you for applying for a job at play studios"
    #_input = "1234567890"
    crypt = stringToCrypt(_input,6)
    uncrypt =  stringToDecrypt(crypt,6)
    pass

        
        