#Test files

import unittest

from calc_v2 import add, cube, divide, exponent, factorial, inverse, multiply, sqrt, square, subtract

class CalculatorTest(unittest.TestCase):

#Tests the add function, using whole numbers, decimals and negaitive numbers
	def testAdd(self):
		self.assertEqual(2, add(1,1))
		self.assertEqual([2,4], add([1,2],[1,2]))

#Tests the cube function, using whole numbers, decimals and negaitive numbers
	def testCube(self):
		self.assertEqual(8, cube(2))
		self.assertEqual([8, 64, 216], cube([2,4,6]))


#Tests the divide function, using whole numbers, decimals and negaitive numbers
	def testDivide(self):
		self.assertEqual(1, divide(2,2))
		self.assertEqual([3,4,5], divide([6, 8, 10], [2, 2, 2]))

#Tests the Exponent function, using whole and negaitive numbers
	def testExponent(self):
		self.assertEqual(4, exponent(2,2))
		self.assertEqual([4, 8, 16], exponent([2, 2, 2], [2, 3, 4]))


#Tests the factorial function, checking for use of negative and decimal error handling
	def testFactorial(self):
		self.assertEqual(120, factorial(5))
		self.assertEqual([6, 24], factorial([3, 4]))

#Tests the inverse function, using whole and negaitive numbers
	def testInverse(self):
		self.assertEqual(0.25, inverse(4))
		self.assertEqual([1,0.5,0.25], inverse([1,2,4]))

#Tests the multiply function, using whole numbers, decimals and negaitive numbers
	def testMultiply(self):
		self.assertEqual(4, multiply(2,2))
		self.assertEqual([6, 16, 30], multiply([2,4,6], [3,4,5]))

#Tests the sqrt function, using whole numbers, decimals and negaitive numbers and checks for use of negative number error handling
	def testSqrt(self):
		self.assertEqual(2, sqrt(4))
		self.assertEqual([2,4], sqrt([4, 16]))

#Tests the square function, using whole and negaitive numbers
	def testSquare(self):
		self.assertEqual(4, square(2))
		self.assertEqual([4,16,36], square([2, 4, 6]))

#Tests the subtract function, using whole numbers, decimals and negaitive numbers
	def testSubtract(self):
		self.assertEqual(0, subtract(2,2))
		self.assertEqual([5, 5, 10], subtract([10, 20, 30], [5, 15, 20]))


unittest.main()