#!/usr/bin/env python3	

	# <QUESTION>

	# The most frequent task in this test is to find out which one of the given numbers differs from the others.
	# Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

	# <EXAMPLES>

	# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

	# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

	# <HINT>
    
def odd_one_out(input):
	even=[]
	odd=[]
	input = list(map(int, input.split(' ')))
	#print(input)
	for number in range(len(input)):
		if int(input[number]) % 2 ==0:
			even.append(number)
			#print(number)
		else:
			odd.append(number)
			#print(number)
	if len(even)>len(odd):
		return int(odd[0]+1)
	else:
		return int(even[0]+1)

#odd_one_out("2 4 7 8 10")