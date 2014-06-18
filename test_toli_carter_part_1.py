import math 

def stringToMatrix(_string,_width):
    # break string into a matrix, empty space is filled with spaces
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
    # rotate data back from crypt
    height = int(math.ceil(len(_string)/float(_width)))
    sizeH = height
    sizeW = _width
    array2d = [["" for x in xrange(_width)] for y in xrange(height)]
    decrypt = ""
    width = 0
    i = 0
    while width < sizeW:
        height = 0
        while height < sizeH:        
            stringpos = width*sizeH+height+i
            if width*_width+height < len(_string):
                array2d[height][width] = _string[stringpos]
            else:
                i -= 1
            height  += 1
        width += 1
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
    #_input = "thank you for applying for a job at play studios"
    _input = "thank you for applying for a job at play studios Thank you for applying for a job at play studios thank you for applying for a job at play studios Thank you for applying for a job at play studios"
    crypt = stringToCrypt(_input,6)
    decrypt =  stringToDecrypt(crypt,6)
    print "Source : {0} \nCrypt  : {1}\nDecrypt: {2}".format(_input,crypt,decrypt)

        
        