#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("countries.csv")
us=data[data.country=="United States"]
#plt.plot(us.year,us.gdpPerCapita,label="US")
us_growth=us.gdpPerCapita/ us.gdpPerCapita.iloc[0] *100
china=data[data.country=="China"]
#plt.plot(china.year,china.gdpPerCapita,label="CHINA")
china_growth=china.gdpPerCapita/ china.gdpPerCapita.iloc[0] *100
plt.plot(us.year,us_growth)
plt.plot(china.year,china_growth)
plt.xlabel("Year")
plt.ylabel("GDP Per Capita")
plt.title("LifeExpectany")
plt.legend()
plt.show()
print (us)
print (data)

