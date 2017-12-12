#!/usr/bin/python3

import pandas as pd
weather_data={
        'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
        'temperature':[32,35,28,24,32,31],
        'windspeed':[6,7,2,7,4,2],
        'event':['rain','snow','rain','hot','hot','rain']
}

my=pd.Series(weather_data)
print (my)
