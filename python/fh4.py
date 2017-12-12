#!/usr/bin/python3

import csv
with open('person.csv','r') as rd_file:
	csv_reader=csv.reader(rd_file)
	with open('csv_copy.txt','w+') as wr_file:
		csv_writer=csv.writer(wr_file,delimiter='-')
		for line in csv_reader:
			csv_writer.writerow(line)

