#!/usr/bin/python3
#Filename:module_using_sys.py

import sys

print("the command line arguments are:")
for i in sys.argv:
    print(i)

print("the pythonpath is ", sys.path)
