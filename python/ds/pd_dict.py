#!/usr/bin/python3

import pandas as pd

weather_data={
	'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
	'temperature':[32,35,28,24,32,31],
	'windspeed':[6,7,2,7,4,2],
	'event':['rain','snow','rain','hot','hot','rain']
}	

df=pd.DataFrame(weather_data)
df['age']=[10,20,30,40,50,'NaN']
print (df.fillna({'age':0}))
print (df)
print ('\n')
print (df['windspeed'].max())
print ('----\n---')
print (df.describe())
print ('\n')
print (df['temperature'].max())
print (df[df.event =='rain'])
print (df[['day','temperature']][df.temperature==df['temperature'].max()])                                       
