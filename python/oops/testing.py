#!/usr/bin/python3

class JustCounter:
   _k=22
   __secretCount = 0
   def count(self):
      print (JustCounter._k)
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter._JustCounter__secretCount)
