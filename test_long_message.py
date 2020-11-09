#!/usr/bin/env python

import unittest
from add import add

class TestAdd(unittest.TestCase):
	def test_pos(self):
		self.assertEqual(add(1,1), 2, "There is a problem with the test, result does not match expected result")

if __name__== '__xmain__':
	unittest.main()