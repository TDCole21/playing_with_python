#!/usr/bin/env python3.8

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
def csvScan(input):
	return []