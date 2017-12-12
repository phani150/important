#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

exam_data = {'name': [np.nan,'Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [np.nan,12.5, 9, 16.5, np.nan, 9, 20, 14.5,np.nan, 8, 19],
'attempts': [np.nan,1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': [np.nan,'yes', np.nan, 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k']

df=pd.DataFrame(exam_data,index=labels)
ss=df.fillna({'score':0})
rr= df.dropna(axis=1, how='any')
print (rr)
zz=df.dropna(axis=0, how='all')
print (zz)
print (ss)
#print (df)
