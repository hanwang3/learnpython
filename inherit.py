#!/usr/bin/python3
#Filename:inherit.py

class SchoolMember:
    '''Represents any school members'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember is: '%s'" %self.name)

    def tell(self):
        print("Name: '%s'\nAge: '%s'" %(self.name, self.age))


class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: '%s'" %self.name)

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: '%d'" %self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
        print("Initialized Student: '%s'" %self.name)

    def tell(self):
        SchoolMember.tell(self)
        print("Score: '%d'" %self.score)

Allen = Teacher('Allen', 28, 200000)
Simon = Student('Simon', 17, 90)

for member in [Allen, Simon]:
    member.tell()
