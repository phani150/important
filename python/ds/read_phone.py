#!/usr/bin/python3

import pandas as pd
data=pd.read_csv('phone_data.csv')
# What is the sum of durations, for calls only, to each network
print (data[data['item'] == 'call'].groupby('network')['duration'].sum())
print (data.groupby(['month', 'item'])['date'].count())
print (data)

