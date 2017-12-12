#!/usr/bin/python3

ks=int(input("Enter the number for armstrong\n"))
sum=0
temp=ks
while temp>0:
	digit=temp%10
	sum+=digit**3
	temp//=10
if sum==ks:
	print (ks,"is a armstrong" )
else:
	print (ks,'is not a armstrong')
