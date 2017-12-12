#!/usr/bin/python3

ls=['abc','def',22,'_','\\','\n','_']
ks="!@#$_"
new_list=[]
for x in ls:
	if x == ks:
		ls.remove(x)
	else:
		new_list.append(x)

print(new_list)
#foobarbaz
