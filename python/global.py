#!/usr/bin/python3
x=88
def outer():
	x=22
	def inner():
		global x
		x=33
		print (x)
	return inner()
outer()
print (x)
