#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

di={'City':["Ger","Hun","Ind","Rome","Ger",'Hun','Ind','Rome','Ind'],'Rank':['1st','2nd','1st','2nd','1st','2nd','1st','2nd','1st'],
'score1':[44,48,39,41,38,44,54,54,61],'score2':[67,63,55,70,64,75,45,66,72]}
df=pd.DataFrame(di,index=pd.Index(['A','B','C','D','E','F','G','H','I'],name="letter"),
			columns=pd.Index(['City','Rank','score1','score2'],name="Attributes"))
print (df)
my_plot = df.plot(df['City'],stacked=True,kind='bar',legend=True)
my_plot.set_xlabel("City")
my_plot.set_ylabel("Score Value")
plt.show()
                                                                                                                                             
    
