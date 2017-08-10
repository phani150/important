ls=[x for y in range(2,9) for x in range(y*2,50,y)]
ks=[i for i in range(2,50) if i not in ls]
print ks
