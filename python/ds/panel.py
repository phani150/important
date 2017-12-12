#!/usr/bin/python3

#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : [1,2,3,4,5,6], 
        'Item2' : ['anil','Phani','basha','satthar','indra']}
p = pd.Panel(data)
print (p.shape)
print (p.values)
