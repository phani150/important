#!/usr/bin/python3

with open('11.txt','r+') as rf:
	hh={}
	for x in rf:
		ss=x.split()
		for y in ss:
			if y in hh:
				hh[y]+=1
			else:
				hh[y]=1
	print (hh)		
	
