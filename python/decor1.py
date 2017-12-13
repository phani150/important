#!/usr/bin/python3

def our_decorator(func):
    def function_wrapper(x):
        print("executed Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi") 

##________________Closures__________________________________##

def outer(a):
    def inner(b):
        return a+b
    return inner
f=outer(2)
g=outer(3)
#print (f)
print (f(11),g(22))
