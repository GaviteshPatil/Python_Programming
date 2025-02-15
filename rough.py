def program1():
    #Program to findout basic calulation
    num1=int(input("Enter a first number=\t"))
    num2=int(input("Enter a second number=\t"))
    m=num1*num2
    d=num1/num2
    a=num1+num2
    s=num1-num2
    mu=num1%num2
    x=int(num1)*int(num2)
    print("\t|function\t|\tresult number")
    print("\t|",num1,"*",num2,"\t|\t",m)
    print("\t|",num1,"/",num2,"\t|\t",d)
    print("\t|",num1,"+",num2,"\t|\t",a)
    print("\t|",num1,"-",num2,"\t|\t",s)
    print("\t|",num1,"%",num2,"\t|\t",mu)
    print("\t|",num1,"*",num2,"\t|\t",x)

def program2():
    #Area of triangle by using Heron's formula
    number1=int(input("Enter value of side 1 \n>"))
    number2=int(input("Enter value of side 2 \n>"))
    number3=int(input("Enter value of side 3 \n>"))
    print("By using the heron's formula")
    S=(number1+number2+number3)/2
    formula=(S*(S-number1)*(S-number2)*(S-number3))**0.5
    print("The value of the 'S' is\n>",S)
    print("The Area of the triangle is\n>",formula)
    print("_________________________")
    print("|Area of triangle\t|",formula)
def program3():
    #Program to print distance between two points
    p1=int(input("Enter x co-ordinate of point A \n>"))
    p2=int(input("Enter y co-ordinate of point A \n>"))
    p3=int(input("Enter x co-ordinate of point B \n>"))
    p4=int(input("Enter y co-ordinate of point B \n>"))
    print("The co-ordinates of point A and point B is ","\n(x1,y1)>",p1,p2,"\nThe co-ordiantes of point B is","\n(x2,y2)",p3,p4)
    print("By using distance formula.")
    formula1=(((p3-p1)**2)+((p4-p2)**2))**0.5
    print("The distance between the point A and poin B is\t>",formula1)

def program4():
    #program to findout the multiplication,division,addition,substraction of two floationg lieral number
    num1=float(input("Enter a first number=\t"))
    num2=float(input("Enter a second number=\t"))
    m=num1*num2
    d=num1/num2
    a=num1+num2
    s=num1-num2
    mu=num1%num2
    print("\t|function\t|\tresult number")
    print("\t|",num1,"*",num2,"\t|\t",m)
    print("\t|",num1,"/",num2,"\t|\t",d)
    print("\t|",num1,"+",num2,"\t|\t",a)
    print("\t|",num1,"-",num2,"\t|\t",s)
    print("\t|",num1,"%",num2,"\t|\t",mu)

def program5():
    #program to show the relational operator
    c1=int(input("Enter the first number  \t|>"))
    c2=int(input("Enter the second number \t|>"))
    print(str(c1),"==",str(c2),"is",c1==c2)
    print(str(c1),"!=",str(c2),"is",c1!=c2)
    print(str(c1),">",str(c2),"is",c1>c2)
    print(str(c1),"<",str(c2),"is",c1<c2)
    print(str(c1),"<=",str(c2),"is",c1<=c2)
    print(str(c1),">=",str(c2),"is",c1>=c2)
def program5():
    #program to findout AREA of circle.
    radius=float(input("Enter the radius of circle :-\n>"))
    area=3.14*radius*radius
    circumference=2*3.14*radius
    print("Radius of the circle is",radius)
    print("AREA =",str(area),"\tCIRCUMFERENCE=",circumference)

def program6():
    #program to findout how many digits in number
    num5=input("Enter a number \n>")
    print("The number contain the digits is",str(len(num5)))

def program7():
    #program to findout digits at a one's place.
    num9=int(input("Enter the number \t="))
    module=num9%10
    print("The number at the one's digit is ",module)

def program8():
    #program to findout the average and devision of numbers.
    z=int(input("Enter the first number \n>"))
    z1=int(input("Enter the second number \n>"))
    average=((z+z1)/2)
    print("The averge of the numbers is \n",average)
    deviation1=z-average
    deviation2=z1-average
    print("The deviation os z and z1 is\n",deviation1,deviation2)

def program9():
    #program to convert degree celusis into fahrehnit
    temp=float(input("Enter the temperature in degree celusis\n  >>>"))
    formula=((1.8*temp)+32)
    print("The tempreature in fahrenheit is \n  >>>",formula,"F.")

def program10():
    #program to calculate the total money in piggybank given the Rs.10,Rs.5,Rs.2,Rs.1.
    r1=int(input("Enter the number of Rs.10 coins is \n >>>"))
    r2=int(input("Enter the number of Rs.5 coins is \n >>>"))
    r3=int(input("Enter the number of Rs.2 coins is \n >>>"))
    r4=int(input("Enter the number of Rs.1 coins is \n >>>"))
    print("The total amount in piggybank is ",((10*r1)+(5*r2)+(2*r3)+(1*r4)))

#program to calculate the total percentage of student out of 3 activities.
weight_activity=30
weight_sports=20
weight_exam=50
w1=float(input("Enter the student marks in activities \n>>>"))
w2=float(input("Enter the student marks in examination \n>>>"))
w3=float(input("Enter the student marks in  sports  \n>>>"))
r1=float((w1/weight_activity)*100)
r2=float((w2/weight_exam)*100)
r3=float((w3/weight_sports)*100)
total=(r1+r2+r3)
print("---------------------------------")
print("*************MARKSHEET***********")
print("|percentage in activites   |",r1,"|")
print("|percentage in examination |",r2,"|")
print("|percentage in sports      |",r3,"|")
print("_________________________________")
print("|Total percentage          |",total,"|")

n=int(input("Enter the number :- \n>>>"))
while n != 0:
    print(n,end=" ")
    n -=1

f=1
for i in range(1,10):
    f=f*i
print(f)
