#!/usr/bin/python3

def aa(n):
	a,b,counter=0,1,0
	while True:
		if counter>n:return
		a,b=b,a+b
		yield a
		counter+=1
kk=aa(8)
for x in kk:
	print (x)

