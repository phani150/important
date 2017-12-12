#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,6]

x1=[1,2,3]
y1=[7,8,9]
plt.plot(x,y,label='First plot')
plt.plot(x1,y1,label='Second plot')
plt.legend()
plt.show()
