#!/usr/bin/python3
import functools
import numpy as np
ls=np.array([
		[
		[1,2,3],[4,5,6]
		],
		[
		[7,8,9],[10,11,12]
		]
])
print (ls.shape)
print (ls.ndim)

dd=np.arange(10)
print (type(dd))
#dh=functools.reduce(lambda x,y:x*y, dd)
#print (dh)
