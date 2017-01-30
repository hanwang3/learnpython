#!/usr/bin/python3
#Filename:method.py

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hello %s" %self.name)

p = Person('Allen')
p.sayHi()
