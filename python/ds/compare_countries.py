#!/usr/bin/python3

import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("countries.csv")
print (set(data['continent']))
data_2007=data[data.year==2007]
asia_2007=data_2007[data_2007.continent=='Asia']
europe_2007=data_2007[data_2007.continent=='Europe']
print (len(set(europe_2007.country)))
plt.subplot(2,1,1)
plt.title('Gdp Per Capital')
plt.hist(asia_2007.gdpPerCapita,20,range=(0,50000),edgecolor='black')
plt.ylabel('Asia')
plt.subplot(2,1,2)
plt.hist(europe_2007.gdpPerCapita,20,range=(0,50000),edgecolor='black')
print (asia_2007[asia_2007.gdpPerCapita <40000])
plt.ylabel('Europe')
plt.show()
