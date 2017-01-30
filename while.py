#!/usr/bin/python3
#Filename:while.py
number = 23
running = True

while running:
    guess = int(input("Enter the number:"))

    if(number == guess):
        print("Congratulations you guess it")
        running = False
    elif(number < guess):
        print("the fact is high")
    else:
        print("the fact is low")

else:
    print("the loop is over")

print("Done")
