#!/usr/bin/python

import re
with open("email.txt",'r+') as rf:
	with open("email_result.txt","w+") as wf:
		for x in rf.readlines():
			mod=re.search(r"\w+\@\w+\.\w+",x)
			if mod:
				y=mod.group()
				print len(y)
				wf.write(y + "\n")
				
#			for r in y:
#				print r	
#			wf.write(y)
				
