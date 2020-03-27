#!/usr/bin/env python3.8

# <QUESTION>

# Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def removes_char(l):
	answer=[]
	for i in l:
		if not isinstance(i, str):
			answer.append(i)

	return answer

#removes_char([1,2,'a','b'])