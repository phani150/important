#!/usr/bin/python


class A():
    d="Hello world!"   
    def __init__(s,a):
        s.b=a
	print "Hello Phanindra"
    def su(s,numlist):
	s.numlist=numlist
	su=0
	for x in s.numlist:
	    su=su+x
	print su

class B(A):
    def su(s):
	print ("This is Polymorphism")
print (A.d)	
#aa=A(99)
#aa.su([11,22,33,44])
bb=B(100)
bb.su()
