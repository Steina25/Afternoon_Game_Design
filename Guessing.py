#Aaron Stein
# create a word guess agme with 10 words
# pseudocode: provide instructions to user, one hint and the amount of words in the list, get guess. If correct congratulate. if not say you missed. if missed provide another hint. if correct congatulate if inncorect say, man wrong again and then provide third hint, if correct congatulate, if innocorect say you missed again, you are really bad at this, stop providing hits and give user unlimited guesses till correct 

from ctypes.wintypes import WORD
import random, datetime
import os 

os.system ('cls')
from time import sleep
seconds=.5

theWord=""

list1 = ["soccer","football","baseball","tennis","golf","lacrose"]
list2 = ["apple","dragon fruit","orange","lemon","lime","tomato","grapes"]
list3 = ["CPU","RAM","GPU","PSU","motherboard",]

Game=True
cnt=0
#a function is a section  the prram that we call when we need it
def hint():
    global cnt     #allow us to modify the variable all over the program
    if cnt ==0:
        print("|************************************************|")
        print("|              Here is a new hint                |")
        print("| look at the corresponding code to your gamemode|")
        print("|   1. this sport can be played on grass         |")
        print("|   2. just guess fruits, what hint do you want? |")
        print("|   3. guess the most important computer parts   |")
        print("|************************************************|")
        

    # guess2 = input("plese put your new guess here: ")
    # if guess2 == theword:
    #     print("Congrats, You got it")
    # else:
    #     print("wrong again, you are pretty bad at this, try again")
    elif cnt ==1:     #else if
        print("|*********************************************************|")
        print("|come on, you don't need another hint. Just guess it right|")
        print("|*********************************************************|")

    else:
        print("You just can't seem to get it right. oh well, keep guesiing")
    
    print()
def selectWrd(choice):  #is a function with a parameter
    global theWord
    if choice ==1:
        theWord= random.choice(list1)    
    if choice ==2:
        theWord= random.choice(list2)
    if choice ==3:
        theWord= random.choice(list3)
    return theWord  
name=input("What is your name? ")
high=0 #tfind highest score
while Game:
    
    print("|******************************************|")
    print("|            Guessing  Game !!             |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|           1.Sports                       |")
    print("|           2.Fruits                       |")
    print("|           3 Computer parts               |")
    print("|you will be given a hint after first guess|")
    print("|*******************************************")

# add user name, make it more personal y will need for keeping score
    


    print(name, end=", ")
    answer=input("Would you like to play this game? ")
    if 'n' in answer:
        break
    while True:
        choice=input("What game would you like to play 1, 2, or 3: ")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice>0 and choice <4:
                break
            else:
                print("give me 1,2,3")
        except:
            print("sorry")
    theWord = selectWrd(choice) #call to a function that will return a value
    #call function to select the word from the right list
    os.system('cls')
    check=True
    while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == theWord:
            print("Congrats, You got it")
            check=False
        else:
            hint()
        cnt+=1   # cnt= cnt + 1
        if cnt ==5:
            print("Sorry! the correct answer is")
            print(theWord)
    score=200-40*cnt
    if score > high:   # find highest sce
        high=score
    print(name+", your score is "+str(score))
    input("Press enter to play again, or exit")
    os.system('cls')
    print("---------------------------------")
    answer=input("Do you want to play again? ")
    if ('n' or 'N') in answer:
        Game=False
        print("Thank you for playing my game" )
    
    cnt=0 
print("your highest score is " + str(high))

hint1=input("1")

#if input == hint1:
    #print("|all sports can be played on grass")







#add highscore to file
# Add name and score 
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
sce=140
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