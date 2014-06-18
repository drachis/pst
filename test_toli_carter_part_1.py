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
    sizeV = math.ceil(len(string)/float(_width))
    v,h= 0    
    while v < sizeV:
        pass    
    return decrypt
                      

def stringMatrixToCrypt(_list):
    crypt = ""
    for line in zip(*_list[::-1]):
        crypt += "".join(line).strip()
    return crypt

def stringMatrixToDecrypt(_list):
    decrypt = ""
    for line in zip(*_list)[::-1]:
        decrypt += "".join(line).strip()
    return decrypt
    

def stringToDecrypt(_string, _width):
    _width = int(math.ceil(len(_string)/float(_width)))
    return stringMatrixToDecrypt(stringToMatrix(_string, _width))

def stringToCrypt( _string, _width):
    _string = _string.replace(" ","")
    return stringMatrixToCrypt(stringToMatrix(_string,_width))
    
    
if __name__ == "__main__":
    #_input = "thank you for applying for a job at play studios"
    _input = "1234567890"
    crypt = stringToCrypt(_input,6)
    uncrypt =  stringToDecrypt(crypt,6)
    pass

        
        