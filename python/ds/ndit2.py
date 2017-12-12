#!/usr/bin/python3

import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print ('First array is:' )
print (a) 
print ('\n')  

print ('Second array is:' )
b = np.array([1, 2, 3, 4], dtype = int) 
print (b)
print ('\n' )

print ('Modified array is:') 
for x,y in np.nditer([a,b]): 
   print ("%d:%d" % (x,y))
