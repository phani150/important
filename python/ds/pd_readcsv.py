#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
file_data = pd.read_csv("pd.csv",header=None,names=['Country','Population','Area','Capital'],na_values={'Area':["not available","n.a",246787]})
print (file_data)
print (len(file_data['Country']))
print (file_data['Population'])
file_data.drop(file_data.index[[1,2]])
print ('\n')
print (file_data)
plt.plot(file_data['Country'],file_data['Population'])
plt.xlabel("Countries")
plt.ylabel("Populations")
plt.show()


