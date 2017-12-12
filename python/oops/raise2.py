#!/usr/bin/python3

class Negetive(Exception):
	pass
	def oops():
		raise Negetive()	
try:
	num=int(input("Enter the number for check\n"))
	print ("The valid age of Phanindra is:{}".format(num))
	if num <0:
		print ("Calling oops")
		oops()

except ValueError:
	print ("Make sure you had entered an integer")
except Negetive: 
	print ("Please make sure you had type in a positive integer")
except:
	print ("Something went wrong")
finally:
	print ("Done Finally")

aa=Negetive()

