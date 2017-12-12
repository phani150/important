#!/usr/bin/python3

ks=int(input("Enter the number for factorial\n"))
fact=1
i=1
while(i<=ks):
	fact=fact*i
	i+=1
print ("The factorial of",ks,"is",fact)
