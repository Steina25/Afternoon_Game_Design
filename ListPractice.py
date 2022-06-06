#Aaron Stein
#we will learn lists, list functios, and methods, add elements

import os
import random
os.system

# A list is an array index, it is changeable, and sizeable
# name use []

mylist=[1,2,3,4,5]
#       0 1 2 3 4
#          -3 -2 -1
print(mylist)
print(mylist[1]) # will print elem in position 1
print(mylist[1:3]) # print elements 1,2
print(mylist[-1])
print(mylist[-3:-1]) #print third and forth to the left
print(mylist[-3:]) #print last three

myfruits= ["apple","banana","kiwi","papaya"]
print(myfruits[:3])
lenghtlist=len(myfruits) #number elements is always one less than your last index
#print(lenghtlist)
#print(myfruits[lenghtlist-1])
#print(myfruits[0])
#print(myfruits[1])
#print(myfruits[2])
# for loop repeats specific number of times
for elem in myfruits:
    print(elem) # control the loop
    
for elem in range(lenghtlist):
    print(myfruits[elem])
    print (elem, ennd="")
    print(myfruits[elem])
if "apple" in myfruits:
    print("yes apple is in the list")

myfruits.append("pineapple") # append only and add elements to edn of list
print(myfruits[0:1])

myfruits.insert(0, "orange") # insert index where u want the element to go
print(myfruits[0:])

print(mylist)
mylist.extend(myfruits)
print(mylist)

mylist=[1,2,3,4,5]
print(mylist)
mylist.append(myfruits)
print(mylist[5])
print(mylist[5][1])

#myfruits[1] = "hi"
print(myfruits)

for i in range(0):
    element = random.choice(myfruits)
    print(element, end = "")

element = random.choice(myfruits)
print(element)

guess = input("Insert a Sport")
if guess.lower() == element.lower():
    print("Your guessed correctly")

#print("*******************")
#print("*       tittle      *"")
#print("*       Instructions1   *")
#print("*       Instructions2   *")
#print("*******************") 





