import fib_gen
def fib(n):
	a,b,count=0,1,0
	while True:
		
		if count>n:return
		a,b=b,a+b
		yield a
		count+=1
f=fib(8)
for x in f:
	print x
