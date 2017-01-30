#!/usr/bin/python3
#Filename:func_global.py

def func():
    global x

    print("x =",x)
    x = 2
    print("x =",x)

x = 50
func()
print("x =",x)
