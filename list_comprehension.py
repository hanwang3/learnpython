#!/usr/bin/python3
#Filename:list_comprehension.py

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)

liststree = []
for item in listone:
    if item > 2:
        liststree.append(item*2)      
print(liststree)
