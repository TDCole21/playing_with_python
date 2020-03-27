#!/usr/bin/env python3.8


	# <QUESTION>

    # Given a string, int and a char, return a boolean value if the 'nth' 
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace. 
    
    # <EXAMPLES>

	# string_check("The",2,'h') → True
	# string_check("AAbb",1,'b') → False
	# string_check("Hi-There",10,'e') → False

	# <HINT>

	# How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.
 
def string_check(string, int, char):
	string=string.lower()
	if int > len(string):
		return False
	elif string[int-1]==char:
		return True
	else:
		return False
