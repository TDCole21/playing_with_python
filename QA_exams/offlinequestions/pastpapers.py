#!/usr/bin/env python3.8

	# Level 3
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

	# Level 2
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

# Level 2
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


	# Level 3
	# Given two Strings of equal length, 'merge' them into one String.
    # Do this by 'zipping' the Strings together.
    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.
    # Maintain case.
    # You will not encounter whitespace.
    # For Example:
	# zipped("String","Fridge") → "SFtrriidngge"
	# zipped("Dog","Cat") → "DCoagt"
	# zipped("True","Tree") → "TTrrueee" 
	# zipped("return","letter") → "rleettutrenr"
# def zipped(input1, input2):
# 	return ""

# Level 2
	# Given a large string that represents a csv, the structure of each record will be as follows:
    # owner,nameOfFile,encrypted?,fileSize
    # Example:
    # "Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445"
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
    # For Example:
    # csvScan("Jeff,private.key,False,1445") → ["Jeff"]
	# csvScan("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445") → ["Jeff"]
	# csvScan("Bert,private.key,False,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
    # csvScan("Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
# def csvScan(input):
# 	return []