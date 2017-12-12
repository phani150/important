#!/usr/bin/python

import re

st="why people are matching this d.phani081@gmail.com"
ks=re.search(r"(.*?)\s[\w\.-]+@[\w\.]+",st)
print ks.group(1)

