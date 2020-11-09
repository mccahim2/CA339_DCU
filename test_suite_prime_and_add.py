#!/usr/bin/env python

import unittest
from test_prime_number_pos_neg import TestIsPrimeNumber
from test_add_single_pos_neg import TestAddition

def test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestIsPrimeNumber))
	suite.addTest(unittest.makeSuite(TestAddition))
	tester = unittest.TextTestRunner()
	print(tester.run(suite))

test_suite()

if __name__== '__xmain__':
	unittest.main()
