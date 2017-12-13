#!/usr/bin/python3
import re
st="aabbbcccc"
ks=re.match(r"(aa)(bbb)(cccc)",st)
if ks:
	rf=ks.group(1,2,3)
	print (rf)
di={}
for x in rf:
	for y in x:
		if x in di:
			di[x]+=1
		else:
			di[x]=1
kk="".join("{}{}".format(k,v) for (k,v) in di.items())
print (kk)
