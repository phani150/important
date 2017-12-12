#!/usr/bin/python3

import argparse

try:
        parser=argparse.ArgumentParser()
        parser.add_argument("-f","--number1",help="first number")
        parser.add_argument("-s","--number2",help="second number")
        parser.add_argument("operation",help="Do operation")

        args=parser.parse_args()
        print (args.number1)
        print (args.number2)
        print( args.operation)


        n1=int(args.number1)
        n2=int(args.number2)

        if args.operation=='add':
                result=n1+n2
        elif args.operation=='subtract':
                result=n1-n2
        elif args.operation=="mul":
                result=n1*n2
        print(result)
except:
	print ("something went wrong")                  
