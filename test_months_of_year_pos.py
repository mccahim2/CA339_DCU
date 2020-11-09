#!/usr/bin/env python

import unittest
from is_month_of_year import is_Month_Of_Year

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class TestMonths(unittest.TestCase):
	def tester(self):
		for month in months:
			self.assertTrue(is_Month_Of_Year(month))


if __name__== '__xmain__':
	unittest.main()
