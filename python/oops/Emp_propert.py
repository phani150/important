#!/usr/bin/python3

class Employee():
	def __init__(self,first,last):
		self.first=first
		self.last=last
##		self.email=first + "." + last + "@gmail.com"
	def email(self):
		return "{}.{}@gmail.com".format(self.first,self.last) 
	def fullname(self):
		return "{}{}".format(self.first,self.last)
emp1=Employee("john","smith")
#print (emp1.email())
#print (emp1.fullname())
emp1.first="Phani"
print (emp1.email())
print (emp1.fullname())

		
