# Aaron Stein
# from ctypes.wintypes import WORD
from itertools import count
from pickle import TRUE
import random
import os
from tkinter import END 

os.system ('cls')
from time import sleep
seconds=.5

list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
theword=random.choice(list)
print("|***************************************|")
print("|         Guess The Animal!!!           |")
print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
print("|          1.Instructions               |")
print("|   There are 10 animals in this game   |")
print("|     You must guess one of them        |")
print("|First we will provide you with one hint|")
print("|           !Your Hint Is!              |")
print("|  These animals are big fans of water  |")
print("|***************************************|")


name = input("What is your name? ")
print(name, END ==", ")
answer = input("Would you like to play the game? ")
answer = answer.lower()
if 'n' in answer:
    Game = False
    #break

#while True:
    #choice= input("What game would you like to play")

os.system('cls')
guess1=input("plese put your guess here: ")
if guess1 == theword:
    print("Congrats, You got it")
else:
    print("you missed it, try again")

def hint(): # alows you to use code in multiple places
    global count
    if count == 0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        count += 1

guess2 = input("plese put your new guess here: ")
if guess2 == theword:
    print("Congrats, You got it")
else:
    print("wrong again, you are pretty bad at this, try again")
if count == 1:

    print("|**************************************|")
    print("|       Here is your final hint        |")
    print("|  These creatures almost never move   |")
    print("|**************************************|")
else:
    print("you are terrible at guessing")
guess3 = input("plese put your final guess here: ")

if guess3 == theword:
    print("Congrats, You got it")
else:
    print("You are horrible at guessing, no more hints, go till you get it right")

while True:
    ans = input("plese put your guess here: ")
    if ans == theword:
        name = True 
        print("Congrats, You got it")
        break 
    else:
        print("wrong again, try again")

