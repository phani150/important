#!/usr/bin/python

ks=raw_input("Enter the ipaddress\t")
ls=ks.split(".")
js=["matched" if 0<=len(x)<=255 and len(ls)==4  else "not matched" for x in ls ]
print js
