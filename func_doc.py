#!/usr/bin/python3
#Filename:func_doc.py

def printMax(x, y):
    '''Print the maximum of two number.

    The two values must be integers.'''

    x = int(x)
    y = int(y)

    if(x > y):
        print(x, " is the max")
    else:
        print(y, " is the max")

a = input("a = ")
b = input("b = ")
printMax(a, b)
print(printMax.__doc__)
help(printMax)
