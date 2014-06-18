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
    stringCrypt = []
    for line in stringSlice(_string.replace(" ", "") , _width):
        stringCrypt.append(line)
    return stringCrypt
        



if __name__ == "__main__":
    _input = "This is an input string for testing"

    print stringToMatrix(_input,6)
        