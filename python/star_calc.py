#!/usr/bin/python
def star(num):
	for x in range(1,num):
		print "*"*x
	for x in range(num):
		print "*" *(num-x)


star(8)
