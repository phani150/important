def f(x):
	return [lambda x:y*x for y in range(4)]
print (f(2))
