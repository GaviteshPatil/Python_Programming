#Programming Tip:- Using a mutable object as a dictionary key causes a TypeError
#syntax:- dictionary_name={key_1:value_1 , key_2:value_2}

#If there are many keys and values in dictionaries , then we can also write just one key-value pair on a line to make the code easier to read and understand .

#Remember that dictionaries are not sequences,rather they are mappings .Mapping are collections of objects that store objects by key instead of by relative position.

"Note:- Dictionary keys are case-sensitive .Two keys with the same name but in different case are not the same in Python."


#Creating a Dictionary

Dict={}
print(Dict,type(Dict))

Dict={'Roll_No' : '16/001','Name':'Arav','Course':'BTech'}
print(Dict)

#Programming Tip:- Hash table is an array whose indexes are obtained using a hash function on the keys .A hash function distrubutes the keys evenlly in the array and minimizes collisions.

print(dict([('Roll_No','16/001'),('Name','Arav'),('Course','BTech')]))

#syntax for creating the list comprehension :- D={expression for variable in sequence [if condition]}

#Note:- The expression generates elements of dictionary from items in the sequence that satisfy the condition.

print("\nProgram to create 10 key-values pairs where key is number in the range 1-10 and the value is twice the number.\n")
Dict={x : 2*x for x in range(1,10)}

print("\n\nACCESSING VALUES \n\n")

print('\nProgram to access values stored in a dictionary.\n')

Dict={'Roll_No':'16/001','Name':'Arav','Course':'Btech'}
print("Dict[Roll_No] = ",Dict['Roll_No'])
print("Dict[Name] = ",Dict['Name'])
print("Dict[Course] = ",Dict['Course'])

#Programming Tip:- Collision means two or more keys pointing to the same location.

print("\n\nADDING AND MODIFYING A iTEM IN A DICTINARY \n\n")

#syntax to add element in the existing dictionary :- dictionary_variable[key] = val

print('\nProgram to add a new item in the dictionary \n\n')
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print('Dict[Roll_No] = ',Dict['Roll_No'])
print('Dict[Name] = ',Dict['Name']  )
print('Dict[Course] = ',Dict['Course'])
Dict['Marks'] = 95 #new entry
print("Dict[Marks] = ",Dict['Marks'])

#Programming Tip: Trying to index a key that isn't part of the dictionary returns a KeyError

print("\n\nMODIFYING AN ENTRY \n\n")
print('\nProgram to modify an item in the dictionary.\n')
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[Roll_No] = ",Dict['Roll_No'])
print('Dict[Course] = ',Dict['Course'])
Dict['Marks'] = 95 #new entry
print("Dict[Marks] = ",Dict['Marks'])

Dict['Course'] = 'BCA'
print("Dict[Course] = ",Dict['Course']) #entry updated

#Note:- Dictionary is an associative array also known as hashes since any key of the dictionary can be associated or mapped to a value
#syntax for delete item from the dictionary variable :- del dictionary_varible[key]

print('\nProgram to demonstarte the use of del statement and clear() function.\n')
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[Roll_No] = ",Dict['Roll_No'])
print("Dict[Name] = ",Dict['Name'])
print('Dict[Course] = ',Dict['Course'])
del Dict['Course']  #deletes a key-value pair
print('After deleting course : ',Dict)
Dict.clear()  #deletes all entries 
print('After clear(),Dictionary has no items : ',Dict)
del Dict #deletes the varible Dict from memory
print("Dict does not exist .......")

#Programming Tip:- Only immutable objects can be used as keys to dictionaries.

#syntax for using the pop() method to delete a particular key from the dictionary.

#syntax:- dict.pop(key[,default])

print("\nProgram to randomly pop() or remove an element from a dictionary.\n")
Dict={'Roll_No':'16/007','Name':'Arav','Course':'BTech'}
print("Name is : ",Dict.pop('Name'))   #returns Name)
print("Dictionary after popping Name is : ",Dict)
print("Marks is : ",Dict.pop("Marks ", -1))  #returns default value
print("Dictionary after popping Marks is : ",Dict)
print("Randomly popping any item : ",Dict.popitem())
# print("Aggregate is : ",Dict.pop('Aggr'))  #generates error
print("Dictionary after popping Aggregate is : ",Dict)


print("\nProgram to illustrate the use of duplicate keys in a dictionary.\n")
Dict={'Roll_No':'16/007','Name':'Arav','Course':'BTech','Name':"Kriti"}
print("Dict[Roll_No ]= ",Dict['Roll_No'])
print("Dict[Name]= ",Dict['Name'])
print("Dict[Course] = ",Dict['Course'])

print("\n\nProgram to illustrate the use of mutable keys in a dictionary.\n")
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[Roll_No] = ",Dict['Roll_No'])
print("Dict[Name] = ",Dict['Name'])
print("Dict[Course] = ",Dict['Course'])

#Programming tip:- In Python 'None' is a spcial value like null or nil which means no value

print('\nProgram to check single key in a dictionary.\n')
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
if 'Course' in Dict: print(Dict['Course'])

#Programming Tip:- A KeyError occurs on an invalid access of a key like when a key that is used is not present in the dictionary.

print("\n\nSORTING ITEMS IN A DICTIONARY \n\n")
print("\nProgram to sort keys of a dictionary.\n")
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(sorted(Dict.keys()))

print("\n\nLOOPING OVER A DICTIONARY \n\n")
print('\nprogram to access items in a dictionary using for loop.\n')
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Keys : ",end=" ")

for key in Dict:
    print(key,end=" ")  #accessing only keys 
print('\nValues : ',end=" ")

for val in Dict.values():
    print(val,end=" ")  #accessing only values 

print('\nDictionary : ',end=" ")
for key , val in Dict.items():
    print(key,val,'\t',end=" ")  #accessing keys and values 

print('\n\nNESTED DICTIONARIES \n\n')

print('\n\nProgram to illurate nested dictionary (i.e.., use of one dictionary inside another.)')
Students = {'Shiv':{'CS':90,'DS':89,'CSA':92},
            'Sadhvi':{'CS':91,'DS':87,'CSA':94},
            'Krish':{'CS':93,'DS':92,'CSA':88}}

print("\n\nBUILT DICTIONARY FUNCTIONS AND METHODS \n\n")

#syntax:- len(Dict)
#description:- Returns the length of dictionary.That is number of items (key-value pairs)
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(len(Dict1),"\n")

#syntax:- str(Dict)
#description :- Returns a string representation of the dictionary
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(str(Dict1),"\n")

#syntax:- Dict.clear()
#description:- Deletes all entries in the dictionary
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
# print(Dict1.clear())
print(Dict1,"\n")

#syntax:- Dict.copy()
#description:- Returns a shollow copy of the dictionary i.e., the dictionary returned will not have a duplicate copy of Dict but will have the same reference 
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict2=Dict.copy()
print('Dict2 : ',Dict2)
Dict2['Name']= 'Saesha'
print('Dict1 after modification: ',Dict1)
print(Dict2,"\n")
print(id(Dict1)==id(Dict2))
print()

#syntax:- Dict.fromkeys(seq[,val])
#description:- Create a new dictionary with keys from seq and values set to val.if no val is specified then,None is assigned as default value.
Subjects=['CSA','C++','DS','OS']
Marks=dict.fromkeys(Subjects,-1)
print(Marks)

#syntax:- Dict.get(key)
#description:-Returns the value for the key passed as argument .If the key is not present in dictionary,it will return the default value is specified then it will return None.
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'} 
print(Dict1.get('Name'))

#syntax:- Dict.has_key(key)
#description:- Returns True if the key is present in the dictionary and False otherwise.
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print('Marks' in Dict1)

#syntax:- Dict.items()
#description:- Returns a list of tuples (key-value pair)
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.items())

#syntax:- Dict.setdefault(key,value)
#description:- Sets a default value for a key that is not present in the dictionary
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict1.setdefault('Marks',0)
print(Dict1['Name'],"has got marks = ",Dict1.get('Marks'))
print()

#syntax:- Dict1.update(Dict2)
#description:- Adds the key-value pairs of Dict2 to the key-value pairs of Dict1
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict2={'Marks':90,'Grade':'O'}
Dict1.update(Dict2)
print(Dict1)
print()

#syntax:- Dict.values()
#description:- Returns a list of values in dictionary
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.values())
print()

#syntax:- Dict.iteritems()
#description:- Used to iterate through items in the dictionary
# Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
# for i,j in Dict1.iteritems():
#     print(i,j)

#syntax:- in and not in
#description:- Checks whether a given key is present in dictionary or not
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print('Name' in Dict1)
print('Marks' in Dict1)

print("\n\nSTRING FORMATTING WITH DICTIONARIES \n\n")
print("\nProgram that uses string formatting feature to print the key-value pairs stored in the dictionary.\n\n")
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
for key,val in Dict.items():
    print("%s is studying %s "%(key,val))

print("\nWrite a program that has a dictionary of states and their codes.Add another state in the pre-defined dictionary , print all the items in the dictionary , and try to print code for a state taht does not exist.SEt a default value prior to printing.\n")

states={'Delhi':'DL','Haryana':'HR','Maharashtra':'MH',"Rajasthan":'RJ'}
states['Tamil Nadu'] = "TN" #add another state
print("Code for Rajasthan is : ",states['Rajasthan'])
print('-'*5,"CODES","-"*5)
for i in states.items():
    print(i)
print("Code for Karnataka : ",states.get("Karnataka"))

print('\nWrite a program that creates a dictionary of radius of a circle and its circumference.\n')
# print("Enter '1' for exit the program ")
# radius=int(input("Enter the number:- "))
# Dict23={}
# while radius!= -1:
#     circumference=2*3.14*float(radius)
#     Dict23[str(radius)]=circumference
#     radius=int(input("Enter the number:- "))
# for i in Dict23.items():
#     print(i)

# print("Next program")
# print("Enter -1 to exit...")
# Circumference={}
# while 1:
#     r=float(input("Enter radius : "))
#     if r==-1:
#         break
#     else:
#         Dict={r:2*3.14*r}
#         Circumference.update(Dict)
# print(Circumference)

print("\nWrite a program that creates two dictionaries . One that stores conversion values from meters to centimeters and the other that stores values from centimeters to meters .\n")
m_meter={x:x*100 for x in range(1,11)}
temp=m_meter.values()
cm_m={x:x/100 for x in temp}
print("Meters : Centimeters ",m_meter)
print("Centimeters : Meters",cm_m)


print("\nWrite a program that has a set of works in English language and their correspoinding words in Hindi. Define another dictionary that has alist ofwords in Hindi and their correspoinding wordsin Urdu.TAke all words from English language and display their meaninga in both the languages.\n")
E_H={'Friends':'Mitr','Teacher':'Shikshak','Book':'Pustak'}
H_U={'Mitr':'Dost','Shikshak':'Adhyapak','Pustak':"Kitab",'Rani':'Begum'}
for i,j in E_H.items():
    print("The meaning of the %s in Hindi and Urdu is %s and %s respectively "%(i,E_H[i],H_U[j]))

print("\nWrite a program that calculates fib(n) using a dictionary.\n")
# Dict={0:0,1:1}
# def fib(n):
#     if n not in Dict:
#         val=fib(n-1)+fib(n-2)
#         Dict[n] = val
#     return Dict[n]
# n=int(input("Enter the value of n: "))
# print("Fib(",n,") = ",fib(n))

print("\nWrite a program that creates a dictionary of cubes of odd numbers in the range 1-10 .\n")
odd_cubes={x*2+1:(x*2+1)**3 for x in range(1,11)}
print(odd_cubes)

Dict9={x:x**2 for x in range(1,11) if x%2==1}
print(Dict9)

print("\nWrite a  program that prompts the user to enter a message .Now count and print the number of occurrences of each character.\n")
message="Good"
mes={}
n=0
for x in message:
    mes[x]=n
    n+=1
print(mes)
print()
print(dict(enumerate(message)))

def count(message):
    letter_counts={}
    for letter in message:
        letter_counts[letter] =letter_counts.get(letter,0)+1
    print(letter_counts)
count(message)

print("\nWrite a program to store a sparse matrix as a dictionary.\n")
matrix=[[0,0,0,1,0],
        [2,0,0,0,3],
        [0,0,0,4,0]]
Dict={}
for x in range(0,len(matrix)):
    print()
    for j in range(0,len(matrix[x])):
        print(matrix[x][j],end=" ")
        if matrix[x][j]>0:
            Dict[(str(x),str(j))]=matrix[x][j]
print("Sparse Matrix can be efficiently represented as Dictionary : ")
print(Dict)

print("\nWrite a program that inverts a dictionary .That is, it makes key of one dictionary value of another and vice versa.")
Dict={'Roll_NO':'16/001','Name':'Arav','Course':'BTech'}
inverted={}
for key,value in Dict.items():
    inverted[value]=key
print(inverted)

print('\nWrite a program that has dictionary of names of students and a list of their marks in 4 subjects.Create another dictionary from this dictionary that has name of the students and their total marks .Find out the topper and his/her score.')
Marks={'Neha':[97,89,94,90],'Mitul':[92,91,94,87],'Shefali':[67,99,88,90]}
t_m={}
for key,value in Marks.items():
    t_m[key]=sum(value)
max1=[]
for x in t_m.values():
    max1.append(x)
print(t_m)
for key ,value in t_m.items():
    if max(max1)==value:
        print("Topper is : ",key ,"with marks = ",value)


tot=0
Tot_Marks=Marks.copy()
for key, val in Marks.items():
    tot=sum(val)
    Tot_Marks[key]=tot
print(Tot_Marks)
max2=0
Topper=''
for key,val in Tot_Marks.items():
    if val>max2:
        max2=val
        Topper=key
print("Topper is : ",Topper,"with marks = ",max2)