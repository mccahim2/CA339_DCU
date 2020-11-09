import unittest
from is_prime import is_Prime

class PrimesTestCase(unittest.TestCase):

    def test_is_five_prime(self):
        self.assertTrue(is_Prime(5))	

    def test_is_four_prime(self):
        self.assertFalse(is_Prime(4))

if __name__== '__xmain__':
    unittest.main()
