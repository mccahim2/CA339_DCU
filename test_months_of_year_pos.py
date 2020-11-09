#!/usr/bin/env python

import unittest
from is_month_of_year import is_Month_Of_Year

class TestMonths(unittest.TestCase):
	def tester(self):
		self.assertTrue(is_Month_Of_Year("January"))

if __name__== '__xmain__':
	unittest.main()
