#!/usr/bin/python
def outer(ls):
	def inner(ks):
		return ls + ks
	return inner
f=outer(22)
g=outer(33)
print f(2),g(3)
