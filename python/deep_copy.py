#!/usr/bin/python3

##A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
from copy import deepcopy

lst1 = ['a','b',['ab','ba']]

lst2 = deepcopy(lst1)

lst2[2][1] = "d"
lst2[0] = "c";

print (lst2)
print (lst1)
