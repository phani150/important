#!/usr/bin/python3

import pickle
cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
ll=pickle.load(fh)
print (ll)
fh.close()
