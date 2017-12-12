#!/usr/bin/python3

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

class D(object):
    def __init__(self):
        self._x =100 

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        print ( self._x)
    @x.deleter
    def x(self):
        del self._x
        print ("To delete")
aa=D()
print (aa.x)
