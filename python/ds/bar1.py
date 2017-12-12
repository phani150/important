#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

di={'Hour':[0,1,2,3],'V1':[15,26,18,65],'V2':[13,52,45,38],'A1':[25,21,48,65]}
df1=pd.Series(di)
print (df1)
df=pd.DataFrame(di)
ax = df[['V1','V2']].plot(kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Hour", fontsize=12)
ax.set_ylabel("V", fontsize=12)
plt.show()
