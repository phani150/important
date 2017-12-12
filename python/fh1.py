#!/usr/bin/python

with open("1.txt",'r+') as ee:
	print ee.read(3)

ls=open('1.txt','r+')
ks=ls.readlines()
for x in ks:
	print x.strip()
print ls.mode
