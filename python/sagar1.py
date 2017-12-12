#!/usr/bin/python
str = """
      B:0,
      C:0,
      a:10,
      b:11,
      c:12,"""
lst = str.split("\n")
lst= lst[1:len(lst)-1]
new_dic = {}
for l in lst:
        ls = l.split(":")
        print ls 
        new_dic[ls[0]] = ls[1]
print new_dic
gg={k:v for (k,v) in new_dic if v}
print gg
