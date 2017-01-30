#!/usr/bin/python3
#Filename:func_local.py

def func(x):
    print("x =", x)
    x = 20
    print("x is changed to", x)

x = 50
func(x)
print("x is",x)
