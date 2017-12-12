#!/usr/bin/python3

class Phani:
	def ss(self,numlist):
		self.numlist=numlist
		su=0
		for x in self.numlist:
			su+=x
		return su
a=Phani()
a.ss([22,33,44])
