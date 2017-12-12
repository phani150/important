#!/usr/bin/python3


class A():
    x=10
    def phani(self):
        self.x+=1
#    pass
s=A()
print (dir(s))
print (A.x)
print (s.x)
