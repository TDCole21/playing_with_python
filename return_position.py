#!/usr/bin/env python3.8


	# Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # Do not ignore case
    # Ignore whitespace
    # If the char does not occur, return the number -1.
    # For Example:
	# returnPosition("This is a Sentence","s") → 4
	# returnPosition("This is a Sentence","S") → 8
	# returnPosition("Fridge for sale","z") → -1
def returnPosition(inputString, char):
    newstring=""
    for words in inputString.split(" "):
        newstring=newstring+words
        #print(newstring)
    for x in range(len(newstring)):
        if newstring[x] == char:
            print(x+1)
            exit(2)
    print(-1)
	#return -1

returnPosition("Fridge for sale","z")