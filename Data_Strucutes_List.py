print("\n\nTUPLE\n\n")
print("\nPrograms to show how to create the different types of tuples.\n")

Tup1=() #Creates an empty tuple
print(Tup1)

Tup1=(5)   # Creates a tuple with a single element 
print(Tup1)

Tup1=(1,2,3,4,5) # Creates a tuple of integers 
print(Tup1)
Tup2=('a','b','c','d' )  #Creates a tuple of characters
print(Tup2)
Tup3=("abc","def","ghi")  #Creates  a tuple of strings
print(Tup3)
Tup4=(1.2,2.3,3.4,4.5)  #creates a tuple of floating point numbers
print(Tup4)
Tup5=(1,"abc",2.3,'d')
print(Tup5)

#Tuple with parentheses
print('a',"bcd",2,4.6)


#Default tuple without parentheses
a,b=10,20
print(a,b)

#Programs to demonstrate the necessity of having a comma in the tuple.
Tup=(10,) #comma after first element 
print(type(Tup))

Tup=(10) #comma missing
print(type(Tup))

print("\nProgram to illustrate the use of divmod() function.\n")
quo,rem=divmod(100,3)
print("Quotient = ",quo)
print("Remainder = ",rem)

print("\nProgram to illustrate the use of slice ooperation to retrieve  value(s) stroed in a tuple")
Tup1=(1,2,3,4,5,6,7,8,9,10)
print("Tup[3:6] = ",Tup1[3:6])
print("Tup[:8] = ",Tup1[:8])
print("Tup[4:] = ",Tup1[4:])
print("Tup[:] = ",Tup1[:])

print("\n\nUPDATING TUPLE\n\n")
#Program to extract values from a tuple
Tup1=(1,2,3,4,5)
Tup2=(6,7,8,9,10)
Tup3=Tup1+Tup2
print(Tup3)

#Note:- You can delete the entire tuple but you can't delete the element present in the tuple
'Program to delete a tuple'
del Tup1

print("\n\nBASIC TUPLE OPERATIONS \n\n")
#Length
print(len((1,2,3,4,5,5)))

#concatenation
print((1,2,3)+(4,5,6))

#Repetition
print(("Good..")*3)

#Membership
print(5 in (1,2,3,4,5,67,8,9,10))

#Iteration
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i,end=" ")

#Comparison(Use >,<,==)
Tup1=(1,2,3,4,5)
Tup2=(1,2,3,4,5)
print(Tup1>Tup2)

#Maximum
print(max(1,0,3,8,2,9))

#Minimum
print(min(1,0,3,8,2,9))

#convert to tuple (converts a sequence into a tuple)
tuple("Hello")
tuple([1,2,3,4,5])

#Tuple Assignment
print("\nProgram to show the different wayss of tuple assignment.\n")
#an unnamed tuple of values assigned to values of another unnamed tuple
(val1,val2,val3)=(1,2,3)
print(val1,val2,val3)

# Tupl=(100,200,300)
# (val1,val2,val3)=Tup1 #tuple assigned to another tuple 
# print(val1,val2,val3)
# #expressions are evaluated before assignment
# (val1,val2,val3)=(2+4,5/3,9%6)
# print(val1,val2,val3)

#Tuples for Returning Multiple Values
print("\nProgram to return the highest as well as the lowest values in the list.\n")
def max_min(vals):
    x=max(vals)
    y=min(vals)
    return (x,y)
vals=( 99,98,90,97,89,86,93,82)
(max_marks,min_marks)=max_min(vals)
print(vals)
print("Highest Marks = ",max_marks)
print("Lowest Marks = ",min_marks)

#Programming Tip= You can't delete elements from tuple Methods like remove() or pop() do not work with a tuple.

"Note:- Unlike lists,tuples do not support remove(),pop(),append(),sort(),reverse(),and insert() methods."

print("\nProgram to demonstarate the use of  nested tuples.\n")
Toppers=(("Arava","BSc",92.0),("Chaitanya","BCA",99.0),("Dhruvika","Btech",97))
for i in range(len(Toppers)):
    for j in Toppers[i]:
        print(j,end=" ")
    print()

print("\nProgram to print the name of the topper and her makrs in 4 subjects whrein the marks are spcified as a list in the tuple Topper.\n")
Topper=("Janvi",[94,95,96,97])
print("Class Topper : ",Topper[0])
print("Highest Scores in 4 Subjects : ",Topper[1:])

print("\nProgram to demonstrate the use of index() method.\n")
Tup=(1,2,3,4,5,6,7,8,9)
print(Tup.index(4))

print("\nProgram to print location at which an element is present in the list using the index() method.\n")
students=("Bhavya","Era","Falguni","Huma")
index=students.index("Falguni")
print("Falguni is present at loacation : ",index)

print("\nCouonting the Elements : count() Method.")
tup="abcdxxxabcdxxxabcdxxx"
print("x appears ",tup.count('x'),"times in ",tup)

print("\nConsider the program given below passes a tuple as an argument to a funciton double().The function scales each value in the tuple by a factor of two and places teh scaled values in another tuple\n")
def double(T):
    return ([i*2 for i in T])
Tup=1,2,3,4,5,6
print("Original Tuple : ",Tup)
print("Double values : ",double(Tup))

"Note :- If a sequence is specified without parentesis , it is treated to be a tuple by default.\n"

print('\n\nVARIABLE LENGTH ARGUMENT TUPLES\n\n')
print('\nProgram to manipulate effciently each value that is passed to the tuple using varaiable-length arguments.\n')
def display(*args):
    print(args)
Tup=(1,2,3,4,5,6)
display(Tup)

#Programming Tip:- If a negative value is used for the step , the slice is done backwards.

print('\nProgram to show the use of zip() function.\n')
Tup=(1,2,3,4,5)
List1=['a','b','c','d','e']
print(list(zip(Tup,List1)))

print("\nProgram to use zip() function on variable-length sequences.\n")
Tup=(1,2,3)
List1=['a','b','c','d','e']
print(list(zip(Tup,List1)))

print('\nProgram to print elements in a tuple using for loop.\n')
Tup=((1,'a'),(2,'b'),(3,'c'))
for i , char in Tup:
    print(i,char)

print("\nProgram that uses enumerate() function to print elements as well as their indices.\n")
for index, element in enumerate('ABCDEFG'):
    print(index,element)

print('\nProgram to sort a tuple of values.\n')
Tup=(5,1,0,2,8,3,9)
print(sorted(Tup))

print('\nProgram to illustrate string formatting function with tuple.\n')
Tup=("Heena",89,82,4)
print("%s go %d marks in CSA and her aggregate was %.2f"%(Tup[0],Tup[1],Tup[2]))

#Programming Tip:- Reassigning a value in a tuple causes a TypeError

print("\nWrite a program to swap two values using tuple assignment.\n")
val1=10
val2=20
print("val1 = ",val1," val2 = ",val2)
(val1,val2)=(val2,val1)
print("val1 = ",val1,"val2 = ",val2)

print("\nWrite a program using a function that returns the area and circumference of a circle whose radius is passed as an argument.\n")
PI=3.14
def cal_ac(radius):
    area=PI*(radius**2)
    circumference=2*PI*radius
    return(area,circumference)
radius=3.44
area,cicumference=cal_ac(radius)
print("Area and the circumference of the circle are %f,%f respectively whcih contain the radus %f "%(area,cicumference,radius))

# print("\nWrite a program that has a nested list to store toppers details .Edit the details and reprint the details.\n")
# #Programming Tip:- You cannot add elements to a tuple .Methods like append() or extend() does not work with tuple.
# Topper=(("Arav","Bsc",92.0),("Chaitanya","BCA",99.0),("Dhruvika",'Bteach',97))
# for i in Topper:
#     print(i)
# choice=input("Enter the choice \nIf you want to edit the tuple enter 'y' \nIf you want to skip the edit enter 'n' \n:- ")
# if choice=='y':
#     choice1=input("\t \nIf you want to change the name of the student enter 'n'\n If you want to change the Subject of the student enter 's' \n If you want to change the marks of the students 'm' \n:- ")
#     if choice1=='n':
#         name=input("\nEnter the name of the student \n:- ")
#         for name1 in Topper:
#             if name1[0]==name:
#                 cname=input("Enter name you want to change \n:- ")

# Toppers=(("Arav","Bsc",92.0),("Chaitanya","BCA",99.0),("Dhruvika","Btech",97))
# for i in Toppers:
#     print(i)
# choice=input("Do you want to edit the details : ")
# if choice=='y':
#     name=input("Enter the correct name: ")
#     new_course=input("Enter the correct course : ")
#     new_aggr=input("Enter the correct aggregate :- ")
#     i=0
#     new_Toppers=()
#     while i<len(Toppers):
#         if Toppers[i][0] == name:
#             new_Toppers+=(name,new_course,new_aggr)
#         else:
#             new_Toppers+=Toppers[i]
#         i+=1
# for i in new_Toppers:
#     print(i,end=" ")

print("\nWrite a program that scans an email address and forms a tuple of user name and domain.\n")
addr="abc@gmail.com"
user_name,domain_name=addr.split('@')
print("User Name : ",user_name)
print("Domain Name : ",domain_name)

print("\nWrite a program that has a list of numbers (both positive as well as negative.).Make a new tuple that has only positive values from this list.\n")
Tup=(-10,1,2,-9,3,4,-8,5,6)
newTup=()
for i in Tup:
    if i>0:
        newTup +=(i,)
print(newTup)

print("\nWrite a program that accepts different number of arguments and return sum of only the positive values passed to it.\n")
def sum_num(*args):
    tot=0
    for i in args:
        tot=tot+i
    return tot
print("sum_num(1,-9,2,-8,3,-7,4,-6,5) = ",sum_num(1,-9,2,-8,3,-7,4,-6,5))

print("\nWrite a program that has two sequences.First which stores some questions and second stores the corresponding answers.Use the zip() function to forms a valid question answer serires.\n")
Ques=["Roll_NO","Name","Course"]
Ans=[7,"Saesha","BSc"]
for q,a in zip(Ques,Ans):
    print("What is your ",q,"?")
    print("My",q,"is : ",a)

#Programming Tip:- If the index specified in the tuple slice is too big , then an IndexError exception is raised.
