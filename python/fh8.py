#!/usr/bin/python3
from pprint import pprint 
with open('modified_person.csv', 'r') as f:
    ks=f.readline().strip().split(',')
    results = {}
    for words in (row.strip().split(',') for row in f):
        results[int (words[0])]={}
        results[int(words[0])].update({ks[1]: words[1],ks[2]:words[2],ks[3]:words[3],ks[4]:words[4],ks[5]:int(words[5])})
    pprint (results)
