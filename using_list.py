#!/usr/bin/python3
#Filename:using_list.py

shoplist = ['apple', 'mikl', 'bread', 'eggs']
print("I have", len(shoplist), "items to buy.")
print("These items are:")
for item in shoplist:
    print(item, end=" ")

print("\n\nI also have rice to buy.")
shoplist.append('rice')
print("The new shoplist is:", shoplist)

print("\nI will sort my shoplist.")
shoplist.sort()
print("Sorted shoplist is:", shoplist)

print("\nThe first item I will buy is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought the", olditem)
print("The new shoplist is", shoplist)
