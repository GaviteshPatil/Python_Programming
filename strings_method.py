#capitalize() is used to capitalize first letter of the string.
print("hello".capitalize())

#syntex:- center(width,fillchar)  Returns a string with the original string centered to a total of width columns and filled with fillchar in columns that do not have characters.
print("hello".center(7,"9"))

#syntex:- count(str,beg,end) 
string1="he"
message="helloworldhellohello"
print(message.count(string1,0,len(message)))

#sytex:- endswith(suffix,beg,end)
message1="She is my best friend"
print(message1.endswith("end",0,len(message1)))

#syntex:- startswith(prefix,beg,end)
string2="The world is beautiful"
print(string2.startswith("Th",0,len(string2)))

#syntex:- find(str,beg,end)
string3="She is my best friend"
print(string3.find("my",0,len(string3)))

#syntex:- index(str,beg,end) Same as find but raises an exception if str is not found
#difference between the find and index that find retrun -1 if str is not found but index method return ValueError in the program
string4="He is mine friend"
print(string4.index("mine",0,len(string4)))

#syntex:- rfind(str,beg,end) Same as find but starts searching from the end.
string5="Is this your bag ?"
print(string5.rfind("is",0,len(string5)))

#syntex:- rindex(str,beg,end) Same as rindex but start searching from the end and raises an exception if str is not found.
string6="Is this your bag?"
print(string6.rindex("your",0,len(string6)))

#syntex:- isalnum()
message2="JamesBond007"
print("Jamesbond007",message2.isalnum())
                                        #Programming tip:- The empty parenthteses means that this method takes no argument.
#syntex:- isalpha()
message3="JamesBond007?"
print("Jamesbond",message3.isalpha())

#syntex:- isdigit()
message4="007"
print(message4.isdigit())

#syntex:- islower()
message5="hello"
print(message5.islower())

#syntex:- isspace()
message6="   "
print(message6.isspace())

#syntex:- isupper()
print("HEllO".isupper())

#syntex:- len(str)
print(len("Hello"))

#syntex:- ljust(width[,fillchar])
print("Hello".ljust(10,"*"))

#syntex:- rjust(width[,fillchar])
print("Hello".rjust(10,"*"))

#syntex:- zfill(width) 
print("1234".zfill(10))

#syntex:- lower()
print("HELLO".lower())

#syntex:- upper()
print("hello".upper())

#syntex:- lstrip()
print("   Hello".lstrip())

#syntex:- rstrip()
print("Hello    ".rstrip())

#syntex:- strip()
print("   Hello  ".strip())

#syntex:- max(str)
print(max("hello friendz"))

#syntex:- min(str)
print(min("hello friendz"))

#syntex:- replace(old,new[,max])
message7="hello hello hello "
print(message7.replace("he","FO"))

#syntex:- title()
print("The world is beautiful".title())

#syntex:- swapcase()
print("The World Is Beautiful".swapcase())

#syntex:- split(delim)
print("abc,def,ghi".split(","))

#syntex:- join(list)
print('-'.join(['abc',"def","ghi"]))

#syntex:- isidentifier()
print("Hello0/".isidentifier)

#syntex:- enumerate(str)
print(dict(enumerate("Hello World")))