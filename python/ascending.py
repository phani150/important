#!/usr/bin/python
import armstrong
ls=[22,2,3,7,5,88,9,99]
ks=[]
while ls:
    ma=ls[0]         ###Taking arbitary values
    for x in ls:
        if x>ma:
            ma=x
    ks.append(ma)
    print ks
    ls.remove(ma)
    print ls 
print ks

