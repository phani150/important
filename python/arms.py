#!/usr/bin/python3

num=int(input("Enter the number for armstrong number\n"))
su=0
temp=num
while temp>0:
	digit=temp%10
	su=su+digit**3
	temp//=10
if su == num:
	print (num,"is a armstrong")
else:
	print (num,"not a armstrong")
