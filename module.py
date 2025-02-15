#program to show the use of from.. import statement.
from math import pi
print("PI =",+pi)

#This imports * statement imports alll names except those beginning with an underscore(_).

#program to show the use of ' as ' keyword
from math import sqrt as square_root
print(square_root(81))

""" Python allows you to pass command line arguments to your program . This can be done using the sys module . The argv 
variable in this module keeps a tarack of command a track of commmand line arguments passed to the .py script as shown below."""

import sys 
print(sys.argv)

#program to add two numbers that are given using command line arguments. 
       # import sys
       # a=int(sys.argv[1])
       # b=int(sys.argv[2])
       # sum=a+b
       # print("Sum= ",sum)

#program to demonstrate sys.exit
      # import sys
      # print("HELLO WORLD")
      # sys.exit("Error Message")

#Note :- Every module has a name. You can find the name of a module by using the __name__ attribute of the module

#program to print the name of the module in which your statements is written 
print("Hello")
print("Name of the module is : ",__name__)

import MyModule 
print("MyModule str = ",MyModule.str)
MyModule.display()
print("Name of calling module is : ",__name__)

#Note :- Modules should be placed in the same directory as that of the program in which it is imported. It can also be stored in one of the directories listed in sys.path.
#Note :- we have been using the dot operator to access members (variables or functions) of the module.
#Note :- Assumin taht MyModule had many other variables or functions definition , we could have specifically imported just str and display() by writing the import statement as 


    #  from MyModule import str ,display


#program that defines a function large in a module which will be used to find larger of two values and called from code in another module
from MyModule import large
print("Large(50,100) = ",large(50,100))

#program used to understnd the funtion of dir() in module.
print(dir())
#dir() is used to known the identifiers present in the current program or module.

#example on dir()
# import sys
# print(dir(sys))
# # comment out the line 57,58,60,61 to see the huge number of identifiers in the sys , builtins module.
# import builtins
# print(dir(__builtins__))


#by convention, modules are named using lowercase letters and optional underscore characters.


#program that prints absoulet value , square root, and cube root.
import math
a=-100
def cube(a):
    c=a**3
    return c

print("abs(a)=",abs(a))
print("Square root of the a is ",math.sqrt(abs(a)))
print("cube root of the is ",cube(a))

#programming tip := always import any object from the module if you want to add in the program .

#program is used to demonstrate the used of the random.randint module in python .
import random
for x in range(1,21):
    value=random.randint(1,100) #it used to get the random value from the list and data type
    print(value,end=" ")

#program to demostrate the use of the time module show the time and date in the current program.
import time
local_time=time.asctime(time.localtime(time.time()))
print("\nThe local time :-",local_time)

import calendar
print(calendar.month(2024,7))

#write the program to demonstrate the use of the getpass() module to prompt the user for a password ,without echoing what they type to console.
import getpass 
password=getpass.getpass("Enter your password:- ")
if password == "oxygen":
    print("Welcome to your program .")
else:
    print("Incorrect password , please write down the correct password.")

#program to demonstrate the redefination of the funtion .
import datetime 
def speech(a):
    print(a)

print(speech("Hello"))
def speech(a):
    print(a)
    now=str(datetime.datetime.now())
    print(now)

