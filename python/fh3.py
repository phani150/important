#!/usr/bin/python3
with open('11.txt','r+') as rf:
	with open('testing.txt','w+') as wf:
		for x in rf.readlines():	
			wf.write(x)

