#!/usr/bin/python3

from sup import Person

class Student1(Person):
	"""Here we are testing the class Person"""
	def __init__(self,id,name,major):
		self.major=major
		super().__init__(id,name)
		print (self.major)
a=Student1("106157","Deepak","CSC")
print (a.details())
