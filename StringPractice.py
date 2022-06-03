# Aaror Stein
# Today we are learning strings

import os
os.system('cls')

print("hi")
message = "you are awesome"
# 0 1 2 3 4 5 6 7 8...
# y o u   a r e   a...
print(message)
print(message[5])

wordLenght = len(message)
print(len(message)) # len starts at 1 not 0
print(message[len(message)-1])

if message.isdligit(): # when using add a dot at end
   sum = message + 3   # if statement is true
else: # if statement is false
    print(message + "I say so") # concatination

print(message.upper())
print(message)

if message.isupper():
    print(message)

else:
    message = message.upper() # permanently change it to uppercase
    print(message)

num1 = 2.0
print(type(num1))
print(int(num1)) # to keep it a whole number

middle = int(wordLenght/2)
print(middle)
print(message[message])

print(message[0:7])
print(message[7:10]) # would say _Awesome

print(help(message.upper))