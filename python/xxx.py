#!/usr/bin/python3

with open('csv_copy.txt','r') as rf:
	for x in rf.readlines():
		oo= (x.strip().split('-'))
		di={}
		di['firstname']={}
		
