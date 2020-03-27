#!/usr/bin/env python3.8

def endsPy(word):
	length=len(word)
	if word.lower()[length-1] == "y" and word.lower()[length-2] == "p":
		return True
	else:
		return False