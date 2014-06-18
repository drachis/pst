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

def stringMatrixToCrypt(_list):
    crypt = ""
    for line in zip(*_list):
        crypt += "".join(line).strip()
    return crypt

def stringToCrypt( _string, _width):
    _string = _string.replace(" ","")
    return stringMatrixToCrypt(stringToMatrix(_string,_width))
    
    
if __name__ == "__main__":
    _input = "thank you for applying for a job at play studios"
    #_input = "AAABBBCC"
    crypt = stringToCrypt(_input,6)
    uncrypt =  stringToCrypt(crypt,6)
    pass

        
        