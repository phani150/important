#!/usr/bin/python3

from collections import Counter
dd=Counter('Hi this is apple')
for vowel in 'aeiou':
	print ("%s:%d"%(vowel,int(dd[vowel])))
