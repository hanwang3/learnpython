#!/usr/bin/python3
#Filename:if.py

number = 23
guess = int(input("Enter number:"))

if(guess == number):
    print("Congratulation you guess it!")
    print("(But you can\'t get any prizes)")
elif(guess < number):
    print("it is higher than that")
else:
    print("it is lower than that")

print("Done")

