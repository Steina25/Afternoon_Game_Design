#Aaron Stein
#This code is a game for multiple lists game

import random
import os
from secrets import choice
from tabnanny import check 

os.system ('cls')
from time import sleep
seconds=.5

count = 0
Game = True
theword = ""

def hint(): # allows us to reuse code in multiple spots
    global count
    if count == 0:
        print("|-------------------------------------|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|-------------------------------------|")
        
    elif count == 1:
        print("|--------------------------------------|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|--------------------------------------|")
    
    else:
        print("You are horrible at guessing, no more hints, go till you get it right")
    

def option1():
    global count
  
    check = True
    count = 0
    list = [""]
    theword=random.choice(list)
    while check and count <5:
        guess=input("plese put your guess here: ")
        if guess == theword:
            print("Congrats, You got it")
            check = False

        count += 1

def option2():
    global count
    
    check = True
    count = 0
    list = ["red", "blue", "yellow", "green", "orange", "purple", "indigo", "black", "white", "brown"]
    theword=random.choice(list)
    while check and count <5:
        guess=input("plese guess a color here: ")
        if guess == theword:
            print("Congrats, You got it")
            check = False
        count += 1

def option3():
    global count
    os.system('cls')
    check = True
    count = 0
    list = ["CPU","GPU","Motherboard","PSU","Hardrive","Heatsink","CPU cooler","RAM",]
    theword=random.choice(list)
    while check and count <5:
        guess=input("plese put your guess here: ")
        if guess == theword:
            print("Congrats, You got it")
            check = False
        count += 1

while Game:
    print("|-----------------------------------------|")
    print("|Guess The Animal, Sport, or Computer part|")
    print("|-----------------------------------------|")
    print("| 1. Animals                              |")
    print("| 2. Sports                               |")
    print("| 3. Computer Parts                       |")
    print("|    Firstly, you will be given a hint    |")
    print("|             Your Hint Is                |")
    print("|-----------------------------------------|")

    
    name = input("What is your name? ")
    print(name, end = ", ")
    answer = input("would you like to play the game? ")
    answer = answer.lower()
    if 'n' in answer:
        Game = False
        break

    while True:
        choice = input("What game would you like to play 1,2, or 3? ")
        try:
            choice = int(choice)
            if choice > 0 and choice < 4:
                break
            else:
                print("give me 1,2, or 3")
        except:
            print("Plese enter a number")

    if choice == 1:
        option1()
    elif choice == 2:
        option2()
    elif choice == 3:
        option3()

    os.system('cls')
    answer = input("Do you want to play again? ")
    if ('n' or 'N') in answer:
        Game = False
        print("Thank you for playing")