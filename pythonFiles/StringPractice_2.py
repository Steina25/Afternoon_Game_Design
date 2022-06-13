# Aaron Stein
# Use strings to type "jms" for the name james

import os
os.system('cls')

message = "james"

print(message[0],end="") # first letter

wordlenght= len(message)
middle = int(wordlenght/2) # second letter or middle letter

print (message[wordlenght-1]) # final letter

# 1B Case 1
message2= "JhonDipPeta"

print(message[4],end="") 
# D

wordlenght2= len(message2)
middle2 = int(wordlenght2/2) 
# middle of word is i
print (message2[middle2], end="")

print (message2[6]) # final letter

# 1B Case 2
message3 = "JaSonAy"
print (message3[2], end="")

wordlenght3= len(message3)
middle3 = int(wordlenght3/2)
print (message3[middle3], end="")

print (message[4],end="")

#2 

string4= "Ault"
string5= "Kelly"
wordlenght4 = len(string4)
middle4 = int(wordlenght4/2)
print(string4[0:middle4]+string5+string4[middle:])

#3

string6 = "America"
string7= "Japan"

message10 = string6

message11 = string7

wordlenght5 = len(string6)
middle5 = int(wordlenght/2)

middle5 = int(wordlenght5/2)

print(message10[0],end="")
print(message11[0],end="")

print(message10[middle],end="")
print(message11[middle],end="")

#4

string8 = "PYnAtivE"

print (string8[1],end="")

wordlenght6=len(string5)
middle6 = int(wordlenght6/2)
print (string8[middle6 -1],end="")
print (string8[middle6 +1],end="")

print (string8[0],end="")
print (string8[2],end="")
print (string8[middle6],end="")

