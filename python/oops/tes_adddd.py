#!/usr/bin/python3

import unittest
from  adddd import Phani
class Test(unittest.TestCase):
	def test_ss(self):
		kk=Phani()	
		self.assertEqual(66,kk.ss([11,22,33]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
