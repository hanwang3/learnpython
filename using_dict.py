#!/usr/bin/python3
#Filename:using_dict.py

#ab is short for 'a'ddress'b'ook
ab = {'Lilei': 'lilei@gmail.com',
      'Hanmeimei': 'hanmeimei@gmail.com',
      'Lily': 'lily@gmail.com',
      'Simon': 'simon@gmail.com'
     }

print("The address-book has %d items." %len(ab))

ab['Eta'] = "eta@gmail.com"
print("Eta's address is %s" %ab['Eta'])

del ab['Eta']
print("the addressbook is:")
for name, address in ab.items():
    print("Contact %s at %s" %(name, address))

if 'Simon' in ab:
    print("Simon's address is %s" %ab['Simon'])

