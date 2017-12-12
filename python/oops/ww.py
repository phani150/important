#!/usr/bin/python3

ls=[('A',11),('B',22),('C',33),('D',44),('E',55),('F',66)]
js={k:v for (k,v) in ls if v<55}
print (js)

def ll(balance=45):
    
    print (balance)
ll()

class CSS:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def dd(self):
		print (self.name)
class Person(CSS):
	def __init__(self,name,age,salary):
		self.age=age
	def ss(self):
		print ("Hi phanindra")

a=Person('Phanindra',33,33000)
a.dd()
