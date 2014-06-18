def stringSlice(_string,_width):
    start = 0
    length = len(_string)
    while start < length:
        yield _string[start:start+_width]
        start += _width

def stringToMatrix(_string = None, _width = None):
    if _input == None or _width == None:
        print "Not enough input data, requires both string and width"
        return None
    _string = _string.replace(" ", "") 
    stringCrypt = []
    for line in stringSlice(_string, _width):
        stringCrypt.append(line)
    return stringCrypt

def stringMatrixToCryptString(_list):
    sizeRows = len(_list)
    sizeColumns = len(_list[0])
    lastColumn = len(_list[-1])
    stringCrypt = ""
    col = 0
    row = 0
    while col < sizeColumns:
        while row < sizeRows:
            if row != sizeRows-1:
                stringCrypt += _list[row][col]
            elif col < lastColumn:
                stringCrypt += _list[row][col]
                
            row += 1
        col += 1
        row = 0
    return stringCrypt

if __name__ == "__main__":
    _input = "thank you for applying for a job at play studios"
    print zip(*stringToMatrix(_input,6))[0]
    pass
        