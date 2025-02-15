print("Program to demonstrate the use of match() function.")
import re 
string = "she sells sea shells on the sea shore"
pattern1= "sells"
if re.match(pattern1,string):
    print("Match Found")
else: print(pattern1, "is not present in the string")
pattern2 = "She"
if re.match(pattern2,string): print("Match Found")
else: print(pattern2,"is not present in the string")

print(help(re))
print(re.__doc__)
print(dir(re))

# Programming tip :- while using regular expressions, always use raw strings.
print("Program to demonstrate the use of search() function.")
string="She sells sea shells on the sea shore."
pattern="sells"
if re.search(pattern,string): print("Match Found")
else: print(pattern,"is not present in the string.")

print("Program to demonstrate the use of sub() function.")
string = "She sells sea shells on the sea shore"
pattern="sea"
repl="ocean"
new_string=re.sub(pattern,repl,string,1)
print("The new string was",new_string)

string1="hello hello print"
pattern1="hello"
repl="bye"
new_string=re.sub(pattern1,repl,string1,1)
print(new_string,"is the new string.")

print("Program to demonstrate the use of findall() function.")
pattern=r"[a-aA-Z]+ \d+"
matches=re.findall(pattern,"LXI 2013,VXI 2015,VDI 20104, Maruti Suzuki Cars in India")
for match in matches:
    print(match,end=" ")


print("\nProgram to demonstrate the use of finditer() function.")
import re 
pattern =r"[a-zA-Z]+ \d+"
matches=re.finditer(pattern,"LXI 2013,VXI 20104,Maruti suzuki cars availble with us")
for match in matches:
    print("Match found at starting index: ",match.start())
    print("Match found at ending index: ",match.end())
    print("Match found at starting and ending index : ",match.span())


print("Program to demonstrate the use of match() function.")
import re 
string ="She sells sea shells on the sea shore"
pattern1= "sells"
if re.match(pattern1,string):
    print("Match Found")
else:
    print(pattern1,"is not present in the string")
pattern2="She "
if re.match(pattern2,string):
    print("Match Found")
else:
    print(pattern2,"is not present in the string")

print(re.match(pattern1,string))
print(re.match(pattern2,string))
#in the code the line 110 gives you None .

string1="She sells sea shells on the sea shore"
pattern="sells"
if re.search(pattern,string1):
    print("Match Found")
else:
    print(pattern,"is not present in the string.")
print(re.search(pattern,string1))
print(re.search("sea",string1))
#On success.match() funciton returns an object representing the match, else returns None.

#Programming Tip: while using regular expressions, always use raw strings.

#NOte = The re.search() finds a match of a pattern anywhere in the string.

print("Program to demonstrate the use of sub() fucntion")
#syntex:- re.sub(Patttern, repl, string , max=0)
string2="She sells sea shells on the sea shore"
pattern="sea"
repl="ocean"
new_string=re.sub(pattern,repl,string2,1)

print(new_string)

#Program to demonstrate the use of findall() function.
pattern=r"[a-zA-Z]+ \d+"
matches=re.findall(pattern,"LXI 2013 , VXI 2015, VDI 20104, Maruti Suzuki Cars in India")
for match in matches:
    print(match,end=" ")

#Note = The re.findall() function returns a list of all substrings that match a pattern.

#Note = The finditer() function is same as findall() function but instead of returning match objects, it returns an iterator. This iterator can be used ot print the index of match in the given string.

print("\n Program to demonstrate the use of finditer() function.")
pattern=r"[a-zA-Z]+ \d+"

matches=re.finditer(pattern,"LXI 2013,VSI 2015,VDI 20104,Maruti suzuki Cars availble with us")
print(matches)
for match in matches:
    print("Match found at starting index : ",match.start())
    print("Match found at ending index : ",match.end())
    print("Match found at starting and ending index : ",match.span())

#Note = The match object returned by search(),match(),and findall() functions have start() and end() methods,that returns the string and ending index of  the first match.


print("Program to demonstrate the use of the Metacharacters and their Description an dUsage.")
# ^ =Matches at the beginning of the line . (Ex:- ^Hi ) (It will match Hi at the start of the string.)
string3="Hi , my name is the Gotham chess . Which was the popular  Grandmatster player of the chess.Login in the chess.com to make your game better.Login now . Hello my name is the Gavitesh Arun Pail."
pattern3=r"^Hi"
if re.search(pattern3,string3):
    print("Match found")
else:
    print(pattern3,"is not found in the given string.")

# $=Matches at the end of the line. (Hi$:- It will match Hi at the end of the string.) 

pattern4=r"Hi$"
if re.match(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")

# .=Matches any single character except the newline character.  (Lo.:- It will match Lot,Log,etc.)

pattern4=r"Lo."
if re.findall(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")
print(re.findall)

# [...]= Matches any single character in brackets. ([Hh]ello :- It will match "Hello" or "hello"
pattern4=r"[Hh]ello"
if re.findall(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")

# [^...]=Matches any single character in brackets. ([^aeiou]:- It will match anything other than a lowercase vowel.)

pattern4=r"[^aeiou]"
if re.findall(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")
print(re.findall(pattern4,string3))

# re*= Matches 0 or more occurrences of regular expression. ([a-z]* :- It will match zero or more occurrence of lowercase characters.)
pattern4=r"[a-z]*"
if re.findall(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")
print(re.findall(pattern4,string3))

# re+ = Matches 1 or more occurrenced of regular expression. ([a-z]+:- It will match one or more occurrence of lowercase characters)
pattern4=r"[a-z]+"
if re.findall(pattern4,string3): print("Match Found")
else : print(pattern4,"is not found in the given string.")
print(re.findall(pattern4,string3))

#Note :- difference between re* and re+ is the re* count the whitespace in the list and re+ does not count the whitespace in the list.

#re? = Matches 0 or 1 occurrence of regular expression . (Book? :- It will match "Book or "Books")
pname=r"Gavitesh?"
name="Gavitesh faGavitesh  Gaviteshs  gavitesh gAVITESH GAVI gavitsh"
if re.findall(pname,name): print("Match Found")
else : print(pattern4,"is not found in the given string.")
print(re.findall(pname,name))

# a|b = Matches either a or b. ("Hello"|"Hi " :- It will match hello or Hi.)
