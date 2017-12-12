#!/usr/bin/python3

import sys
sys.path.append("python")
with open("11.txt",'r+') as rf:
	for x in rf:
		s=x.strip().split()
		print (s)
