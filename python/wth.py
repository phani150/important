#!/usr/bin/python

with open('1.txt','r+') as rf:
	with open('11.txt','w+') as wf:
		for x in rf:
			wf.write(x)
