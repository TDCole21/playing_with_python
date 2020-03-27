#!/usr/bin/env python3.8

	# <QUESTION>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.
    
    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

	# <EXAMPLES>

    # i_before_e("ceiling") → True
    # i_before_e("believe") → True
    # i_before_e("glacier") → False
    # i_before_e("height") → False

	# <HINT>

	# Step through the logic here in order to solve the problem, you may find help(range) helpful.

import re
def i_before_e(input):
	if re.search('cei', input.lower()):
		return True
	elif re.search('cie', input.lower()):
		return False
	elif re.search('[^c]ie', input.lower()):
		return True
	elif re.search('[^c]ei', input.lower()):
		return False