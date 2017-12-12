#!/usr/bin/python3

ls=int(input("Enter the number for armstrong\n"))
su=0
temp=ls
while (temp>0):
	digit=temp%10
	su+=digit**3
	temp//=10
if ls==su:
	print (ls,"is armstrong number")
else:
	print (ls,'is not a armstrong')	
