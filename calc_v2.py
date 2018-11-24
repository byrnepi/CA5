#Big Data CA 1

from functools import reduce
from math import factorial as fact

#Function returns the sum of the two numbers provided
def add(a, b):

	func = lambda x, y: x+y

	if type(a) == list:
		ans = list(map(func, a, b))
	else:
		ans = func(a, b)
	return ans

#Function returns the cube of the number provided
def cube(a): 

	func = lambda x: x**3

	if type(a) == list:
		ans = list(map(func, a))
	else:
		ans = func(a)
	return ans

#Function checks the divsor is not 0 and returns the first number divided by the second number provided
def divide(a, b):

	func = lambda x,y: x/y

	if type(a) == list:
		ans = list(map(func, a, b))
	else:
		ans = func(a, b)
	return ans

#Function returns the result of the first number to the power of the second number
def exponent(a, b):

	func = lambda x,y: x**y

	if type(a) == list:
		ans = list(map(func, a, b))
	else:
		ans = func(a, b)
	return ans

#Function checks the number provided is not a negative, then returns 
def factorial(a):

	func = lambda x: fact(x)

	if type(a) == list:
		ans = list(map(func, a))
	else:
		ans = func(a)
	return ans

#Function returns the inverse of the number provided
def inverse(a):

	func = lambda x: 1.0/x

	if type(a) == list:
		ans = list(map(func, a))
	else:
		ans = func(a)
	return ans

#Function returns the product of the two numbers provided
def multiply(a, b):

	func = lambda x, y: x*y

	if type(a) == list:
		ans = list(map(func, a, b))
	else:
		ans = func(a, b)
	return ans

#Function return() the square root of the number provided
def sqrt(a):

	func = lambda x: x**0.5

	if type(a) == list:
		ans = list(map(func, a))
	else:
		ans = func(a)
	return ans

#Function returns the square of the number provided
def square(a):

	func = lambda x: x**2

	if type(a) == list:
		ans = list(map(func, a))
	else:
		ans = func(a)
	return ans

#Function returns the difference between the first and second number 
def subtract(a, b):

	func = lambda x,y: x-y

	if type(a) == list:
		ans = list(map(func, a, b))
	else:
		ans = func(a, b)
	return ans














