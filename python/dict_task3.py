#!/usr/bin/python3
from collections import Counter
l1={'A':1,'B':2}
l2={'A':11,'B':22}
ls=Counter(l1)+Counter(l2)
print (dict(ls))
