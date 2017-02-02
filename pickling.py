#!/usr/bin/python3
#Filename:pickling.py

import pickle as p

shoplistfile = 'shoplist.data'
shoplist = ['tomato', 'mango', 'potato']

f = open(shoplistfile, 'wb')
p.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storelist = p.load(f)
print(storelist)
