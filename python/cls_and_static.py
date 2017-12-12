#!/usr/bin/python3

# a.py
class A:
   message = "class message"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo():
#      self.message = msg
      print("This is basic method")

   @staticmethod
   def sfoo():
      print ("Hi this is static method")

   def __str__(self):
      return self.message
A.sfoo()
A.foo()
A.cfoo()
