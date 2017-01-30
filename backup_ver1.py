#!/usr/bin/python3
#Filename:backup_ver1.py

import os
import time

source = ['/home/ubuntu/python/if.py', '/home/ubuntu/python/var.py']
target_dir = '/home/ubuntu/python/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print("Successful backup to", target)
else:
    print("Backup Failed")
