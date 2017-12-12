#!/usr/bin/python3 

num=int(input("Enter the number for prime check===>"))
if num>1:
    for x in range(2,num):
        if num%x==0:
            print (num,"is not a prime")
            print (num,"is",num//x,'times of',x)
            break
    else:
        print (num,'is a prime')
else:
    print (num,'is not a prime')    
