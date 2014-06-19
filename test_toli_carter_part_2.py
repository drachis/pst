import random

def findDuplicates(array2d,size):
    _dict = {}
    closest = (size+1,size+1)
    foundDup = False
    for coord in rectangularWalk(size):
        if foundDup == False:
            value = array2d[coord[0]][coord[1]]
            if value not in _dict:
                _dict[value] = [coord]
            else:
                foundDup = True
                closest = coord
        elif distanceSimple((0,0), coord) < distanceSimple((0,0), closest):
            # duplicates beyond the radius of the initial point are of no intrest
            if value not in _dict:
                _dict[value] = [coord]
            else:
                closest = coord
        elif coord[0] > closest[0]*1.5 or coord[1] > closest[1]*1.5:            
            # once beyond the radius of the circle on the axis stop looking.
            break
    if foundDup:
        return closest
    else:
        return (-1,-1)

def distanceSimple(a,b):
    # distance with out a square root, faster for comparison work
    x = a[0]-b[0]
    y = a[1]-b[1]
    return x**2+y**2

def distance(a,b):
    return math.sqrt(istanceSimple(a,b))    

def rectangularWalk(size):        
    # generate walking coordinates for points closer to 0,0 sooner
    # assumes data is square and uses an edge length for max
    x,y,n = (0,0,0)
    while n < size:
        while x <= n:        
            yield (x,n)
            x += 1
        while y < n:
            yield (n,y)
            y += 1
        n += 1
        x,y = (0,0)

if __name__ == "__main__":
    size = 128
    dummyData = [[ random.randint(0,256) for x in xrange(size)] for y in xrange(size)]
    dup = findDuplicates(dummyData,size)
    print "Closest duplicate value is at: ({0},{1})".format(dup[0], dup[1])
    pass