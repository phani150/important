#!/usr/bin/python3

class Person:
	"""Details of the person"""
	def __init__(self,id,name):
		self.id=id
		self.name=name
	def ss(self):
		print ("Hi this is phanindra")
	def details(self):
		return "id=%s name=%s" %(self.id,self.name)
class Student(Person):
	"""Gives the details of Student"""
	def __init__(self,average,id,name):
		self.average=average
		super().__init__(id,name)
	def details(self):
		return super().details() + "average=%s" % self.average

mo=Student("Emp106158","Phanindra","75")
print (mo.details())
