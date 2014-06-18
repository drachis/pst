def stringSlice(_string,_width):
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


if __name__ == "__main__":
    _input = "thank you for applying for a job at play studios"
    #print zip(stringSlice(_input.replace(" ",""),6))
    
    _list = zip(*stringSlice(_input.replace(" ",""),6))
    _crypt = ""
    for line in _list:
        _crypt+="".join(line).replace(" ","")
        
    pass

        
        