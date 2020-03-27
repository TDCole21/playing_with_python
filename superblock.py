#!/usr/bin/env python3.8

	# Given a string, return the length of the largest "block" in the string.
	# A block is a run of adjacent chars that are the same, do not ignore case.
    # For Example:
	# superBlock("hoopplla") → 2
	# superBlock("abbCCCddDDDeeEEE") → 3
	# superBlock("") → 0
def superBlock(input):
    block=[]
    count=0
    if input=="":
        return 0
    for x in range(len(input)-1):
        if input[x] == input[x+1]:
            count=count+1
            #print(input[x])
        else:
            count=0
	#return -1
        block.append(count)
    print(max(block)+1)

superBlock("hooeooppplla")