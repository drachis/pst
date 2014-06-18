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

def decrypt(_string,sizeH):
    sizeV = int(math.ceil(len(_string)/float(sizeH)))
    v = 0
    h = 0
    array2d = [["" for s in xrange(sizeH)] for a in xrange(sizeV)]
    decrypt = ""
    stringPos = 0 
    while v < sizeV:
        while h < sizeH:
            array2d[v][h] = _string[stringPos]
            stringPos += 1
            h += 1
        v += 1
        
    return array2dToString(array2d)

def array2dToString(_list):
    _string = ""
    for line in _list:
        _string += "".join(line).strip()
    return _string

def stringMatrixToCrypt(_list):
    crypt = array2dToString(zip(*_list[::-1]))
    return crypt

def stringMatrixToDecrypt(_list):
    decrypt = array2dToString(zip(*_list)[::-1])
    return decrypt
    

def stringToDecrypt(_string, _width):
    _width = int(math.ceil(len(_string)/float(_width)))
    return decrypt(stringToMatrix(_string, _width),_width)

def stringToCrypt( _string, _width):
    _string = _string.replace(" ","")
    return stringMatrixToCrypt(stringToMatrix(_string,_width))
    
    
if __name__ == "__main__":
    #_input = "thank you for applying for a job at play studios"
    _input = "1234567890"
    crypt = stringToCrypt(_input,6)
    uncrypt =  stringToDecrypt(crypt,6)
    pass

        
        