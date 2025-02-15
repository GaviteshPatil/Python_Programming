#program to make a simple calculator
import math
print("\t___CALCULATOR___")
def sum(a,b):
    c=a+b
    return c
def sub(a,b):
    c=b-a
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def squr(a):
    x=math.sqrt(a)
    return x
while 1:
    print('Welcome in calculator which is formed by gavitesh.')
    print('\t1.ADDITION')
    print('\t2.SUBSTRACTION')
    print('\t3.MULTIPLICATION')
    print('\t4.DIVISION')
    print('\t5.SQUARE ROOT')
    print("\t6.EXIT")
    num1=int(input("Enter the number of the function, you want to perform \t:"))
    num2=float(input("Enter the first number \t:"))
    num3=float(input("Enter the second number \t:"))
    if num1==1:
        s=sum(num2,num3)
        print("The addition of the "+str(num2),"and",str(num3),"is",s)
    elif num1==2:
        s=sub(num2,num3)
        print("The substraction of the "+str(num2),"and",str(num3),"is",s)
    elif num1==3:
        s=mul(num2,num3)
        print("The multiplication of the "+str(num2),"and",str(num3),"is",s)
    elif num1==4:
        s=div(num2,num3)
        print("The division of the "+str(num2),"and",str(num3),"is",s)
    elif num1==5:
        s=squr(num2)
        print("The square root of the "+str(num2),"is",s)
    else:
        print("\nYou chose to exit.Bye.....")
        break
    print("-----------------------------")
    for x in range(1,3):
        print()
        