#!/usr/bin/python3

import re
st="I don't know why people are trying this email matching phani081.ch@gmail.com"
dd=re.search(r'[\w\.]+@[\w\.]+',st)
print (dd.group())

