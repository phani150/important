#!/usr/bin/python

import re
st="Hi this is phanindra081@gmail.com"
mobj=re.sub(r'((.*?)[\w+\.]+)\@([\w+\.\w+]+)',r'\1@hotmail.com',st)
print mobj
