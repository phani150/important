#!/usr/bin/python3

# Function definition is here
#mylist=[55,66,77,88]
def changeme( mylist ):
   "This changes a passed list into this function"
   global mylist
   mylist=[11,22,33,44]
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
