import collections
a=[66,2,3,'phani',22,3,4,2,2,22]
print [item for item, count in collections.Counter(a).items() if count > 1]
