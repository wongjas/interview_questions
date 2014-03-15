#!/usr/bin/python

import random
import unittest

from cartesian import *

class TestCartesian(unittest.TestCase):
    
    def setUp(self):
        self.point1 = Point(2, 3)
        self.point2 = Point(3, 4)
        self.point3 = Point(4, 5)
        self.point4 = Point(2, 7)
        self.point5 = Point(5, 10)
        self.list5 = [self.point1, self.point2, self.point3, 
                     self.point4, self.point5]

    def testCartesian(self):
        self.assertEqual(threeClosest(self.list5),
                         [self.point1, self. point2, self.point3])

if __name__ == '__main__':
    unittest.main()
