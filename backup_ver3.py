#!/usr/bin/python3
#Filename:backup_ver3.py

import os
import time

source = ['/home/ubuntu/python/if.py', '/home/ubuntu/python/var.py']
target_dir = '/home/ubuntu/python/backup/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input("Enter the comment-->")
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print("mkdir", today)

zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print("Successfully backup to", target)
else:
    print("Backup FAILED")
