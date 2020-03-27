#!/usr/bin/env python3.8

	# given a string - return the number of times "am" appears in the String
	# ignoring case -
	# BUT ONLY WHEN the word "am" appears without being followed or preceded by
	# other letters
    # For Example:
	# amISearch("Am I in Amsterdam") → 1
	# amISearch("I am in Amsterdam am I?") → 2
	# amISearch("I have been in Amsterdam") → 0
def amISearch(arg1):
    count=0
    for words in arg1.split(" "):
        if len(words)>1:
            #print(words[-1])
            if words[0] == "a" and words[-1] =="m":
                count=count+1
    print (count)
	#return 0
amISearch("I have been in Amsterdam")