#/usr/bin/python

import unittest
import palindrome as pal

class testPalindrome(unittest.TestCase):
    def setUp(self):
        self.palin1 = "racecar"
        
    def testPalindrome(self):
        self.assertTrue(pal.palindrome(self.palin1))

if __name__ == "__main__":
    unittest.main()
