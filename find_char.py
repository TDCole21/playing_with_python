#!/usr/bin/env python3.8

	# <QUESTION>

    # Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.
    
    # <EXAMPLES>

	# find_char("This is a Sentence","s") → 4
	# find_char("This is a Sentence","S") → 8
	# find_char("Fridge for sale","z") → -1

	# <HINT>

	# Take a look at the documentation for Strings, List and range.

def find_char(inputString, char):
    newstring=""
    for words in inputString.split(" "):
        newstring=newstring+words
    for x in range(len(newstring)):
        if newstring[x] == char:
            return x+1 
    return -1