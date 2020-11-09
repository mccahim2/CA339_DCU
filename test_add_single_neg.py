#!/usr/bin/env python

import unittest
from add import add


class TestAdd(unittest.TestCase):
	def test_pos(self):
		self.assertEqual(add(1,1), 2)

class TestAdd(unittest.TestCase):
	def test_neg(self):
		self.assertNotEqual(add(-1,-1), 2)

if __name__== '__xmain__':
	unittest.main()
