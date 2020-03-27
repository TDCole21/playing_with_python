#!/usr/bin/env python3.8

	# <QUESTION>

    # Return the string that is between the first and last appearance of "bert" in the given string
	
	# Return the empty string "" if there is not 2 occurances of "bert" 
	
	# IGNORE CASE
    
    # <EXAMPLES>

	# inbetween_berts("bertclivebert") → "clive"
	# inbetween_berts("xxbertfridgebertyy") → "fridge"
	# inbetween_berts("xxBertfridgebERtyy") → "fridge"
	# inbetween_berts("xxbertyy") → ""
	# inbetween_berts("xxbeRTyy") → ""

	# <HINT>

	# What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?
	
	# Use your CLI to access the Python documentation and get help manipulating strings - help(str).

# import re
# def inbetween_berts(input):
# 	if re.search('bert(.*)bert', input.lower()):
# 		return re.search('bert(.*)bert', input.lower()).group(1)
# 	else:
# 		return ""

import re
def inbetween_berts(input):
	return re.search('bert(.*)bert', input.lower()).group(1) if re.search('bert(.*)bert', input.lower()) else ""
