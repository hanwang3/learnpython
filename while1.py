#!/usr/bin/python3
#Filename:while1.py

running = True
while running:
    s = input("Enter the string:")
    if(s == "zzz"):
        print("error, continue")
        continue
    elif(s == "quit"):
        print("quit")
        break
    elif(s == "abc"):
        running = False
    else:
        print(s)
else:
    print("the loop is over")
