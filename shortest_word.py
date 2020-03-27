#!/usr/bin/env python3	

# <QUESTION>

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def shortest_word(s):
	lengths=[]
	for words in s.split():
		lengths.append(len(words))
	return min(lengths) 

#shortest_word("bitcoin take over the world maybe who knows perhaps")