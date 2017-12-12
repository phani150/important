#!/usr/bin/python
st=raw_input('Enter the string for palindrome\n')
ks=""
for x in range(-1,-len(st)-1,-1):
	ks+=st[x]
if ks is st:
	print st,'is a palindrome'
else:
	print st,"is not a palindrome"
print id(ks)
print id(st)
