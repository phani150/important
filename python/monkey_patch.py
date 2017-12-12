#!/usr/bin/python3
"""Changing the code sneakily at runtime"""
class Phani():
	def add(self, x, y):
		return x + y

inst = Phani()
def not_exactly_add(self, x, y):
	return x * y
Phani.add = not_exactly_add
print (inst.add(3, 3))

