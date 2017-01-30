#!/usr/bin/python3
#Filename:str_methods.py

name = "Allen Wang"

if name.startswith("Al"):
    print("Yes, this string is start with 'Al'")
else:
    print("this string is not start with 'Al'")

if 'W' in name:
    print("Yes, it contains the string 'W'")

if name.find("ang") != -1:
    print("Yes, it contains string 'ang'")

delimiter = "_*_"
mylist = ['China', 'Brazil', 'Russia', 'India']
print(delimiter.join(mylist))
