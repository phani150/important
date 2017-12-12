#!/usr/bin/python

import re

def gg(fil):
    with open(fil,'r+') as ewf:
        num_err=0
        num_fail=0
        num_war=0
        for x in ewf:
            tt=re.match(r'([A-Z][a-z]+)(.*)',x)
	    zz=tt.group(1)
            if zz=="Error":
	        num_err+=1
	    elif zz=="Fail":
		num_fail+=1
	    elif zz=="Warning":
		num_war+=1	 	
            kk=re.search(r'(^Error|Fail:)(.*)',x)
            if kk:
                print kk.group()	
    return "Errors count:{},Failed count:{},Warnings count:{}".format(num_err,num_fail,num_war)

if __name__=='__main__':
    print gg('err_fail.txt')

