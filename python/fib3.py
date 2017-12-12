#!/usr/bin/python3

ls=int(input("Enter the number of terms you want\n"))
f,s=0,1
i=0
while (i<=ls):
	if (i<=1):
		nex=i
	else:
		nex=f+s
		f=s
		s=nex
	i+=1
print (nex)
