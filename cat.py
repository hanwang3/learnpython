#!/usr/bin/python3
#Filename:cat.py

import sys

def readfile(filename):
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            print(line)
    f.close()

if len(sys.argv) < 2:
    print("No specified action")
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print("Version 1.0")
    elif option == 'help':
        print('''\
This program prints files to the standard output
Any number of files can be specified
Option includes:
--version: Print the version number
--help:    Display the help''')
    else:
        print("Unknown option")

else:
    for filename in sys.argv[1:]:
        readfile(filename)
