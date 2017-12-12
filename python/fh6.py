#!/usr/bin/python3

def stat(inf):
	num_lines=0
	num_words=0
	num_char=0
	
	with open(inf,'r+') as rf:
		hh={}
		for line in rf:
			num_lines+=1
			lines=line.split()
			hh[lines[0]]=lines[2]
			num_words+=len(lines)
			for x in lines:
				num_char+=len(x)
		print (hh)
		print ("num_lines:{},num_words:{},num_char:{}".format(num_lines,num_words,num_char))
stat('11.txt')

crs=open('11.txt','r+')
for column in (row.strip().split() for row in crs):
	print (column[0])

