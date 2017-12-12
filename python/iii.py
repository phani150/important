#!/usr/bin/python3

#crs=open("csv_copy.txt")
#for column in (row.strip().split('-') for row in crs):
#	print (column[0])

with open("csv_copy.txt",'r+') as rf:
	num_lines=0
	num_words=0
	num_chars=0
	words={}
	for x in rf:
		num_lines+=1
		kk=x.strip().split('-')
		num_words+=len(kk)
		for ch in kk:
			num_chars+=len(ch)
			if ch in words:
				words[ch]+=1
			else:
				words[ch]=1
	print (words)
	print ("Lines:{},Words:{},Chars:{}".format(num_lines,num_words,num_chars))	

#with open("csv_copy.txt") as wf:
#	words={}
#	for x in wf:
#		hh=x.strip().split('-')
#		for key in hh:
#			if key in words:
#				words[key]+=1
#			else:
#				words[key]=1
#print (words)
