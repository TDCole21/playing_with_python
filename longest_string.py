#!/usr/bin/env python3.8

	# <QUESTION>

	# Define a function that can accept two strings as input and returns the string with maximum length to the console. 
	
	# If two strings have the same length, then the function should return both strings separated by a " ".

	# In this case, the strings should be returned in the same order in which they were given.

	# <EXAMPLES>

	# longest_string("hi","hello") → "hello"
	# longest_string("three", "two") → "three"
	# longest_string("three", "hello") → "three hello"

	# <HINT>

	# What was the name of the function we have seen to check the length of a container?  Use your CLI to access the Python documentation and get help(len).

def longest_string(input1, input2):
	if len(input1)>len(input2):
		return input1
	elif len(input2)>len(input1):
		return input2
	else:
		return input1+" "+input2