#!/usr/bin/python3

ls=[{'AA':11},{'BB':12},{'CC':13},{'AA':11}]
name=set()
ks=[]
for x in ls:
	t=tuple(x.items())
	if t not in name:
		name.add(t)	
		ks.append(x)
print (ks)
