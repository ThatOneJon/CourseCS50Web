import unittest
from lectureForTesting import isPrime


class Tests(unittest.TestCase):
    #Defines a class which inherits from unittest.TestCase

    def test_1(self):
        self.assertFalse(isPrime(8))
        """First test"""
    #first function asserts, that 8 is not prime

    def test_2(self):
        self.assertTrue(isPrime(7))


if __name__ == "__main__":
    unittest.main()
    # runs all test, if the main function is called, > the name if the file no import
