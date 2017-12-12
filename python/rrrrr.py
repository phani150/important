#!/usr/bin/python3

with open("modified_person.csv",'r') as rf:
	for x in rf:
		print (x.strip().split(','))
