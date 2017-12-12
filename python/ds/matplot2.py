#!/usr/bin/python3

from matplotlib import pyplot as plt 
x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center',label="gents") 
plt.bar(x2, y2, color = 'g', align = 'center',label="Ladies") 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.legend()
plt.show()
#plt.savefig("fig_matplot2")
