#!/usr/bin/python3

def outer(a):
	def inner(b):
		return  a + b
	return inner
ff=outer(1)
gg=outer(2)
print (ff.__name__)
print (ff(11),gg(22))
