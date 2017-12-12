#!/usr/bin/python
ls=open("12.txt","r")
ks=ls.readlines()
for x in ks:
	k=x.split()
	print k[0]
