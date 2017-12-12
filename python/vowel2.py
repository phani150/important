#!/usr/bin/python3

from collections import Counter

st="Hi this is apple and orange"
c=Counter(st)
di={}
for x in 'aeiou':
	print ('%s : %d' % (x, c[x]))
