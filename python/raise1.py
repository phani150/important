#!/usr/bin/python3

class Accident(Exception):
	def __init__(self,msg):
		self.msg=msg
	def call(self):
		print ("accident occured between two cars")
try:
	raise Accident('Two cars crashed')
except Accident as e:
	e.call()
finally:
	print ("This is the way to produce raise keyword")
