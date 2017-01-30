#!/usr/bin/python3
#Filename:objvar.py

class Person:
    '''Represents a person'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data'''
        self.name = name
        print("(Initializing %s)" %self.name)
        Person.population += 1
    
    def __del__(self):
        '''I am dying'''
        print("%s says bye" %self.name)
        Person.population -= 1

        if Person.population == 0:
            print("I am the last one")
        else:
            print("There are still %d persons left" %Person.population)

    def sayHi(self):
        print("Hi, my name is %s" %self.name)

    def HowMany(self):
        if Person.population == 1:
            print("I am the only person")
        else:
            print("There are %d persons here" %Person.population)

Allen = Person('Allen')
Allen.sayHi()
Allen.HowMany()

Simon = Person('Simon')
Simon.sayHi()
Simon.HowMany()

Allen.sayHi()
Allen.HowMany()
