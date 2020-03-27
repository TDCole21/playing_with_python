#!/usr/bin/env python3.8

	# <QUESTION>

    # given a number
	# if this number is divisible by 3 return "fizz"
	# if this number is divisible by 5 return "buzz"
	# if this number is divisible by both 3 and 5 return "fizzbuzz"
	# if this number is not divisible by 3 or 5 return "null"
	    
    # <EXAMPLES>

	# fizz_buzz(3) → "fizz"
	# fizz_buzz(10) → "buzz"
	# fizz_buzz(15) → "fizzbuzz"
	# fizz_buzz(8) → "null"

	# <HINT>

	# No Hints for this question

def fizz_buzz(arg1):
	if arg1 % 3 == 0 and arg1 % 5 == 0:
		return "fizzbuzz"
	elif arg1 % 5 == 0:
		return "buzz"
	elif arg1 % 3 ==0:
		return "fizz"
	else:
		return "null"
