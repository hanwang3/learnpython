#!/usr/bin/python3
#Filename:backup_ver4.py

import os
import time

source = ['/home/ubuntu/python/if.py', '/home/ubuntu/python/var.py']
target_dir = '/home/ubuntu/python/backup/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input("Enter the comment ->")
if len(comment) == 0:
    target = today + os.sep + now + '.tar'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar'

tar_command = 'tar -cvf %s %s' %(target, ' '.join(source))

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully create directory", today)

if os.system(tar_command) == 0:
    print("Successfully tar to", target)
else:
    print("Tar Failed")

gzip_command = 'gzip -v %s' %target
if os.system(gzip_command) == 0:
    target = target +'.gz'
    print("Successfully gzip to", target)
else:
    print("gzip failed")
