#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('countries.csv')
data_1997=df[df.year==1997]
print (data_1997)
americas_1997=data_1997[data_1997.continent=='Americas']
europe_1997=data_1997[data_1997.continent=='Europe']
print (len(set(europe_1997.country)))
plt.subplot(211)
plt.title("Distribution of LifeExpectancy")
bins=20
plt.hist(americas_1997.lifeExpectancy,bins,range=(55,85),edgecolor='black')
plt.ylabel("Americas")
plt.subplot(212)
plt.ylabel("Europe")
plt.hist(europe_1997.lifeExpectancy,bins,range=(55,85),edgecolor='black')
print (americas_1997[americas_1997.lifeExpectancy < 65])
print (df.groupby(['year','continent'])['lifeExpectancy'].count())
plt.show()

