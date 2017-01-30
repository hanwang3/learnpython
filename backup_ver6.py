#!/usr/bin/python3
#Filename:backup_ver6.py

import os
import time

source = ['/home/ubuntu/learnpython/if.py', '/home/ubuntu/learnpython/var.py']
target_dir = '/home/ubuntu/learnpython/backup/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully make directory", today)

comment = input("Please comment ->")
if len(comment) == 0:
    target = today + os.sep + now + '.tar.gz'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

command = 'tar -cvzf %s %s' %(target, ' '.join(source))
if os.system(command) == 0:
    print("Successfully Backup to", target)
else:
    print("Failed to Backup")

print("Hello Linux & Python & Git & GitHub")
