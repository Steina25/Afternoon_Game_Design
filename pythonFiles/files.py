#Aaron Stein
# This code is notes about using files, datetime
# 'r' read 
# 'a' append 
# 'w' write  
# open a file and make sure you close
# datetime
import random
import os, datetime

os.system('cls')

date=datetime.datetime.now()
print(date)
print(date.strftime("%m-%d-%Y"))

name="Aaron"
sce=344
scrLine=str(sce)+"\t "+name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
#print(scrLine)
#create a file
myFile = open("scre.txt", 'w')
myFile.write(scrLine)
myFile.close()
#Create new line
name="Peter"
sce=132
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