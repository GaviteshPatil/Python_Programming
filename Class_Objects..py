# #Python has a very simple syntax of defining a class.This syntax can be given as 
# #syntax:- class class_name:
#             <statement-1>
#             <statement-N>
#Programming Tip:- A class can be defined in a funciton or with an if statement.

print("\n\nCREATING OBJECTS \n\n")
#syntax for creating the objects :- object_name=class_name()

#Programming Tip:- Python does not require the new operator to create an object

'Note:- Creating an object or instance of a class is known as class instantiation.\n'

#syntax for accessing a class member through the class object :- object_name.class_member_name

print("\nProgram to access class variable using class object\n")
class ABC:
    var=10  #class variable
obj=ABC()
print(obj.var)  #class variable is accessed using class object

#Programming Tip:- self in Python works in the same way as the "this" pointer in C++

"Note:- Functions defined inside a class are called class methods."

"Note:- If you have a method which takes no arguments then you still have to define the method to have a self argument."


print("\nprogram to accesss class members using the class object.\n")
class ABC():
    var=10
    def display(self):
        print("In class method...")
obj=ABC()
print(obj.var)
obj.display()

#Programming Tip:- You can give any name for the self parameter, but you should not do so .

print("\nTHE __intit__() METHOD ")

"\nNote __init__() is prefixed as well as suffixed by double underscores.\n"

print("\nProgram illustrating the use of __init__() method.\n")
class ABC():
    def __init__(self,val):
        print("In class method..... ")
        self.val=val
        print('The value is : ',val)
obj=ABC(1000)

#Programming Tip:- The __init__() method is same as constructor in C++ and java

#Note :- It is a good programming habit to initialize all attributes in the __init__() method.Although values can be initialized in other methods also but it is not recommended


print("\nProgram to differentiate between class and object variables.\n")
class ABC():
    class_var=0 #class variable 
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var #object variable 
        print("The Object value is : ",var)
        print("The value of class variable is : ",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)

#Programming Tip:- Class variable must be prefixed by the class name and dot operator

"Note :- Class variables are usually used to keep a count of number of objects created from a class.\n"

class Number:
    even = 0 #default value 
    def check(self,num):
        if num%2==0:
            self.even=1
    def Even_Odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.Even_Odd(21)

#Programming Tip:- Class attributes are defined at the same indentation level as that of class methods

print('\nProgram modifying a mutable type attribute .\n')
class Number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
N1=Number(21)
N2=Number(32)
N3=Number(43)
N4=Number(54)
N5=Number(65)
print("Even Numbers are : ",Number.evens)
print("Odd Numbers are  :",Number.odds)


print("\nProgram to illustrate the use of __del__() method.\n")
class ABC():
    class_var=0 #class variable
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var #object variable
        print("The Object value is : ", var)
        print("The value of class variable is ",ABC.class_var)
    def __del__(self):
        ABC.class_var-=1
        print("Object with value %d  is going out of scope "%self.var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
del obj1
del obj2
del obj3

#Programming Tip :- In C++ and Java, all members are private by default but in Python , they are public by default.

print("\nProgram to illustrate the use of special methods in Python classes .")
class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
    
obj = ABC("abcdef",10)
print("The value stored in object is : ",repr(obj))
print("The length of name stored in object is : ",len(obj))
obj1=ABC("ghijkl",1)
val=obj.__cmp__(obj1)
if val == 0:
    print("Both values are equal ")
elif val==-1:
    print("First value is less than second")
else:
    print("Second value is less than first ")


print("\nProgram to demonstrate the use of __getitem__() and __setitem__() methods \n")
class Numbers:
    def __init__(self,myList):
        self.myList=myList
    
    def __getitem__(self,index):
        return self.myList[index]
    
    def __setitem__(self,index,val):
        self.myList[index] = val

NumList=Numbers([x for x in range(1,10)])
print(NumList[5])
NumList[3]=10
print(NumList.myList)

#Note :- Trying to access an attribute of an instance that is not defined or a method that is undefined causes an AttributeError

print()
print("Program to illustrate the difference between public and private variables .")
class ABC():
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("From class method , Var1 = ",self.var1)
        print("From class method , Var2 = ",self.__var2)
obj=ABC(10,20)
obj.display()
print("From main module, Var1= ",obj.var1)
# print("From class method, Var2 = ",obj.__var2)
print("From main module , Var2 = ",obj._ABC__var2)

print("\nProgram to illustrate the use of a private method.\n")
class ABC():
    def __init__(self,var):
        self.var=var
    def __display(self):
        print("From class method , Var = ",self.__var)
obj=ABC(20)
# obj._ABC__display()

"Note:- Like private attributes, Python also allows you to have private methods to discourage people from accessing parts of a class that have implementation details."

print("\nProgram to call a class method from another method of the same class.\n")
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is = ",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj=ABC(10)
obj.add_2()

print("Program to show how a class method calls a function defined in the global namespace.\n ")
def scale_10(x):
    return x*10
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is = ",self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=ABC(10)
obj.display()
obj.modify()
obj.display()

#Note:- A class is never used as a global scope.

print("\nProgram to add variables to a class at run-time.\n")
# class ABC():
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("Var is = ",self.var)
#     # def new_var(self,var):
#     #     self.var= var
# obj=ABC(10)
# obj.display()
# obj.new_var=20  #variable added at run-time
# print("New Var = ",obj.new_var)
# obj.new_var=30 #modifying newly added variable
# print("New Var after modification = ",obj.new_var)
# del obj.new_var #newly created variable is deleted 
# print("New var after deletion = ",obj.new_var)

print("\nProgram to demonstrate the use of getattr(),seattr(), and delattr() functions.\n")
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is = ",self.var)
obj=ABC(10)
obj.display()
print("Check if object has attribute var .....",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("After setting value , var is : ",obj.var)
setattr(obj,'count',10)
print("New variable count is created and its value is : ",obj.count)
delattr(obj,'var')
# print("After deleting the attribute , var is : ",obj.var)

print("\nProgram to demonstarte the use of built-in class attributes\n")
class ABC():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("Var1 is =",self.var1)
        print("Var2 is = ",self.var2)
obj=ABC(10,12.34)
obj.display()
print("object.__dict__ - ",obj.__dict__)
print("object.__doc__ - ",obj.__doc__)
print("class.__name__ - ",ABC.__name__)
print("object.__module__ - ",obj.__module__)
print("class.__bases__ - ",ABC.__bases__)

#Note :- The __repr__() special method is used for string representation of the instance.

"The process by which Python periodically reclaims unwanted memory is known as garbage collection ."

#Note :- When an object's reference count reaches zero, Python recollects the memory used by it .

"Programming Tip :- Object of a class can be deleted using del statement ."

"""
var1=10         # Create object var1
var2=var1       # Increase ref. count of var1 - objcet assigment 
var3= [var2]    #Increase ref.count of var1 - object used in a list 
var2 =  50      # Decrease ref.count of var1 - reassignment
var3[0] = -1    #Decrease ref.count of var1 - removal from list 
del var1        #Decrease ref.count of var1 - object deleted """

print("\nPROGRAMMING EXAMPLES \n")
print()
print("\nWrite a program that uses class to store the name and marks of students .Use list to store the marks in three subjects.\n")
class Students:
    def __init__(self, name ):
        self.name=name
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in subject %d : "%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
# s1=Students("Anisha")
# s1.enterMarks()
# s2=Students("Jignesh")
# s2.enterMarks()
# s1.display()
# s2.display()

print("\nWrite a program with class Employee that keeps a track of the number of employees in an organization and also stores their name, designation , and salary details.\n")
class Employee:
    empCount=0
    def __init__(self,name,salary,designation):
        self.name=name
        self.salary=salary
        self.designation=designation
        Employee.empCount+=1
    def displayCount(self):
        print("There are %d  employees ."%(Employee.empCount))
    def diplayDetails(self):
        print("Name : %s , Designation : %s , Salary :  %d "%(self.name,self.designation,self.salary))
e1=Employee("Farhan",9000,"Team leader ")
e1.displayCount()
e1.diplayDetails()
print(e1.designation)

print("\nWrite a program that has a class Person storing name and date of birth(DOB) of a person.The program should subtract the DOB from today's date to find out wheather a person is eligible to vote or not .\n")
import datetime
class Person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age= today.year - self.dob.year
        if today<datetime.date(today.year, self.dob.month, self.dob.day):
            age-=1
        if age>=18:
            print(self.name,",Congratulations... You are eligible to vote.")
        else:
            print(self.name, ", Sorry.... You should be at least 18  years  of age to cast your vote. ")
P=Person("Saesha",datetime.date(1998,12,11))
P.check()

print("\nWrite a program that has a class Circle.Use a class variable to define the value of constant PI. Use this class variable to calculate area and cicumference of a circle with specified radius.\n")
class Circle():
    PI=3.14159
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.PI*self.radius**2
    def circumference(self):
        return 2*Circle.PI*self.radius
C= Circle(7.5)
print(("The Area of the circle is %s and The Circumference of the circle is %s")%(C.area(),C.circumference()))

print("\nWrite a program that has a class student that stores roll number, name , and marks ( in three subjects ) of the students .Display the information (roll number, name ,and total marks ) stored about the student .\n")
class student():
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        student.__marks=marks
    def total(self):
        return sum(student.__marks)
    def stu_details(self):
        return "Name = ",self.name,"Roll = ",self.roll
s1=student("Gaurav",41,[89,38,34])
print("Total marks =", s1.total())
print(s1.stu_details())


class student2():
    __marks=[]
    def set_data(self,r,n,m1,m2,m3):
        student.__rollno=r
        student.__name=n
        student.__marks.append(m1)
        student.__marks.append(m2)
        student.__marks.append(m3)
    def display_data(self):
        print("Student Details ")
        print("Roll Number : ",student.__rollno)
        print("Name : ",student.__name)
        print("Marks : ",self.total())
    def total(self):
        m=student.__marks
        return m[0] + m[1] + m[2]

r=int(input("Enter the roll number : "))
n=input("Enter the name : ")
m1=int(input("Enter the marks in first subject : "))
m2=int(input("Enter the marks in second subject : "))
m3=int(input("Enter the marks in third subject : "))
s1=student()
s1.set_data(r,n,m1,m2,m3)
s1.display_data()