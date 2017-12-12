#!/usr/bin/python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("countries.csv")
data_2007=df[df.year==2007]
plt.scatter(data_2007.gdpPerCapita,data_2007.lifeExpectancy,5)
plt.title("GDP and lifeExpectancy in 2007")
plt.xlabel("GDP per Capita($)")
plt.ylabel("Life Ecpectancy")
print(np.log10([10,100,1000]))
plt.scatter(np.log10(data_2007.gdpPerCapita), data_2007.lifeExpectancy)
plt.show()
#print (df)
