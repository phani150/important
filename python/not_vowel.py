#!/usr/bin/python
vowel=('a','e','i','o','u')
st=raw_input("Please enter the string\n")
ks=""
for x in st:
	if x not in vowel:
		ks+=x
print ks
