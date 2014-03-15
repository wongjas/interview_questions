#!/usr/bin/python

import sys
import math

class Point():
    """Represents a cartesian coordinate with x and y"""

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def __str__(self):
        return ''.join(["(", str(self.xpos), ", ",str(self.ypos),")"])

    def __eq__(self, other):
        return self.xpos == other.xpos and self.ypos == other.ypos

    def shortestDistance(self):
        dist = math.pow(self.xpos**2 + self.ypos**2, 0.5)
        self.dist = dist
        return self

# ListOfPoints -> ListOfPoints
def threeClosest(points):
    ptsWithDist = [p.shortestDistance() for p in points]
    ptsWithDist.sort()
    return ptsWithDist[0:3]
    
if __name__ == '__main__':
    threeClosest()
