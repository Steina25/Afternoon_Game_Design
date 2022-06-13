# Aaron Stein
# This code is my first game.
#Start
#Input: (hint about soprt)
#process: type the answer in
#output: if correct say "good job" if incorrect say "try again"
#End

import os
import random
os.system ('cls')

print("---------------------------")
print("Types of Sports Games")
print("----Instructions----")
print("You will be given a")
print("question about sports")
print(" and you will need to")
print("type the correct answer.")
print("Keep answers in lowercase")
print("---------------------------")

#mysports= ["Soccer","Basketball","Football","Baseball","Tennis","Hockey","Golf","Volleyball","Track","Swimming"]
#           0           1           2           3           4       5       6         7         8         9

#myhints= ["Sport that you kick a ball","Sport that you shoot a ball into a basket","Sport that you can score a touchdown","You use a bat and glove","you use a green fuzzy ball","you use a puck and stick","you use clubs and a white ball","position called libero","you run fast","you dive into water" ]

#mysports = myhints 

QUESTION1 = input ("A sport that you kick a ball: Answer Here: ")
if QUESTION1 == ("soccer"):
    print("Correct!")

if QUESTION1 != ("soccer"):
    print("Sorry, try again next time.")

QUESTION2 = input ("A sport that you shoot a ball into a basket: Answer Here: ")
if QUESTION2 == ("basketball"):
    print("Correct!")

if QUESTION2 != ("basketball"):
    print("Sorry, try again next time.")

QUESTION3 = input ("Sport that you can score a touchdown: Answer Here: ")
if QUESTION3 == ("football"):
    print("Correct!")

if QUESTION3 != ("football"):
    print("Sorry, try again next time.")

QUESTION4 = input ("You use a bat and glove: Answer Here: ")
if QUESTION4 == ("baseball"):
    print("Correct!")

if QUESTION4 != ("baseball"):
    print("Sorry, try again next time.")

QUESTION5 = input("you hit a green fuzzy ball with a racket: Answer Here: ")
if QUESTION5 == ("tennis"):
    print("Correct!")

if QUESTION5 != ("tennis"):
    print("Sorry, try again next time.")

QUESTION6 = input ("you use a puck and stick: Answer Here: ")
if QUESTION6 == ("hockey"):
    print("Correct!")

if QUESTION6 != ("hockey"):
    print("Sorry, try again next time.")

QUESTION7 = input("you use clubs and a white ball: Answer Here: ")
if QUESTION7 == ("golf"):
    print("Correct!")

if QUESTION7 != ("golf"):
    print("Sorry, try again next time.")

QUESTION8 = input ("there is a position called libero: Answer Here: ")
if QUESTION8 == ("volleyball"):
    print("Correct!")

if QUESTION8 != ("volleyball"):
    print("Sorry, try again next time.")

QUESTION9 = input ("you run fast: Answer Here: ")
if QUESTION9 == ("track"):
    print("Correct!")

if QUESTION9 != ("track"):
    print("Sorry, try again next time.")

QUESTION10 = input ("you dive into water: Answer Here: ")
if QUESTION10 == ("swim"):
    print("Correct!")

if QUESTION10 != ("swim"):
    print("Sorry, try again next time.")

#list1 = [QUESTION1,QUESTION2]

#element = random.choice(list1)
#print(element)

QUESTION4 = input ("You use a bat and glove: Answer Here: ")
if QUESTION4 == ("baseball"):
    print("Correct!")

if QUESTION4 != ("baseball"):
    print("Sorry, try again next time.")

QUESTION7 = input("you use clubs and a white ball: Answer Here: ")
if QUESTION7 == ("golf"):
    print("Correct!")

if QUESTION7 != ("golf"):
    print("Sorry, try again next time.")

QUESTION5 = input("you hit a green fuzzy ball with a racket: Answer Here: ")
if QUESTION5 == ("tennis"):
    print("Correct!")

if QUESTION5 != ("tennis"):
    print("Sorry, try again next time.")

QUESTION9 = input ("you run fast: Answer Here: ")
if QUESTION9 == ("track"):
    print("Correct!")

if QUESTION9 != ("track"):
    print("Sorry, try again next time.")

QUESTION8 = input ("there is a position called libero: Answer Here: ")
if QUESTION8 == ("volleyball"):
    print("Correct!")

if QUESTION8 != ("volleyball"):
    print("Sorry, try again next time.")



#for i in range(0):
    #element1 = random.choice(myhints)
    #print(element1, end = "")

#for i in range(0):
    #element2 = random.choice(mysports)
    #print(element2, end = "")

#element2 = random.choice(mysports)
#print(element2)

#guess = input("Insert a Sport: ")
#if guess.lower() == element2.lower():
    #print("Your guessed correctly!")

#if guess.lower() != element2.lower():
    #print("Better luck next time! That was incorrect")
