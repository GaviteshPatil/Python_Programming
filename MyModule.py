#Every Program is a module, that is , every file that you save as .py extension is a module.

#Note :- the below steps to making own modules
#First write these lines in a file and save the file as MyModule.py

def display():
    print("Hello")
    print("Name of called module is: ",__name__)

str = "Welcome to the world of Python !!! "

def large(a,b):
    if a<b:
        return b
    else:
        return a
print("Its in the part of the MyModule , name of the module is ",__name__)

def G_cap(s):
    """This program is used to capitalize the first alphabet of each word access from the sentence"""
    S=s.split()
    for x in S:
        print(x.capitalize(), end=" ")
