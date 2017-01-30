#!/usr/bin/python3
#Filename:func_return.py

def maximum(x, y):
    if(x > y):
        return x
    else:
        return y

x = int(input("x = "))
y = int(input("y = "))
val = maximum(x, y)
print(val)
