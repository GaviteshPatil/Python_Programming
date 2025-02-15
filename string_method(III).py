#Program to demostrate the uses character to iterate
def copy(str):
    new_str=" "
    for i in str:
        new_str+=i
    return new_str
str1="Python"
print("\n The copied string is : ",copy(str1))
#to check wheather the string is new or old compare its id().
print(id(copy(str1)))
print(id(str1))

print("Program index of character to iterate.")
def copy1(str2):
    new_str=""
    for i in range(len(str2)):
        new_str+=str[i]
    return new_str
str2="Jython"
print("\n The copied string is : ",copy(str2))
#to check wheather the string is new or old compare its id().
print(id(copy(str2)))
print(id(str2))

print("PROGRAMMING EXAMPLES")

print("Program to print the following pattern in the python programming.")
for x in range(1,7):
    chr1="A"
    print()
    for j in range(1,x+1):
        print(chr1,end=" ")
        chr1=chr(ord(chr1)+1)
#If you don't understand the above program revise the ASII character code.

print("\n",chr(65))
print()
print(chr(ord("A")+1))
print(ord("A"))

print("Program to print the sequence of alphabete by using the for loop.")
ch="A"
for j in range(1,27):
    print(ch,end=" ")
    ch=chr(ord(ch)+1)
print()
print(ch)

print('Program to print below letter .')
c1='Z'
for j  in range(27,0,-1):
    print(c1,end=" ")
    c1=chr(ord(c1)-1)
print()

print("\n\n to print the below pattern.")
for j in range(27,0,-1):
    print(j,end=" ")

print("\n\nProgram that takes user's name and PAN card number as input.\nValidate the information using isX function and print the details.")
while True: 
    name="Om"
    if name.isalpha() == False:
        print("Invalid Name, Sorry you cannot proceed.")
        break
    else:
        pan_card_no = "ABCDE1234F"
        if pan_card_no.isalnum() == False:
            print("Invalid PAN card Number, Sorry you cannot proceed.")
            break
    print("Please check, "+name+" ,your PAN card number is : "+pan_card_no)
    break

print("\n\nProgram that encrypts a message by adding a key value to every character.(Caesar Cipher)")
#Hint : Say, if key =3 , then add 3 to every character .
message = "Teri M*A KI c***"
index =0
co=""
while index<len(message):
    letter =message[index]
    print(chr(ord(letter)+3),end=" ")
    co+=chr(ord(letter)+3)
    index+=1
print("\n",co)

print("\n\nProgram that uses split() to split a multiline string.")
letter="""Dear Students,
I am pleased to inform you that, 
there is a workshop on Python in college tomorrow.
everyone should come and 
there will also be a quiz in Python, whosoever wins 
will win a Gold Medal."""

print(letter.split("\n"))

print("\n\nProgram to generate an Abecedarian series.")
#Hint :- Abecedarian refers to a series or list in which the elements appear in alphabetical order.
l1="ABCDEFGH"
l2="ate"
for x in l1:
    print(str(x)+l2,end=" ")

print("\n\nProgram that accepts a string from user and redisplays the same string after removing vowels from it.")
def remove_vowels(s):
    new_str=""
    for i in s:
        if i in "aeiouAEIOU":
            pass
        else:
            new_str+=i
    print("The string without vowels is : ",new_str)
str="Welcome the Python programming ."
remove_vowels(str)

print("\n\nProgram that finds whether a given character is present in a string or not.In case it is present it prints the index at which it is present . Do not use built-in find functions to search the character.")
#Hint :- Index numbers allow us to access specific characters wihtin a string .
print()
def find_ch(s,c):
    index = 0
    while (index <len(s)):
        if s[index] == c:
            print(c,"Elment found at index :",index)
        else:
            pass
        index+=1
    print(c,"is not present in the string.")

s3="God is Great"
t="r"
find_ch(s3,t)

print("\n\nProgram that emulates the rfind function .")
#Hint :- The start and end parameters in find () and rfind() are optional.
def rfind_ch(s,c):
    index =len(s)-1
    while index>=0:
        if s[index] == c:
            return index
        index -=1
    return -1
string1="Let us study Python"
ch2="s"
index = rfind_ch(string1,ch2)
if index != -1:
    print(ch2," is found at location ",index)
else:
    print(ch2," is not present in the string .")

print("\n\nWrite a program that counts the occurrences of a character in a string. do not use built-in count function.")

def count_ch(s,c): # type: ignore
    count=0
    for i in s:
        if i==c:
            count+=1
    return count
str="Lovely flowers"
ch="e"
count=count_ch(str,ch)
print("In",str,ch,"occurs",count,"times")

print("\n\nModify the above program so that it starts counting from the specified location.")
def count_ch(s,c,beg=0):
    count = 0
    index =beg
    while index<len(s):
        if s[index] == c:
            count+=1
        index+=1
    return count

str="Good Going"
ch="o"
print("In",str,ch,"occurs ",count,"times from beginning to end")
loc=2
count=count_ch(str,ch,loc)
print("In",str,ch,"occurs",count,"times from position ",loc,"to end")

str="Welcome in the Python programming."
print(str[len(str):0:-1])

print("\n\nWrite a program to reverse a string.")
def reverse(str):
    new_str=""
    i=len(str)-1
    while i>=0:
        new_str +=str[i]
        i-=1
    return new_str
str="Welcome to the python programming part 2"
print("\n The reversed string is : ",reverse(str))

print("\n\nProgram to parse an email id to print from which email server it was sent and when.")
info ="From priti.rao@gmail.com Sun Oct 16  20:29:16 2016"
start = info.find("@") +1        # Extract characters after @symbol
end=info.find(".com") +4         # Extract till m, find returns index of m.
mailserver =info[start:end]      #Extract characters

start = end+1                    #Ignore whitespace
end=len(info)-1                  #Extract till last character
date_time =info[start:end]

print("The email has been sent through " +mailserver)
print("It was sent on " +date_time)

