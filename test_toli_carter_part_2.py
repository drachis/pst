import random
import math

def findDuplicates(array2d):
    _dict = {}
    bestDup = [-1,-1]
    closest = len(array2d)**2
    for i,x, in enumerate(array2d):
        for j,y in enumerate(x):
            if y not in _dict:
                _dict[y] = [(i,j)]
            else:
                _dict[y].append((i,j))
    for value in _dict:
        if len(_dict[value]) > 1:
            for pair in _dict[value]:
                _distance = distanceSimple(pair, (0,0))
                if _distance < closest:
                    closest  = _distance
                    bestDup = pair
    return bestDup
def distanceSimple(a,b):
    #distance with out a square root for faster comparisons
    x = a[0]-b[0]
    y = a[1]-b[1]
    return x+y

def distance(a,b):
    return math.sqrt(istanceSimple(a,b))    

if __name__ == "__main__":
    dummyData = [[ random.randint(0,256) for x in range(4)] for y in range(4)]
    dup = findDuplicates(dummyData)
    print "Closest duplicate value is at: {0},{1}".format(dup[0], dup[1])