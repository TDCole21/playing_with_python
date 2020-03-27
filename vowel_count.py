#!/usr/bin/env python3.8

	# <QUESTION>

    # Write a function which returns the integer number of vowels in a given string. 
    # You should ignore case.

	# <EXAMPLES>

    # vowel_count("Hello") → 2
    # vowel_count("hEelLoooO") → 6

	# <HINTS>

	# How do we ignore case in a String? help(str) may offer some insight.

def vowel_count(input):
	count=0
	lowercase=input.lower()
	for vowel in "aeiou":
		count= count + lowercase.count(vowel)
	return count