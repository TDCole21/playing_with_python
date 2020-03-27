#!/usr/bin/env python3.8


	# <QUESTION>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

	# String example = "55 72 86"
	
	# "55" will = the integer 10
	# "72" will = the integer 9
	# "86" will = the integer 14
	
	# You then need to return the highest value, in the example above this would be 14.
	 
    # <EXAMPLES>

	# sum_digits("55 72 86") → 14
	# sum_digits("15 72 80 164") → 11
	# sum_digits("555 72 86 45 10") → 15

	# <HINT>

	# help(int) for working with numbers and help(str) for working with Strings.

def sum_digits(arg1):
	total=[]
	numbers=arg1.split(" ")
	for i in numbers:
		sum=0
		for x in i:
			x= int(x)
			sum=sum+x
		total.append(sum)	
	return max(total)