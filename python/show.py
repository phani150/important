import os
os.system('find . -type f -name "*.txt" ')

def ss(f,*args,**kwargs):
	print (f,args,kwargs)
ss("Narasimhan",11,22,33,44,55,a=11,b=22,c=33)
