#!/usr/bin/env python3.8


	# <QUESTION>

    # Given a large string that represents a csv, the structure of each record will be as follows:
    
    # owner,nameOfFile,encrypted?,fileSize
    
    # "Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445"
    
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
	# If all records are encrypted, return an empty Array.
    
    # <EXAMPLES>
    
    # file_owner("Jeff,private.key,False,1445") → ["Jeff"]
	# file_owner("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445") → ["Jeff"]
	# file_owner("Bert,private.key,False,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
    # file_owner("Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
    
	# <HINT>

	# Dont't forget, False is a String, not a Boolean value in the Tests above.

	# help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).

def file_owner(input):
	input= input.split(",")
	length=len(input)
	owners=[]
	for i in range(0,length-1):
		if input[i]=="False":
			owners.append(input[i-2])
	return owners

#file_owner("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445")