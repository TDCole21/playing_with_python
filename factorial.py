#!/usr/bin/env python3.8

	# <QUESTION>

	# Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
	# eg If the input is 4, the function calculates 4x3x2x1 = 24 

	# <EXAMPLES>

	# factorial(1) → 1
	# factorial(4) → 24
	# factorial(8) → 40320

	# <HINT>

	# You may need to create a list of numbers from 0 to i, take a look at help(range).

def factorial(input):
	if input == 0:
		return 1
	else:
		return input * factorial(input-1)