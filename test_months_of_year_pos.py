#!/usr/bin/env python

import unittest
from is_month_of_year import is_Month_Of_Year

class TestMonths(unittest.TestCase):
	def tester(self):
		self.assertTrue(is_Month_Of_Year("January"))
		self.assertTrue(is_Month_Of_Year("February"))
		self.assertTrue(is_Month_Of_Year("March"))
		self.assertTrue(is_Month_Of_Year("April"))
		self.assertTrue(is_Month_Of_Year("May"))
		self.assertTrue(is_Month_Of_Year("June"))
		self.assertTrue(is_Month_Of_Year("July"))
		self.assertTrue(is_Month_Of_Year("August"))
		self.assertTrue(is_Month_Of_Year("September"))
		self.assertTrue(is_Month_Of_Year("October"))
		self.assertTrue(is_Month_Of_Year("November"))
		self.assertTrue(is_Month_Of_Year("December"))

if __name__== '__xmain__':
	unittest.main()
