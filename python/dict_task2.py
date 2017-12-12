#!/usr/bin/python
l=[{'aa':11},{'bb':22},{'aa':44},{'aa':11}]
seen = set()
new_l = []
for d in l:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)

print new_l

from collections import Counter

c=Counter()
for f in l:
    c.update(f)
print c
print dict(c)
