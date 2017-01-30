#!/usr/bin/python3
#Filename:class_init.py

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hello, this is", self.name)

name = input("Enter the name:")
p = Person(name)
p.sayHi()
