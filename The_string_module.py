import os
from socket import SO_KEEPALIVE


print("Program that uses different methods (upper,lower, split, join , count , replace ,and find) on string object.")
str="Welcome to the world of Python "
print("Uppercase - ",str.upper())
print("Lowercase - ", str.lower())
print("Split - ",str.split())
print("Join - ",'-'.join(str.split()))
print("Replace - ",str.replace("Python","Java"))
print("Count of  o - ",str.count('o'))
print("Find of  - ",str.find("of"))

#Programming Tip : A method is called by appending its name to the variable name using the period as a delimiter.


#hackerrank capitalize
s="Gavitesh patil 123ur"
for x in s.split():
    s=s.replace(x,x.capitalize())
print(s)

#hackerrank "Find String"
print("\n\nProgram to find the substring from main string.")
def sub_string(s, ss):
    count = 0
    sub_len = len(ss)
    
    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == ss:
            count += 1
            
    return count
print(sub_string("ABCDCDC","CDC"))


s="ABCDCDC"
ss="CDC"
sub_len=len(ss)

for i in range(len(s)-sub_len + 1):
    print(i,end="")

print(len(s)-(sub_len+1))

#Copying and Pasting Strings with the Pyperclip Module.


print("\n\nA method is called by appending its name to the variable name using the period as a delimiter.")


print("\n\nProgram that displays the type  of an item in the string module.")
import string 
print(type(string.digits))

print(type(string.ascii_letters))

print("\n\nProgram that displays the type of an item in the string module.")
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.printable)
print(string.punctuation)
print(string.whitespace)

print("\n\nProgram to print the docstring of an item in string module.")
print(string.__builtins__.__doc__)
print(string.__doc__)
print(string.ascii_uppercase.__doc__)

print("\n\nProgram using help()")
str="Hello"
print(help(str.isalpha))

# Programming Tip :- Passing '\n' in split() allows us to split the multiline string stored in the string variable.

print("\n\nWORKING WITH CONSTANTS IN STRING MODULE")
#First Way 
# print(string.find(string.ascii_lowercase,'g') != -1)

#Second Way 
print("g" in string.ascii_lowercase)

#Third Way 
ch="g"
print("a" <= ch <= "z")

#Note :- Type()  shows the type of an object and the dir() shows the available methods.
print(dir(string))

print(string.whitespace.split("\n"))

import string
print(string)

import pyperclip
print(dir(pyperclip))
print(pyperclip.__doc__)
print(help(pyperclip))

pyperclip.copy("Welcome to the world of Python !!! ")
pyperclip.paste()
"Welcome to the world of Python !!!"
print(pyperclip.paste())

#Note :- After copying your Python text, if you copy something outside of your program, then the contents of the clipboard will change and the paste() function will return it.

print("hello \n\n")
print(string.whitespace)



