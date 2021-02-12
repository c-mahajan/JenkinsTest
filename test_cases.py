# Python code to demonstrate working of unittest 
import unittest
from Calculator import * 

class TestCalculator(unittest.TestCase):
    def test_Add(self):
        a = 2
        b = 3
        c = a + b
        self.assertEqual(add(a, b), c)
    
    def test_mul(self):
        a=2
        b=3
        mul_res= a * b
        self.assertEqual(mul(a, b), mul_res)

    def test_sub(self):
        a=2
        b=3
        sub_res= a - b
        self.assertEqual(sub(a, b), sub_res)

    def test_div(self):
        a=2
        b=3
        div_res= a / b
        self.assertEqual(div(a, b), div_res)

if __name__ == '__main__': 
	unittest.main() 
