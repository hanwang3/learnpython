#!/usr/bin/python3
#Filename:using_file.py

poem = '''\
Programming is fun
When the work is done
If you wanna make your work fun
Using Python'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        print(line, end = '')
f.close()
