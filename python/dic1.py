#!/usr/bin/python
di1={'AA':11,'BB':22}
di2={'CC':33,'DD':44}
di3={}
for x in (di1,di2):
	di3.update(x)
print di3
