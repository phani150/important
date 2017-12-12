
from __future__ import braces,absolute_import, division, print_function
from future.builtins.disabled import *

inp=int(input('Enter the number of terms fibinocci\n'))
ls=[0,1]
i=1
while inp>=i:
    js=ls[-1] + ls[-2] 
    ls.append(js)
    i+=1
print ls

