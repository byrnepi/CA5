#Test files

import unittest

from calc_v2 import add, cube, divide, exponent, factorial, inverse, multiply, sqrt, square, subtract

class CalculatorTest(unittest.TestCase):

#Tests the add function, using whole numbers, decimals and negaitive numbers
	def testAdd(self):
		self.assertEqual(4, add(2,2))
		self.assertEqual(2, add(2,0))
		self.assertEqual(0, add(0,0))
		self.assertEqual(3, add(-1,4))
		self.assertEqual(3.8, round(add(2.2,1.6),1))

#Tests the cube function, using whole numbers, decimals and negaitive numbers
	def testCube(self):
		self.assertEqual(8, cube(2))
		self.assertEqual(-8, cube(-2))
		self.assertEqual(27, cube(3))
		self.assertEqual(3375, cube(15))
		self.assertEqual(15.625, round(cube(2.5),3))

#Tests the divide function, using whole numbers, decimals and negaitive numbers
	def testDivide(self):
		self.assertEqual(1, divide(2,2))
		self.assertEqual(2, divide(6,3))
		self.assertEqual(2.72, round(divide(3.4,1.25),2))
		self.assertEqual(-2, divide(6,-3))
		self.assertEqual(2, divide(-6,-3))

#Tests the Exponent function, using whole and negaitive numbers
	def testExponent(self):
		self.assertEqual(4, exponent(2,2))
		self.assertEqual(32, exponent(2,5))
		self.assertEqual(1, exponent(6,0))
		self.assertEqual(0.25, exponent(2,-2))
		self.assertEqual(9765625, exponent(5,10))

#Tests the factorial function, checking for use of negative and decimal error handling
	def testFactorial(self):
		self.assertEqual(120, factorial(5))
		self.assertEqual(3628800, factorial(10))
		self.assertEqual(1, factorial(0))

#Tests the inverse function, using whole and negaitive numbers
	def testInverse(self):
		self.assertEqual(0.25, inverse(4))
		self.assertEqual(-0.1, inverse(-10))
		self.assertEqual(0.2, inverse(5))

#Tests the multiply function, using whole numbers, decimals and negaitive numbers
	def testMultiply(self):
		self.assertEqual(4, multiply(2,2))
		self.assertEqual(0, multiply(2,0))
		self.assertEqual(-6.6, multiply(5.5,-1.2))
		self.assertEqual(15, multiply(3,5))
		self.assertEqual(1, multiply(2,0.5))

#Tests the sqrt function, using whole numbers, decimals and negaitive numbers and checks for use of negative number error handling
	def testSqrt(self):
		self.assertEqual(2, sqrt(4))
		self.assertEqual(4, sqrt(16))
		self.assertEqual(2.345, round(sqrt(5.5),3))

#Tests the square function, using whole and negaitive numbers
	def testSquare(self):
		self.assertEqual(4, square(2))
		self.assertEqual(4, square(-2))
		self.assertEqual(9, square(3))
		self.assertEqual(16, square(4))
		self.assertEqual(625, square(25))

#Tests the subtract function, using whole numbers, decimals and negaitive numbers
	def testSubtract(self):
		self.assertEqual(0, subtract(2,2))
		self.assertEqual(2, subtract(2,0))
		self.assertEqual(-1, subtract(2,3))
		self.assertEqual(5, subtract(2,-3))
		self.assertEqual(-5, subtract(-2,3))
		self.assertEqual(-2.3, subtract(2.2, 4.5))


unittest.main()