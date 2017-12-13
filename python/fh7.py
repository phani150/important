#!/usr/bin/python3

from pprint import pprint
with open("person.csv",'r+') as rf:
	for x in rf:
		words=x.split(',')
		print (words)
