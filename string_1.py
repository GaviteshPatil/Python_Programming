#program to demonstrate string tranversal using indexing.
message="Hello!"
index=0
for x in message:
    print("message",[index],"=",message[index])
    index+=1
str6="Hello, welcome to the world  of python"
i=2
print(str6[i])      #index is an integer.
print(str6[i*3+1])  #index is an expression that evaluates to an integer.

#program to conacatenate two strings using + operator.
str1="Hello "
str2="World"
str3=str1+str2
print("The concatenated string is :",str3)

# program to demonstrate the appending in string datatype
s="Hello "
s+=input("\nEnter your name:- ")
s+=".Welcome to our program of the strings method."
print(s)

#program to demostrate the use of the "*" operator in the python programming to repeat the string .
s="Yellow \t"
print(s*5)

#we using the typecasting to convert one datatype into to another datatype to perform method on the specific datatype in python programmning.
c,i="True","False"
t=0
print("the type of the t is ",type(t))
j=str(t)+c+i
print(c,i,j,"The type of the t is now ",type(j))

#program to explain use of the raw "r" in the python .
print("\nHello")
print("jK",r"Hello\n")   #"r" is used to print the raw string .In raw string string is not executed in the special way ,even escape sequence charcter is not executed sepcially

# Note :- "U" prefix is used to write Unicode string literals.
print(u"Hello")
"""imp:- The unicode string is used to encoded the any symbol,letter,character,etc. from any language
   Unicode is a standard for encoding text that allows for the representation of diverse character sets, 
   including letters, digits, symbols, and even emojis.
   """
# Encoding
s = "Hello, world!"
b = s.encode('utf-8')
print(b)  # b'Hello, world!'

# Decoding
u = b.decode('utf-8')
print(u)  # Hello, world!

s = "Hello, world! 😊"
print(s)

print("😊".encode("utf-8"))

print(b'\xf0\x9f\x98\x8a'.decode("UTF-8"))

smiley = "\u263A"
print(smiley)  # ☺

print("The type of the emoji is ",type(b'\xf0\x9f\x98\x8a'))
print("The type of the emoji is ",type("\u263A"))

"""The string is the immutable character which means that once created they cannot be changed.
    Whenever you try to modify an existing string variable , a new string is created."""

#program to demostrate string references using the id() funciton

string1="Gavitesh"
print("String1 is ",string1)
print("The ID of the string1 is ",id(string1))
                                                    #id() returns the memory address of that object.
string2="Samyak"
print("String2 is ",string2)
print("The ID of the string2 is ",id(string2))

string1+=string2
print(string1)
print("The Id() of the string1 is ",id(string1))
string3=string2
print("The string3 is ",string3,"\nThe id of the string3 is ",id(string3))

#from the above program ,hence prove that the strings are immutable.

string4="Hi"
new_string4="Bi"
print("The Old string4 is ",string4,"\nThe new string is ",new_string4)

#Note :- We cannot delete or remove characters from a string . However, we can delete the entire string using the keyword del.

"""STRING FORMATTING OPERATOR 
SYNTEX:- "<Foramt>"% (<VALUES>)"""
Name,Age="Gavitesh",18
print("Name  of the person is %s and age of the person is %d ." %(Name,Age))
print("Name of the Girls is %s and her age was %d" %("Ankita",18))

"""Types of the formatting symbol .
    Format Symbol   Purpose
    %c              Character
    %d or %i        Signed decimal integer 
    %s              String 
    %u              Unsigned decimal integer
    %o              Octal integer
    %x or %X        Hexadecimal integer (x for lower case characters a-f and X for upper case characters A-F)
    %e or %E        Exponential notation 
    %f              Floating point number
    %g or %G        Short Numbers in floatinig point or exponential notation"""

#program to demonstrate the used of the string formatting operator in python .
i=1
print("i\ti**2\ti**3\ti**3\ti**4\ti**5")
while i<=10:
    print(i,"\t",i**2,"\t",i**3,"\t",i**4,"\t",i**5)
    i+=1


#program to surpass the above misalignedness in the above program using the string formatting operator
i=1
print("%-4s%-5s%-6s%-8s%-13s%-15s%-17s%-19s%-21s%-23s" % \
      ("i","i**2","i**3","i**4","i**5","i**6","i**7","i**8","i**9","i**10"))
while i <=10:
    print("%-4d%-5s%-6d%-8d%-13d%-15d%-17d%-19d%-21d%-23d" % (i,i**2,i**3,i**4,i**5,i**6,i**7,i**8,i**9,i**10))
    i+=1
#Note :- %-4d meaning of the program is the left align the character.

print("%-4d%-10s" % (3,"left"))
# Output: '3   left      '

print("%-4d%-2s print" % (3, "left"))
# Output: '3   left      '

#Note :- YOu don't need to type semi-colon aat the end of each line in python because python treats each line of code as a separate statement.

"""In the python programming the string is an object (object is an entity 
that contains both data as well as funtons to manipulate strings.)
Difference between the funtions and the method is that method is opration on object and funtion as you known."""

#program to demonstrate format() function.
string5="{},{} and {} ".format("Sun","Moon","Stars")
print("\n The default sequence of arguments is  : "+ string5)

string6="{1},{0} and {2} ".format("Sun","MOon","Stars")
print("\n The positional sequence of arguments (1,0 and 2 ) is :" +string6)

string7="{c},{b} and {a}".format(a="Sun",b="moon",c="stars")
print("\n The keyword sequence of arguments is : " + string7)

#program to demostrate the use of the splitlines in python programming
#syntex:- str.splitlines([keepends]) keepends syntex is optional.
print("Sun and \n\n Stars, Planets \r and Moon \r \n".splitlines())
print("Sun and \n\n Stars, Planets \r and Moon \r\n".splitlines((True)))

#program to demonstrate slice operation on string objects.
string8="PYTHON"
print("string8[1:5] = ",string8[1:5])  #characters starting at index 1 and extending up to but not including index 5
print("string8[:6]= ",string8[:6]) #defaults to the start of the string
print("string8[1:]]= ",string8[1:])     #defaults to the end of the string
print("string8[:] = ",string8[:]) #defaults to the entire string
print("string8[1:20] =",string8[1:20]) #an index that is too big is truncated down to length of the string

#Note :- Python does not have any separate date type for characters. They are represented as a single character string.

print("Negative indexing start")
#Program to understand how characters in a string are accessed using negative indexes.
string9="PYTHON"
print("string9[-1=",string9[-1])   #last character is accessed
print("string9[-6]= ",string9[-6])   #first character is accessed
print("string9[-2:] =",string9[-2:])   #second last and the last characters are accessed
print("string9[:-2]=",string9[:-2])     #all characters upto but not including second last character
print("string9[-5:-2] =",string9[-5:-2])   # characters from second upto second last are accessed.

#Elements are accessed from left towards right.
#For any index n,s[:n] + s[n:] = s.

#program to use slice operation with stride.
u="Welcome to the world of Python!!"
print("u[2:10] = ",u[2:10])   #default stride is 1
print("u[2:10:1] =",u[2:10:1])  #same as stride = 1
print("u[2;10:2] =",u[2:10:2])    #skips every alternative character
print("u[2:13:4] = ",u[2:13:4])    #skips every fourth character

#program to demonstrate splice opertion with just last (positive ) arguments.
t="Welcome to the world of Python"
print('t[::3] =',t[::3])

#program to demonstrate splice operation with just last (negative ) argument.
r="Welcome to the world of Python "
print("r[::-1] =",r[::-1])

#program to print the string in reverse thereby skipping every third character.
b="Welcome to the world of Python "
print("b[::-3] = ",b[::-3])

# program to demonstrate the ord() and chr() function in the python programming.
#ord() function returns the ASCII  code of the character
#chr() function returns character represented by a ASCII number.
ch=("R")
print(ord(ch))

print(chr(82))

print(chr(112))

print(ord("p"))

#program to represented the use of the membership operator (in or not in ) in python program.
t1="Welcome to the world of Python"
t2="the"
if t2 in t1: print('Found')
else : print("Not Found")

u1="This is a very good book"
u2="best"
if u2 not in u1: print("The book is very good but it may not be the best one.")
else: print("It is the best book.")

#You can also use the in and not in operator to check wheather a character is present is in a word. For example
print("u" in "stars","v " not in "Success" ,"vi" in "victory")

#Comparing of the string.
#We compare the string by using the relational operator and the comparision operator .
#For Example are :
string10,string11="Abc","abc"
print(string10==string11)
print(string10 <string11)
print(string10 <= string11)
print(string10 >= string11)
print(string10>string11)

#ITERATING THE STRING
#we can access the string character by using the while and for loop in python programming.
#for example are :
string12="Hello , my name is gavitesh arun patil . "
for x in string12:
    print(x,end=" ")

#for example by using the while loop are:
string12="Welcome to python programming."
ij=0
while ij<len(string12):
    print("\n",string12[ij],end="")
    ij+=1
