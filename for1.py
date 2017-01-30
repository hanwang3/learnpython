#!/usr/bin/python3
#Filename:for1.py

for i in range(1,10,2):
    if(i == 5):
        continue
    elif(i == 7):
        break
    else:
        print(i)
        
