#!/usr/bin/python

class customer(object):
    """A customer of abc bank for checking account summary """
    def __init__(self,name,balance=0):
        """Return a customer object whose having name and balance"""
        self.name=name
        self.balance=balance

    def withdraw(self,amount):
	"""Checking for withdrawal"""
	if amount >self.balance:
	    raise RuntimeError("Amount greater than available balance")
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
	self.balance+=amount
        return self.balance

if __name__=='__main__':
    obj1=customer(name='Phanindra',balance=100000) 
    obj2=customer(name='chaitu',balance=500000) 
    balance=obj1.withdraw(5000000) 
    print customer.__doc__
    print obj1.balance
    print obj2.deposit(250000) 
