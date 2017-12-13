#!/usr/bin/python3
import csv
from pprint import pprint 
with open('person.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
    print (mydict)
