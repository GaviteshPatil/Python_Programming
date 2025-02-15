def differ(x,y):
    return y-x
a=20
b=30
opration=differ
print(opration(a,b))

def func():
    """hellow the is my code
    to execute function for beigneers level."""
    for x in range(4):
        print("Hellow world.")
func()

def func1(i,j):
    print("Hellow world",i,j)
func1(5,"HEllOW WORLD")

#program to demostrate mismatch of name of function parameters and arguments
def func2(i):
    print("HELLO WORLD",i)
j=2477
func2(j)

#program to demostrate the arguments may be passed in the form of expressions to the called function.
def func3(e):
    print("HEllo World.",e)
func3(5+2*3)

#program to add two different number using the function.
def add(a,b):
    c=a+b
    return print("Sum of the",str(a),"and",str(b),"is",c)
a=int(input("Enter the number\n"))
b=int(input("Enter the second number\n"))
add(a,b)

#program to demonstrate the use of the global statement
var="Good"
def show():
    global var1
    var1="Morning"
    print("In Function var is -",var)
show()
print("Outside function,var1 is -",var1)
print("var is -",var)

#program to demonstrate name clash of local and global variable
var="Good"
def show1():
    var="Morning"
    print("In Function var is -",var)
show1()
print("Outside function,var is ",var)

#program to demostrate access of variables in inner and outer functions.
def outer_fun():
    outer_var=10
    def inner_func():
        global inner_var
        inner_var=20
        print("Outer Variable =",outer_var)
        print("Inner Variable =",inner_var)
    inner_func()
    print("Outer Variable =",outer_var)
    print("Inner Variable =",inner_var)
outer_fun()

#program to demonstrate name clash variables in case of nested functions.
def Outer():
    var1=10
    def Inner():
        var1=20
        print("Inner variable =",var1)
    Inner()
    print("Outer Variable =",var1)
Outer()

#program that demostrate using a variable defined in global namespace.
def func4():
    print(str)
str="Hello world !!!"
func4()

#program that demostrate using a local variable with same name as that of global .
def f():
    global str
    print(str)
    str="Welcome to the python programming."
    print(str)
str="HEllo World !"
f()

def display(str):
    print(str)
str="Hello"
display(str)

def display2(tr,int_x,float_y):
    print("The string is : ",tr)
    print("The integer value is : ",int_x)
    print("The floating point value is : ",float_y)
display2(float_y=56789.045,tr="Hello",int_x=1234)

#consider another program for keyword arguments in which duriing function call we use assignment operator to assign values to function parameters using other variables(instead of values).
def fun5(name,age,salary):
    print("Age :",age)
    print("name : ",name)
    print("salary:  ",salary)
n="Gavitesh"
a=18
s=999999999999999999
fun5(salary=s,age=a,name=n)

#program to demonstrate the default arguments.
def fun6(namel,course="B.Tech"):
    print("Name : "+ namel)
    print("course :",course)
fun6(course="B.Tech",namel="Gavitesh") # Keyword Arguments
fun6(namel="Aditya")                  #Default Arguments

def display65(name,mark,course='B.Tech'):
    print("The marks of "+name+" in "+course+" .He got in "+mark+" in his course.")
display65("Gavitesh","68")

#program to demonstrate the use of variable -length arguments.
def func7(name,*fav_subjects):
    for x in fav_subjects:
        print("\n",name,"likes to read ",x,end=" ,")
func7("Manish","Mathmatics","Android Programming")
func7("Ricky","C","Data Structures","Design and Analysis of Algorithms ")
func7("Aditya")

#program to demonstrate the lambda function.
sum=lambda x,y:x+y
print("Sum = ",sum(3,5))

#demostrate a program to return the full name of a a person.
def name(a,b):
    """function will produce the full name of the person
        a (_type_): First name of person
        b (_type_): Sirname of person
    Returns:
        _type_: Full name of the person with separator.
    """
    separator=" "
    name=a+separator+b
    return name
#program to return the average of its arguments.
def avg(n1=0,n2=0):
    n1=int(input("Enter the number:\n>>>"))
    n2=int(input("Enter the number:\n>>>"))
    print("The average of the numbers",n1,n2,"is ",(n1+n2)/2)
#program to demonstrate the check wheather the number is even or odd.

def numcheck(a):
    if a%2==0:
        print("The num"+str(a),"is even number.")
    else:
        print("The number ",a,"is the odd number.")
numcheck(1091)

def numch(a):
    if a%2==0:
        return 0
    else:
        return 1
j=int(input('Enter the number:\n>>>'))
a=numch(j)
if a==1:
    print("The number is the odd number.")
else:
    print("The number is even number.")

#program to demostrate the conversion of time into minutes.
def covert_time(a,b):
    """function will convert the minutes and hours into minuets.

    Args:
        a (_type_): hours enter by the user
        b (_type_): minutes enter by the user

    Returns:
        _type_: Total count of minutes.
    """
    j=(a*60)+b
    return j
m=34
h=6
k=covert_time(h,m)
print("Total minutes is ",k)

#program to demonstrate the simple intrest.formul = interest*principle amount*time
def interes(p,t,i):
    """program will show the simple intrest

    Args:
        p (_type_): princple intrest
        t (_type_): time
        i (_type_): "y"or "n" for senior citzen

    Returns:
        _type_: total intrest
    """
    if i=="y":
        return (p*t*12)/100
    else:
        return (p*t*10)/100
i="y"
t=3
p=200000
k=interes(p,t,i)
print("your total interst amount is ",k)

#program to demostrate the calculation of the volume of cuboid using default arguments.
def volu(l,w=3,h=4):
    print("Length:",l,"\tWidth:",w,"\tHeight:",h)
    return l*w*h
print(volu(4))

#program that uses docstings and variable-length arguments to add the values passed to the function.
def add(*s):
    '''function will return the sum of values passed to it'''
    sum=0
    for x in s:
        sum+=x
    return sum
k=add(25,30,45,50)
print("Sum:\t",k)

#program thath greets a person.
def greet(masg,name):
    '''This function welcomes the person passed whose name is passed as a parameter'''
    return (masg+" "+name)
masg="Happy Reading. Python is Fun !"
name="Jason"
print(greet(masg,name))

def func():
    "The program is created to print the hello world by usinig funtion."
    print("Hello World")
print(func.__doc__)
