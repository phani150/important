#!/usr/bin/python

ls=int(input("Enter the number for armstrong number\n"))
temp=ls
su=0
while temp>0:
	digit=temp%10
	print digit
        su=su+digit**3	
	print su
	temp//=10
if ls==su:
	print ls,"is a armstrong"
else:
	print ls,"is not a armstrong"
        
        	
