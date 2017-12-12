#!/usr/bin/python

import re

st="my name is phani and ip is 192.168.1.3"
jj=re.sub(r'(.*?)(\d{3})(.*)',r'\g<1>194\3',st)
print jj

st1="My name is phanindra with 192"
dd=re.sub(r'(.*?)(phanindra)(.*?)',r'\1raghu',st1)
print dd

#ls=[1,2,3,4,5]
#ks=['ph','an','in','dr','a']
#dd={k:v for k,v in zip(ls,ks)}
#print dd

st3="My name"
ff=re.sub(r'(.*?)(name)','\1phanindra',st3)
print ff
