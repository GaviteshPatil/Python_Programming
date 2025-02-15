"""A Data Structure is a group of data elements that are put together under on name."""

"Note :- All data structures discussed in this chapter are compound data structure as they are made of simple elements . For example , if we have defined a list as List = [1,2,3,4,5] then List is a compound data structure having integers 1,2,3,4,and 5, which are the simple or basic elements."

" 'Sequence' is the most basic data structure in Python . (Sequence = Array)"
"Sequence = ordered set "
"Types of the sequence are tuples and sets "

print("\nList\n")
#Syntax:- List_variable=[val1,val2,...]

list_A=[1,2,3,4,5]
print(list_A)

list_B=['A','B','C','d','E']
print(list_B)

list_C=["Good","Going"]
print(list_C)

list_D=[1,'a','bcd']
print(list_D)

#Note=list is mutable which means that value of its elment can be changed.

"Sytax:- seq=List[start:stop:step]"
"""
Ex:- seq = List[::2] #get every other element , starting with index 0 """

print("Program to demonstrate the slice operations used to access the elements of the list ")
num_list= [ 1,2,3,4,5,6,7,8,9,10]
print("num_list is : ",num_list)
print("First element in the list is ",num_list[0])
print("num_list[2:5] = ",num_list[2:5])
print("num_list[::2] = ",num_list[::2])
print("num_list[1::3] = ",num_list[1::3])

print("\nProgram to illustrate updating values in a list.\n")
num_list=[1,2,3,4,5,6,7,8,9,10]
print("List is : ",num_list)
num_list[5] =100
print("List after udpation is : ",num_list)
num_list.append(200)
print("List after appending a value is ",num_list)
del num_list[3]
print("List after deleting a value is ",num_list)

#Programming Tip : append() and insert() methods are list methods .They cannot be called on other values such as strings or integers.

"Note :- If you know exactly which element(s) to delete , use the del statement ,otherwise use the remove() method to delete the unknown elements ."

print("\nPrograms to illustrate deletion of numbers from a list using del statements.\n")
num_list=[1,2,3,4,5,6,7,8,9,10]
del num_list[2:4]    #deletes numbers at index 2 and 3 
print(num_list)

del num_list[:] #deletes all the numbers from the list 
print(num_list)

#Note:- Can you now imagine what will happen if you write del num_list? Yes, the entire variables will be deleted. If you make any attempt to use this variable to use this variable after the del statement, then an error will be generated .
print("\nProgram to illustrate deletion of a list \n")
num_list=[1,2,3,4,5,6,7,8,9,10]
del num_list
# print(num_list)

#Programming tip:- when using slice operation , an IndexError is generated if the index is outside the list.
print("\nProgram to insert a list in another list using the slice operation.\n")
num_list=[1,9,11,13,15]
print("Original List: ",num_list)
num_list[2] =[3,5,7]
print("After inserting another list , the updated list is : ",num_list)

print("\n\nNESTED LISTS\n\n")

print("\nProgram to illustrate nested list.")
list1=[1,'a','abc',[2,3,4,5],8.9]
i=0
while i<(len(list1)):
    print(f"List[{i}] = {list1[i]}")
    i+=1
print("Program to access the another list element in the main list.\n")
nested_list=[1,2,['a','b'],4,5,6]
print("nested_list[2][1] = ",nested_list[2][1] )

print("\n\nCLONING LISTS\n\n")
"defination:- If you want to modify a list and also keep a copy of the original list, then you should create a separate copy  of the list(not just the reference ).This process is called cloning."
print("\nProgram to create a copy as well as the clone of the original list.\n")
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1 #copies a list using reference 
print("List1 = ",list1)
print("List2 = ",list2) #both lists point to the same list 
list3=list1[2:6]
print("List3 = ",list3) #list is a clone of list1

print(id(list1))
print(id(list2),id(list3))

print("\n\nBasic List Operations\n\n")
#len:- Returns length of list 
print(len([1,2,3,4,5,6,7,8,9,10]))

#concatenation:- Joins two lists 
print([1,2,3,4,5]+[6,7,8,9,10])

#repetition:- Repeats elements in hte list 
print("Hello","World"*2)

#in:- Checks if the value is present in the list
print('a' in ['a','e','i','o','u'])

#not in :- Checks if the value is present in the list 
print(3 not in [0,2,4,6,8])

#max:- Returns maximum value in the list 
num_list=[6,3,7,0,1,2,4,9]
print(max(num_list))

#min:- Returns minimum value in the list 
num_list=[6,3,7,0,1,2,4,9]
print(min(num_list))

#sum:- Adds the values in the list that has numbers 
num_list=[6,3,7,0,1,2,4,9]
print("SUM = ",sum(num_list))

#all :- Returns True if all elements of the list are true(or if the list is empty)
num_list=[0,1,2,3]
print(all(num_list))

#any:- Returns True if any element of the list is true. If the list is empty, returns False
num_list=[0,1,2,3]
print(any(num_list))

#list:- Converts an iterable (tuple, string , set, dictionary) to a list.
list1=list("HELLO")
print(list1)

#sorted:- Returns a new sorted list. The original list is not sorted.
list1=[3,4,1,2,7,8] #unsorted list
list2=sorted(list1)
print(list1,list2)

#Programming Tip:- An error is generated if you try to delete an element from the list that is not present in the list.

list_A= ["Hello","World","good","Morning"]
print(list_A[2])
print(list_A[-3])
print(list_A[1:])

print("\n\nLIST METHODS \n\n")
#append() :- Appends an element to the list .
"In insert(),if the index is 0, then element is inserted as the first element and if we write , list.insert(len(list),obj),then it inserts obj as the last element in the list.That is , if index=len(list) then insert() method behaves exactly same as append() method."

#syntax:- list.append(obj)
num_list=[6,3,7,0,1,2,4,9]
num_list.append(10)
print(num_list)

#count:- counts the number of times an element appears in the list.
#syntax:- list.count(obj)
print(num_list.count(4))

#index() :- Returns the lowest index of obj in the list. Gives a ValueError if obj is not present in the list.
#syntax:- list.index(obj)
num_list=[6,3,7,0,3,7,6,0]
print(num_list.index(7))

#insert() :- Inserts obj at the specified index in the list.
#syntax:- list.insert(index,obj)
num_list=[6,3,7,0,3,7,6,0]
num_list.insert(3,100)
print(num_list)

#pop() :- Removes the element at the specified index from the list.Index is an optional parameter . If no index is specified , then removes the last object (or element ) from the list.
#syntax:- list.pop([index])
num_list=[6,3,7,0,3,7,6,0]
print(num_list.pop())
print(num_list)

#remove() :- Removes or deletes obj from the list ValueError is generated if obj is not present in the list.If multiple copies of obj exists in the list, then the first value is deleted.
#syntax:- list.remove(obj)
num_list=[6,3,7,0,3,7,6,0]
num_list.remove(0)
print(num_list)

#reverse():- Reverse the elements in the list.
#syntax:- list.reverse()
num_list=[6,3,7,0,3,7,6,0]
num_list.reverse()
print(num_list)

#sort() :- Sorts the elements in the list.
#syntax:- list.sort()
num_list=[6,3,7,0,1,2,4,9]
num_list.sort()
print(num_list)

#extend() :- Adds the elements in a list to the end of another list.Using + or += on a list is similar to using extend().
#list1.extend(list2)
num_list1=[1,2,3,4,5]
num_list2=[6,7,8,9,10]
num_list1.extend(num_list2)
print(num_list1)

#Programming Tip:- It is safer to avoid aliasing when you are working with mutable objects.
print("\nTo print the return values.\n")
num_list=[6,3,7,0,3,7,6,0]
print(num_list.insert(2,250))
print(num_list)
#Defination :- When one list is assigned to another list using the assignment operator(=),then a new copy of the list is not made.Instead, assigment makes the two variables point to the one list in meomory .This is alos known as aliasing.

print("\nProgram that uses the assignment operator to assign one list to another list variable.\n")
num_list1=[1,2,3,4,5]
num_list2=num_list1
print(num_list2)
print(id(num_list1),id(num_list2))
print(id(num_list1)==id(num_list2))

print("\nProgram that uses the assignment operator to assign one list to another list variable.\n")
num_list=[1,2,3,4,5]
num_list2=num_list1
print(num_list2) #if changed is made another list also affect.

"Note:- An alias is a second name for a piece of data.In Python , aliasing happens whenever one variable's value is assigned to another variable."

print("\nProgram to show the sort() mentioned.\n")
list1=['1','a','abc','2','B','Def']
list1.sort()
print(list1)

#The sort() method uses ASCII values to sort the values in the list.

print("\nProgram to delete items using empty list.\n")
list55=['p','r','o','g','r','a','m']
list55[2:5] = []
print(list55)

print("\nProgram to illustrate operations on a stack.\n")
stack=[1,2,3,4,5,6]
print("Original stack is : ",stack)
stack.append(7)
print("Stack after push operation is : ",stack)
stack.pop()
print("Stack after pop opertion is : ",stack)
last_element_index=len(stack)- 1
print("Value obtained after peep operation is : ",
stack[last_element_index])

#Note :- The del statement and the pop() method does the same thing .The only difference between them is that pop() returns the removed item.

print("\nProgram to show the implementation of a queue using list data structure.\n")
queue=[1,2,3,4,5,6]
print("Original queue is : ",queue)
queue.append(7)
print("Queue after insertion is : ",queue)
queue.pop(0)
print("Queue after deletion is : ",queue)
print("Value obtained after peep operation is : ",queue[len(queue)-1])

print("\n\nProgram to make a list of cubes.\n\n")
cubes=[] # an empty list
for i in range(11):
    cubes.append(i**3)
print("Cubes of numbers from 1-10 : ",cubes)

#Note:- You can also create an empty list by using the built-in list type object.For example, by writing L=list(),an empty list L is created.

"Python also supports computed lists called list comprehensions"
#syntax:- List = [expression for variable in sequence ]

#Note:- An iterable is an object that cna be used repeatedly in subsequent loop statements, say for example, for loop.

print("\n\nProgram to combine three lines of code into one.\n\n")
cubes=[i**3 for i in range(11)]
print(cubes)

print("\n\nProgram to combine and print elements of two list using list comprehension.\n\n")
print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!=y])

print("\n\nLOOPING IN LISTS \n\n")
print('\n\nProgram to find the sum and mean of elements in a list.\n\n')
num_list=[1,2,3,4,5,6,7,8,9,10]
sum1=0
for i in num_list:
    sum1+=i
print("Sum of elements in the list = ",sum1)
print("Average of elements in the  list = ",
float(sum1/float(len(num_list))))

print("\n\nMULTIPLE WAYS TO ACCESS A LIST .\n\n")
#Using the enumerate() function 
print("\n\nProgram to illustrate the use of enumerate() to print an individual item and its index in the list.\n\n")
num_list=[6,3,7,0,3,7,6,0]
for index4, i in enumerate(num_list):
    print(i,"is at index : ",index4)

#Using the range() function
print("\n\nProgram to print the index of values in a list.\n\n")
num_list=[6,3,7,0,3,7,6,0]
for i in range(len(num_list)):
    print("index : ",i)

#Programming Tip:- The index must be an integer. If you specify a non-integer number as the index, the TypeError will be generated.

#Using an iterator
print("\n\nProgram to print the elements in the list using an iterator.\n")
num_list=[1,2,3,4,5]
it=iter(num_list)
for i in range(len(num_list)):
    print("Element at index ",i,"is : ",next(it))

"""Note:- An iterator is often used to wrap an iterable and return each 
item of interest . All iterators are iterable, but all iterables are not iterators.
An iterator can only be used in a single for loop,
whereas an iterable can be used repeatedly in subsequent for loops."""

print("\n\nFUNCTIONAL PROGRAMMING\n\n")
print("\tfileter() Function \n")
#syntax:- filter(function,sequence)

print("\n\nProgam to create a list of numbers divisible by 2 or 4 using list comprehension.\n\n")
def check(x):
    if(x%2 == 0 or x % 4 ==0 ):
        return 1
#call check() for every value between 2 to 21
evens=list(filter(check,range(2,22)))
print(evens)

#Programming Tip:- Do not add or remove elements from the list during iteration.

print("\tmap() Function.\n\n")
#syntax:- map(function,sequence)
print("\n\nProgram that adds 2 to every value in the list.\n\n")
def add_2(x):
    x += 2
    return x
num_list = [1,2,3,4,5,6,7]
print("Original List is : ",num_list)
new_list=list(map(add_2,num_list))
print("Modified List is : ",new_list)

"""Note :- That in the above code , the map() function calls add_2() which adds 2 
to every value in the list."""

"""
Two factors that was checked before applying the map() function.
1) First, the function must have as many arguments as there are sequences.
2) Second, each argument is called with the correspoinding item from each 
   sequence( or None if one sequence is shorter than another)"""

print("\n\nProgram to pass more than one sequence to the map() function.\n\n")
def add(x,y):
    return x+y
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list(map(add,list1,list2))
print("Sum of ",list1 , "and ",list2," = ",list3)

#reduce() Function
#syntax:- reduce(function,sequence)

print("\n\nProgram to calculate the sum of values in a list using the reduce() function.\n\n")
import functools #functools is a module that contains the function reduce()
def add(x,y):
    return x+y
num_list=[1,2,3,4,5]
print("Sum of values in list = ")
print(functools.reduce(add,num_list))

print("\n\nExample of the reduce\n")
multiply = lambda x,y:x*y
num_list=[9,8,7,6,5,4,5,6,7]
print(functools.reduce(multiply,num_list))

print("\n\nPROGRAMMING EXAMPLES\n\n")
print("\n Write a program that creates a list of numbers from 1-20 that are either divisible by 2 or divisible by 4 without using the filter funciton.\n ")

list_program1=[ x for x in range(1,21)]
for x in list_program1:
    if x%2==0 or  x%4== 0:
        pass
    else:
        list_program1.remove(x)
print("The result list is ",list_program1)

list_program1_2=[]
for x in range(1,21):
    if x%2==0 or x%4==0:
        list_program1_2.append(x)
print("\nThe result is ",list_program1_2)

print("\n\nWrite a program using.filter function to a list of squares of numbers from 1-10 . Then use the for .. in construct to sum the elements in the list generated.\n")
# def square(x):
#     return x**2
# square_list=[]
# square_list=list(filter(square,range(1,11)))
# print("The list is ",square_list)
# sum=0
# for x in square_list:
#     sum+=x
# print("The sum of the elements in the list is ",sum)

square_list=[x**2 for x in range(1,11)]
print("The list is ",square_list)
print("The sum of the list is ",sum(square_list))

print("\n\nWrite a program the defined a list of countries that are a memeber of BRICS. check whether a country is member of BRICS or not.")

country=["Brazil","India","China","Russia","Sri Lanka"]
its_member=input("Enter the name of the country: ")
if its_member in country: print(f"{its_member} is the member of the BRICS")
else: print(f"{its_member} is not a member of the BRICS.")


print("\n\nWrite  a program to create a list of numbers in the range 1 to 10 .Then delete all the even numbers from the list and print the final list.\n")
allnum_list=[x for x in range(1,11)]
for num in allnum_list:
    if num%2==1:
        pass
    else:
        allnum_list.remove(num)
print("The result list is ",allnum_list)


allnum_list = []
for x in range(1,11):
    if x%2==1:
        allnum_list.append(x)
print("The result list is ",allnum_list)
odd_list=[x for x in range(1,11) if x%2==1]
print("The result list is ",odd_list)

num_list=[]
for i in range(1,11):
    num_list.append(i)
print("Original List : ",num_list)

for index5,i in enumerate(num_list):
    if(i%2==0):
        del num_list[index5]
print("List after deleting even numbers : ",num_list)

print("\n\nWrite a program to print index at which a particular value exists . If the value exists at multiple locations in the list, then print all the indices.Also, count the number of times that values is reapeated in the list.\n")
num_list=[1,2,3,4,5,6,7,6,5,4,3,2,1]
num_enter=int(input("Enter the number :- "))
occur=0
for x in num_list:
    if x==num_enter:
        occur+=1
i=0
while i<len(num_list):
    if num_enter==num_list[i]:
        print(f"{num_enter} is present at the {i} index in the list.")
    i+=1
print("The count of the number in the list is ",occur)

print("\n\nWrite a program that creates a list of words by combining the words in two individual lists.\n")
alphabet=[]
words=["Hello ","hii "]
words2=[" Python ",' Java ']
for x in words:
    for j in words2:
        alphabet.append(x+j)
print("List combining the words in two individual lists is ",alphabet)

print("\n\nWrite a program that forms a list of first character of every word in another list.\n")
list1=["Hello","Welcome","To","The","World","Of","Python"]
words=[]
for x in list1:
    words.append(x[0])
print("The Original list is ",list1)
print("The list contain the first number of the given list is ",words)

print("\n\nWrite a program to remove all duplicates from a list.\n")
num_list=[1,2,3,4,5,6,7,6,5,4]

print("The program with duplictes",num_list)
for x in num_list:
    if num_list.count(x)>1:
        while num_list.count(x)>1:
            num_list.pop(num_list.index(x))
num_list.sort()
print("The final list is ",num_list)

print("\n\n")
print("Original List : ",num_list)
i=0
while i<len(num_list):
    num=num_list[i]
    for j in range(i+1,len(num_list)):
        val=num_list[j]
        if val==num:
            num_list.pop(j)
    i = i+1
print("List after removing duplicates : ",num_list)

print("Write a program to create a list of numbers in the spcified range in particular steps.Reverse the list and print its values.\n\n")
import random as rd
begine=rd.randrange(1,40)
end=rd.randrange(1,45)
num_list=[x for x in range(begine,end)]
print("The original list is : ",num_list)
num_list.reverse()
print("The reversed list is : ",num_list)

num_list=[]
m=int(input("Enter the starting of the range : "))
n=int(input("Enter the ending of the range : "))
o=int(input("Enter the steps in the range : "))
for i in range(m,n,o):
    num_list.append(i)
print("Original List : ",num_list)
num_list.reverse()
print("Reversed List : ",num_list)

print("Write a program that creates a list of 10 random integers. Then create two lists-Odd List and Even List that has all odd and even values in the list respectively.\n\n")
num_list=[]
for i in range(10):
    val=rd.randint(1,100)
    num_list.append(val)
print("Original List : ",num_list)
odd_list=[]
even_list=[]
for number in num_list:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("The list contain odd numbers is ",odd_list)
print("The list contain even numbers is ",even_list)

print("\nWrite a program to create a list of first 20 odd num")
odd=[2*i + 1 for i in range(20)]
print(odd)

print("""\nWrite a program that passes a list to a function that scales each element in the 
list by a factor of 10.Print the list values at different stages to show that changes made to one list is 
automatically reflected in the other list.\n\n""")
# def change(list1):
#     for i in range(len(list1)):
#         list[i]=list[i] * 10 
#     print("After change in function , List is : ",list1)
# num_list=[1,2,3,4,5,6]
# print("Original List is : ",num_list)
# change(num_list)
# print("List after change is : ",num_list)

#Programming Tip:- Creating a list in a very extensive range will result in a Overflow Error.This can be corrected by using generators.

print("\nWrite a program that has a list of both positive and negative numbers.Create another list using filter() that has only positive values.\n\n")
def positive(x):
    if x>=0:
        return x 
integers=[-10,-20,-30,-40,0,10,20,30,40]
list4=list(filter(positive,integers))
print("Positive Values List = ",list4)

print("\n\nWrite a program that converts strings of all uppercase characters into staings of all lowercase characters using the map() funtion.\n\n")
def char(i):
    return i.lower()
string=["Hello","WElcome","TO","PYthon"]
list9=[]
list9=list(map(char,string))
print("THE list is ",list9)
print(list(filter(char,list9)))

print("\n\nWrite a program using map() funciton to create a list of squares of numbers.\n")
#using the lambda function 
square_list1=list(map(lambda x : x**2,range(1,11)))
print("The list contain the squares of the numbers from 1-10 is ",square_list1)

def squares(x):
    return x*x
sq_list=list(map(squares,range(1,11)))
print("\nList of squares from 1-10 : ",sq_list)

print("\nWrite a program to combine values in two lists using list comprehension .Combine only those values of a list that are multiples of values in the first list.\n\n")

print([(x,y) for x in [10,20,40,50] for y in [35,40,55,60] if y %x ==0 or x%y==0])

print("Write a program that converts a list of temperatures in Celsius into Fahrenheit.\n\n")
def convert_to_F(Temp_C):
    return ((float((9/5)*Temp_C+32)))
Temp_in_C=(36.5,37,37.5,39)
Temp_in_F=list(map(convert_to_F,Temp_in_C))
print("List of temperatures in Celsius : ",Temp_in_C)
print("List of temperatures in Fahrenheit : ",Temp_in_F)

print("\n\nWrite a program to find largest value in a list  using reduce() function. \n\n")
import functools
def max_ele(x,y):
    return x>y
num_list=[4,1,8,2,9,3,0]
print("Largest value in the list is : ",functools.reduce(max,num_list))

print(max(num_list))

print("\nWrite  a program that has a list of functions that scales a number by a factor of 2,3 and 4.Call each fuction in the list on a given number .\n\n")
L=[lambda x : x*2,lambda x:x *3 ,lambda x : x*4]
for f in L:
    print(f(5))
print("\nMultiplying the value of 100 by 2 we get : ",(L[0](100)))

print("\nWrite a program to generate in the Fibonacci sequence and  store it in a list.Then find the sum of the even-valued terms.\n")
# i=0
# fiboonnachi=[]
# # input1=int(input("Enter the numbers :- "))
# while i<11:

#     if len(fiboonnachi)>1:
#             fiboonnachi.append(i+fiboonnachi[fiboonnachi.index(i)-1])
#     else:
#             fiboonnachi.append(i)
#     i+=1
# print("The fibonacci sequence is ",fiboonnachi)

print("\nWrite a program to generate in the Fibonacci sequence and  store it in a list.Then find the sum of the even-valued terms.\n")

a=0
b=1
n=int(input("Enter the number of terms : "))
i=2
List2=[a,b]
while i<n:
    s=a+b
    List2.append(s)
    a=b
    b=s
    i+=1
print(List2)
i=0
sum=0
while i<n:
    sum+= List2[i]
    i+=2
print("SUM = ",sum)

print("\n\nWrite a program to add two matrices (usinig nested lists).\n")
X=[[2,3,4],
   [3,4,5],
   [3,1,2]]
Y=[[6,7,8],
   [8,7,5],
   [5,6,4]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]
for r in result:
    print(r)

print("\n\nWrite a program to find the median of a list of numbers.\n\n")
List2=[]
no_number=int(input("Enter the number of numbers you want to enter :- "))
for x in range(no_number):
    num=int(input("Enter the number :- "))
    List2.append(num)
print("Sorted List is .....")
List2.sort()
print(List2)
median=sum(List2)/len(List2)
print("MEDIAN = ",median)

print("\n\nWrite a program to calculate distance between two points .\n")
import math
p1=[]
p2=[]
x1=int(input("Enter the x co-ordinate of starting point : "))
y1=int(input("Enter the y co-ordinate of starting point : "))
x2=int(input("Enter x co-ordinate of ending point : "))
y2=int(input("Enter the y co-ordinate of ending point : "))
p1.append(x1)
p1.append(x2)
p2.append(y1)
p2.append(y2)
distane=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print("DISTANCE = %f"%distane)

print("To be continue ... in the data structure1")