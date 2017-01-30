#!/usr/bin/python3
#Filename:reference.py

shoplist = ['apple', 'orange', 'pear', 'banana']
mylist = shoplist

del shoplist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)

mylist = shoplist[:]
del mylist[0]
print("shoplist is", shoplist)
print("mylist is", mylist)
