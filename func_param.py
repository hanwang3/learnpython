#!/usr/bin/python3
#Filename:func_param.py

def printMax(a,b):
    if(a>b):
        print(a,"is the maximum")
    else:
        print(b,"is the maximum")
        
x = int(input("x = "))
y = int(input("y = "))
printMax(x,y)
