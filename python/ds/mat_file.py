#!/usr/bin/python3

import matplotlib.pyplot as plt
import csv

x=[]
y=[]
with open('person.csv','r') as rf:
	read_file=csv.reader(rf)
	for row in read_file:
		x.append(int(row[4]))
		y.append(str(row[1]))

plt.plot(x,y,label="Loaded file easily")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()		
