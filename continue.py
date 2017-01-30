#!/usr/bin/python3
#Filename:continue.py

while True:
    s = input("enter something:")
    if s == "quit":
        break
    elif len(s) < 3:
        print("short")
        continue
    print("length is OK")

print("loop is over")
