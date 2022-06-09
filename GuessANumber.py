#Aaron Stein
# this code is about number guessing and it has multiple levels

from pdb import Restart
import random, datetime
import os
from tokenize import Number 

os.system('cls')

name=input("What is your name? ")

Game=True

#print(scrLine)
#create a file
#myFile = open("inst.txt", 'r')
#content = myFile.readlines()
#myFile.close()

cnt= 0

#Create new line
#REad the file
theNumber=""

list1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
list2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]
list3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]


#myFile = open("inst.txt", 'r')
#stuff=myFile.readlines()
#stuff.sort(reverse=True)
#myFile.close()
#for line in stuff:
   # print(line)

def selectWrd(choice):  #is a function with a parameter
    global theNumber
    if choice ==0: #side note. We spent 15 min in class trying to get this in a file and it never worked.
        print("|----------------------------------|")
        print("|-----------Instructions-----------|")
        print("|Welcome to my number guessing game|")
        print("|----------Select a level----------|")
        print("|--#1-------Level1: 1-25-----------|")
        print("|--#2-------Level2: 1-50-----------|")
        print("|--#3-------Level3: 1-100----------|")
        print("|When you guees you will get a hint|")
        print("|--Saying if the number is > or <--|")
        print("|----------------------------------|")
        input("What game would you like to play 1, 2, or 3: ")
        
    if choice ==1:
        #theNumber=random.randint(1, 25)
        theNumber= random.choice(list1)
    if choice ==2:
        #theNumber=random.randint(1, 50)
        theNumber= random.choice(list2)
    if choice ==3:
        #theNumber.randint(1, 100)
        theNumber= random.choice(list3)
    return theNumber  


print(name, end=", ")
answer=input("Would you like to play this game? ")
#if 'n' in answer:
    #break


while True:
        choice=input("Type 0 for instructions, or choose levels 1,2, or 3: ")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice >-1 and choice <4:
                break
            else:
                print("give me 0,1,2,3")
        except:
            print("sorry")
theNumber = selectWrd(choice)


high=0

#os.system('cls')
check=True
while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == theNumber:
            print("Congrats, You got it")
            check=False
        else:
            if guess > theNumber:
                print("the correct answer is LOWER than your guess")
            if guess < theNumber:
                print("the correct answer is HIGHER than your guess")
        cnt+=1   # cnt= cnt + 1
        if cnt ==5:
            print("Sorry! the correct answer is")
            print(theNumber)
score=200-40*cnt
if score > high:   # find highest sce
        high=score
print(name+", your score is "+str(score))
input("Press enter to play again, or exit")
#os.system('cls')
print("---------------------------------")
answer=input("Do you want to play again? ")
if ('n' or 'N') in answer:
        Game=False
        print("Thank you for playing my game" )
    
cnt=0 
print("your highest score is " + str(high))



#hint1=input("1")

#if input == hint1:
    #print("|all sports can be played on grass")


date=datetime.datetime.now()
print(date)
print(date.strftime("%m / %Y"))

sce= high

scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
#print(scrLine)
#create a file
myFile = open("scre.txt", 'w')
myFile.write(scrLine)
myFile.close()
#Create new line
name="Ronald"
sce=40
scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
#Append tyr file add lines tthe file
myFile = open("scre.txt", 'a')
myFile.write(scrLine)
myFile.close()
#REad the file
myFile = open("scre.txt", 'r')
stuff=myFile.readlines()
stuff.sort(reverse=True)
myFile.close()
for line in stuff:
    print(line)




































#|----------------------------------|
#|-----------Instructions-----------|
#|Welcome to my number guessing game|
#|----------Select a level----------|
#|--#3-------Level1: 1-25-----------|
#|--#3-------Level2: 1-50-----------|
#|--#4-------Level3: 1-100----------|
#|When you guees you will get a hint|
#|--Saying if the number is > or <--|
#|----------------------------------|