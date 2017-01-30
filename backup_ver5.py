#!/usr/bin/python3
#Filename:backup_ver5.py

import os
import time
import sys

source = []
target_dir = '/home/ubuntu/python/backup/'
source.append(sys.argv[1])
source.append(sys.argv[2])
print(source)

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully create directory", today)

comment = input("enter ->")
if len(comment) == 0:
    target = today + os.sep + now + '.tar.gz'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

command = 'tar -cvzf %s %s' %(target, ' '.join(source))
if os.system(command) == 0:
    print("Successfully backup to", target)
else:
    print("Backup FAILED")
    
