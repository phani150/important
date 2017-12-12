#!/usr/bin/python3
import numpy as np
ls=[10,1,2,4,5,20,30]
ks=[10,20,30,40,50,60,70]

js=np.empty((0,10),int)
for x in ls:
	if x in ks:
		np.append(js,np.array([x]),axis=0)
print (js)
