#!/usr/bin/python3

class Employee(object):
	"""Details of the Employee"""
	def __init__(self,salary,age):
		self.salary=salary
		self.age=age
	def __str__(self):
		return "Employee (Salary is :%d,Age is: %d)" %(self.salary,self.age)
	def __add__(self,other):
		return Employee(self.salary +other.salary,self.age + other.age) 
v1=Employee(50000,30)
v2=Employee(10000,20)
print (v1.salary,v2.salary)
print (v1+v2)
