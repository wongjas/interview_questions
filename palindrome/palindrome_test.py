#/usr/bin/python

import unittest
import palindrome as pal

class testPalindrome(unittest.TestCase):

    def setUp(self):
        self.palin1 = "racecar"
        self.palin2 = "kanakanak"
        self.palin3 = "kayak"
        self.nonpalin1 = "jason"
        self.nonpalin2 = "hello"
        self.nonpalin3 = "leool"

    def testPalindrome(self):
        self.assertTrue(pal.palindrome(self.palin1))
        self.assertTrue(pal.palindrome(self.palin2))
        self.assertTrue(pal.palindrome(self.palin3))
        self.assertFalse(pal.palindrome(self.nonpalin1))
        self.assertFalse(pal.palindrome(self.nonpalin2))
        self.assertFalse(pal.palindrome(self.nonpalin3))

if __name__ == "__main__":
    unittest.main()
