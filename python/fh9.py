#!/usr/bin/python3
from pprint import pprint 
with open('modified_person.csv', 'r') as f:
    ks=f.readline().strip().split(',')
    print (ks)
    results = {}
    for line in f:
        print (line)
        """        words = line.strip().split(',')
        print (words[0])
        results[words[0]]={}
        results[words[0]].update({'firstname': words[1],'lastname':words[2],'city':words[3],'skillset':words[4],'salary':int(words[5])})
    pprint (results)"""
